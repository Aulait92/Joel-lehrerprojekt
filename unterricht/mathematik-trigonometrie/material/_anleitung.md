# Verbindliche Anleitung für die Materialien dieser Einheit

## Grundlagen (zuerst lesen)
`../00-auftrag.md` (Vorgaben der Lehrkraft, Vorrang) · `../01-lehrplanbezug.md` (Stufen, Fehlerbild-Kürzel Abschn. 7) · `../04-verlaufsplanung.md` (Stundenverlauf + **Materialliste ab ca. Zeile 270** = dein Auftrag) · `../03-kreative-ideen.md` (roter Faden „Vermessungsbüro Spree-Vermessung“, fiktiv) · `../02-diagnose.md` (Exit-Tickets – keine Dopplungen; falls noch nicht vorhanden, ignorieren) · `../vorhandenes-material/` (AB1 ◼ als Stil- und Niveauvorbild!).

## Dateien
Eine Datei pro Material-ID: `M1.2-ab1-feder.md`, `M2.5-loesung-ab2.md` usw. Erste Zeile: `# M1.2 – <Titel>`.
Aufbau wie in der anderen Einheit: `## Teil A – Für die Lehrkraft (nicht austeilen)` (kurz: Stunde, Einsatz, Stufe, Fehlerbilder), dann die Kopiervorlage(n) als `## Teil B – …`, Lösungen als `## Teil C – Lösungen (nicht austeilen)` bzw. eigene Lösungsblatt-Datei laut Materialliste. Abschnitte mit „Lehrkraft“/„Lösung“ in der Überschrift werden automatisch aus den Kopiervorlagen-PDFs herausgelassen.

## Arbeitsblätter
- Kopfzeile (erste Zeile der Kopiervorlage):
  `<div class="kopf"><span>Name: ____________________ Datum: __________</span><span>Klasse 10.___: Trigonometrie · 🪶 Feder</span></div>` (bzw. `◼ Gewicht` / `◼◼ Doppelgewicht`)
- Titel als `### …`, Aufgaben als `**Aufgabe 1)** …` (Stil wie AB1), Operatoren fett.
- **Dreiecke** als Block (wird maßstabsgetreu gezeichnet, Zeichen für den rechten Winkel automatisch):
  ````
  ```dreieck
  winkel_A: 38
  winkel_B: 52
  namen: A B C
  seiten: AB="c = 7,3 cm" AC="b" BC="a"
  winkel: A="α" B="β = 52°"
  breite: 280
  ```
  ````
  Rechter Winkel bei C ⇔ winkel_A + winkel_B = 90. Werte in der Skizze müssen zu den Winkeln passen (Seitenverhältnisse stimmen automatisch, die Beschriftung ist frei).
- Andere Skizzen (Leiter, Haus, Dach, Geometer, Turm, Fluss) als schlichtes **Inline-SVG** (schwarz, stroke-width 1.5, font-family "Liberation Sans", font-size 13, max. width 320). Keine Platzhalter „[Bild: …]“.
- Rechenplatz wie auf den Blättern der Lehrkraft: `<div class="rechenfeld" style="height:5cm"></div>` (Höhe passend zur Aufgabe).
- 1 Arbeitsblatt = ca. 2 Seiten A4, Bearbeitungszeit laut Verlaufsplanung (meist 20 Min.). Differenzierung: gleicher Kern, 🪶 mit Tipps/Schema/markierten Seiten, ◼ Standard (wie AB1), ◼◼ mehrschrittig/begründen/offen.
- **Lösungscode** (Idee 2 aus 03), wo die Verlaufsplanung ihn vorsieht: Ergebnis → Buchstabe; Codewort im Lösungsblatt.
- **Spannung gegen Unruhe:** kurze Aufgaben mit klarer Zielzahl, Auftragskarte des Vermessungsbüros als Einstieg, echte Kontexte (Berliner Werte nur als „angenommen“/gerundet), Fehler-Detektiv-Aufgaben.

## Lösungsblätter (für die Lehrkraft)
Vollständige Rechenwege (Formel → Umstellen → Einsetzen → TR-Eingabe → Ergebnis mit Einheit, sinnvoll gerundet), typische Fehler mit Kürzel (HYP, AG, VER, RAD, UMK, INV, UMS, RUND, PLAU, AUG, MESS, PAAR, FALL, SSW, KVZ, KZU, KRF), Codewort. **Jedes Ergebnis zweimal nachrechnen** (Taschenrechner im Kopf: sin/cos/tan auf 4 Nachkommastellen genau; Winkel auf 0,1°).

## Hilfekarten
Gestuft: H1 Denkanstoß → H2 Strategie/Schema → H3 durchgerechnetes Parallelbeispiel (andere Zahlen!). Als ausschneidbare Karten (`> ✂ ---------- H1 … ----------`).

## Folien
Die Lehrkraft arbeitet mit Folien (Stil siehe Tafel-PDF Std. 1): pro Folie `### Folie n – Titel`, darunter Stichpunkte/Text genau so, wie er auf der Folie stehen soll, plus `*Moderation:*`-Zeile für die Lehrkraft. Fahrplan-Folie mit Zeiten am Anfang, Abschlussfolie am Ende.

## Daten für Std. 3–5 (verbindlich, damit alles zusammenpasst)
Beispieldaten aus `04-verlaufsplanung.md` (M3.5) verwenden: Abstand e = 15,0 m, Höhenwinkel α = 38°, Augenhöhe 1,55 m → h ≈ 15,0 · tan 38° + 1,55 ≈ 11,72 + 1,55 ≈ 13,3 m. Zweiter Standpunkt: siehe M3.5 in der Materialliste (Werte dort übernehmen und nachrechnen).
