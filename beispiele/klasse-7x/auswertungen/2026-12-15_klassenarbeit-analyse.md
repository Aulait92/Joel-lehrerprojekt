# Analyse Klassenarbeit „Brüche und Dezimalzahlen“: Klasse 7x (15.12.2026)

> **DEMO MIT ERFUNDENEN DATEN.** Alle Kürzel, Punkte und Fehlerbilder sind fiktiv und dienen nur der Vorführung des Auswertungs-Workflows. Echte Klassendaten gehören nach `klassen/<klasse>/` (per `.gitignore` geschützt).

> **🔄 Nachtrag nach dieser Analyse:** Der hier in Abschnitt 6 bemängelte Schlüssel wurde korrigiert (★★★-Varianten jetzt Stufe E), die Berichte `2026-12-15_klassenarbeit.md` und `verlauf.md` sind neu erzeugt. Dadurch ändern sich zwei Aussagen: Der mittlere Niveau-Wert steigt von C+ (3,4) auf **C++ (3,9)**, also um ca. **+0,5 statt +0,8 Stufen**. Die **Schere geht nicht auf**, sondern leicht zu (SD 0,93 → **0,86**). Der in Kernaussage 4 vermutete Messartefakt-Anteil war also der ganze Effekt. Unverändert gelten: C nicht sicher 11 → 4, unteres Zehntel ohne Zuwachs, AD hartnäckig, Umwandeln stagniert. Die Kategorien in `verlauf.md` haben sich leicht verschoben; die Einzelfall-Prüfung in Abschnitt 4 bleibt gültig, S16 erscheint jetzt unter „konstant unter C“. S09 (durchgehend E) wird nach einer Skript-Verbesserung als „konstant stark“ statt „fällt zurück“ geführt (Deckeneffekt).

**Grundlage:** `2026-12-15_klassenarbeit.md` (Testbericht), `verlauf.md` (5 Messpunkte: Eingangstest, Exit-Tickets 1–3, Klassenarbeit), `2026-11-24_eingangstest.md` (neu erzeugt mit Gruppen), Einheit `unterricht/mathematik-brueche-dezimalzahlen/` (02-diagnose, 04-verlaufsplanung, material/, bewertung/).
**Einschränkungen, die man beim Lesen kennen sollte:**
- Fehlerbilder wurden nur in **Teil A** (und bei wenigen ★-Varianten) kodiert. Für die Wahlvarianten ★★/★★★ gibt es nur Punkte. Fehlerbild-Anteile beziehen sich deshalb vor allem auf die 13 Schüler:innen, die ★ gewählt haben.
- Die Niveau-Werte „F“ und „E: 0/7 sicher“ sind teilweise **Schlüssel-Artefakte** (siehe Abschnitt 6): ★★★ ist im Schlüssel komplett als F eingetragen, ist laut `bewertung/klassenarbeit.md` aber „Stufe E mit F-Anteil“. Wer ★★★ gewählt hat, hat in der Arbeit gar keine reinen E-Items bearbeitet.
- Exit-Tickets bestehen aus nur einem Item mit Selbstwahl des Niveaus. Einzelne Ausschläge im Verlauf bitte nicht überbewerten.

---

## 1. Kernaussagen

