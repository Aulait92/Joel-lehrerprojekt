# 02 – Diagnose: Trigonometrie (Mathematik, Kl. 10, Berlin, 8 × 60 Min.)

> **Grundlage:** `00-auftrag.md` (Vorrang), `01-lehrplanbezug.md` (Standards Abschn. 3, Fehlerbild-Kürzel Abschn. 7 – hier **unverändert** verwendet), `03-kreative-ideen.md` (Vermessungsbüro, Auftragskarten).
> **Niveaus:** 🪶 Feder = Stufe **F** (Fundament + G-Kern) · ◼ Gewicht = **G** (MSA) · ◼◼ Doppelgewicht = **H**. In allen Auswertungsdateien gilt: 🪶 = F, ◼ = G, ◼◼ = H.
> **Stand:** Es liegt **kein Klassenprofil** vor. Das Dokument enthält nur **Instrumente**. Ergebnisse werden mit Kürzeln (S01 …) in `klassen/<klasse>/` erfasst und mit `tools/lernauswertung.py` ausgewertet (siehe Abschn. 9).

**Inhalt**
1. Hinweise für die Lehrkraft
2. Vorwissens-Check Std. 1 („Einstellungstest“) – Schülerbogen
3. Item-Tabelle (nur Lehrkraft)
4. Auswertungsschlüssel und Fehlerbilder
5. Startempfehlung 🪶/◼/◼◼ – einfache Regel
6. Erfassungsbogen (nur Kürzel)
7. Selbsteinschätzungsbogen „Was geht?“ (Std. 1 / Std. 8)
8. Exit-Tickets 1–8 mit Lösungen
9. Auswertung mit dem Skript

---

## 1. Hinweise für die Lehrkraft

| Punkt | Hinweis |
|---|---|
| Zeitpunkt | Std. 1, Einstiegsphase **MSA-Basisaufgaben (8 Min.)**. Der Check **ersetzt** an diesem Tag die MSA-Basisaufgaben oder wird als „Teil 2“ daneben projiziert. Ritual wie gewohnt: „Notiere deine Lösungen auf einem eigenen Blatt. Arbeite alleine und ruhig! Nutze das Formelblatt und deinen Taschenrechner!“ |
| Umfang | 6 Items, je 1 Punkt, 8 Min. Items 1–3 sind Grundlagen, 4–5 MSA-typisch, 6 ist ein Ausblick (darf offen bleiben). |
| Rahmung im Büro-Szenario | „Einstellungstest im Vermessungsbüro Spree-Vermessung: Wir prüfen, welche Werkzeuge ihr schon mitbringt. Keine Note.“ |
| Hilfsmittel | Taschenrechner und Formelblatt **erlaubt** (wie im MSA). Item 6 prüft genau die Taschenrechner-Einstellung. |
| Ohne Bloßstellung | Auf dem Schülerbogen stehen **keine** Stufen und keine Symbole. Lösungen nicht laut im Plenum vergleichen, sondern nach dem Einsammeln kurz auflösen (Folie). |
| Sprache | Wortspeicher auf dem Bogen. Bei Fehlern in Item 1 und 4 kurz nachfragen: Mathe- oder Sprachhürde („Hypotenuse“, „Verhältnis“)? Im Erfassungsbogen mit **S** markieren. |
| Datenschutz | Vornamen bleiben auf den Papierbögen in der Klasse. Ins Projekt und nach `klassen/` gehen **nur Kürzel**. Die Zuordnungsliste bleibt bei Ihnen. |
| Korrekturzeit | ca. 1 Min. pro Bogen, für 28 Bögen ca. 25–30 Min. Exit-Tickets: 5 Min. pro Stunde (drei Stapel). |
| Selbsteinschätzung | „Was geht?“ (Abschn. 7) in Std. 1 nach der Zielfolie „Was geht am Ende der Stunde?“ oder am Ende von Std. 1 ausfüllen lassen (3 Min.), in Std. 8 die zweite Spalte. |

---

## 2. Vorwissens-Check – Schülerbogen

> ✂ ---------- Kopiervorlage / Folie (1 Seite) ----------

### Einstellungstest – Vermessungsbüro Spree-Vermessung

Klasse 10.___: Trigonometrie   Name: ______________________  Datum: ____________

**ca. 8 Minuten.** Arbeite alleine und ruhig. Taschenrechner und Formelblatt sind erlaubt.
Wenn du eine Aufgabe nicht kannst: Mach ein **?** und gehe weiter. Das ist **keine** Note.

**Wortspeicher:** **Hypotenuse** = Seite gegenüber dem rechten Winkel (die längste Seite) · **Kathete** = eine der beiden Seiten am rechten Winkel · **Verhältnis** = Quotient zweier Längen, z. B. 3 : 4 = 0,75 · **runden auf eine Nachkommastelle** = 8,06 → 8,1

---

**a)** Kreuze an, welche Seite die **Hypotenuse** ist.  (1 P)

```dreieck
winkel_A: 30
winkel_B: 60
namen: R S T
seiten: RS="t" RT="s" ST="r"
spiegeln: ja
breite: 240
```

☐ r  ☐ s  ☐ t

---

**b)** Ein rechtwinkliges Dreieck hat die Katheten **4,0 cm** und **7,0 cm**.
Berechne die Länge der Hypotenuse. Runde auf eine Nachkommastelle.  (1 P)

```dreieck
winkel_A: 29.7
winkel_B: 60.3
seiten: AC="b = 7,0 cm" BC="a = 4,0 cm" AB="c = ?"
breite: 260
```

c ≈ __________ cm

---

**c)** Gib die Lösung der Gleichung an:  **0,6 = a / 15**  (1 P)

a = __________

---

**d)** Die beiden Dreiecke haben **gleich große Winkel**.  (1 P)

```dreieck
winkel_A: 36.9
winkel_B: 53.1
seiten: BC="3,0 cm" AC="4,0 cm" AB="5,0 cm"
breite: 160
```

```dreieck
winkel_A: 36.9
winkel_B: 53.1
namen: D E F
seiten: EF="4,5 cm" DF="x" DE="y"
breite: 240
```

