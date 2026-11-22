#!/usr/bin/env python3
"""
Erzeugt druckfertige PDFs aus den Markdown-Materialien einer Einheit.

    python3 tools/pdf_erstellen.py unterricht/mathematik-brueche-dezimalzahlen

Ergebnis in <einheit>/material/pdf/:
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


def pandoc_html(md: str) -> str:
    erg = subprocess.run(
        ["pandoc", "-f", "markdown+pipe_tables+fenced_divs-tex_math_dollars-raw_tex+hard_line_breaks"
         "-yaml_metadata_block-subscript-superscript", "-t", "html5", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True)
    return erg.stdout


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


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    einheit = Path(sys.argv[1]).resolve()
    mat = einheit / "material"
    dateien = sorted(mat.glob("M*.md"), key=lambda p: [int(x) if x.isdigit() else x
                                                        for x in re.split(r"(\d+)", p.name)])
    if not dateien:
        sys.exit(f"Keine Materialien in {mat}")
    ziel = mat / "pdf"
    ziel.mkdir(exist_ok=True)
    einheit_titel = einheit.name.replace("-", " ").title()
    readme = einheit / "README.md"
    if readme.exists():
        erste = readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        einheit_titel = erste or einheit_titel

    def titel_von(p: Path) -> str:
        z = p.read_text(encoding="utf-8").splitlines()[0]
        return z.lstrip("# ").strip()

    tmp = Path(tempfile.mkdtemp(prefix="pdf_"))
    jobs = []
    for variante, dateiname, untertitel in [
        (True, "00-kopiervorlagen.pdf", "Kopiervorlagen – ohne Lehrer- und Lösungsteile"),
        (False, "00-komplett.pdf", "Komplett – mit Lehrerteilen und Lösungen"),
    ]:
        teile = []
        for p in dateien:
            html = pandoc_html(md_vorbereiten(p.read_text(encoding="utf-8"), variante))
            teile.append(f'<section class="material">{html}</section>')
        inhalt = "".join(f"<li>{titel_von(p)}</li>" for p in dateien)
        titel = (f'<section class="titelseite"><h1>{einheit_titel}</h1><p>{untertitel}</p>'
                 f'<ol class="inhalt">{inhalt}</ol></section>'
                 f'<div class="seitenumbruch"></div>')
        h = tmp / dateiname.replace(".pdf", ".html")
        h.write_text(html_seite(einheit_titel, titel + "".join(teile)), encoding="utf-8")
        jobs.append({"html": str(h), "pdf": str(ziel / dateiname), "fuss": f"{einheit_titel} · {untertitel.split(' –')[0]}"})

    for p in dateien:
        html = pandoc_html(md_vorbereiten(p.read_text(encoding="utf-8"), False))
        h = tmp / (p.stem + ".html")
        h.write_text(html_seite(titel_von(p), f'<section class="material">{html}</section>'), encoding="utf-8")
        jobs.append({"html": str(h), "pdf": str(ziel / (p.stem + ".pdf")), "fuss": titel_von(p)})

    js = tmp / "drucken.js"
    js.write_text(NODE_SKRIPT, encoding="utf-8")
    subprocess.run(["node", str(js), json.dumps(jobs)], check=True)


if __name__ == "__main__":
    main()