1. Die Klasse hat sich über die Einheit klar entwickelt: Der mittlere Niveau-Wert stieg von C+ (3,4) auf D (4,1). Die Zahl derer, die Stufe C noch nicht sicher beherrschen, sank von 11 auf 4. Acht von elf Schüler:innen, die mit 🌱-Aufgaben gestartet sind, haben Stufe C oder sogar D sicher erreicht.
2. Der Engpass liegt beim Übergang C → D in Teil A. Die D-Items A4–A9 werden nur zu rund 60 % gelöst. In der Gruppe „C sicher, D noch nicht“ (9 Personen) zeigen je 4 die Fehlerbilder AD, KV und ZN und 3 das Fehlerbild LG. Am schwächsten ist die Kompetenz **Umwandeln** (54 %, ohne Fortschritt seit dem Eingangstest).
3. **AD (additives Erweitern) ist das hartnäckigste Fehlerbild.** Sechs Schüler:innen zeigen es im Eingangstest *und* in der Klassenarbeit, obwohl in Std. 3 mit H-KW daran gearbeitet wurde. Die bisherige Förderung hat bei ihnen nicht gegriffen, also den Zugang wechseln (enaktiv: Bruchstreifen falten statt Regel). Bei LG und ZN zeigt dagegen die große Mehrheit der früher Betroffenen das Fehlerbild in der Arbeit nicht mehr.
4. Die Schere geht auf: Die SD des Niveau-Werts stieg von 0,93 auf 1,13. Ein Teil davon liegt an der Messung, denn der Eingangstest reichte nur bis E, die Arbeit bis F. Echt ist aber, dass drei Schüler:innen über alle fünf Messpunkte unter C bleiben und zwei nach einem soliden Eingangstest in der Arbeit deutlich abfallen. Das sollte vor Weihnachten geklärt werden.
5. Die Schüler:innen auf D+ (★★-Wähler:innen) zeigen beim Schritt zu E eine gemeinsame Hürde: **mehrschrittige Anteilsaufgaben** (B3-2: 35 %, alle ★★-Wählenden unter 60 %). Das ist ihr Lernbereich und kein Aufgabenfehler. Sie brauchen in der Nachsorge gezielte Sachaufgaben mit „Anteil vom Ganzen → Rest als Bruch/Prozent“.

---

## 2. Sofortmaßnahmen nächste Stunde (Rückgabe-Stunde, 45 Min.)

**Ablauf**

| Zeit | Phase | Inhalt |
|---|---|---|
| 5' | Rückgabe | Arbeit mit Rückmeldebogen (`bewertung/klassenarbeit.md`, Abschn. 7) austeilen. Ritual: Zuerst die zwei ⭐-Zeilen lesen, dann die Punkte. |
| 10' | **Plenum-Impuls AD/KW** | siehe unten |
| 25' | **Berichtigung in Kleingruppen** nach Fehlerbild (statt alle alles) | siehe unten, gestufte Hilfekarten an der Hilfetheke |
| 5' | Abschluss | Kompetenzraster (`bewertung/kompetenzraster.md`): „Meine **eine** Zeile für die nächsten 2 Wochen“ auf die Schichtkarte (M0.1, Rückseite „Mein Ziel und mein ★-Rest“) |

**Plenum-Impuls (10 Min.): „Wird es mehr, wenn ich feiner teile?“ (Fehlerbild AD, Aufgabe A5)**
- Warum für alle: AD ist das häufigste (8 Betroffene) und das hartnäckigste Fehlerbild (6 Betroffene in ≥ 2 Tests). Erweitern ist außerdem die Voraussetzung für ZN (gleichnamig machen) und für Umwandeln (7/20 = 35/100).
- Wie: Eine anonymisierte Fehllösung an die Tafel schreiben: „2/5 = ☐/20 → 17, weil 5 + 15 = 20, also 2 + 15“. Alle falten mit dem Bruchstreifen (M0.4 a) 2/5 und färben ihn. Dann jedes Fünftel in 4 gleiche Teile falten und zählen: 8/20, nicht 17/20. Merksatz der Karte H-KW gemeinsam formulieren: „Jedes Stück wird gleich oft geteilt. Oben und unten mal dieselbe Zahl.“
- Differenzierung im Plenum: Die 🌳-Tische begründen *zusätzlich* schriftlich, warum „+ dieselbe Zahl“ den Wert ändert (Gegenbeispiel 1/2 → 2/3). So entsteht Tiefe statt Wartezeit.

**Kleingruppen-Berichtigung (25 Min.)**