① Berechne die Länge x.   x = __________ cm
② Das Verhältnis **kurze Kathete : Hypotenuse** ist im großen Dreieck …
☐ größer als im kleinen  ☐ gleich groß  ☐ kleiner als im kleinen

---

**e)** Löse die Gleichung **0,35 = 7,4 / x** und runde auf eine Nachkommastelle.  (1 P)

x ≈ __________

---

**f)** Die Taste **sin** auf dem Taschenrechner gibt für einen Winkel im rechtwinkligen Dreieck das Verhältnis **Gegenkathete : Hypotenuse** an (das lernt ihr heute).
Jonas behauptet: **„Wenn ich den Winkel von 30° auf 60° verdopple, verdoppelt sich auch dieses Verhältnis.“**
Tippe sin(30) und sin(60) in deinen Taschenrechner. Hat Jonas recht? Begründe.  (1 P)

sin(30°) = ________  sin(60°) ≈ ________  ☐ Jonas hat recht ☐ Jonas hat nicht recht, weil ______________________

> ✂ ---------- Ende Schülerbogen ----------

---

## 3. Item-Tabelle (nur für die Lehrkraft)

| Item | Stufe | Kompetenz (CSV) | Bezug (01) | Fehlerbild bei falscher Antwort (01, Abschn. 7) |
|---|---|---|---|---|
| a) = 1 | **F** | Seiten benennen | Grundlage für G S. 45; K6 | **HYP**: r oder s angekreuzt (längste Seite in ungewohnter Lage nicht erkannt) |
| b) = 2 | **F** | Voraussetzungen | Pythagoras E S. 43; sinnvolle Genauigkeit F S. 45 | **PLAU**: √33 ≈ 5,7 (subtrahiert) oder 65 bzw. 11 – Hypotenuse kürzer als bzw. „falsch lang“; **RUND**: 8 oder 8,06225…; **HYP**: 7,0 als Hypotenuse behandelt |
| c) = 3 | **F** | Umstellen | Umstellen von Formeln E S. 54 | **UMS**: 0,04 (0,6 : 15) oder 25 (15 : 0,6) |
| d) = 4 | **G** | Verhältnisse | Längenverhältnisse bei Ähnlichkeit E S. 49 → Kernidee Std. 1 | ①: 5,5 (additiv +1,5, ohne eigenes Kürzel, in der Notiz vermerken); ② „größer“ → **LIN** (Verhältnis wächst mit der Dreiecksgröße, sin als „Länge“ gedacht) |
| e) = 5 | **G** | Umstellen | Umstellen mit Variable im Nenner; TR (K5) | **UMS**: 2,59 (0,35 · 7,4) oder 0,05 (0,35 : 7,4); **RUND**: 21 oder 21,142857 |
| f) = 6 | **H** | Verhältnisse | Begründen mit trig. Beziehungen H S. 50; K1, K5 | **RAD**: −0,99 und −0,30 (RAD) bzw. 0,45 und 0,81 (GRAD); **LIN**: „Jonas hat recht“ |

**Abdeckung:** Hypotenuse erkennen (1), Pythagoras (2), Ähnlichkeit/Verhältnisse (4, 6), Formel umstellen einfach (3) und mit Variable im Nenner (5), Taschenrechner (5, 6), Runden (2, 5).
**Bewusst nicht im Check:** An-/Gegenkathete und sin/cos/tan selbst – das ist Inhalt von Std. 1 und wird mit Exit-Ticket 1 erfasst.

---

## 4. Auswertungsschlüssel und Fehlerbilder

**Bepunktung:** jedes Item 1 Punkt. Item 4 und 6: Punkt nur, wenn beide Teile stimmen, sonst **0,5**. Fehlerbild-Kürzel dazuschreiben (z. B. `0:UMS`, `0,5:RUND`).

| Item | Richtig | Auch richtig | Häufige Fehlantwort → Kürzel |
|---|---|---|---|
| 1 | **t** | – | r, s → **HYP** |
| 2 | **c = √(4² + 7²) = √65 ≈ 8,1 cm** | 8,06 cm (0,5 P., **RUND**) | √33 ≈ 5,7 / 65 / 11 → **PLAU**; 8 oder 8,0622… → **RUND** (0,5 P.) |
| 3 | **a = 0,6 · 15 = 9** | – | 0,04 / 25 → **UMS** |
| 4 | ① **x = 4,0 · 1,5 = 6,0 cm** (Faktor 4,5 : 3,0 = 1,5); ② **gleich groß** (3 : 5 = 4,5 : 7,5 = 0,6) | ① 6 cm | ① 5,5 (additiv, Notiz); ② „größer“ → **LIN** |
| 5 | **x = 7,4 : 0,35 ≈ 21,1** | 21,14 (0,5 P., **RUND**) | 2,59 / 0,05 → **UMS**; 21 → **RUND** (0,5 P.) |
| 6 | **sin 30° = 0,5; sin 60° ≈ 0,87** → **nicht recht**, weil 0,87 nicht das Doppelte von 0,5 (= 1) ist | auch: „Das Verhältnis kann nie größer als 1 werden, weil die Hypotenuse die längste Seite ist.“ | −0,99 / −0,30 → **RAD** (TR-Modus DEG einstellen!); „recht“ → **LIN**; Werte richtig, Begründung fehlt → 0,5 P. |

**Hinweis Taschenrechner:** Wer bei Item 6 **RAD** zeigt, braucht vor dem ersten Rechnen in Std. 1 die Kontrolle „sin(30) muss 0,5 ergeben“ (Merksatz an die Tafel). Taucht RAD bei mehr als 3 Kürzeln auf: 2-Minuten-Plenum „Modus-Check“ für alle.

---

## 5. Startempfehlung 🪶/◼/◼◼ – einfache Regel

### Schritt 1 – Punkte pro Stufe

| Stufe | Items | max. | „sicher“ ab |
|---|---|---|---|
| F | 1–3 | 3 | **2** |
| G | 4–5 | 2 | **1,5** |
| H | 6 | 1 | **1** |

(Entspricht der Skript-Schwelle 66 %.)

### Schritt 2 – Startempfehlung für das Üben in Std. 1 und 2

