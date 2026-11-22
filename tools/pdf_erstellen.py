#!/usr/bin/env python3
"""
Erzeugt druckfertige PDFs aus den Markdown-Materialien einer Einheit.

    python3 tools/pdf_erstellen.py unterricht/mathematik-brueche-dezimalzahlen

Ergebnis in <einheit>/material/pdf/ (außerdem aufgabenpool/pdf/ und bewertung/pdf/ für Diagnose,
Exit-Tickets und Klassenarbeit, falls vorhanden):
  - 00-kopiervorlagen.pdf   alle Materialien OHNE Lehrer- und Lösungsteile (zum Kopieren)
  - 00-komplett.pdf         alle Materialien vollständig (Lehrerteil, Kopiervorlagen, Lösungen)
  - M*.pdf                  jedes Material einzeln, vollständig

Benötigt: pandoc und Node.js mit Playwright/Chromium.
Layout-Regeln:
  - Jeder "## Teil …"-Abschnitt beginnt auf einer neuen Seite.
  - Zeilen "> ✂ ---------- Titel ----------" werden zu Schnittlinien; der folgende Block
    (bis zur nächsten Schnittlinie / Überschrift 2) wird möglichst nicht über Seiten getrennt.
  - Abschnitte, deren Überschrift "Lehrkraft", "Lösung" oder "nicht austeilen" enthält,
    fehlen in den Kopiervorlagen.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dreieck_svg import ersetze_dreiecke  # noqa: E402

LEHRER_MUSTER = re.compile(r"lehrkraft|lehrerteil|lösung|nicht (mit )?austeilen|lehrer-", re.I)
SCHNITT = re.compile(r"^>\s*✂\s*-*\s*(.*?)\s*-*\s*$")

CSS = """
@page { size: A4; margin: 14mm 14mm 16mm 14mm; }
:root { --ink:#1a1a1a; --muted:#555; --line:#999; --soft:#f3f3f3; }
html { font-family: "Liberation Sans", "DejaVu Sans", "Noto Color Emoji", sans-serif;
       font-size: 10.5pt; color: var(--ink); line-height: 1.38; }
body { margin: 0; }
h1 { font-size: 17pt; margin: 0 0 6pt; border-bottom: 2px solid var(--ink); padding-bottom: 3pt; }
h2 { font-size: 13.5pt; margin: 0 0 6pt; padding: 3pt 6pt; background: var(--soft);
     border-left: 4px solid var(--ink); }
h3 { font-size: 12pt; margin: 10pt 0 4pt; }
h4 { font-size: 11pt; margin: 8pt 0 3pt; }
p, ul, ol { margin: 3pt 0 5pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 8pt; font-size: 9.5pt;
        break-inside: auto; }
tr { break-inside: avoid; }
th, td { border: 1px solid var(--line); padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: var(--soft); }
pre { font-family: "DejaVu Sans Mono", "Liberation Mono", "Noto Color Emoji", monospace;
      font-size: 9pt; line-height: 1.25; background: #fafafa; border: 1px solid #ddd;
      padding: 5pt 7pt; white-space: pre; overflow: hidden; break-inside: avoid; margin: 4pt 0 8pt; }
code { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 9.2pt; }
blockquote { margin: 4pt 0 6pt; padding: 2pt 8pt; border-left: 3px solid var(--line); color: #333; }
hr { display: none; }
.seitenumbruch { break-before: page; }
.material + .material { break-before: page; }
.schnitt { display: flex; align-items: center; gap: 6pt; color: var(--muted); font-size: 8.5pt;
           margin: 10pt 0 4pt; }
.schnitt::before, .schnitt::after { content: ""; flex: 1; border-top: 1.2px dashed var(--line); }
.karte.kurz { break-inside: avoid; }
.grafik { margin: 4pt 0 6pt; break-inside: avoid; }
.rechenfeld { box-sizing: border-box; width: 100%; border: 1px solid #888; margin: 3pt 0 8pt; break-inside: avoid; min-height: 3cm;
  background-image: linear-gradient(#b4b4b4 1px, transparent 1px),
                    linear-gradient(90deg, #b4b4b4 1px, transparent 1px);
  background-size: 5mm 5mm; }
.kopf { display: flex; justify-content: space-between; font-size: 9.5pt; color: #333;
  border-bottom: 1px solid #999; padding-bottom: 3pt; margin-bottom: 6pt; }
.grafik svg { max-width: 100%; height: auto; }
h1, h2, h3, h4, .schnitt { break-after: avoid; }
h3 + p, h3 + table { break-before: avoid; }
.titelseite { text-align: center; padding-top: 60mm; }
.titelseite h1 { border: none; font-size: 24pt; }
.titelseite p { color: var(--muted); }
.inhalt { margin: 14mm auto 0; text-align: left; width: 70%; }
.inhalt li { margin: 2pt 0; }
"""


def md_vorbereiten(text: str, nur_kopiervorlagen: bool) -> str:
    """Fügt Seitenumbrüche/Schnittlinien als Pandoc-Divs ein, filtert Lehrerteile."""
    zeilen = text.splitlines()
    aus: list[str] = []
    im_code = False
    karte_offen = False
    abschnitt_ausgeblendet = False
    erste_h2 = True

    karte: list[str] = []

    def karte_schliessen():
        nonlocal karte_offen, karte
        if karte_offen:
            # Nur kurze Karten (passen sicher auf eine Seite) nicht trennen,
            # sonst entstehen fast leere Seiten vor langen Kopiervorlagen.
            inhalt = [z for z in karte if z.strip()]
            klasse = "karte kurz" if len(inhalt) <= 28 and sum(z.count("|") for z in inhalt) < 120 else "karte"
            aus.append("")
            aus.append(f"::: {{.{klasse.replace(' ', ' .')}}}")
            aus.extend(karte)
            aus.append(":::")
            aus.append("")
            karte_offen = False
            karte = []

    for zeile in zeilen:
        if zeile.lstrip().startswith("```"):
            im_code = not im_code
            if not abschnitt_ausgeblendet:
                (karte if karte_offen else aus).append(zeile)
            continue
        if im_code:
            if not abschnitt_ausgeblendet:
                (karte if karte_offen else aus).append(zeile)
            continue

        if zeile.startswith("## "):
            karte_schliessen()
            abschnitt_ausgeblendet = nur_kopiervorlagen and bool(LEHRER_MUSTER.search(zeile))
            if abschnitt_ausgeblendet:
                continue
            if not erste_h2:
                aus.append('<div class="seitenumbruch"></div>')
                aus.append("")
            erste_h2 = False
            aus.append(zeile)
            continue
        if abschnitt_ausgeblendet:
            continue
        if zeile.strip() == "---":
            continue
        m = SCHNITT.match(zeile)
        if m:
            karte_schliessen()
            karte = [f'<div class="schnitt">✂ {m.group(1)}</div>', ""]
            karte_offen = True
            continue
        (karte if karte_offen else aus).append(zeile)
    karte_schliessen()
    return "\n".join(aus) + "\n"


SVG_BLOCK = re.compile(r"<svg\b.*?</svg>", re.S)


def pandoc_html(md: str) -> str:
    # SVG-Grafiken vor Pandoc schützen (sonst werden <text>-Elemente herausgelöst)
    svgs: list[str] = []

    def merken(m):
        svgs.append(m.group(0))
        return f"\n\nSVGPLATZHALTER{len(svgs) - 1}ENDE\n\n"

    md = ersetze_dreiecke(md)
    md = SVG_BLOCK.sub(merken, md)
    erg = subprocess.run(
        ["pandoc", "-f", "markdown+pipe_tables+fenced_divs-tex_math_dollars-raw_tex+hard_line_breaks"
         "-yaml_metadata_block-subscript-superscript", "-t", "html5", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True)
    html = erg.stdout
    for i, svg in enumerate(svgs):
        html = re.sub(rf"(<p>)?SVGPLATZHALTER{i}ENDE(</p>)?", lambda _m, svg=svg: f'<div class="grafik">{svg}</div>', html)
    return html


def html_seite(titel: str, koerper: str) -> str:
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{titel}</title>'
            f"<style>{CSS}</style></head><body>{koerper}</body></html>")


NODE_SKRIPT = r"""
const { chromium } = require('playwright');
(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const j of jobs) {
    await page.goto('file://' + j.html, { waitUntil: 'load' });
    await page.pdf({
      path: j.pdf, format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-size:7.5pt;color:#777;width:100%;padding:0 14mm;
        font-family:Liberation Sans,sans-serif;display:flex;justify-content:space-between">
        <span>${j.fuss}</span><span>Seite <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    });
    console.log('PDF: ' + j.pdf);
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
"""


def natuerlich(p: Path):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", p.name)]


def titel_von(p: Path) -> str:
    return p.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()


def sammlung(dateien: list[Path], ziel: Path, einheit_titel: str, art: str, tmp: Path, jobs: list):
    """Sammel-PDFs (Kopiervorlagen + komplett) und Einzel-PDFs für eine Gruppe von Dateien."""
    ziel.mkdir(exist_ok=True)
    for variante, dateiname, untertitel in [
        (True, "00-kopiervorlagen.pdf", f"{art} · Kopiervorlagen – ohne Lehrer- und Lösungsteile"),
        (False, "00-komplett.pdf", f"{art} · Komplett – mit Lehrerteilen und Lösungen"),
    ]:
        teile = []
        for p in dateien:
            html = pandoc_html(md_vorbereiten(p.read_text(encoding="utf-8"), variante))
            teile.append(f'<section class="material">{html}</section>')
        inhalt = "".join(f"<li>{titel_von(p)}</li>" for p in dateien)
        titel = (f'<section class="titelseite"><h1>{einheit_titel}</h1><p>{untertitel}</p>'
                 f'<ol class="inhalt">{inhalt}</ol></section>'
                 f'<div class="seitenumbruch"></div>')
        h = tmp / f"{ziel.parent.name}-{dateiname.replace('.pdf', '.html')}"
        h.write_text(html_seite(einheit_titel, titel + "".join(teile)), encoding="utf-8")
        jobs.append({"html": str(h), "pdf": str(ziel / dateiname),
                     "fuss": f"{einheit_titel} · {untertitel.split(' –')[0]}"})
    for p in dateien:
        html = pandoc_html(md_vorbereiten(p.read_text(encoding="utf-8"), False))
        h = tmp / (p.stem + ".html")
        h.write_text(html_seite(titel_von(p), f'<section class="material">{html}</section>'), encoding="utf-8")
        jobs.append({"html": str(h), "pdf": str(ziel / (p.stem + ".pdf")), "fuss": titel_von(p)})


def _blatt(p: Path, modus: str, schueler: bool = False) -> str:
    md = p.read_text(encoding="utf-8")
    if modus == "ohne_a":
        md = "".join(t for t in re.split(r"(?m)^(?=## )", md) if not re.match(r"## Teil A", t))
    html = pandoc_html(md_vorbereiten(md, modus == "kv"))
    if schueler:
        html = re.sub(r"<h1[^>]*>.*?</h1>", "", html, flags=re.S)
        html = re.sub(r"<h2[^>]*>[^<]*(Teil [A-Z]|Kopiervorlage)[^<]*</h2>", "", html)
    return re.sub(r'^\s*<div class="seitenumbruch"></div>', "", html)


def zusammenstellungen(einheit: Path, einheit_titel: str, material: list[Path], tmp: Path, jobs: list):
    """Sammel-PDFs für den Alltag: Arbeitsblätter (Schülerfassung), Lösungen, Hilfekarten + Merkblätter.
    Ein vorhandenes Original (vorhandenes-material/AB<n>-Gewicht*.pdf) wird hinter die Feder-Fassung einsortiert."""
    ziel = einheit / "material" / "pdf"
    muster = re.compile(r"(feder|gewicht|stationen|messprotokoll|gutachten|schichtauftrag)", re.I)
    gruppen = {
        "00-arbeitsblaetter-schueler.pdf": [(p, "kv", True) for p in material if muster.search(p.name) and "loesung" not in p.name],
        "00-loesungen-lehrkraft.pdf": [(p, "voll", False) for p in material if "loesung" in p.name],
        "00-hilfekarten-merkblaetter.pdf": [(p, "ohne_a" if "merkblatt" in p.name else "kv", False)
                                            for p in material if re.search(r"(hilfekarten|methodenkarte|merkblatt|wortspeicher)", p.name)],
    }
    vorhanden = einheit / "vorhandenes-material"
    for dateiname, liste in gruppen.items():
        if not liste:
            continue
        teile = []  # Folge aus ("html", pfad) und ("pdf", pfad)
        for p, modus, schueler in liste:
            h = tmp / f"sammel-{dateiname}-{p.stem}.html"
            titel = "" if schueler else f"<h1>{titel_von(p)}</h1>" if modus != "voll" else ""
            h.write_text(html_seite(p.stem, f'<section class="material">{titel}{_blatt(p, modus, schueler)}</section>'), encoding="utf-8")
            einzel = tmp / f"sammel-{dateiname}-{p.stem}.pdf"
            jobs.append({"html": str(h), "pdf": str(einzel), "fuss": f"{einheit_titel} · {titel_von(p)}"})
            teile.append(einzel)
            m = re.match(r"M(\d+)\.\d+-.*feder", p.name)
            if schueler and m and vorhanden.exists():
                orig = sorted(vorhanden.glob(f"AB{m.group(1)}-Gewicht*.pdf"))
                if orig:
                    teile.append(orig[0])
        ZUSAMMENFUEGEN.append((teile, ziel / dateiname))


ZUSAMMENFUEGEN: list = []


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    einheit = Path(sys.argv[1]).resolve()
    einheit_titel = einheit.name.replace("-", " ").title()
    readme = einheit / "README.md"
    if readme.exists():
        erste = readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        einheit_titel = erste or einheit_titel

    tmp = Path(tempfile.mkdtemp(prefix="pdf_"))
    jobs: list = []
    mat = einheit / "material"
    material = sorted(mat.glob("M*.md"), key=natuerlich)
    if material:
        sammlung(material, mat / "pdf", einheit_titel, "Unterrichtsmaterial", tmp, jobs)

    pool = einheit / "aufgabenpool"
    if (pool / "index.csv").exists():
        reihenfolge = [z.split(";")[2].strip() for z in
                       (pool / "index.csv").read_text(encoding="utf-8").splitlines()[1:] if z.count(";") >= 2]
        pool_dateien = [pool / d for d in reihenfolge if (pool / d).exists()]
        if pool_dateien:
            sammlung(pool_dateien, pool / "pdf", einheit_titel, "Aufgabenpool", tmp, jobs)

    bew = einheit / "bewertung"
    diag = sorted(einheit.glob("02-diagnose*.md"))
    bew_dateien = diag + sorted(bew.glob("*.md"), key=natuerlich) if bew.exists() else diag
    if bew_dateien:
        bew.mkdir(exist_ok=True)
        sammlung(bew_dateien, bew / "pdf", einheit_titel, "Diagnose und Bewertung", tmp, jobs)

    if not jobs:
        sys.exit(f"Keine Materialien in {einheit}")
    zusammenstellungen(einheit, einheit_titel, material, tmp, jobs)
    js = tmp / "drucken.js"
    js.write_text(NODE_SKRIPT, encoding="utf-8")
    subprocess.run(["node", str(js), json.dumps(jobs)], check=True)
    if ZUSAMMENFUEGEN:
        from pypdf import PdfReader, PdfWriter
        for teile, ziel in ZUSAMMENFUEGEN:
            w = PdfWriter()
            for t in teile:
                for seite in PdfReader(str(t)).pages:
                    w.add_page(seite)
            w.write(str(ziel))
            print(f"PDF: {ziel} ({len(w.pages)} Seiten)")


if __name__ == "__main__":
    main()