| Gruppe | Kürzel | Inhalt | Material |
|---|---|---|---|
| **G1 Grundlagen am Lehrertisch** (enaktiv) | S16, S19, S24, S26 | Teil-Ganzes und Bruch als Geldbetrag: A1, A2, A6 (1/5 = 0,2 = 20 %) mit Rechengeld berichtigen („1/5 von 1 € = 20 ct“) | Rechengeld (Schulbestand oder M4.2), H-ZP (inkl. TT), H-KT, M1.1 Inventurkisten |
| **G2 Erweitern → Addieren** | S05, S08, S18, S20 | A5 und A9 mit dem Bruchstreifen berichtigen. Erst AD, dann ZN („Ist das Ergebnis größer als jeder Summand?“) | M0.4 a Bruchstreifen, H-KW, H-ZN |
| **G3 Dezimalzahlen und Umwandeln** | S07, S10, S13, S14, S15 | A4 (Nullen auffüllen), A8 (Stellenwerttafel: Ziffern wandern), A6/B1-1 (Bruch → Hundertstel → Dezimalzahl) | M0.4 b/c Stellenwerttafel und Zahlenstrahl mit Lupe, H-LG, H-KV, H-ZP |
| **G4 Schritt zu E: Anteile** (Tandems) | S01, S03, S04, S11, S17, S22, S23, S25, S27 | B3-2 im Tandem berichtigen (★★-Wählende). ★★★-Wählende vergleichen ihre Lösung zu B3-3 d mit dem Lösungsblatt und schreiben eine „Fehlerdetektiv“-Notiz | M0.3 Signalwörter („von“, „Rest“), M7.1 Lösungsteil als Muster |
| **G5 Vertiefung** | S02, S06, S09, S12, S21 | Statt Berichtigung (kaum Fehler): Expertenaufgabe aus Abschnitt 5 | s. Abschnitt 5 |

---

## 3. Gruppen neu sortieren (für die 2 Wochen Nachsorge)

Die Gruppen sind flexibel („Aufzug, nicht Schublade“). Die Zuordnung gilt für die Nachsorge-Aufgaben und wird nach dem Mini-Re-Check (Abschnitt 4, Woche 2) erneut angesehen.

| Fokus | Kürzel | Begründung |
|---|---|---|
| 🌱 **C sichern** | S16, S19, S24, S26 | C in der Arbeit nicht sicher (36–64 %). Bei S26 ist das ein Abfall (Eingangstest C sicher). Ursache erst im Gespräch klären, bevor die Gruppe festgelegt wird. |
| 🌿 **D festigen** | S05, S07, S08, S10, S13, S14, S15, S18, S20 | C sicher, D 10–62 %. S07 und S14 knapp an C (68 %/73 %). Sie bekommen in G2/G3 zusätzlich Lehrertisch-Zeit. |
| 🌿→🌳 **Übergang E** | S01, S03, S04, S11, S17, S22, S23, S25, S27 | D sicher (77–96 %), E/★★★ um 50 % |
| 🌳⭐ **Vertiefung** | S02, S06, S09, S12, S21 | Gesamtquote ≥ 81 %, ★★★ überwiegend sicher |

**Wechsel gegenüber der Startgruppe (Eingangstest):**
- **Rauf:** S11 und S17 (🌱 → Übergang E, beide über die Einheit um rund eine Stufe gewachsen). S06, S12 und S21 (🌿 → Vertiefung). S08, S10, S14, S15 und S20 (🌱 → D festigen; C jetzt sicher). S07 knapp ebenfalls.
- **Runter / genauer hinsehen:** S26 (🌿 → C sichern). S18 bleibt in „D festigen“, kommt aber zuerst in den Lehrertisch-Slot (starker Abfall in D). S22 und S27 (🌳 → Übergang E): Sie haben im Eingangstest bei nur 3 E-Items E erreicht und seitdem stabil auf D+ bis E gearbeitet. Mit ★★★ in der Arbeit lagen sie bei 65 % bzw. 47 %. Das ist kein Abstieg, sondern ein ehrlicher Stand. S22 darf im Bereich Rechnen (B2-3: 8/10) in die Vertiefung wechseln.

---

## 4. Nächster Schritt je Kürzel