| Wenn … | Empfehlung | Fokus |
|---|---|---|
| F **nicht** sicher (0–1,5 P.) | 🪶 | Feder-Blatt (Seiten markiert, ein Rechenschritt) + Mini-Förderung zum Fehlerbild (Schritt 3) |
| F sicher, G **nicht** sicher | 🪶 oder ◼ mit Hilfekarte „Umstellen“ (Wahl) | meist Lücke **UMS** (Variable im Nenner) oder **LIN** – kurz schließen, dann ◼ |
| F und G sicher, H nicht | ◼ | Gewicht-Blatt (AB1 vorhanden) |
| F, G und H sicher | ◼◼ anbieten | Doppelgewicht + „Wer schnell fertig ist …“-Aufgaben; auf Unterforderung achten |
| Sonderfall: H = 1, aber F < 2 | ◼ | Fehlerbilder ansehen (oft **RUND** oder **HYP** aus Flüchtigkeit) – Lücke ansprechen, nicht herabstufen |

Die Lehrkraft lässt die Lernenden **selbst wählen** („Bearbeite ein Arbeitsblatt …“). Die Empfehlung wird **leise** gegeben (Kürzel-Liste nur bei der Lehrkraft, ggf. Haftnotiz mit Symbol auf dem zurückgegebenen Bogen).

### Schritt 3 – Fehlerbild → Mini-Förderung (5 Min., Hilfekarte oder Tischgruppe)

| Kürzel | Mini-Förderung |
|---|---|
| **HYP** | „Die Hypotenuse liegt dem rechten Winkel gegenüber“ – Dreieck drehen, rechten Winkel mit dem Finger zudecken: Die Seite, die man dann noch „sieht“, ist die Hypotenuse. |
| **PLAU** | Kontrollfrage nach jeder Rechnung: Ist die Hypotenuse die längste Seite? Ist der Wert kleiner als die Summe der Katheten? |
| **RUND** | Erst am Ende runden, Zwischenergebnis im TR-Speicher lassen (Ans-Taste). Regel: so genau wie die Angaben (eine Nachkommastelle). |
| **UMS** | Probe mit Zahlen: 0,5 = 4 / x. Was muss x sein? (8) – „Was im Nenner steht, wird zum Faktor auf der anderen Seite: x · 0,5 = 4, dann x = 4 : 0,5.“ |
| **LIN** | GeoGebra oder Falten aus Std. 1: großes und kleines Dreieck mit gleichen Winkeln, Verhältnisse vergleichen. „Gleiche Winkel → gleiche Verhältnisse, egal wie groß.“ |
| **RAD** | DEG-Modus einstellen (Modell-spezifische Kurzkarte), Kontrolle sin(30) = 0,5 auf jede Hilfekarte drucken. |

> Taucht ein Fehlerbild bei **mehr als ⅓ der Klasse** auf, lohnt ein gemeinsamer 3-Minuten-Impuls statt Einzelförderung.

### Schritt 4 – Abgleich mit der Selbsteinschätzung (Abschn. 7)
- Check gut, Selbsteinschätzung viele 🔴 → ermutigen, ◼ oder ◼◼ vorschlagen, Wahl lassen.
- Check schwach, viele 🟢 → Fehler im Einzelgespräch ansehen, nicht im Plenum.
- Item 6 richtig und Std.-1-Blatt schnell fertig → ◼◼ und Zusatzaufgaben (Begabtenförderung).

### ⚠ Gruppen sind flexibel
- Die Empfehlung gilt **nur für den Einstieg** und wird **nach jedem Exit-Ticket** neu angesehen. Wechsel in beide Richtungen ist ausdrücklich erwünscht.
- 🪶/◼/◼◼ beschreiben **Aufgaben**, nicht Personen: „Du startest mit dem Gewicht-Blatt“ – nicht „Du bist Gewicht“.
- Kein Urteil aus einem einzelnen Test: Erst Check + Exit-Ticket 1 + 2 zusammen ergeben ein Bild.
- Feste Zeitpunkte für den Blick auf die Gruppen: nach ET 2 (Ende rechtwinklig), nach ET 4 (Übergang zu beliebigen Dreiecken), nach ET 7 (vor dem Abschluss-Gutachten).

---

## 6. Erfassungsbogen (nur Kürzel)

> Eintrag: **1** / **0,5** / **0**, **–** = nichts geschrieben. Fehlerbild dazu: `0:UMS`. **S** = evtl. Sprachhürde.
> Digital: Vorlage `auswertung/vorwissen.vorlage.csv` nach `klassen/<klasse>/<JJJJ-MM-TT>_vorwissen.csv` kopieren.

### 6a. Vorwissens-Check

| Kürzel | 1 | 2 | 3 | **F** | 4 | 5 | **G** | 6 | **H** | Selbsteinsch. Std. 1 (überwiegend 🟢/🟡/🔴) | Empfehlung | Fehlerbilder / Notiz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | | | | | | | | | | | | |
| S02 | | | | | | | | | | | | |
| S03 | | | | | | | | | | | | |
| S04 | | | | | | | | | | | | |
| S05 | | | | | | | | | | | | |
| S06 | | | | | | | | | | | | |
| S07 | | | | | | | | | | | | |
| S08 | | | | | | | | | | | | |
| S09 | | | | | | | | | | | | |
| S10 | | | | | | | | | | | | |
| S11 | | | | | | | | | | | | |
| S12 | | | | | | | | | | | | |
| S13 | | | | | | | | | | | | |
| S14 | | | | | | | | | | | | |
| S15 | | | | | | | | | | | | |
| S16 | | | | | | | | | | | | |
| S17 | | | | | | | | | | | | |
| S18 | | | | | | | | | | | | |
| S19 | | | | | | | | | | | | |
| S20 | | | | | | | | | | | | |
| S21 | | | | | | | | | | | | |
| S22 | | | | | | | | | | | | |
| S23 | | | | | | | | | | | | |
| S24 | | | | | | | | | | | | |
| S25 | | | | | | | | | | | | |
| S26 | | | | | | | | | | | | |
| S27 | | | | | | | | | | | | |
| S28 | | | | | | | | | | | | |
| **Anzahl richtig** | | | | | | | | | | | | |

**Klassenüberblick:** 🪶 ___  ◼ ___  ◼◼ ___   Häufigste Fehlerbilder: ____________

