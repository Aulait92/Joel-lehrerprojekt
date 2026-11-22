#!/usr/bin/env python3
"""
Erzeugt bearbeitbare Word-Dateien (.docx) aus den Markdown-Materialien einer Einheit.

    python3 tools/docx_erstellen.py unterricht/mathematik-trigonometrie

Ergebnis:
  <einheit>/docx/                      Planung (00-auftrag … 06, README)
  <einheit>/material/docx/             jedes Material einzeln (vollständig, mit Lehrerteil)
     00-kopiervorlagen.docx            alle Materialien ohne Lehrer-/Lösungsteile
     00-arbeitsblaetter-schueler.docx  nur Arbeitsblätter/Protokolle/Stationen/Gutachten (Schülerfassung)
     00-loesungen-lehrkraft.docx       alle Lösungsblätter
     00-hilfekarten-merkblaetter.docx  Hilfekarten, Methodenkarten, Merkblätter
  <einheit>/bewertung/docx/            Diagnose, Klassenarbeit, Kompetenzraster, Feedback

Weg: Markdown → Druck-HTML (wie beim PDF-Export) → Skizzen (```dreieck, Inline-SVG) als PNG,
Rechenkästchen als Kästchenbild, Rahmenkästen als einzellige Tabellen → Pandoc (HTML → DOCX)
→ Seitenumbrüche und Tabellenrahmen per python-docx.
Benötigt: pandoc, python-docx, Pillow, Node.js mit Playwright/Chromium.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pdf_erstellen as P  # noqa: E402
from dreieck_svg import ersetze_dreiecke  # noqa: E402

UMBRUCH = "§§SEITENUMBRUCH§§"
TMP = Path(tempfile.mkdtemp(prefix="docx_"))
SVG_AUFTRAEGE: dict[str, str] = {}  # dateiname -> svg


# ---------------------------------------------------------------- Markdown-Vorstufe
def kaesten_zu_tabellen(md: str) -> str:
    """::: {style="border…"} … ::: → einzellige HTML-Tabelle (Rahmen bleibt in Word erhalten)."""
    aus, stapel, im_code = [], [], False
    for z in md.splitlines():
        if z.lstrip().startswith("```"):
            im_code = not im_code
        if not im_code and re.match(r"^:{3,}\s*\{[^}]*border", z):
            stapel.append("kasten")
            aus += ["", '<table class="kasten"><tr><td>', ""]
            continue
        if not im_code and re.match(r"^:{3,}\s*\S", z):
            stapel.append("div")
            aus.append(z)
            continue
        if not im_code and re.match(r"^:{3,}\s*$", z) and stapel:
            art = stapel.pop()
            aus += (["", "</td></tr></table>", ""] if art == "kasten" else [z])
            continue
        aus.append(z)
    return "\n".join(aus) + "\n"


def nur_ohne_teil_a(md: str) -> str:
    teile = re.split(r"(?m)^(?=## )", md)
    return "".join(t for t in teile if not re.match(r"## Teil A", t))


# ---------------------------------------------------------------- HTML-Nachbearbeitung
def svg_zu_img(html: str) -> str:
    def ersatz(m):
        svg = m.group(0)
        name = "svg_" + hashlib.md5(svg.encode()).hexdigest()[:12] + ".png"
        SVG_AUFTRAEGE[name] = svg
        w = re.search(r'width="([\d.]+)', svg)
        breite_cm = min(float(w.group(1)) * 0.0265, 16.5) if w else 8
        return f'<img src="{name}" width="{breite_cm:.1f}cm" alt="Skizze">'
    return P.SVG_BLOCK.sub(ersatz, html)


def raster_png(hoehe_cm: float) -> str:
    from PIL import Image, ImageDraw
    name = f"raster_{hoehe_cm:.1f}.png"
    pfad = TMP / name
    if not pfad.exists():
        px_cm = 118  # 300 dpi
        w, h = int(17 * px_cm), int(hoehe_cm * px_cm)
        img = Image.new("RGB", (w, h), "white")
        d = ImageDraw.Draw(img)
        schritt = px_cm / 2  # 5 mm
        x = 0.0
        while x <= w:
            d.line([(int(x), 0), (int(x), h)], fill=(185, 185, 185), width=2)
            x += schritt
        y = 0.0
        while y <= h:
            d.line([(0, int(y)), (w, int(y))], fill=(185, 185, 185), width=2)
            y += schritt
        d.rectangle([0, 0, w - 1, h - 1], outline=(110, 110, 110), width=3)
        img.save(pfad, dpi=(300, 300))
    return name


def html_fuer_word(html: str) -> str:
    html = svg_zu_img(html)
    html = re.sub(r'<div class="grafik">\s*(<img[^>]*>)\s*</div>', r"<p>\1</p>", html)

    def rechenfeld(m):
        hm = re.search(r"height:\s*([\d.]+)\s*cm", m.group(0))
        h = float(hm.group(1)) if hm else 4.0
        return f'<p><img src="{raster_png(h)}" width="17cm" height="{h:.1f}cm" alt="Rechenkästchen"></p>'
    html = re.sub(r'<div class="rechenfeld"[^>]*>\s*</div>', rechenfeld, html)

    def kopf(m):
        teile = re.findall(r"<span>(.*?)</span>", m.group(0), re.S)
        return "<p><em>" + " &nbsp;&nbsp;|&nbsp;&nbsp; ".join(t.strip() for t in teile) + "</em></p>"
    html = re.sub(r'<div class="kopf">.*?</div>', kopf, html, flags=re.S)
    html = re.sub(r'<div class="seitenumbruch"></div>', f"<p>{UMBRUCH}</p>", html)
    html = re.sub(r'<div class="schnitt">\s*(.*?)\s*</div>',
                  lambda m: f"<p>✂ – – – – – – {m.group(1).replace('✂', '').strip()} – – – – – –</p>", html, flags=re.S)
    return html


# ---------------------------------------------------------------- Bausteine
def datei_html(pfad: Path, modus: str, schueler: bool = False) -> str:
    """modus: 'voll' | 'kv' (ohne Lehrer-/Lösungsteile) | 'ohne_a' (ohne Teil A)."""
    md = pfad.read_text(encoding="utf-8")
    if modus == "ohne_a":
        md = nur_ohne_teil_a(md)
    md = kaesten_zu_tabellen(md)
    md = ersetze_dreiecke(md)
    html = P.pandoc_html(P.md_vorbereiten(md, modus == "kv"))
    if schueler:
        html = re.sub(r"<h1[^>]*>.*?</h1>", "", html, flags=re.S)
        html = re.sub(r"<h2[^>]*>[^<]*(Teil [A-Z]|Kopiervorlage)[^<]*</h2>", "", html)
    html = re.sub(r'^\s*<div class="seitenumbruch"></div>', "", html)
    return html_fuer_word(html)


def svgs_rendern():
    offen = {n: s for n, s in SVG_AUFTRAEGE.items() if not (TMP / n).exists()}
    if not offen:
        return
    auftrag = TMP / "svgs.json"
    auftrag.write_text(json.dumps({str(TMP / n): s for n, s in offen.items()}), encoding="utf-8")
    js = TMP / "svg.js"
    js.write_text(r"""
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const auftraege = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 3 });
  for (const [pfad, svg] of Object.entries(auftraege)) {
    await page.setContent(`<html><body style="margin:0;background:#fff">${svg}</body></html>`);
    await page.locator('svg').first().screenshot({ path: pfad, omitBackground: false });
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
""", encoding="utf-8")
    subprocess.run(["node", str(js), str(auftrag)], check=True)


def referenz_docx() -> Path:
    ref = TMP / "referenz.docx"
    if ref.exists():
        return ref
    with open(ref, "wb") as f:
        f.write(subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                               capture_output=True, check=True).stdout)
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    d = Document(ref)
    for s in d.sections:
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.left_margin = s.right_margin = Cm(1.8)
        s.top_margin, s.bottom_margin = Cm(1.6), Cm(1.6)
    groessen = {"Normal": 11, "Body Text": 11, "First Paragraph": 11, "Compact": 11,
                "Title": 20, "Heading 1": 16, "Heading 2": 13.5, "Heading 3": 12, "Heading 4": 11}
    for name, pt in groessen.items():
        try:
            st = d.styles[name]
        except KeyError:
            continue
        st.font.name = "Arial"
        st.font.size = Pt(pt)
        rpr = st.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is None:
            fonts = OxmlElement("w:rFonts")
            rpr.append(fonts)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            fonts.set(qn(a), "Arial")
        if name.startswith("Heading") or name == "Title":
            st.font.color.rgb = RGBColor(0, 0, 0)
            farbe = rpr.find(qn("w:color"))
            if farbe is not None:
                for attr in ("w:themeColor", "w:themeShade", "w:themeTint"):
                    farbe.attrib.pop(qn(attr), None)
            st.font.bold = True
        pf = st.paragraph_format
        pf.space_before = Pt(8 if name.startswith("Heading") else 0)
        pf.space_after = Pt(4)
    d.save(ref)
    return ref


def nachbearbeiten(pfad: Path):
    from docx import Document
    from docx.enum.text import WD_BREAK
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    d = Document(pfad)
    for p in d.paragraphs:
        if UMBRUCH in p.text:
            for r in p.runs:
                r.text = ""
            (p.runs[0] if p.runs else p.add_run()).add_break(WD_BREAK.PAGE)
    for t in d.tables:
        tblpr = t._tbl.tblPr
        alt = tblpr.find(qn("w:tblBorders"))
        if alt is not None:
            tblpr.remove(alt)
        rahmen = OxmlElement("w:tblBorders")
        for seite in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement(f"w:{seite}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")
            el.set(qn("w:color"), "808080")
            rahmen.append(el)
        tblpr.append(rahmen)
    d.save(pfad)


def schreibe_docx(html_teile: list[str], ziel: Path, titel: str):
    svgs_rendern()
    html = (f'<!doctype html><html lang="de"><head><meta charset="utf-8"></head><body>'
            + f"<p>{UMBRUCH}</p>".join(html_teile) + "</body></html>")
    quelle = TMP / (ziel.stem + ".html")
    quelle.write_text(html, encoding="utf-8")
    ziel.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pandoc", "-f", "html", "-t", "docx", "--reference-doc", str(referenz_docx()),
                    "--resource-path", str(TMP), "-o", str(ziel), str(quelle)], check=True)
    nachbearbeiten(ziel)
    print("DOCX:", ziel)


def deckblatt(titel: str, untertitel: str, eintraege: list[str]) -> str:
    return (f"<h1>{titel}</h1><p><em>{untertitel}</em></p><ol>"
            + "".join(f"<li>{e}</li>" for e in eintraege) + "</ol>")


# ---------------------------------------------------------------- main
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    einheit = Path(sys.argv[1]).resolve()
    readme = einheit / "README.md"
    einheit_titel = (readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
                     if readme.exists() else einheit.name)
    mat = einheit / "material"
    material = sorted(mat.glob("M*.md"), key=P.natuerlich)

    # Planung
    for p in sorted(einheit.glob("0*.md")) + ([readme] if readme.exists() else []):
        schreibe_docx([datei_html(p, "voll")], einheit / "docx" / (p.stem + ".docx"), P.titel_von(p))

    if material:
        ziel = mat / "docx"
        for p in material:
            schreibe_docx([datei_html(p, "voll")], ziel / (p.stem + ".docx"), P.titel_von(p))
        schreibe_docx([deckblatt(einheit_titel, "Kopiervorlagen – ohne Lehrer- und Lösungsteile",
                                 [P.titel_von(p) for p in material])] + [datei_html(p, "kv") for p in material],
                      ziel / "00-kopiervorlagen.docx", einheit_titel)

        ab_muster = re.compile(r"(feder|gewicht|stationen|messprotokoll|gutachten|schichtauftrag)", re.I)
        arbeitsblaetter = [p for p in material if ab_muster.search(p.name) and "loesung" not in p.name]
        if arbeitsblaetter:
            teile = [deckblatt(einheit_titel, "Arbeitsblätter – Schülerfassung", [P.titel_von(p) for p in arbeitsblaetter])]
            vorhanden = einheit / "vorhandenes-material"
            for p in arbeitsblaetter:
                teile.append(datei_html(p, "kv", schueler=True))
                m = re.match(r"M(\d+)\.\d+-.*feder", p.name)
                if m and vorhanden.exists() and list(vorhanden.glob(f"AB{m.group(1)}-Gewicht*")):
                    datei = sorted(vorhanden.glob(f"AB{m.group(1)}-Gewicht*.pptx")) or sorted(vorhanden.glob(f"AB{m.group(1)}-Gewicht*"))
                    teile.append(f"<h2>◼ Gewicht – AB{m.group(1)}</h2><p>Hier kommt dein vorhandenes Arbeitsblatt hinein: "
                                 f"<code>vorhandenes-material/{datei[0].name}</code>.</p>")
            schreibe_docx(teile, ziel / "00-arbeitsblaetter-schueler.docx", einheit_titel)

        loesungen = [p for p in material if "loesung" in p.name]
        if loesungen:
            schreibe_docx([deckblatt(einheit_titel, "Lösungsblätter für die Lehrkraft", [P.titel_von(p) for p in loesungen])]
                          + [datei_html(p, "voll") for p in loesungen], ziel / "00-loesungen-lehrkraft.docx", einheit_titel)

        hilfen = [p for p in material if re.search(r"(hilfekarten|methodenkarte|merkblatt|wortspeicher)", p.name)]
        if hilfen:
            teile = [deckblatt(einheit_titel, "Hilfekarten und Merkblätter", [P.titel_von(p) for p in hilfen])]
            for p in hilfen:
                teile.append(datei_html(p, "ohne_a" if "merkblatt" in p.name else "kv"))
            schreibe_docx(teile, ziel / "00-hilfekarten-merkblaetter.docx", einheit_titel)

    bew = einheit / "bewertung"
    bew_dateien = sorted(einheit.glob("02-diagnose*.md")) + (sorted(bew.glob("*.md"), key=P.natuerlich) if bew.exists() else [])
    for p in bew_dateien:
        schreibe_docx([datei_html(p, "voll")], bew / "docx" / (p.stem + ".docx"), P.titel_von(p))


if __name__ == "__main__":
    main()