**Prüfung der Skript-Kategorie „fällt zurück“ (8 Fälle):**
- **Echter Förderanlass:** S16, S19 und S24 (konstant B/B+ über 5 Messpunkte, also eher Stagnation als Abfall, mit mehreren hartnäckigen Fehlerbildern). S18 und S26: Der Eingangstest war solide, in der Arbeit ist der D-Teil fast leer bzw. voller neuer Fehlerbilder. **Gegenprüfen: Fehlzeiten in Std. 3–6? Tagesform/Prüfungsangst? Abschreiben im Eingangstest?** Erst danach Förderung festlegen.
- **Stagnation:** S05 bleibt an allen 5 Messpunkten bei C+ und wächst nicht mit der Klasse mit. Das ist nicht alarmierend, aber AD blockiert den Schritt zu D.
- **Artefakt / kein Rückfall:** S22 und S27. Der Ausgangswert E stammt aus nur 3 E-Items. Beide haben in der Arbeit ★★★ gewählt, und ★★★ ist im Schlüssel als F kodiert.
- **„Konstant unter C“ veraltet:** S20 hat C in der Arbeit sicher erreicht (69 % gesamt). S08 ebenfalls (C 91 %).

| Kürzel | Ziel | Fehlerbild / Beleg | Material / Hilfekarte |
|---|---|---|---|
| S01 | E: Mult./Div. verständig einschätzen | B2-2 2/7. MG in Exit-Ticket 3 (B2-2 nicht kodiert, in der Arbeit nachsehen) | H-MG, H-DM, M6.1 Teller 🌳 |
| S02 | Vertiefung F | – (94 %) | Abschnitt 5 |
| S03 | E im Zahlbereich: periodisch ↔ Bruch, Dichte | B1-3 3,5/10 (holt deutlich auf) | H-TR, M2.1 🌳-Karten (0,3̅, 0,6̅, 5/15) |
| S04 | E: periodische Dezimalzahlen, Ordnen mit % | B1-2 3/7, B2-2 3,5/7. AD aus dem Eingangstest überwunden | H-TR, M4.1 Bon 🌳-1/-2 |
| S05 | D: Erweitern/Kürzen | **AD hartnäckig** (Eingangstest + Arbeit). Stagnation bei C+ → **Zugang wechseln:** falten statt Regel | M0.4 a Bruchstreifen (enaktiv), H-KW erst danach |
| S06 | Vertiefung F: allgemeines Verfahren begründen | B1-3 6,5/10, B3-3 7/10 | Abschnitt 5 |
| S07 | D: Dezimalzahlen ordnen | **LG hartnäckig** (Eingangstest + Arbeit), außerdem ZN, KV. Nur **ein** Fokus: LG | Preisschilder mit Rechengeld legen (0,30 € / 0,35 €), M0.4 c Zahlenstrahl mit Lupe, H-LG |
| S08 | D: Erweitern als Basis für Addieren | **AD und ZN hartnäckig**, außerdem LG, ZP, KV. Reihenfolge: AD → ZN | M0.4 a, H-KW, dann H-ZN |
| S09 | Vertiefung F: Modellieren/Begründen | B3-3 6/10 | Abschnitt 5 |
| S10 | D: Umwandeln Bruch → Dezimal | A6 2,5/4, B1-1 2,5/4, keine Fehlerbilder kodiert. Mutig ★★ in B3 versucht, das würdigen | H-ZP, M3.1 Etiketten-Werkstatt 🌿 |
| S11 | E: mehrschrittige Anteile | B3-2 4/7. ZN/LG aus früheren Tests in der Arbeit nicht mehr kodiert (A9 1/2, kurz prüfen) | M7.1 Bereich 🌿/🌳, M0.3 Signalwörter |
| S12 | Vertiefung F | – (90 %) | Abschnitt 5 |
| S13 | D: Umwandeln + Wahlstrategie | B3-2 0/7 (nur ★★ bearbeitet). Im Gespräch klären: Leseproblem oder Selbstüberschätzung? Wahlregel „beide Varianten dürfen bearbeitet werden“ wiederholen | H-ZP, M0.3 Wortspeicher |
| S14 | D: Kommaverschiebung | KV und ZN in der Arbeit, B2-1 0/4. Fokus KV (Start bei B, jetzt C sicher) | M0.4 b Stellenwerttafel, H-KV |
| S15 | D: Umwandeln und Addieren | B1-1 1/4, B2-1 1/4. LG früher hartnäckig, in der Arbeit nicht mehr kodiert | H-ZP, H-ZN, M3.1 🌿 |
| S16 | C: Bruch als Anteil und Geldbetrag | **AD, ZP, KV hartnäckig**. Konstant B/B+. Vorrang beim Lernentwicklungsgespräch | Rechengeld, H-ZP, M0.4 a, Lehrertisch |
| S17 | E im Zahlbereich (holt stark auf: B+ → D+) | ★★★ überall 40 %, B1-3 2/10. Nächstes Übungsniveau ★★, dann ★★★ | H-TR, M2.1 🌳-Karten |
| S18 | Ursache klären, dann D: ZN/KV | **ZN und KV hartnäckig**. Abfall C+ → C, B2-1 leer. Gespräch zuerst | H-ZN, H-KV, Lehrertisch-Slot |
| S19 | C: Teil-Ganzes, Komma im Geld | **TT, ZP, KT hartnäckig**. Sprach-/Lesehürde mündlich prüfen (Kennzeichen „S“ aus 02) | M1.1 Inventurkisten (TT), Rechengeld + H-KT, H-ZP, M0.3 |
| S20 | D: Erweitern/Kürzen | **AD hartnäckig**, NZ überwunden. Gesamt 69 %, deutlicher Fortschritt | M0.4 a Bruchstreifen falten, H-KW |
| S21 | Vertiefung F | – (92 %) | Abschnitt 5 |
| S22 | E: Zahlbereich und Sachaufgaben. Im Bereich Rechnen Vertiefung | B1-3 5,5/10, B3-3 6/10, A6 2,5/4. LG überwunden | M2.1 🌳-Karten, M7.1 Bereich 🌳 |
| S23 | E: mehrschrittige Anteile | B3-2 1,5/7. ZN aus Exit-Ticket 2 in der Arbeit überwunden (A9 2/2) | M7.1 Bereich 🌿, M0.3 Signalwörter |
| S24 | C: Teil-Ganzes, Bruch als Division | **TT, AD, ZP hartnäckig**. Konstant B/B+. Vorrang beim Gespräch | M1.1, Rechengeld, H-ZP, Lehrertisch |
| S25 | E: Anteile, periodische Dezimalzahlen | B3-2 2/7, B1-2 3/7. LG und ZN überwunden | M7.1, H-TR |
| S26 | Ursache klären, dann C wieder sichern | Abfall C+ → B+. KT, LG, AD, ZP, ZN in der Arbeit, **AD hartnäckig**. Fehlzeit? | Gespräch, dann M0.4 a + H-KW |
| S27 | E sichern, dann F | ★★★ 40–50 %, B3-3 4/10. Kein Rückfall (s. o.). ★★ konsolidieren | M7.1 Bereich 🌳, M6.1 Teller 🌳 |