### 6b. Exit-Tickets (gewähltes Niveau + Stapel)

> Eintrag z. B. `◼2` = Gewicht gewählt, sicher; `🪶1:UMS` = Feder, fast, Umstellfehler. In der CSV nur in der Spalte des gewählten Niveaus (`ET2-G`) die Zahl eintragen.

| Kürzel | ET1 | ET2 | ET3 | ET4 | ET5 | ET6 | ET7 | ET8 | Selbsteinsch. Std. 8 | Notiz / nächster Schritt |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | | | | | | | | | | |
| S02 | | | | | | | | | | |
| S03 | | | | | | | | | | |
| S04 | | | | | | | | | | |
| S05 | | | | | | | | | | |
| S06 | | | | | | | | | | |
| S07 | | | | | | | | | | |
| S08 | | | | | | | | | | |
| S09 | | | | | | | | | | |
| S10 | | | | | | | | | | |
| S11 | | | | | | | | | | |
| S12 | | | | | | | | | | |
| S13 | | | | | | | | | | |
| S14 | | | | | | | | | | |
| S15 | | | | | | | | | | |
| S16 | | | | | | | | | | |
| S17 | | | | | | | | | | |
| S18 | | | | | | | | | | |
| S19 | | | | | | | | | | |
| S20 | | | | | | | | | | |
| S21 | | | | | | | | | | |
| S22 | | | | | | | | | | |
| S23 | | | | | | | | | | |
| S24 | | | | | | | | | | |
| S25 | | | | | | | | | | |
| S26 | | | | | | | | | | |
| S27 | | | | | | | | | | |
| S28 | | | | | | | | | | |

---

## 7. Selbsteinschätzungsbogen „Was geht?“

> ✂ ---------- Kopiervorlage ----------

### Trigonometrie – Was geht?

Klasse 10.___: Trigonometrie   Name: ______________________

**So geht's:** Lies jeden Satz. Male in **Std. 1** und in **Std. 8** einen Kreis aus. Ehrlich sein lohnt sich – es gibt keine Note.

🟢 Das kann ich sicher und könnte es erklären. 🟡 Das klappt manchmal. 🔴 Das kann ich noch nicht.

| Nr. | Ich kann … | Beispiel | Std. 1 | Std. 8 |
|---|---|---|---|---|
| | 🪶 | | | |
| 1 | … im rechtwinkligen Dreieck Hypotenuse, Ankathete und Gegenkathete zu einem markierten Winkel benennen. | Gegenkathete von α liegt α gegenüber. | ○ | ○ |
| 2 | … aus einer Skizze die passende Formel (sin/cos/tan) auswählen und **eine** fehlende Seite in einem Schritt berechnen. | a = 6,5 · sin(38°) | ○ | ○ |
| 3 | … eine einfache Formel wie a = c · sin(α) nach der gesuchten Größe umstellen. | c = a : sin(α) | ○ | ○ |
| 4 | … mein Ergebnis sinnvoll runden und prüfen, ob es passt. | Kathete kürzer als Hypotenuse? | ○ | ○ |
| | ◼ | | | |
| 5 | … im rechtwinkligen Dreieck jede fehlende Seite und jeden fehlenden Winkel berechnen, auch mit sin⁻¹. | α = sin⁻¹(4 : 6,5) ≈ 38,0° | ○ | ○ |
| 6 | … eine Sachsituation (Dach, Leiter, Rampe) skizzieren und als Dreieck lösen. | Dachhöhe mit dem Geometer | ○ | ○ |
| 7 | … ein beliebiges Dreieck mit einer Höhe in zwei rechtwinklige Dreiecke zerlegen. | h = b · sin(α) | ○ | ○ |
| 8 | … entscheiden, ob ich den Sinussatz oder den Kosinussatz brauche, und damit Seiten berechnen. | zwei Seiten + eingeschlossener Winkel → Kosinussatz | ○ | ○ |
| | ◼◼ | | | |
| 9 | … mit dem Kosinussatz aus drei Seiten einen Winkel berechnen. | 7 m, 8 m, 12 m → γ ≈ 106,1° | ○ | ○ |
| 10 | … begründen, warum der Sinussatz gilt (Herleitung über die Höhe). | h = b · sin α = a · sin β | ○ | ○ |
| 11 | … erklären, warum der Satz des Pythagoras ein Sonderfall des Kosinussatzes ist. | γ = 90° → cos γ = 0 | ○ | ○ |
| 12 | … erkennen, wann es bei SSW zwei Lösungen gibt. | β oder 180° − β | ○ | ○ |
| 13 | … erklären, was RAD auf dem Taschenrechner bedeutet. | sin(30) = −0,99?! | ○ | ○ |

**Std. 8:** Darauf bin ich stolz: ______________________  Das übe ich noch: ______________________

> ✂ ---------- Ende Selbsteinschätzungsbogen ----------

**Hinweis für die Lehrkraft:** Sätze wörtlich aus `01-lehrplanbezug.md`, Abschn. 3 („Ich kann …“). Zuordnung zu Instrumenten: 1 → Check 1 / ET1 · 2 → ET1, ET2 · 3 → Check 3, 5 / ET2 · 4 → Check 2, 5 / ET3 · 5 → ET2 · 6 → ET3 · 7 → ET4 · 8 → ET5–ET8 · 9, 11 → ET7 ◼◼ · 10 → ET5 ◼◼ · 12 → ET6 ◼◼ · 13 → Check 6. Satz 12 (SSW) ist im RLP nicht ausdrücklich genannt (01: „nicht verifiziert“). Wer die Symbolzeilen nicht möchte, deckt sie beim Kopieren ab.

---

## 8. Exit-Tickets 1–8

**Prinzip:** halbes A5-Blatt, **4 Min.** am Stundenende, **eine** Aufgabe auf drei Niveaus, **freie Wahl** (Empfehlung: das Niveau, an dem man heute gearbeitet hat; Mutige dürfen höher). Kopf jeweils: „Exit-Ticket N  Name: ______“. Unten: „Heute: 🟢 verstanden 🟡 teilweise 🔴 noch nicht“.

