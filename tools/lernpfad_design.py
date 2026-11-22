#!/usr/bin/env python3
"""
Lernpfad-Design: die Arbeitsblätter einer Einheit als spielerische Fassung (Lernpfad, XP, Abzeichen).

    python3 tools/lernpfad_design.py unterricht/mathematik-trigonometrie

Ergebnis in <einheit>/material/pdf-lernpfad/:
  00-lernpass.pdf                    Lernpass für die ganze Reihe (Level, Abzeichen, XP-Konto, Exit-Ticket-Serie)
  00-arbeitsblaetter-lernpfad.pdf    alle Arbeitsblätter im Lernpfad-Design
  M*.pdf                             jedes Arbeitsblatt einzeln

Inhalt = dieselben Markdown-Dateien wie im klassischen Design; nur Darstellung und Spiel-Elemente
kommen hinzu: Pfad der Aufgaben oben, Aufgaben als Karten mit XP, „Geschafft“-Häkchen, Hilfe-Hinweis,
XP-Zähler und Abzeichen am Blattende.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pdf_erstellen as P  # noqa: E402

XP = {"pflicht": 10, "bonus": 15, "profi": 25, "schritt": 5}
ABZEICHEN = {1: ("Kalibriert", "Verhältnisse am Dreieck"), 2: ("Feuerwehr-Profi", "Winkel berechnen & umstellen"),
             3: ("Dachvermesser:in", "draußen gemessen"), 4: ("Zerlegungs-Ass", "Dreiecke zerlegt"),
             5: ("Sinus-Entdecker:in", "Sinussatz gefunden"), 6: ("Baustellen-Ass", "Sinussatz angewendet"),
             7: ("Kosinus-Knacker:in", "Kosinussatz geknackt"), 8: ("Gutachter:in", "Auftrag gewonnen")}

THEO = ('<svg class="theo" width="{s}" height="{s}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
        '<polygon points="8,8 8,92 92,92" fill="#7C3AED" stroke="#4C1D95" stroke-width="3" stroke-linejoin="round"/>'
        '<circle cx="26" cy="62" r="9" fill="#fff"/><circle cx="46" cy="62" r="9" fill="#fff"/>'
        '<circle cx="28" cy="64" r="4" fill="#1E1B4B"/><circle cx="48" cy="64" r="4" fill="#1E1B4B"/>'
        '<path d="M24 76 Q36 86 48 76" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>')

ABZEICHEN_SVG = ('<svg width="74" height="74" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
                 '<circle cx="50" cy="50" r="44" fill="#FEF3C7" stroke="#F59E0B" stroke-width="6" stroke-dasharray="{dash}"/>'
                 '<polygon points="50,20 58,40 80,41 63,55 69,77 50,64 31,77 37,55 20,41 42,40" fill="#F59E0B"/>'
                 '<text x="50" y="58" text-anchor="middle" font-family="Liberation Sans" font-weight="700" font-size="18" fill="#7C2D12">{nr}</text></svg>')

CSS = """
@page { size: A4; margin: 12mm 13mm 14mm 13mm; }
:root { --lila:#7C3AED; --dunkel:#1E1B4B; --tief:#4C1D95; --hell:#F4F1FF; --rand:#DDD6FE;
        --gruen:#16A34A; --gruenhell:#DCFCE7; --gelb:#F59E0B; --gelbhell:#FEF3C7; --blau:#0EA5E9; }
html { font-family: "Liberation Sans", "DejaVu Sans", "Noto Color Emoji", sans-serif; font-size: 10.6pt;
       color: var(--dunkel); line-height: 1.42; }
body { margin: 0; }
h1 { display: none; }
h2 { font-size: 12pt; color: var(--tief); margin: 8pt 0 4pt; }
h3 { font-size: 15pt; color: var(--tief); margin: 4pt 0 6pt; }
h4 { font-size: 12pt; margin: 0 0 4pt; color: var(--tief); }
p, ul, ol { margin: 3pt 0 5pt; }
strong { color: var(--dunkel); }
table { border-collapse: separate; border-spacing: 0; width: 100%; margin: 4pt 0 8pt; font-size: 9.8pt;
        border: 1.5px solid var(--rand); border-radius: 8px; overflow: hidden; }
th, td { border-bottom: 1px solid var(--rand); border-right: 1px solid var(--rand); padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: var(--hell); color: var(--tief); }
tr:last-child td { border-bottom: none; }
td:last-child, th:last-child { border-right: none; }
pre { font-family: "DejaVu Sans Mono", monospace; font-size: 8.8pt; background: var(--hell); border-radius: 8px;
      padding: 6pt 8pt; white-space: pre; overflow: hidden; break-inside: avoid; }
blockquote { margin: 4pt 0; padding: 4pt 10pt; background: var(--gelbhell); border-radius: 8px; border: none; }
hr { display: none; }
.seitenumbruch { break-before: page; }
.material + .material { break-before: page; }
.grafik { margin: 4pt 0 6pt; break-inside: avoid; }
.grafik svg { max-width: 100%; height: auto; }
.rechenfeld { box-sizing: border-box; width: 100%; border: 1.5px solid var(--rand); border-radius: 10px; margin: 4pt 0 6pt;
  min-height: 3cm; break-inside: avoid;
  background-image: linear-gradient(#E4DEFA 1px, transparent 1px), linear-gradient(90deg, #E4DEFA 1px, transparent 1px);
  background-size: 5mm 5mm; background-color: #fff; }
.schnitt { display: flex; align-items: center; gap: 6pt; color: #8B7FC7; font-size: 8.5pt; margin: 8pt 0 4pt; }
.schnitt::before, .schnitt::after { content: ""; flex: 1; border-top: 1.5px dashed #C4B5FD; }
.karte.kurz { break-inside: avoid; }

/* Kopf */
.lp-kopf-blatt { display: flex; align-items: center; gap: 10pt; background: var(--hell); border-radius: 14px;
  padding: 8pt 12pt; margin-bottom: 8pt; }
.lp-kopf-blatt .theo { flex: none; }
.lp-kopf-mitte { flex: 1; }
.lp-level { font-size: 9pt; font-weight: 700; color: #fff; background: var(--lila); border-radius: 20px; padding: 2pt 9pt; display: inline-block; }
.lp-niveau { font-size: 9pt; font-weight: 700; color: var(--tief); background: #fff; border: 1.5px solid var(--rand); border-radius: 20px; padding: 2pt 9pt; display: inline-block; margin-left: 4pt; }
.lp-name { font-size: 9.5pt; color: #4B5563; margin-top: 4pt; }

/* Pfad */
.lp-pfad { display: flex; align-items: center; margin: 2pt 0 10pt; padding: 6pt 10pt; border-radius: 12px; background: #fff;
  border: 1.5px solid var(--rand); gap: 0; }
.lp-pfad-titel { font-size: 8.5pt; font-weight: 700; color: var(--tief); margin-right: 8pt; white-space: nowrap; }
.lp-knoten { width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-size: 9pt; font-weight: 700; flex: none; }
.lp-knoten.pflicht { background: var(--lila); color: #fff; }
.lp-knoten.bonus { background: #fff; color: var(--lila); border: 2px dashed var(--lila); width: 18px; height: 18px; }
.lp-knoten.profi { background: var(--gelb); color: #fff; }
.lp-knoten.schritt { background: var(--blau); color: #fff; }
.lp-knoten.ziel { background: var(--gelbhell); color: #92400E; border: 2px solid var(--gelb); width: 18px; height: 18px; }
.lp-linie { flex: 1; height: 3px; background: var(--rand); min-width: 8px; }

/* Aufgabenkarten */
.lp-karte { border: 2px solid var(--rand); border-radius: 14px; padding: 6pt 10pt 4pt; margin: 0 0 9pt; background: #fff; }
.lp-karte.pflicht { border-color: #C4B5FD; }
.lp-karte.profi { border-color: var(--gelb); background: #FFFDF5; }
.lp-karte.schritt { border-color: #BAE6FD; }
.lp-karte-kopf { display: flex; align-items: center; gap: 6pt; margin-bottom: 3pt; break-after: avoid; }
.lp-nr { width: 22px; height: 22px; border-radius: 50%; background: var(--lila); color: #fff; font-weight: 700;
  display: flex; align-items: center; justify-content: center; font-size: 10pt; flex: none; }
.lp-karte.bonus .lp-nr { background: #fff; color: var(--lila); border: 2px dashed var(--lila); width: 18px; height: 18px; }
.lp-karte.profi .lp-nr { background: var(--gelb); }
.lp-karte.schritt .lp-nr { background: var(--blau); }
.lp-tag { font-size: 8pt; font-weight: 700; border-radius: 20px; padding: 1pt 7pt; background: var(--hell); color: var(--tief); }
.lp-xp { font-size: 8pt; font-weight: 700; border-radius: 20px; padding: 1pt 7pt; background: var(--gruenhell); color: var(--gruen); margin-left: auto; }
.lp-karte-fuss { display: flex; justify-content: space-between; font-size: 8.5pt; color: #6B7280; border-top: 1px dashed var(--rand);
  margin-top: 4pt; padding-top: 3pt; break-before: avoid; }
.lp-check { color: var(--gruen); font-weight: 700; }

/* Blattende */
.lp-ende { display: flex; gap: 10pt; align-items: stretch; margin-top: 8pt; break-inside: avoid; }
.lp-xpbox { flex: 1; border-radius: 14px; background: var(--gruenhell); padding: 8pt 12pt; font-size: 10pt; }
.lp-xpbox b { color: var(--gruen); }
.lp-abzeichen { flex: 1; display: flex; align-items: center; gap: 8pt; border-radius: 14px; background: var(--gelbhell); padding: 6pt 10pt; font-size: 9.5pt; }

/* Lernpass */
.lp-pass h1 { display: block; font-size: 22pt; color: var(--tief); margin: 0; }
.lp-pass .intro { display: flex; align-items: center; gap: 12pt; background: var(--hell); border-radius: 16px; padding: 10pt 14pt; }
.lp-raster { display: grid; grid-template-columns: repeat(4, 1fr); gap: 9pt; margin: 12pt 0; }
.lp-feld { border: 2px solid var(--rand); border-radius: 14px; padding: 8pt; text-align: center; font-size: 9pt; min-height: 128px; }
.lp-feld .titel { font-weight: 700; color: var(--tief); font-size: 10pt; margin: 2pt 0; }
.lp-feld .zeile { color: #6B7280; }
.lp-feld .xp { margin-top: 5pt; font-size: 9pt; }
.lp-serie { display: flex; gap: 6pt; margin: 6pt 0 10pt; }
.lp-serie div { flex: 1; border: 2px dashed var(--gelb); border-radius: 10px; text-align: center; padding: 6pt 0; font-size: 9pt; color: #92400E; }
.lp-regeln { display: grid; grid-template-columns: 1fr 1fr; gap: 9pt; }
.lp-regel { background: #fff; border: 1.5px solid var(--rand); border-radius: 12px; padding: 7pt 10pt; font-size: 9.5pt; }
"""

START = re.compile(
    r'(<p>\s*(?:<strong>\s*)?(?P<s1>★\s*)?(?:</strong>\s*)?<strong>\s*(?P<s2>★\s*)?'
    r'(?P<art>Aufgabe|Station|Schritt|Profi-Challenge|Bonus|Zusatz)\s*(?P<nr>\d+[a-z]?)?[^<]*?</strong>)'
    r'|(<h4[^>]*>\s*(?P<s3>★\s*)?(?P<art2>Teil)\s*(?P<nr2>\d+)[^<]*</h4>)')
GRENZE = re.compile(r'<h2|<h3|<div class="seitenumbruch"|<div class="karte|</div>|<p><strong>Freigabe|<p>✂|§ENDE§')


def karten(html: str) -> tuple[str, list[dict]]:
    # Rechenfelder/Grafiken schützen (sie liegen innerhalb von Aufgaben)
    geschuetzt: list[str] = []

    def merke(m):
        geschuetzt.append(m.group(0))
        return f"§G{len(geschuetzt) - 1}§"
    html = re.sub(r'<div class="rechenfeld"[^>]*>\s*</div>|<div class="grafik">.*?</div>', merke, html, flags=re.S)
    html += "§ENDE§"
    aufgaben, aus, pos = [], [], 0
    treffer = list(START.finditer(html))
    for i, m in enumerate(treffer):
        if m.start() < pos:
            continue
        aus.append(html[pos:m.start()])
        art = (m.group("art") or m.group("art2") or "").lower()
        stern = bool(m.group("s1") or m.group("s2") or m.group("s3") or "★" in m.group(0)[:200])
        nr = m.group("nr") or m.group("nr2") or ""
        if art in ("profi-challenge",):
            klasse, label = "profi", "Profi"
        elif art == "schritt":
            klasse, label = "schritt", "Messen"
        elif art in ("bonus", "zusatz"):
            klasse, label = "bonus", "Bonus"
        elif art == "station":
            klasse, label = "pflicht", "Station"
        else:
            klasse, label = ("pflicht", "Pflicht") if stern else ("bonus", "Bonus")
        nachfolger = treffer[i + 1].start() if i + 1 < len(treffer) else len(html)
        g = GRENZE.search(html, m.end())
        ende = min(nachfolger, g.start() if g else len(html))
        inhalt = html[m.start():ende]
        anzeige = nr if nr else ("★" if klasse == "profi" else "+")
        aufgaben.append({"klasse": klasse, "nr": anzeige})
        aus.append(
            f'<section class="lp-karte {klasse}"><div class="lp-karte-kopf"><span class="lp-nr">{anzeige}</span>'
            f'<span class="lp-tag">{label}</span><span class="lp-xp">+{XP[klasse]} XP</span></div>{inhalt}'
            f'<div class="lp-karte-fuss"><span class="lp-check">☐ Geschafft!</span>'
            f'<span>Hängst du fest? 💡 Hilfekarte holen · Lösung prüfen ✓</span></div></section>')
        pos = ende
    aus.append(html[pos:])
    html = "".join(aus).replace("§ENDE§", "")
    html = re.sub(r"§G(\d+)§", lambda m: geschuetzt[int(m.group(1))], html)
    return html, aufgaben


def pfad_html(aufgaben: list[dict]) -> str:
    if not aufgaben:
        return ""
    teile = ['<div class="lp-pfad"><span class="lp-pfad-titel">Dein Pfad</span>']
    for i, a in enumerate(aufgaben):
        if i:
            teile.append('<span class="lp-linie"></span>')
        teile.append(f'<span class="lp-knoten {a["klasse"]}">{a["nr"]}</span>')
    teile.append('<span class="lp-linie"></span><span class="lp-knoten ziel">🏆</span></div>')
    return "".join(teile)


def ende_html(aufgaben: list[dict], std: int) -> str:
    pflicht = sum(XP[a["klasse"]] for a in aufgaben if a["klasse"] in ("pflicht", "schritt"))
    bonus = sum(XP[a["klasse"]] for a in aufgaben if a["klasse"] == "bonus")
    profi = sum(XP[a["klasse"]] for a in aufgaben if a["klasse"] == "profi")
    name, zeile = ABZEICHEN.get(std, ("Level geschafft", ""))
    return (f'<div class="lp-ende"><div class="lp-xpbox"><b>Meine XP heute</b><br>'
            f'Pflicht: ____ / {pflicht} &nbsp; Bonus: ____ / {bonus}' + (f' &nbsp; Profi: ____ / {profi}' if profi else "") +
            f'<br><b>Summe: ______ XP</b> → in den Lernpass eintragen</div>'
            f'<div class="lp-abzeichen">{ABZEICHEN_SVG.format(dash="none", nr=std)}<div><b>Abzeichen „{name}“</b><br>'
            f'{zeile}<br>freigeschaltet, wenn alle Pflicht-Karten ☑ sind.</div></div></div>')


def kopf_ersetzen(html: str, std: int) -> str:
    def ersatz(m):
        teile = re.findall(r"<span>(.*?)</span>", m.group(0), re.S)
        rechts = teile[1] if len(teile) > 1 else ""
        niveau = rechts.split("·")[-1].strip() if "·" in rechts else ""
        return (f'<div class="lp-kopf-blatt">{THEO.format(s=46)}<div class="lp-kopf-mitte">'
                f'<span class="lp-level">LEVEL {std}</span>' + (f'<span class="lp-niveau">{niveau}</span>' if niveau else "") +
                f'<div class="lp-name">Name: ____________________ &nbsp; Datum: __________ &nbsp; Klasse 10.___</div></div></div><!--KOPFENDE-->')
    return re.sub(r'<div class="kopf">.*?</div>', ersatz, html, count=0, flags=re.S)


def blatt_html(pfad: Path) -> str:
    std = int(re.match(r"M(\d+)", pfad.name).group(1))
    md = pfad.read_text(encoding="utf-8")
    html = P.pandoc_html(P.md_vorbereiten(md, True))
    html = re.sub(r"<h2[^>]*>[^<]*(Teil [A-Z]|Kopiervorlage)[^<]*</h2>", "", html)
    html = re.sub(r'^\s*<div class="seitenumbruch"></div>', "", html)
    html, aufgaben = karten(html)
    html = kopf_ersetzen(html, std)
    pfad_teil = pfad_html(aufgaben)
    if "<!--KOPFENDE-->" in html:
        html = html.replace("<!--KOPFENDE-->", pfad_teil, 1).replace("<!--KOPFENDE-->", "")
    else:
        html = pfad_teil + html
    return html + ende_html(aufgaben, std)


def lernpass_html(einheit_titel: str, stunden: dict[int, str]) -> str:
    felder = []
    for std in range(1, 9):
        name, zeile = ABZEICHEN[std]
        felder.append(f'<div class="lp-feld">{ABZEICHEN_SVG.format(dash="8 6", nr=std)}<div class="titel">{name}</div>'
                      f'<div class="zeile">Level {std}: {zeile}</div><div class="xp">XP: ______ &nbsp; ☐ Abzeichen</div></div>')
    serie = "".join(f"<div>Exit-Ticket {i}<br>☐ 🔥</div>" for i in range(1, 9))
    return (f'<section class="material lp-pass"><div class="intro">{THEO.format(s=80)}<div><h1>Mein Lernpass</h1>'
            f'<div>{einheit_titel}</div><div class="lp-name">Name: ______________________ &nbsp; Klasse 10.___</div></div></div>'
            f'<h2>8 Level – 8 Abzeichen</h2><div class="lp-raster">{"".join(felder)}</div>'
            f'<h2>🔥 Meine Serie: Exit-Tickets</h2><p>Jedes abgegebene Exit-Ticket verlängert deine Serie – egal auf welchem Niveau.</p>'
            f'<div class="lp-serie">{serie}</div>'
            f'<h2>So funktioniert’s</h2><div class="lp-regeln">'
            f'<div class="lp-regel"><b>XP sammeln:</b> ★-Pflicht-Karte +10 XP · Bonus-Karte +15 XP · Profi-Challenge +25 XP · Mess-Schritt +5 XP.</div>'
            f'<div class="lp-regel"><b>Abzeichen:</b> Alle Pflicht-Karten eines Levels ☑ → Abzeichen ausmalen.</div>'
            f'<div class="lp-regel"><b>Niveau frei wählen:</b> 🪶 Feder, ◼ Gewicht oder ◼◼ Doppelgewicht – du darfst jederzeit wechseln. XP zählen überall gleich.</div>'
            f'<div class="lp-regel"><b>Feststecken ist erlaubt:</b> 1. Wortspeicher · 2. Hilfekarte · 3. Partner:in fragen · 4. Lehrkraft. Fehler gehören zum Lernen.</div>'
            f'<div class="lp-regel"><b>Klassen-Ziel:</b> Alle XP der Klasse zusammen füllen den Balken an der Tafel – wir spielen miteinander, nicht gegeneinander.</div>'
            f'<div class="lp-regel"><b>Meine Gesamt-XP:</b> ________ &nbsp; Bestes Level: ________</div></div></section>')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    einheit = Path(sys.argv[1]).resolve()
    mat = einheit / "material"
    ziel = mat / "pdf-lernpfad"
    ziel.mkdir(exist_ok=True)
    readme = einheit / "README.md"
    einheit_titel = readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip() if readme.exists() else einheit.name
    muster = re.compile(r"(feder|gewicht|stationen|messprotokoll|gutachten)", re.I)
    blaetter = [p for p in sorted(mat.glob("M*.md"), key=P.natuerlich) if muster.search(p.name) and "loesung" not in p.name]
    tmp = Path(tempfile.mkdtemp(prefix="lernpfad_"))
    css_alt = P.CSS
    P.CSS = CSS
    jobs = []
    pass_html = tmp / "lernpass.html"
    pass_html.write_text(P.html_seite("Lernpass", lernpass_html(einheit_titel, {})), encoding="utf-8")
    jobs.append({"html": str(pass_html), "pdf": str(ziel / "00-lernpass.pdf"), "fuss": f"{einheit_titel} · Lernpass"})
    teile = []
    for p in blaetter:
        h = blatt_html(p)
        teile.append(f'<section class="material">{h}</section>')
        datei = tmp / (p.stem + ".html")
        datei.write_text(P.html_seite(p.stem, f'<section class="material">{h}</section>'), encoding="utf-8")
        jobs.append({"html": str(datei), "pdf": str(ziel / (p.stem + ".pdf")),
                     "fuss": f"Level {re.match(r'M(\d+)', p.name).group(1)} · {P.titel_von(p)}"})
    gesamt = tmp / "alle.html"
    gesamt.write_text(P.html_seite("Lernpfad", "".join(teile)), encoding="utf-8")
    jobs.append({"html": str(gesamt), "pdf": str(ziel / "00-arbeitsblaetter-lernpfad.pdf"), "fuss": f"{einheit_titel} · Lernpfad"})
    P.CSS = css_alt
    js = tmp / "d.js"
    js.write_text(P.NODE_SKRIPT, encoding="utf-8")
    subprocess.run(["node", str(js), json.dumps(jobs)], check=True)


if __name__ == "__main__":
    main()