**Plan für die 2 Wochen nach der Arbeit**

| Wann | Was |
|---|---|
| Woche 1, Std. 1 | Rückgabe-Stunde (Abschnitt 2) |
| Woche 1, Std. 2 | „Stolperstein-Werkstatt“: Förderpakete je Gruppe (Abschnitt 8, bis dahin Hilfekarten M0.2 + Werkzeugblatt M0.4). Parallel 4–5 Lernentwicklungsgespräche (`bewertung/feedback-formate.md`, Abschn. 3). **Reihenfolge:** S18, S26 (Abfall klären), S16, S19, S24 (konstant unter C), dann S05 (Stagnation) und S13 (Wahlstrategie) |
| Woche 2 (Folgeeinheit) | **„Täglich 3“**: 5-Min.-Starter in jeder Stunde der neuen Einheit, je 1 Aufgabe zu AD, KV/LG, ZN/ZP im Wechsel (🌳: MG, DM, periodisch). Restliche Gespräche (4–5 pro Stunde) |
| Ende Woche 2 | **Mini-Re-Check** als Exit-Ticket (4 Items, analog zu Eingangstest 5–8 + A5). In `tests.csv` eintragen. So zeigt sich, ob AD/KV/ZN/LG sich auflösen (6. Messpunkt) |
| Folgeeinheit allgemein | Wenn es um Prozent, Zuordnungen oder Terme geht: Umwandeln Bruch ↔ Dezimal ↔ Prozent (schwächste Kompetenz) gezielt wieder aufgreifen. Für die Eingangsdiagnose der neuen Einheit 2–3 Items zu AD/ZP/KV einplanen |