**Auswertung (5 Min.):** drei Stapel = Punkte für die CSV:
**2 = sicher** (richtig mit nachvollziehbarem Weg) → nächste Stunde gleich oder höher · **1 = fast** (Ansatz richtig, ein Fehler) → Hilfekarte zum Fehlerbild · **0 = noch nicht** (Ansatz fehlt oder falsch) → Mini-Förderung zu Stundenbeginn (Abschn. 5, Schritt 3). Fehlerbild-Kürzel aus 01, Abschn. 7 dazuschreiben.
**Lösungscode-Idee (03, Idee 2):** Ergebnisse der Exit-Tickets in der Folgestunde als „Büro-Prüfstempel“ an die Tafel, Selbstkontrolle beim Zurückgeben.

---

### Exit-Ticket 1 – Verhältnisse aufstellen (Std. 1)

> ✂ ----------

**Exit-Ticket 1**  Name: ______________  Wähle **eine** Aufgabe.

🪶 Ergänze die Verhältnisse.

```dreieck
winkel_A: 37
winkel_B: 53
seiten: AB="c" AC="b" BC="a"
winkel: A="α"
breite: 240
```

sin(α) = ―――  cos(α) = ―――  tan(α) = ―――

◼ Achtung, der rechte Winkel liegt bei A. Gib die Verhältnisse an.

```dreieck
winkel_A: 90
winkel_B: 35
seiten: AB="c" AC="b" BC="a"
winkel: B="β" C="γ"
breite: 240
```

sin(β) = ―――  cos(β) = ―――  tan(γ) = ―――

◼◼ Ein rechtwinkliges Dreieck hat a = 3,0 cm, b = 4,0 cm, c = 5,0 cm (rechter Winkel bei C).
① Berechne sin(α) und cos(β). ② Begründe, warum sin(α) = cos(β) in **jedem** rechtwinkligen Dreieck gilt.

```dreieck
winkel_A: 36.9
winkel_B: 53.1
seiten: BC="a = 3,0 cm" AC="b = 4,0 cm" AB="c = 5,0 cm"
winkel: A="α" B="β"
breite: 220
```

> ✂ ----------

**Lösungen ET1**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | sin(α) = **a/c**, cos(α) = **b/c**, tan(α) = **a/b** | 3 richtig / 2 richtig / sonst | b/c bei sin → **VER**; c im Zähler/als Kathete → **HYP**; a und b vertauscht → **AG** |
| ◼ G | Hypotenuse ist **a**. sin(β) = **b/a**, cos(β) = **c/a**, tan(γ) = **c/b** | 3 / 2 / sonst | c als Nenner → **HYP**; bei γ wie bei β gedacht (tan γ = b/c) → **AG** |
| ◼◼ H | ① sin(α) = 3/5 = **0,6**; cos(β) = a/c = 3/5 = **0,6**. ② Die Seite a ist **Gegenkathete von α** und zugleich **Ankathete von β**; beide Verhältnisse sind „a durch c“. (Auch: β = 90° − α.) | ① + ② / nur ① / sonst | 4/5 → **AG**; „weil 3-4-5 besonders ist“ → Begründung unvollständig (1) |

---

### Exit-Ticket 2 – Winkel berechnen und umstellen (Std. 2)

> ✂ ----------

**Exit-Ticket 2**  Name: ______________  Wähle **eine** Aufgabe.

🪶 Berechne den Winkel α.

```dreieck
winkel_A: 38
winkel_B: 52
seiten: BC="a = 4,0 cm" AB="c = 6,5 cm" AC="b"
winkel: A="α = ?"
breite: 240
```

◼ Kunde Feuerwehr: Eine Leiter lehnt im Winkel von **70°** an einer Wand und reicht **8,0 m** hoch. Wie lang ist die Leiter?

```dreieck
winkel_A: 70
winkel_B: 90
namen: F M S
seiten: FS="Leiter = ?" MS="8,0 m"
winkel: F="70°"
breite: 180
```

◼◼ Eine Drehleiter ist **30 m** lang, ihr Drehpunkt liegt **3,0 m** über dem Boden.
① Unter welchem Winkel muss sie stehen, um ein Fenster in **25 m** Höhe zu erreichen?
② Der Anstellwinkel darf höchstens **75°** sein. Wie lang muss die Leiter mindestens ausgefahren werden, um die 25 m zu erreichen?

> ✂ ----------

**Lösungen ET2**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | sin(α) = 4,0 / 6,5 ≈ 0,6154; α = sin⁻¹(0,6154) ≈ **38,0°** | richtig / Ansatz richtig, TR-Fehler / sonst | sin(0,6154) ≈ 0,0107 → **UMK**; 1/sin(0,6154) → **INV**; Ergebnis 0,66 bzw. 0,67 → **RAD** (sin⁻¹ im RAD-Modus); cos/tan gewählt → **VER** |
| ◼ G | sin(70°) = 8,0 / c ⇒ c = 8,0 / sin(70°) = 8,0 / 0,9397 ≈ **8,5 m** | richtig / Ansatz richtig, Rundung o. ä. / sonst | c = 8,0 · sin(70°) ≈ 7,5 m → **UMS** + **PLAU** (Leiter kürzer als Höhe!) |
| ◼◼ H | ① Höhenunterschied 25 − 3 = 22 m; sin(α) = 22/30 ≈ 0,7333; α ≈ **47,2°**. ② c = 22 / sin(75°) = 22 / 0,9659 ≈ **22,8 m** | ① + ② / ein Teil / sonst | sin(α) = 25/30 → α ≈ 56,4° → **AUG** (Gerätehöhe nicht abgezogen); ② 22 · sin 75° ≈ 21,3 m → **UMS** |

---

### Exit-Ticket 3 – Messung auswerten (Std. 3, Außeneinsatz)

> ✂ ----------

**Exit-Ticket 3**  Name: ______________  Wähle **eine** Aufgabe.

🪶 Ein Trupp hat gemessen: Abstand zur Wand **18,0 m**, Höhenwinkel **35°**, Augenhöhe **1,60 m**. Ergänze und rechne.

