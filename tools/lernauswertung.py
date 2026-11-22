#!/usr/bin/env python3
"""
Lernauswertung – wertet Tests, Exit-Tickets und Klassenarbeiten aus.

Nur Python-Standardbibliothek, damit es auf jedem Schulrechner läuft.

Zwei Modi:

  test     Einen Test auswerten (Item-Analyse, Niveaustufen, Fehlerbilder, Einzelprofile)
           python3 tools/lernauswertung.py test \
               --schluessel unterricht/.../auswertung/eingangstest.schluessel.csv \
               --ergebnisse klassen/7b/2026-11-24_eingangstest.csv \
               --out klassen/7b/auswertungen/2026-11-24_eingangstest.md \
               [--gruppen "keine:🌱,C:🌿,D:🌿,E:🌳"] [--schwelle 0.66] [--anonym]

  verlauf  Lernentwicklung über mehrere Tests
           python3 tools/lernauswertung.py verlauf \
               --index klassen/7b/tests.csv \
               --out klassen/7b/auswertungen/verlauf.md [--anonym]

Dateiformate (CSV, Trennzeichen ; oder , – Excel-Export "CSV (Trennzeichen-getrennt)" funktioniert):

  Schlüssel:  item;max_punkte;niveau;kompetenz;wahlblock;beschreibung
              (wahlblock leer = Pflicht; gleicher Name = Schüler:in wählt eine Variante)
  Ergebnisse: kuerzel;<item1>;<item2>;...
              Zelle  "1" / "0,5"          = Punkte
                     "0:LG" / "0,5:TR+KV" = Punkte + Fehlerbild-Kürzel
                     "-"                  = bearbeitet bzw. vorgelegt, aber leer (0 Punkte)
                     leer                 = nicht vorgelegt / andere Wahlvariante (zählt nicht)
  Index:      datum;test;schluessel;ergebnisse   (Pfade relativ zur Index-Datei oder zum Projekt)

Datenschutz: Nur Kürzel (S01, S02, ...) verwenden. --anonym unterdrückt alle Einzelangaben,
damit der Bericht ins Repository darf.
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

NIVEAU_ORDNUNG = "ABCDEFGH"


# --------------------------------------------------------------------------- Einlesen
def lies_csv(pfad: Path) -> list[dict[str, str]]:
    text = pfad.read_text(encoding="utf-8-sig")
    try:
        dialekt = csv.Sniffer().sniff(text.splitlines()[0], delimiters=";,\t")
    except csv.Error:
        dialekt = csv.excel
        dialekt.delimiter = ";"
    zeilen = list(csv.DictReader(io.StringIO(text), dialect=dialekt))
    sauber = []
    for z in zeilen:
        rest = z.pop(None, None)  # überzählige Felder (z. B. Trennzeichen im Text)
        if rest and any(str(r).strip() for r in rest):
            print(f"Hinweis: Zeile mit zu vielen Feldern in {pfad.name}: {rest}", file=sys.stderr)
        zeile = {(k or "").strip(): (v or "").strip() for k, v in z.items()}
        if any(zeile.values()):
            sauber.append(zeile)
    return sauber


def zahl(text: str) -> float:
    return float(text.replace(",", "."))


ZELLE = re.compile(r"^\s*(-|[0-9]+(?:[.,][0-9]+)?)\s*(?:[:\s]\s*([A-Za-zÄÖÜäöü0-9+/ _-]+))?\s*$")


def parse_zelle(text: str):
    """-> (punkte | None, [fehlerbilder]) ; None = nicht vorgelegt"""
    if text == "":
        return None, []
    m = ZELLE.match(text)
    if not m:
        raise ValueError(f"Zelle nicht lesbar: '{text}' (erlaubt: 1 | 0,5 | 0:LG | - | leer)")
    punkte = 0.0 if m.group(1) == "-" else zahl(m.group(1))
    codes = [c.strip().upper() for c in re.split(r"[+/ ]", m.group(2) or "") if c.strip()]
    return punkte, codes


class Test:
    def __init__(self, schluessel: Path, ergebnisse: Path, name: str | None = None):
        self.name = name or ergebnisse.stem
        self.items: dict[str, dict] = {}
        for z in lies_csv(schluessel):
            iid = z.get("item", "")
            if not iid:
                continue
            self.items[iid] = {
                "max": zahl(z.get("max_punkte", "1") or "1"),
                "niveau": (z.get("niveau", "") or "?").upper()[:1],
                "kompetenz": z.get("kompetenz", "") or "–",
                "wahlblock": z.get("wahlblock", ""),
                "beschreibung": z.get("beschreibung", ""),
            }
        self.daten: dict[str, dict[str, tuple]] = {}
        unbekannt = set()
        for z in lies_csv(ergebnisse):
            kz = z.get("kuerzel") or z.get("Kürzel") or z.get("kürzel") or ""
            if not kz:
                continue
            zeile = {}
            for spalte, wert in z.items():
                if spalte.lower() in ("kuerzel", "kürzel"):
                    continue
                if spalte not in self.items:
                    if wert:
                        unbekannt.add(spalte)
                    continue
                p, codes = parse_zelle(wert)
                if p is not None and p > self.items[spalte]["max"] + 1e-9:
                    raise ValueError(f"{kz}, Item {spalte}: {p} > max {self.items[spalte]['max']}")
                zeile[spalte] = (p, codes)
            self.daten[kz] = zeile
        if unbekannt:
            print(f"Hinweis: Spalten ohne Schlüssel ignoriert: {', '.join(sorted(unbekannt))}", file=sys.stderr)

    # ----- Kennzahlen pro Schüler:in
    def bearbeitet(self, kz):
        return {i: v for i, v in self.daten[kz].items() if v[0] is not None}

    def quote(self, kz) -> float | None:
        b = self.bearbeitet(kz)
        mx = sum(self.items[i]["max"] for i in b)
        return sum(v[0] for v in b.values()) / mx if mx else None

    def punkte(self, kz):
        b = self.bearbeitet(kz)
        return sum(v[0] for v in b.values()), sum(self.items[i]["max"] for i in b)

    def niveau_quoten(self, kz) -> dict[str, float]:
        p, m = defaultdict(float), defaultdict(float)
        for i, (pk, _) in self.bearbeitet(kz).items():
            n = self.items[i]["niveau"]
            p[n] += pk
            m[n] += self.items[i]["max"]
        return {n: p[n] / m[n] for n in m if m[n]}

    def kompetenz_quoten(self, kz) -> dict[str, tuple[float, float]]:
        p, m = defaultdict(float), defaultdict(float)
        for i, (pk, _) in self.bearbeitet(kz).items():
            k = self.items[i]["kompetenz"]
            p[k] += pk
            m[k] += self.items[i]["max"]
        return {k: (p[k], m[k]) for k in m}

    def fehlerbilder(self, kz) -> list[str]:
        return [c for _, (_, codes) in self.daten[kz].items() for c in codes]


def sicher_bis(nq: dict[str, float], schwelle: float) -> str:
    """Höchste Stufe, bis zu der alle getesteten Stufen 'sicher' sind. '-' = keine."""
    ergebnis = "-"
    for n in sorted(nq, key=lambda x: NIVEAU_ORDNUNG.find(x) if x in NIVEAU_ORDNUNG else 99):
        if nq[n] + 1e-9 >= schwelle:
            ergebnis = n
        else:
            break
    return ergebnis


def ziel_niveau(sb: str, getestet: list[str]) -> str:
    if sb == "-":
        return min(getestet, key=NIVEAU_ORDNUNG.find) if getestet else "?"
    i = NIVEAU_ORDNUNG.find(sb)
    return NIVEAU_ORDNUNG[i + 1] if 0 <= i < len(NIVEAU_ORDNUNG) - 1 else sb


def niveau_wert(nq: dict[str, float], schwelle: float) -> float | None:
    """Geschätzte Niveaustufe als Zahl (A=1 … H=8), vergleichbar über Tests mit
    unterschiedlichen / selbst gewählten Niveaus.
    = höchste sicher erreichte Stufe + Anteil gelöst auf der nächsthöheren getesteten Stufe.
    Ohne sichere Stufe: (niedrigste getestete Stufe − 1) + deren Lösungsquote."""
    if not nq:
        return None
    ordn = sorted(nq, key=NIVEAU_ORDNUNG.find)
    sb = sicher_bis(nq, schwelle)
    if sb == "-":
        return NIVEAU_ORDNUNG.find(ordn[0]) + nq[ordn[0]]
    wert = NIVEAU_ORDNUNG.find(sb) + 1.0
    hoeher = [n for n in ordn if NIVEAU_ORDNUNG.find(n) > NIVEAU_ORDNUNG.find(sb)]
    if hoeher:
        wert += min(nq[hoeher[0]], 0.99)
    return wert


def niveau_text(w: float | None) -> str:
    """4,0 → 'D', 4,4 → 'D+', 4,7 → 'D++' (auf dem Weg zu E)."""
    if w is None:
        return "–"
    i = int(w + 1e-9)
    rest = w - i
    basis = NIVEAU_ORDNUNG[i - 1] if 1 <= i <= len(NIVEAU_ORDNUNG) else "<A"
    return basis + ("++" if rest >= 0.66 else "+" if rest >= 0.33 else "")


def anzeige_sb(sb: str) -> str:
    return "keine" if sb == "-" else sb


def parse_gruppen(text: str | None) -> dict[str, str]:
    if not text:
        return {}
    m = {a.strip().upper(): b.strip() for a, b in (p.split(":", 1) for p in text.split(",") if ":" in p)}
    if "KEINE" in m:
        m["-"] = m.pop("KEINE")
    return m


def pct(x: float | None) -> str:
    return "–" if x is None else f"{round(100 * x)} %"


def balken(x: float | None, breite: int = 10) -> str:
    if x is None:
        return ""
    n = round(x * breite)
    return "█" * n + "░" * (breite - n)


def korrelation(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 4:
        return None
    try:
        return statistics.correlation(xs, ys)
    except statistics.StatisticsError:
        return None


# --------------------------------------------------------------------------- Modus: test
def bericht_test(t: Test, schwelle: float, gruppen: dict[str, str], anonym: bool) -> str:
    kz_liste = sorted(t.daten)
    n = len(kz_liste)
    out: list[str] = []
    a = out.append
    a(f"# Auswertung: {t.name}\n")
    a(f"*{n} Schüler:innen · {len(t.items)} Items · „sicher“ ab {round(schwelle*100)} % einer Stufe*\n")

    quoten = [q for kz in kz_liste if (q := t.quote(kz)) is not None]
    a("## 1. Klasse auf einen Blick\n")
    if quoten:
        a(f"- **Mittlere Lösungsquote:** {pct(statistics.mean(quoten))} "
          f"(Median {pct(statistics.median(quoten))}, Spannweite {pct(min(quoten))} – {pct(max(quoten))})")
        if len(quoten) > 1:
            a(f"- **Streuung (SD):** {round(100*statistics.pstdev(quoten))} Prozentpunkte "
              "– Maß für die Heterogenität; sinkt sie über die Zeit, schließt sich die Schere.")
        verteilung = Counter(min(int(q * 5), 4) for q in quoten)
        a("- **Verteilung:**")
        for b, label in enumerate(["0–19 %", "20–39 %", "40–59 %", "60–79 %", "80–100 %"]):
            a(f"  - `{label:>9}` {'■' * verteilung.get(b, 0)} {verteilung.get(b, 0)}")
    a("")

    # Niveaustufen
    a("## 2. Niveaustufen\n")
    a("| Stufe | Lösungsquote Klasse | Anteil „sicher“ |")
    a("|---|---|---|")
    niveaus = sorted({it["niveau"] for it in t.items.values()}, key=lambda x: NIVEAU_ORDNUNG.find(x))
    for nv in niveaus:
        qs = [t.niveau_quoten(kz).get(nv) for kz in kz_liste]
        qs = [q for q in qs if q is not None]
        if qs:
            a(f"| {nv} | {balken(statistics.mean(qs))} {pct(statistics.mean(qs))} | "
              f"{sum(q + 1e-9 >= schwelle for q in qs)}/{len(qs)} |")
    sb_counter = Counter(sicher_bis(t.niveau_quoten(kz), schwelle) for kz in kz_liste)
    a("\n**Sicher erreicht bis Stufe:** " + " · ".join(f"{anzeige_sb(k)}: {v}" for k, v in sorted(sb_counter.items())))
    if gruppen:
        gc = Counter(gruppen.get(sicher_bis(t.niveau_quoten(kz), schwelle), "?") for kz in kz_liste)
        a("\n**Gruppenvorschlag:** " + " · ".join(f"{k} {v}" for k, v in gc.items()))
    a("")

    # Kompetenzen
    a("## 3. Kompetenzen\n")
    a("| Kompetenz | Lösungsquote | Items |")
    a("|---|---|---|")
    komp_items = defaultdict(list)
    for iid, it in t.items.items():
        komp_items[it["kompetenz"]].append(iid)
    komp_q = {}
    for k, its in komp_items.items():
        p = m = 0.0
        for kz in kz_liste:
            for i in its:
                v = t.daten[kz].get(i)
                if v and v[0] is not None:
                    p += v[0]
                    m += t.items[i]["max"]
        if m:
            komp_q[k] = p / m
    for k, q in sorted(komp_q.items(), key=lambda x: x[1]):
        a(f"| {k} | {balken(q)} {pct(q)} | {', '.join(komp_items[k])} |")
    a("")

    # Item-Analyse
    a("## 4. Item-Analyse\n")
    a("*p = Lösungsquote (Schwierigkeit) · r = Trennschärfe (Korrelation Item ↔ Rest-Test). "
      "r < 0,2: Item misst evtl. etwas anderes oder ist missverständlich.*\n")
    a("| Item | Stufe | Kompetenz | n | p | r | Häufigste Fehlerbilder | Hinweis |")
    a("|---|---|---|---|---|---|---|---|")
    item_flags = []
    for iid, it in t.items.items():
        werte = [(kz, t.daten[kz][iid]) for kz in kz_liste if t.daten[kz].get(iid, (None,))[0] is not None]
        if not werte:
            a(f"| {iid} | {it['niveau']} | {it['kompetenz']} | 0 | – | – | – | nicht bearbeitet |")
            continue
        ps = [v[0] / it["max"] for _, v in werte]
        p = statistics.mean(ps)
        rest = []
        for kz, v in werte:
            pk, mk = t.punkte(kz)
            mk -= it["max"]
            rest.append((pk - v[0]) / mk if mk > 0 else 0)
        r = korrelation(ps, rest)
        fb = Counter(c for _, v in werte for c in v[1])
        fb_txt = ", ".join(f"{c} ({k})" for c, k in fb.most_common(3)) or "–"
        hinweis = []
        if p < 0.3:
            hinweis.append("⚠ sehr schwer – wiederholen")
        elif p < 0.5:
            hinweis.append("schwer")
        if p > 0.9:
            hinweis.append("fast alle sicher")
        if r is not None and r < 0.2:
            hinweis.append("⚠ Trennschärfe prüfen")
        if any(k / len(werte) > 1 / 3 for k in fb.values()):
            hinweis.append("Fehlerbild > ⅓ → Plenum")
        item_flags.append((iid, p, r, hinweis))
        a(f"| {iid} | {it['niveau']} | {it['kompetenz']} | {len(werte)} | {pct(p)} | "
          f"{'–' if r is None else f'{r:.2f}'.replace('.', ',')} | {fb_txt} | {'; '.join(hinweis)} |")
    a("")

    # Fehlerbilder
    a("## 5. Fehlerbilder (Klasse)\n")
    # Ein Fehlerbild zählt als "im Lernbereich", wenn das Item höchstens auf dem nächsten
    # Ziel-Niveau der Person liegt. Fehler weit über dem eigenen Niveau sind erwartbar
    # (Inhalt noch nicht dran) und lösen keinen Plenums-Alarm aus.
    niveaus_alle = sorted({it["niveau"] for it in t.items.values()}, key=NIVEAU_ORDNUNG.find)
    fb_pers, fb_rel = defaultdict(set), defaultdict(set)
    for kz in kz_liste:
        ziel = ziel_niveau(sicher_bis(t.niveau_quoten(kz), schwelle), niveaus_alle)
        for iid, (_, codes) in t.daten[kz].items():
            for c in codes:
                fb_pers[c].add(kz)
                if NIVEAU_ORDNUNG.find(t.items[iid]["niveau"]) <= NIVEAU_ORDNUNG.find(ziel):
                    fb_rel[c].add(kz)
    if fb_pers:
        a("*„im Lernbereich“ = Fehler bei Aufgaben bis zum nächsten Ziel-Niveau der Person. "
          "Nur diese Fehler sind ein echter Förderanlass; Fehler weit oberhalb sind erwartbar.*\n")
        a("| Fehlerbild | betroffen gesamt | davon im Lernbereich | Anteil Klasse | Empfehlung |")
        a("|---|---|---|---|---|")
        for c, s in sorted(fb_pers.items(), key=lambda x: (-len(fb_rel[x[0]]), -len(x[1]))):
            rel = fb_rel[c]
            anteil = len(rel) / n
            empf = ("**Plenum-Impuls** für alle" if anteil > 1 / 3 else
                    "Kleingruppe / Tischgruppe" if len(rel) >= 3 else
                    "Einzelförderung (Hilfekarte)" if rel else "noch kein Lernziel – später")
            a(f"| {c} | {len(s)} | {len(rel)} | {pct(anteil)} | {empf} |")
    else:
        a("*Keine Fehlerbilder kodiert. Tipp: In der Ergebnisdatei z. B. `0:LG` eintragen – "
          "Fehlerbilder zeigen den nächsten Lernschritt viel genauer als Punkte.*")
    a("")

    # Einzelprofile
    if not anonym:
        a("## 6. Einzelprofile (nur Kürzel – nicht veröffentlichen)\n")
        hdr = ("| Kürzel | Punkte | Quote | " + " | ".join(niveaus) +
               " | sicher bis | Niveau-Wert | nächstes Ziel |")
        if gruppen:
            hdr += " Gruppe |"
        hdr += " Fehlerbilder |"
        a(hdr)
        a("|" + "---|" * (hdr.count("|") - 1))
        getestet = niveaus
        for kz in kz_liste:
            pk, mk = t.punkte(kz)
            nq = t.niveau_quoten(kz)
            sb = sicher_bis(nq, schwelle)
            zeile = (f"| {kz} | {str(round(pk, 1)).replace('.', ',')}/{str(round(mk, 1)).replace('.', ',')} | "
                     f"{pct(t.quote(kz))} | " + " | ".join(pct(nq.get(nv)) for nv in niveaus) +
                     f" | {anzeige_sb(sb)} | {niveau_text(niveau_wert(nq, schwelle))} | {ziel_niveau(sb, getestet)} |")
            if gruppen:
                zeile += f" {gruppen.get(sb, '?')} |"
            fb = Counter(t.fehlerbilder(kz))
            zeile += " " + (", ".join(f"{c}×{k}" if k > 1 else c for c, k in fb.most_common()) or "–") + " |"
            a(zeile)
        a("")

        # Förderbedarf / Enrichment
        a("## 7. Auffälligkeiten\n")
        schwach = [kz for kz in kz_liste if (q := t.quote(kz)) is not None and q < 0.4]
        stark = [kz for kz in kz_liste if (q := t.quote(kz)) is not None and q >= 0.9]
        luecke = []
        for kz in kz_liste:
            nq = t.niveau_quoten(kz)
            ordn = sorted(nq, key=NIVEAU_ORDNUNG.find)
            for lo, hi in zip(ordn, ordn[1:]):
                if nq[hi] - nq[lo] >= 0.34:
                    luecke.append(f"{kz} (Stufe {lo} {pct(nq[lo])} < Stufe {hi} {pct(nq[hi])})")
        a(f"- **Unter 40 % – engmaschig begleiten:** {', '.join(schwach) or '–'}")
        a(f"- **Ab 90 % – Enrichment / Experten-Aufgaben:** {', '.join(stark) or '–'}")
        a(f"- **Lücke unter höherer Stufe (gezielte Lücke schließen):** {', '.join(luecke) or '–'}")
        a("")
    return "\n".join(out)


# --------------------------------------------------------------------------- Modus: verlauf
def finde(pfad: str, basis: Path) -> Path:
    for kandidat in (basis / pfad, Path(pfad), Path.cwd() / pfad):
        if kandidat.exists():
            return kandidat
    raise FileNotFoundError(pfad)


def steigung(ys: list[float]) -> float:
    if len(ys) < 2:
        return 0.0
    xs = list(range(len(ys)))
    mx, my = statistics.mean(xs), statistics.mean(ys)
    nenner = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / nenner if nenner else 0.0


def bericht_verlauf(index: Path, anonym: bool, schwelle: float = 0.66) -> str:
    eintraege = sorted(lies_csv(index), key=lambda z: z.get("datum", ""))
    tests: list[tuple[str, Test]] = []
    for e in eintraege:
        t = Test(finde(e["schluessel"], index.parent), finde(e["ergebnisse"], index.parent),
                 name=e.get("test") or None)
        tests.append((e.get("datum", ""), t))
    if not tests:
        return "Keine Tests im Index."
    alle_kz = sorted({kz for _, t in tests for kz in t.daten})
    out: list[str] = []
    a = out.append
    a(f"# Lernverlauf ({len(tests)} Tests, {len(alle_kz)} Schüler:innen)\n")
    a("*Prozentwerte sind zwischen Tests kaum vergleichbar (unterschiedlich schwer, bei Exit-Tickets "
      "wählen Schüler:innen ihr Niveau selbst). Maßgeblich ist deshalb der **Niveau-Wert**: "
      "höchste sicher erreichte RLP-Stufe + Fortschritt zur nächsten (z. B. D+ = auf dem Weg von D zu E). "
      "Der **Trend** ist die Steigung über alle Tests im Vergleich zur Klasse – robuster als „erster vs. letzter Test“.*\n")

    nw = {}  # (testname, kz) -> Niveau-Wert
    for _, t in tests:
        for kz in t.daten:
            nw[(t.name, kz)] = niveau_wert(t.niveau_quoten(kz), schwelle)

    # Klasse
    a("## 1. Klasse über die Zeit\n")
    a("| Datum | Test | n | Mittel % | Ø Niveau | SD Niveau (Schere) | unter Stufe C sicher | ab Stufe E |")
    a("|---|---|---|---|---|---|---|---|")
    mittel, mittel_nw = {}, {}
    for datum, t in tests:
        qs = [q for kz in t.daten if (q := t.quote(kz)) is not None]
        ws = [w for kz in t.daten if (w := nw[(t.name, kz)]) is not None]
        if not qs:
            continue
        mittel[t.name] = statistics.mean(qs)
        mittel_nw[t.name] = statistics.mean(ws)
        sd = statistics.pstdev(ws) if len(ws) > 1 else 0
        a(f"| {datum} | {t.name} | {len(qs)} | {pct(mittel[t.name])} | "
          f"{niveau_text(mittel_nw[t.name])} ({mittel_nw[t.name]:.1f}) | {sd:.2f} | "
          f"{sum(w < 3 for w in ws)} | {sum(w >= 5 for w in ws)} |".replace(".", ","))
    a("")

    # Kompetenzen über alle Tests
    a("## 2. Kompetenzen über alle Tests\n")
    a("| Kompetenz | " + " | ".join(t.name for _, t in tests) + " | Trend |")
    a("|---|" + "---|" * (len(tests) + 1))
    alle_komp = sorted({it["kompetenz"] for _, t in tests for it in t.items.values()})
    for k in alle_komp:
        werte = []
        for _, t in tests:
            p = m = 0.0
            for kz in t.daten:
                pk, mk = t.kompetenz_quoten(kz).get(k, (0, 0))
                p += pk
                m += mk
            werte.append(p / m if m else None)
        vorhanden = [w for w in werte if w is not None]
        trend = ""
        if len(vorhanden) >= 2:
            d = vorhanden[-1] - vorhanden[0]
            trend = "↗" if d > 0.1 else "↘" if d < -0.1 else "→"
        a(f"| {k} | " + " | ".join(pct(w) for w in werte) + f" | {trend} |")
    a("")

    # Hartnäckige Fehlerbilder (Klassenebene)
    a("## 3. Hartnäckige Fehlerbilder\n")
    fb_tests = defaultdict(lambda: defaultdict(set))  # code -> kz -> {testnamen}
    for _, t in tests:
        for kz in t.daten:
            for c in t.fehlerbilder(kz):
                fb_tests[c][kz].add(t.name)
    hart = {c: [kz for kz, ts in d.items() if len(ts) >= 2] for c, d in fb_tests.items()}
    hart = {c: v for c, v in hart.items() if v}
    if hart:
        a("*Fehlerbild tritt bei derselben Person in ≥ 2 Tests auf → bisherige Förderung reicht nicht, "
          "Zugang wechseln (z. B. enaktiv statt symbolisch).*\n")
        letzter = {}  # kz -> Name des letzten Tests, an dem die Person teilnahm
        for _, t in tests:
            for kz in t.daten:
                letzter[kz] = t.name
        for c, v in sorted(hart.items(), key=lambda x: -len(x[1])):
            aktuell = sorted(kz for kz in v if letzter.get(kz) in fb_tests[c][kz])
            a(f"- **{c}:** {len(v)} {'Schüler:in' if len(v) == 1 else 'Schüler:innen'}"
              + ("" if anonym else f" ({', '.join(sorted(v))})")
              + f" – davon **im letzten Test noch:** {len(aktuell)}"
              + ("" if anonym or not aktuell else f" ({', '.join(aktuell)})"))
    else:
        a("*Keine wiederkehrenden Fehlerbilder gefunden (oder keine kodiert).*")
    a("")

    # Einzelentwicklung über Niveau-Werte
    tnamen = [t.name for _, t in tests if t.name in mittel_nw]
    klassen_steigung = steigung([mittel_nw[n] for n in tnamen])
    kategorien = defaultdict(list)
    zeilen = []
    for kz in alle_kz:
        werte = [nw.get((n, kz)) for n in tnamen]
        paare = [(i, w) for i, w in enumerate(werte) if w is not None]
        if len(paare) < 3:
            kat, rel_txt = "zu wenig Daten (< 3 Tests)", "–"
        else:
            # Steigung der Abweichung vom Klassenschnitt, hochgerechnet auf den ganzen Zeitraum
            abw = [w - mittel_nw[tnamen[i]] for i, w in paare]
            xs = [i for i, _ in paare]
            mx, my = statistics.mean(xs), statistics.mean(abw)
            nen = sum((x - mx) ** 2 for x in xs)
            s = sum((x - mx) * (y - my) for x, y in zip(xs, abw)) / nen if nen else 0
            rel = s * (xs[-1] - xs[0])
            rel_txt = f"{'+' if rel >= 0 else ''}{rel:.1f} Stufen".replace(".", ",")
            mittelwert = statistics.mean(w for _, w in paare)
            if min(w for _, w in paare) >= 5.0 and rel < 0.5:
                # Deckeneffekt: durchgehend ≥ E – Tests messen oft nicht höher,
                # ein relatives "Zurückfallen" ist dann kein Lernrückgang.
                kat = "⭐ konstant stark → Enrichment"
            elif rel >= 0.5:
                kat = "🚀 holt auf"
            elif rel <= -0.5:
                kat = "⚠ fällt zurück"
            elif mittelwert >= 5.0:
                kat = "⭐ konstant stark → Enrichment"
            elif mittelwert < 3.0:
                kat = "⚠ konstant unter C → Zugang ändern"
            else:
                kat = "→ entwickelt sich wie die Klasse"
        kategorien[kat].append(kz)
        zeilen.append(f"| {kz} | " + " | ".join(niveau_text(w) for w in werte) + f" | {rel_txt} | {kat} |")

    a("## 4. Entwicklung im Vergleich zur Klasse\n")
    a(f"Die Klasse insgesamt: **{'+' if klassen_steigung * (len(tnamen) - 1) >= 0 else ''}"
      f"{klassen_steigung * (len(tnamen) - 1):.1f} Stufen** über den Zeitraum.\n".replace(".", ",", 1))
    if anonym:
        a(" · ".join(f"{k}: {len(v)}" for k, v in kategorien.items()))
    else:
        a("### Einzelverläufe (nur Kürzel – nicht veröffentlichen)\n")
        a("| Kürzel | " + " | ".join(tnamen) + " | Trend ggü. Klasse | Entwicklung |")
        a("|---|" + "---|" * (len(tnamen) + 2))
        out.extend(zeilen)
        a("\n## 5. Handlungsbedarf\n")
        for kat in ["⚠ fällt zurück", "⚠ konstant unter C → Zugang ändern", "🚀 holt auf",
                    "⭐ konstant stark → Enrichment", "→ entwickelt sich wie die Klasse",
                    "zu wenig Daten (< 3 Tests)"]:
            if kategorien.get(kat):
                a(f"- **{kat}:** {', '.join(kategorien[kat])}")
    a("")
    return "\n".join(out)


# --------------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="modus", required=True)
    pt = sub.add_parser("test")
    pt.add_argument("--schluessel", required=True, type=Path)
    pt.add_argument("--ergebnisse", required=True, type=Path)
    pt.add_argument("--name")
    pt.add_argument("--schwelle", type=float, default=0.66)
    pt.add_argument("--gruppen", help='z. B. "keine:🌱,C:🌿,D:🌿,E:🌳" (sicher-bis-Stufe → Gruppe)')
    pt.add_argument("--anonym", action="store_true")
    pt.add_argument("--out", type=Path)
    pv = sub.add_parser("verlauf")
    pv.add_argument("--index", required=True, type=Path)
    pv.add_argument("--anonym", action="store_true")
    pv.add_argument("--schwelle", type=float, default=0.66)
    pv.add_argument("--out", type=Path)
    args = ap.parse_args(argv)

    if args.modus == "test":
        t = Test(args.schluessel, args.ergebnisse, args.name)
        text = bericht_test(t, args.schwelle, parse_gruppen(args.gruppen), args.anonym)
    else:
        text = bericht_verlauf(args.index, args.anonym, args.schwelle)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"Bericht geschrieben: {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, KeyError) as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        sys.exit(1)