*Falls Weihnachtsferien zwischen Woche 1 und 2 liegen: Woche 2 direkt nach den Ferien. Der Mini-Re-Check misst dann zugleich, was die Ferien überdauert hat.*

---

## 5. Enrichment (Vertiefung statt Mehrarbeit)

**Wer:** S02, S06, S09, S12, S21. Im Bereich Rechnen zusätzlich S22.
**Womit (statt Berichtigung und statt „mehr vom Gleichen“):**
- **Fehlerdetektiv-Karten für die Mitschüler:innen:** Je ein anonymes, typisches Fehlerbeispiel zu AD bzw. ZN als Aufgabe gestalten, mit „Woran erkennt man ohne Rechnen, dass das nicht stimmt?“. Das erfordert tiefes Verständnis (Begründen, K1). Geprüfte Karten gehen in die Förderpakete ein.
- **F-Ausblick aus der Arbeit weiterdenken:** „0,9̅ = 1?“ (aufbauend auf B1-3 b, 0,4̅ = 4/9), allgemeines Verfahren für die Dichte (B1-3 a) als Beweisskizze, „¼ mehr Inhalt ≠ 25 % billiger“ verallgemeinern (Gilt allgemein: x mehr Inhalt = x/(1+x) billiger?).
- **Material:** ⭐-Aufgaben auf den 🌳-Karten von M2.2, M3.1 und M4.1 (Extra-Bons 🌳-4). M0.7 „Tresorfragen“ und M0.6 „Erklärclip“ sind in 04 als optional geplant, aber noch nicht erstellt (siehe Abschnitt 8).
- Peer-Tutoring als „Hilfskassierer:in“ höchstens 10 Min. pro Stunde (04, Abschn. 5), damit die Starken selbst weiterlernen.

---

## 6. Hinweise zum Test selbst

1. **Schlüssel-Kodierung der Wahlvarianten verzerrt die Niveau-Auswertung.** B1-3, B2-3 und B3-3 sind im Schlüssel komplett als **F** eingetragen. Laut `bewertung/klassenarbeit.md` sind sie aber „Stufe E mit F-Anteil“ (z. B. B2-3 a–d = E, nur e = F). Folgen: (a) „Sicher bis F“ für 5 Personen ist überschätzt, (b) „E: 0/7 sicher“ ist nicht aussagekräftig, weil ★★★-Wählende keine E-Items hatten. **Empfehlung:** Für künftige Durchgänge die Varianten im Schlüssel in Teilaufgaben aufteilen (z. B. B2-3ad = E / 8 P., B2-3e = F / 2 P.). Analog A9 (laut Arbeit C/D) und B3-2 a (D). Änderungen an `unterricht/` hier bewusst nicht vorgenommen.
2. **B1-2, B2-2, B3-2 mit negativer bzw. Null-Trennschärfe** (r = −0,12 / −0,16 / 0,03): Bei n = 5–7 ist das statistisch nicht interpretierbar. Ein Aufgabenproblem lässt sich daraus nicht ableiten.
3. **B1-1 und B2-1 (★, 30–35 %)** sind laut Bericht „sehr schwer“. Das ist überwiegend ein **Auswahleffekt**: Gewählt haben sie die 13 Schwächsten, und die ★-Varianten liegen auf Stufe D, also für diese Gruppe am oberen Rand des Lernbereichs. Inhaltlich gibt es aber eine Lücke: In B1 und B2 gibt es **keine Variante mit C-Einstieg** (nur B3-1 ist C). Vorschlag: In ★-Varianten eine C-Teilaufgabe voranstellen (z. B. B2-1 mit Geldbeträgen beginnen), damit auch C-sichere Schüler:innen im Wahlteil etwas zeigen können.
4. **Fehlerbilder im Wahlteil nachkodieren:** B1-2 a (TR), B2-2 c/B2-3 b (DM), B2-3 d (MG), B3-3 b („¼ als 0,25 kg“). Das geht in wenigen Minuten aus den korrigierten Arbeiten und würde den Verlauf von MG/DM/TR über die Einheit erst sichtbar machen (aktuell nur im Eingangstest und in Exit-Ticket 3).
5. A2 (p = 94 %, r = 0,25): Deckeneffekt. Als Einstiegsaufgabe sinnvoll, keine Änderung nötig.