<svg width="320" height="175" viewBox="0 0 320 175" font-size="12" font-family="sans-serif">
  <line x1="10" y1="150" x2="310" y2="150" stroke="black"/>
  <rect x="250" y="20" width="50" height="130" fill="none" stroke="black"/>
  <line x1="40" y1="150" x2="40" y2="118" stroke="black" stroke-width="2"/>
  <circle cx="40" cy="112" r="6" fill="none" stroke="black"/>
  <line x1="40" y1="118" x2="250" y2="118" stroke="black" stroke-dasharray="4 3"/>
  <line x1="40" y1="118" x2="250" y2="20" stroke="black"/>
  <text x="80" y="113">35°</text>
  <text x="125" y="167">18,0 m</text>
  <text x="2" y="138">1,60 m</text>
  <text x="205" y="75">x</text>
  <text x="255" y="14">Dachkante</text>
</svg>

x = 18,0 · ______(35°) ≈ ______ m  Dachhöhe = x + ______ ≈ ______ m

◼ Messung: Abstand **24,5 m**, Höhenwinkel **28°**, Augenhöhe **1,55 m**.
① Berechne die Dachhöhe. ② Trupp B hat mit demselben Abstand **47,6 m** herausbekommen. Finde den Fehler.

◼◼ Messung: Abstand **20,0 m**, Augenhöhe **1,60 m**, Höhenwinkel **36°** – der Geometer ist aber nur auf **± 1°** genau.
① Berechne die Dachhöhe für 35°, 36° und 37°. ② Mit welcher Genauigkeit sollte das Büro die Höhe angeben? Begründe.

> ✂ ----------

**Lösungen ET3**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | x = 18,0 · **tan**(35°) ≈ 18,0 · 0,7002 ≈ 12,6 m; Dachhöhe ≈ 12,6 + 1,60 ≈ **14,2 m** | richtig / nur x / sonst | 12,6 m als Ergebnis → **AUG**; sin/cos statt tan → **VER**; 18 · tan(35 rad) ≈ 8,5 → **RAD** |
| ◼ G | ① 24,5 · tan(28°) ≈ 24,5 · 0,5317 ≈ 13,0 m; + 1,55 m ≈ **14,6 m**. ② Trupp B hat **62° = 90° − 28°** abgelesen: 24,5 · tan(62°) + 1,55 ≈ 47,6 m. Ein 47 m hohes Schuldach ist unrealistisch. | ① + ② / ein Teil / sonst | ② nicht gefunden → **MESS**, keine Bewertung → **PLAU**; 13,0 m → **AUG** |
| ◼◼ H | ① 35°: 20,0 · 0,7002 + 1,60 ≈ **15,6 m**; 36°: 20,0 · 0,7265 + 1,60 ≈ **16,1 m**; 37°: 20,0 · 0,7536 + 1,60 ≈ **16,7 m**. ② Schwankung etwa ± 0,5 m → Angabe „**ca. 16 m**“ (auf ganze bzw. halbe Meter), nicht 16,13 m. | ① + ② / nur ① / sonst | Angabe mit cm → **RUND**; Augenhöhe vergessen → **AUG** |

---

### Exit-Ticket 4 – Zerlegung in rechtwinklige Teildreiecke (Std. 4)

> ✂ ----------

**Exit-Ticket 4**  Name: ______________  Wähle **eine** Aufgabe.

Gemeinsames Dreieck für 🪶 und ◼: α = 40°, β = 65°, b = 7,0 cm. Die Höhe h von C auf die Seite c hat den Fußpunkt D.

```dreieck
winkel_A: 40
winkel_B: 65
seiten: AC="b = 7,0 cm" BC="a" AB="c"
winkel: A="α = 40°" B="β = 65°"
breite: 260
```

🪶 Das Teildreieck ADC ist rechtwinklig. Berechne die Höhe h.

```dreieck
winkel_A: 40
winkel_B: 90
namen: A D C
seiten: AC="b = 7,0 cm" DC="h" AD=""
winkel: A="40°"
breite: 200
```

◼ Zeichne h ein. Berechne h und die Seite a.

◼◼ Das Büro darf nicht bis an die Wand: Von Standpunkt S₁ sieht man die Dachkante unter **30°**, von S₂, das **15,0 m** näher am Gebäude liegt, unter **45°**. Augenhöhe **1,50 m**. Berechne die Dachhöhe.

<svg width="320" height="170" viewBox="0 0 320 170" font-size="12" font-family="sans-serif">
  <line x1="10" y1="150" x2="310" y2="150" stroke="black"/>
  <line x1="280" y1="150" x2="280" y2="30" stroke="black" stroke-width="2"/>
  <line x1="72" y1="150" x2="280" y2="30" stroke="black"/>
  <line x1="160" y1="150" x2="280" y2="30" stroke="black"/>
  <text x="62" y="166">S₁</text>
  <text x="152" y="166">S₂</text>
  <text x="96" y="146">30°</text>
  <text x="178" y="146">45°</text>
  <text x="100" y="128">15,0 m</text>
  <text x="285" y="95">h</text>
</svg>

(Skizze ohne Augenhöhe.)

> ✂ ----------

**Lösungen ET4**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | sin(40°) = h / 7,0 ⇒ h = 7,0 · sin(40°) ≈ 7,0 · 0,6428 ≈ **4,5 cm** | richtig / Ansatz richtig / sonst | cos statt sin → **VER** bzw. **AG**; sin im ganzen Dreieck ABC angesetzt → **RW** |
| ◼ G | h ≈ 4,50 cm (wie 🪶). Im Teildreieck DBC: sin(65°) = h / a ⇒ a = 4,50 / 0,9063 ≈ **5,0 cm** (4,96 cm). Kontrolle mit Sinussatz: 7,0 · sin 40° / sin 65° ≈ 4,96 cm. | h und a / nur h / sonst | a = h · sin 65° ≈ 4,1 → **UMS**; mit gerundetem h = 4 gerechnet → **RUND**; sin(β) = h/c → **RW** |
| ◼◼ H | Abstand S₂–Wand = h / tan 45° = h; Abstand S₁–Wand = h / tan 30° ≈ 1,7321 h. Differenz: 1,7321 h − h = 15,0 ⇒ h = 15,0 / 0,7321 ≈ 20,5 m. Dachhöhe ≈ 20,5 + 1,50 ≈ **22,0 m** | richtig / h ≈ 20,5 m ohne Augenhöhe bzw. Ansatz richtig / sonst | sin/tan im schiefwinkligen Dreieck S₁S₂-Dach → **RW**; 20,5 m → **AUG** |