---

## 7. Anonymer Klassenbefund (Übergabe an `unterrichts-optimierer`, ohne Kürzel)

**Kontext:** Klassenarbeit am Ende der Einheit „Brüche und Dezimalzahlen“ (Jg. 7 ISS, 27 Schüler:innen, Pflichtteil C/D + Wahlteil mit 3 Varianten je Block). 5 Messpunkte über 3 Wochen. Demo mit erfundenen Daten.

**Verlauf (Niveau-Wert):**
- Mittlerer Niveau-Wert von C+ (3,4) auf D (4,1), also +0,8 Stufen über die Einheit. Der Anstieg verläuft stetig über alle Messpunkte.
- Anteil „Stufe C noch nicht sicher“: 41 % → 15 %. Anteil „mindestens D sicher“: 26 % → 52 %.
- Verteilung am Ende: C nicht sicher 15 % · C sicher 33 % · D sicher 33 % · E/F (★★★ sicher) 19 %.
- Etwa ein Fünftel holt deutlich auf (≥ +0,6 Stufen über dem Klassentrend), darunter zwei mit 🌱-Start.

**Schere:** SD des Niveau-Werts 0,93 → 1,13 (steigend). Ein Teil davon ist Messartefakt (Eingangstest bis E, Arbeit bis F). Inhaltlich: Rund 11 % bleiben über alle fünf Messpunkte unter Stufe C, ohne erkennbaren Zuwachs. Weitere rund 7 % fallen nach solidem Start in der Arbeit ab (Ursache offen). Der Unterricht hat das obere und mittlere Feld gut mitgenommen, das untere Zehntel kaum. **Hinweis:** Die Kleingruppe am Lehrertisch und das enaktive Material haben für diese Gruppe nicht ausgereicht. Sie braucht mehr und früher feste Lehrertisch-Zeit, gegebenenfalls einen zieldifferenten Strang.

**Kompetenzen (Lösungsquote Arbeit, Trend seit Eingangstest):**
- Stark: Geld/Stellenwert 94 % (↗), Darstellen/Anteile 77 % (→), Vergleichen/Ordnen 69 % (↗), Multiplizieren/Dividieren 69 % (↗, nur ★★/★★★-Wählende).
- Mittel: Erweitern/Kürzen 61 % (↗ von 46 %), Addieren/Subtrahieren 61 % (→), Sachaufgaben/Anteile 61 % (→), Zehnerpotenzen 63 % (→), Periodisch/TR 61 % (↗).
- **Schwach und stagnierend: Umwandeln Bruch ↔ Dezimal ↔ Prozent 54 %** (Eingangstest 57 %). Diese Kompetenz wurde nur in Std. 3 schwerpunktmäßig behandelt.

**Fehlerbilder im Lernbereich (Klassenarbeit; Kodierung nur in Teil A):**
- In der Gruppe „C sicher, D noch nicht“ (ein Drittel der Klasse): **AD 44 %, KV 44 %, ZN 44 %, LG 33 %** dieser Gruppe. Bezogen auf die ganze Klasse je 11–15 %.
- AD tritt insgesamt bei 30 % der Klasse auf. Alle Betroffenen haben im Wahlteil die einfachste Variante gewählt.
- ZP, TT, KT: je 7 % der Klasse, fast ausschließlich im unteren Zehntel und dort gehäuft (mehrere Fehlerbilder pro Person).
- **Hartnäckig (gleiche Person, ≥ 2 Messpunkte, auch in der Arbeit noch vorhanden):** AD 22 %, ZN 11 %, ZP 11 %, LG 7 %, KV 7 %, TT 7 %. → Die Förderung von AD (Std. 3, Hilfekarte H-KW, symbolisch-bildlich) wirkt bei einem Fünftel nicht.
- **Rückläufig:** LG und ZN wurden bei der großen Mehrheit der früher Betroffenen (rund drei Viertel und mehr) in der Arbeit nicht mehr beobachtet. NZ ist weitgehend verschwunden. Hier haben die Schwerpunktstunden (Std. 2 U-Bahn-Linie, Std. 5 Restekiste) gegriffen.