---

### Exit-Ticket 5 – Sinussatz (Std. 5)

> ✂ ----------

**Exit-Ticket 5**  Name: ______________  Wähle **eine** Aufgabe.

🪶 Berechne b mit dem Sinussatz:  a / sin(α) = b / sin(β)

```dreieck
winkel_A: 50
winkel_B: 70
seiten: BC="a = 6,0 cm" AC="b = ?" AB="c"
winkel: A="α = 50°" B="β = 70°"
breite: 240
```

◼ Gegeben: c = 8,0 cm, α = 48°, β = 62°. Berechne a.

```dreieck
winkel_A: 48
winkel_B: 62
seiten: AB="c = 8,0 cm" BC="a = ?" AC="b"
winkel: A="α = 48°" B="β = 62°"
breite: 240
```

◼◼ Zeige mithilfe der Höhe h_c, dass in jedem spitzwinkligen Dreieck gilt: a / sin(α) = b / sin(β).

> ✂ ----------

**Lösungen ET5**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | b = 6,0 · sin(70°) / sin(50°) = 6,0 · 0,9397 / 0,7660 ≈ **7,4 cm** | richtig / Einsetzen richtig, Umstellen falsch / sonst | 6,0 · sin 50° / sin 70° ≈ 4,9 → **PAAR** bzw. **UMS** |
| ◼ G | γ = 180° − 48° − 62° = **70°**; a = 8,0 · sin(48°) / sin(70°) = 8,0 · 0,7431 / 0,9397 ≈ **6,3 cm** | richtig / γ fehlt, sonst richtig / sonst | c mit sin(62°) gepaart → a ≈ 6,7 → **PAAR**; Winkelsumme ≠ 180° → **PLAU** |
| ◼◼ H | Im rechtwinkligen Teildreieck ADC: sin α = h_c / b ⇒ h_c = b · sin α. Im Teildreieck DBC: sin β = h_c / a ⇒ h_c = a · sin β. Gleichsetzen: b · sin α = a · sin β ⇒ a / sin α = b / sin β. | vollständig / ein Teildreieck richtig / sonst | sin im ganzen Dreieck → **RW**; a mit sin α im falschen Teildreieck → **PAAR** |

---

### Exit-Ticket 6 – Sinussatz anwenden (Std. 6)

> ✂ ----------

**Exit-Ticket 6**  Name: ______________  Wähle **eine** Aufgabe.

Gemeinsame Situation für 🪶 und ◼: Am Spreeufer liegen A und B **80 m** auseinander. Ein Baum C steht am anderen Ufer. Gemessen: α = **62°** (bei A), β = **71°** (bei B). (Werte angenommen.)

```dreieck
winkel_A: 62
winkel_B: 71
seiten: AB="c = 80 m" AC="b = ?" BC="a"
winkel: A="62°" B="71°"
breite: 240
```

🪶 Berechne γ und die Entfernung von A zum Baum (b).

◼ Wie breit ist die Spree hier (Abstand von C zur Uferlinie AB)?

◼◼ Gegeben: a = 5,0 cm, b = 6,0 cm, α = 40°. Berechne β. Wie viele Dreiecke gibt es? Begründe.

> ✂ ----------

**Lösungen ET6**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | γ = 180° − 62° − 71° = **47°**; b = 80 · sin(71°) / sin(47°) = 80 · 0,9455 / 0,7314 ≈ **103 m** (103,4 m) | richtig / nur γ oder Rechenfehler / sonst | 80 · sin 62° / sin 47° ≈ 97 m → **PAAR**; γ falsch → **PLAU** |
| ◼ G | b ≈ 103,4 m (wie 🪶), Breite = b · sin(62°) ≈ 103,4 · 0,8829 ≈ **91 m** | richtig / nur b / sonst | Breite = b oder c → **RW** (Abstand ist das Lot); mit b = 100 gerechnet → **RUND** |
| ◼◼ H | sin β = 6,0 · sin(40°) / 5,0 ≈ 0,7713 ⇒ β₁ ≈ **50,5°** oder β₂ = 180° − 50,5° ≈ **129,5°**. Beide möglich, weil α + β₂ ≈ 169,5° < 180°: **zwei Dreiecke** (γ₁ ≈ 89,5°, c₁ ≈ 7,8 cm; γ₂ ≈ 10,5°, c₂ ≈ 1,4 cm – Zusatz). | beide β + Begründung / nur β₁ / sonst | nur 50,5° → **SSW**; sin β = 5 · sin 40° / 6 → **PAAR** |

---

### Exit-Ticket 7 – Kosinussatz (Std. 7)

> ✂ ----------

**Exit-Ticket 7**  Name: ______________  Wähle **eine** Aufgabe.

🪶 Berechne c mit  c² = a² + b² − 2ab · cos(γ).

```dreieck
winkel_A: 43.9
winkel_B: 76.1
seiten: BC="a = 5,0 cm" AC="b = 7,0 cm" AB="c = ?"
winkel: C="γ = 60°"
breite: 240
```

◼ Von einem Standpunkt aus sind zwei Funkmasten **4,2 km** und **5,8 km** entfernt. Die Peilrichtungen schließen einen Winkel von **73°** ein. Wie weit sind die Masten voneinander entfernt?

```dreieck
winkel_A: 41.3
winkel_B: 65.7
namen: M1 M2 S
seiten: S-M2="4,2 km" S-M1="5,8 km" M1-M2="?"
winkel: S="73°"
breite: 240
```

◼◼ Ein dreieckiges Grundstück hat die Seiten **7,0 m**, **8,0 m** und **12,0 m**.
① Berechne den größten Winkel. ② Begründe ohne Kosinussatz, dass dieser Winkel stumpf sein muss.

> ✂ ----------