**Übergang D → E:** Wer D sicher hat und ★★ wählt, löst E-Aufgaben zu etwa 50 %. Engpass sind **mehrschrittige Anteilsaufgaben** (Anteil vom Ganzen, Rest als Bruch und Prozent; 35 %).

**Empfehlungen für die Überarbeitung der Einheit:**
1. Erweitern/Kürzen früher und enaktiv verankern (Bruchstreifen falten in Std. 1–2, nicht erst in Std. 3), da es Voraussetzung für ZN und Umwandeln ist.
2. Umwandeln als Spirale über mehrere Stunden statt als einzelne Schwerpunktstunde.
3. Für das untere Zehntel einen festen Lehrertisch-Strang ab Std. 1 einplanen.
4. Mehr mehrschrittige Anteilsaufgaben auf 🌿→🌳-Niveau (M6.1/M7.1).
5. Im Schlüssel der Arbeit die ★★★-Varianten in E- und F-Teile aufteilen und den Wahlteil künftig mit Fehlerbildern kodieren.

---

## 8. Förderpaket-Auftrag für `material-ersteller`

Vorhandenes zuerst: M0.2 (H-KW, H-ZN, H-KV, H-LG, H-ZP, H-KT), M0.4 (Bruchstreifen, Stellenwerttafel, Zahlenstrahl), M1.1 (Inventurkisten). Neu nötig sind nur kurze **Übungspakete** (je 10–15 Min., 3 Stufen, Selbstkontrolle auf der Rückseite, Späti-Kontext beibehalten, ohne Niveau-Etikett auf dem Schülerblatt):

| Paket | Zielgruppe (anonym) | Inhalt | Besonderheit |
|---|---|---|---|
| **FP-AD „Feiner einteilen“** | hartnäckiges AD (ca. 6 Personen) | Stufe 1: Streifen falten und Ergebnis ablesen (2/5 → ?/10, ?/20). Stufe 2: Etiketten prüfen („6/8 kg = 3/4 kg?“) mit Streifen-Kontrolle. Stufe 3: Fehlerlösungen „+ dieselbe Zahl“ widerlegen | **Neuer Zugang** gegenüber H-KW: rein enaktiv und mit Falt-Anleitung, Regel erst am Ende selbst formulieren |
| **FP-DZ „Komma und Stellen“** | KV / LG (ca. 6 Personen) | Stufe 1: Preise in die Stellenwerttafel legen (Rechengeld). Stufe 2: ×10/:100 als „Ziffern wandern“-Schieber. Stufe 3: Ordnen mit Nullen-Auffüllen und Lupe | Schiebestreifen zum Ausschneiden für die Stellenwerttafel |
| **FP-ZN „Gleich große Stücke“** | ZN (ca. 4 Personen), nach FP-AD | Stufe 1: Plausibilitätscheck „größer als jeder Summand?“. Stufe 2: gleichnamig machen mit Streifen. Stufe 3: Restekiste-Aufgaben (M5.1) mit Selbstkontrolle | baut auf FP-AD auf |
| **FP-G „Bruch, Geld, Anteil“** | unteres Zehntel (TT/ZP/KT gehäuft, ca. 3–4 Personen) | Stufe 1: Teil-Ganzes an Kisten (M1.1). Stufe 2: 1/2, 1/4, 1/5, 1/10 von 1 € mit Rechengeld. Stufe 3: dieselben Anteile als Dezimalzahl und Prozent | Vorlese-Version / Audio-Hinweis (Abstimmung mit `inklusion-sprachfoerderung`) |
| **FP-E „Anteile in mehreren Schritten“** | Übergang D → E (ca. 9 Personen) | Stufe 1: Anteil von einem Betrag. Stufe 2: zwei Anteile → Rest als Bruch. Stufe 3: Rest als Prozent + Probe auf zweitem Weg (Muster B3-2) | Signalwörter aus M0.3 an der Aufgabe markieren |

**Optional (Enrichment):** M0.7 „Tresorfragen“ fertigstellen (in 04 als optional geplant). Mindestens die Karten „0,9̅ = 1?“ und „periodisch → Bruch“ bis zur Rückgabe-Woche.