**Lösungen ET7**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | c² = 25 + 49 − 2 · 5,0 · 7,0 · 0,5 = 74 − 35 = 39; c = √39 ≈ **6,2 cm** | richtig / Wurzel vergessen (39) / sonst | + 35 → √109 ≈ 10,4 → **KVZ**; (74 − 70) · 0,5 = 2 → **KRF**; 39 ohne Wurzel → **KRF**; cos(60 rad) → **RAD** |
| ◼ G | d² = 4,2² + 5,8² − 2 · 4,2 · 5,8 · cos(73°) = 17,64 + 33,64 − 48,72 · 0,2924 ≈ 51,28 − 14,24 = 37,04; d ≈ **6,1 km** | richtig / ein Rechenfehler / sonst | + 14,24 → ≈ 8,1 km → **KVZ**; (51,28 − 48,72) · cos 73° → **KRF**; Sinussatz versucht → **FALL** |
| ◼◼ H | ① Größter Winkel γ liegt der 12,0-m-Seite gegenüber: cos γ = (7² + 8² − 12²) / (2 · 7 · 8) = −31 / 112 ≈ −0,2768; γ ≈ **106,1°**. ② 12² = 144 > 7² + 8² = 113: Die längste Seite ist länger als beim rechten Winkel (Pythagoras als Grenzfall), also ist γ > 90°. | ① + ② / ein Teil / sonst | Winkel gegenüber 7 m statt 12 m → **KZU**; „negativer cos ist falsch“ → **PLAU** |

---

### Exit-Ticket 8 – Welcher Satz passt? (Std. 8)

> ✂ ----------

**Exit-Ticket 8**  Name: ______________  Wähle **eine** Aufgabe.

🪶 Welcher Weg passt? Schreibe **R** (rechtwinklig: sin/cos/tan), **S** (Sinussatz) oder **K** (Kosinussatz).

① rechter Winkel bei C, c = 7 cm, α = 35°, gesucht a  ____
② a = 5 cm, b = 6 cm, γ = 48°, gesucht c  ____
③ a = 6 cm, α = 40°, β = 75°, gesucht b  ____
④ a = 4 cm, b = 5 cm, c = 6 cm, gesucht γ  ____

◼ Gegeben: b = 9,0 cm, c = 6,0 cm, α = 52°. Welcher Satz passt? Begründe kurz und berechne a.

```dreieck
winkel_A: 52
winkel_B: 86.3
seiten: AC="b = 9,0 cm" AB="c = 6,0 cm" BC="a = ?"
winkel: A="α = 52°"
breite: 240
```

◼◼ Ein Dreieck hat die Seiten **6,0 cm**, **9,0 cm** und **11,0 cm**. Berechne den **größten** Winkel und begründe, warum man bei SSS zuerst den größten Winkel berechnen sollte. (Zusatz: die übrigen Winkel.)

> ✂ ----------

**Lösungen ET8**

| Niveau | Lösung | 2 / 1 / 0 | Fehlerbilder |
|---|---|---|---|
| 🪶 F | ① **R** (a = 7 · sin 35°) ② **K** (zwei Seiten + eingeschlossener Winkel) ③ **S** (Seite + gegenüberliegender Winkel bekannt) ④ **K** (drei Seiten) | 4 richtig / 3 richtig / sonst | ② oder ④ mit S → **FALL**; R bei ②–④ → **RW** |
| ◼ G | Kosinussatz, weil zwei Seiten und der **eingeschlossene** Winkel gegeben sind (kein Paar Seite/Gegenwinkel). a² = 81 + 36 − 2 · 9,0 · 6,0 · cos(52°) = 117 − 108 · 0,6157 ≈ 117 − 66,49 = 50,51; a ≈ **7,1 cm** | Wahl + a / a richtig ohne Begründung oder Wahl richtig mit Rechenfehler / sonst | Sinussatz versucht → **FALL**; + 66,49 → ≈ 13,1 cm → **KVZ**; (117 − 108) · cos 52° → **KRF** |
| ◼◼ H | Größter Winkel γ gegenüber 11,0 cm: cos γ = (36 + 81 − 121) / (2 · 6 · 9) = −4 / 108 ≈ −0,0370; γ ≈ **92,1°**. Begründung: Mit sin⁻¹ (Sinussatz) erhält man nur Winkel bis 90°; ein stumpfer Winkel würde übersehen. Die beiden kleineren Winkel sind sicher spitz. Zusatz: α ≈ 33,0° (gegenüber 6,0 cm), β ≈ 54,8° (gegenüber 9,0 cm). | γ + Begründung / nur γ / sonst | γ per Sinussatz als 87,9° → **SSW**/**FALL**; Winkel nicht der passenden Seite gegenüber → **KZU** |

---

## 9. Auswertung mit dem Skript

| Instrument | Schlüssel | Erfassung (Kopie nach `klassen/<klasse>/`) | Gruppen-Parameter |
|---|---|---|---|
| Vorwissens-Check (Abschn. 2) | `auswertung/vorwissen.schluessel.csv` | `auswertung/vorwissen.vorlage.csv` | `keine:🪶,F:🪶/◼,G:◼,H:◼◼` |
| Exit-Ticket 1–8 (Abschn. 8) | `auswertung/exit-ticket-N.schluessel.csv` | `auswertung/exit-ticket-N.vorlage.csv` | – |

- Punkte: Check `1` / `0,5` / `0`; Exit-Tickets nur in der Spalte des **gewählten** Niveaus `2` / `1` / `0`, andere Spalten **leer**. Fehlerbild mit Doppelpunkt: `0:UMS`, mehrere mit `+`: `1:AUG+RUND`. `-` = vorgelegt, nichts geschrieben.
- Kompetenz-Namen (einheitlich in allen Schlüsseln): Seiten benennen · Voraussetzungen · Verhältnisse · Umstellen · Winkel berechnen · Modellieren/Messen · Zerlegung · Sinussatz · Kosinussatz · Satzwahl.
- Beispiel: `python3 tools/lernauswertung.py test --schluessel unterricht/mathematik-trigonometrie/auswertung/vorwissen.schluessel.csv --ergebnisse klassen/<klasse>/<datum>_vorwissen.csv --gruppen "keine:🪶,F:🪶/◼,G:◼,H:◼◼" --anonym`
- Verlauf über alle Tickets: `/lernverlauf <klasse>`; Förderung je Kürzel: `lernfortschritt-analyst`.
