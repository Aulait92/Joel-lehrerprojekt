# 06a – Rechenprüfung Trigonometrie (Kl. 10)

> Geprüft am 22.11.2026 mit `python3` (math-Modul, Grad → `math.radians`). Es wurden **keine** Dateien in `unterricht/` geändert. Die Korrekturvorschläge unten setzt ein anderer Agent bzw. die Lehrkraft um. Danach die PDFs neu erzeugen: `python3 tools/pdf_erstellen.py unterricht/mathematik-trigonometrie`.

## Zusammenfassung

| Bereich | geprüft | Ergebnis |
|---|---|---|
| 1. Lösungsblätter M1.4, M2.5, M3.5, M3.7, M4.5, M5.2/M5.8, M6.6, M7.5, M8.5 inkl. Abgleich mit Arbeitsblättern, Stationen, Gutachten, Folien und Hilfekarten | ca. 520 Einzelrechnungen (Ergebnisse, Zwischenwerte, Fehler-/Ablenkerwerte, TR-RAD/GRAD-Werte) | alle Aufgabenangaben stimmen mit den Lösungsblättern überein; 1 Fehler (M5.1), 3 Hinweise |
| 2. ```dreieck-Blöcke (alle 121 Blöcke der Einheit, automatisch) | 121 Blöcke: Winkelbeschriftung ↔ winkel_A/winkel_B/γ, rechter Winkel, alle Seitenpaare über den Sinussatz (Toleranz 3 %) | **keine Abweichung**. Größte Seitenabweichung < 1 % (Entdeckerkarten M5.2 max. 0,56 %) |
| 3. Lösungscodes | 19 Codewörter (KALI, BRIE, RUNG, WASSER, DREHLEITER, MARSCH, LOT, 3 × HOEHE, 3 × PEILUNG, 3 × TURM, KRAN, RADIO, MASTEN) und alle Lockbuchstaben | alle Codewörter ergeben sich korrekt; Lockbuchstaben stimmen mit den Fehlerrechnungen überein. **3 Kollisionen** (Std. 4): richtig berechnete, auf dem Blatt verlangte Zwischenergebnisse führen auf Lockbuchstaben |
| 4. 02-diagnose.md (Vorwissens-Check, ET1–ET8), klassenarbeit.md, auswertung/*.schluessel.csv | ca. 110 Rechnungen, Notenschlüssel (10 Grenzen), Punktsummen (Pflicht 18, Blöcke 6/8/10, F/G-Aufteilung 10/8), 10 Schlüsseldateien | alles korrekt; max_punkte-Summen passen exakt zur Klassenarbeit |
| 5. Querbezug Beispieldaten Std. 3–5 (e = 15,0 m, α₁ = 38°, 1,55 m, d = 10 m, α₂ = 25,1°) | alle Fundstellen (M3.1, M3.5, M3.7, M4.1, M4.3, M4.4, M4.5, M5.1, M5.5, M5.8, 04, _anleitung) | direkt **13,269 m → 13,27 m ≈ 13,3 m** ✓, Zerlegung/Sinussatz **13,248 m → 13,25 m ≈ 13,2 m** ✓ überall – **außer M5.1** (dort 13,3 m für Zerlegung/Sinussatz) |

**Summe:** ca. 650 Einzelrechnungen + 121 Dreiecks-Blöcke + 19 Codewörter. **1 Fehler**, **3 Code-Kollisionen**, **4 Hinweise**.

Kontrollwerte Beispieldaten (Python): tan 38° = 0,7812856 · x = 11,71928 m · h = 13,26928 m · exakt passendes α₂ = 25,1158° · von S₂: 13,26086 m · S₁L = 4,241994 m · δ = 12,9° · S₁D = 19,001084 m · x (Zerlegung) = 11,698235 m · h = 13,248235 m · e₁ = 14,97306 m · Formel d·sin α₁·sin α₂/sin(α₁−α₂) = 11,698235 m ✓.

## Befunde

| Datei | Stelle (Aufgabe/Abschnitt) | angegeben | korrekt | Art | Korrekturvorschlag (exakter Ersatztext) |
|---|---|---|---|---|---|
| material/M5.1-folien-std5.md | Z. 132, Folie Vergleich | „Std. 4 (Zerlegung): 13,3 m · heute: 13,3 m ✓“ | Zerlegung und Sinussatz: 11,698 + 1,55 = 13,248 m ≈ **13,2 m** (so in M4.1 Z. 166, M4.5, M3.5) | **Fehler** (widerspricht M4.1/M4.5) | `Vergleich: Std. 3 (mit e = 15,0 m): 13,3 m (13,27 m) · Std. 4 (Zerlegung): 13,2 m (13,25 m) · heute: 13,2 m (13,25 m) ✓ – der Unterschied kommt nur vom Runden von α₂.` |
| material/M5.1-folien-std5.md | Z. 130, Folie Rückbezug | „h = 19,0 · sin(38°) + 1,55 ≈ 11,7 + 1,55 ≈ **13,3 m**“ | 19,001 · sin 38° = 11,698 → h = 13,248 m ≈ 13,2 m (auch mit 19,0: 13,2476 m) | **Fehler** (doppelte Rundung 11,7 + 1,55 = 13,25 → 13,3) | `h = 19,0 · sin(38°) + 1,55 ≈ 11,70 + 1,55 ≈ **13,25 m ≈ 13,2 m**` |
| material/M5.1-folien-std5.md | Z. 37, Folie Rückblick Std. 4 | „h′ … ≈ 11,7 m → Dachhöhe ≈ 13,3 m“ | 13,248 m ≈ 13,2 m | **Fehler** (gleiche Ursache) | `4. h′ = S₁D · sin(38°) ≈ 11,70 m → Dachhöhe ≈ 13,2 m (13,25 m)` |
| material/M5.1-folien-std5.md | Z. 7, Teil A | „h ≈ 13,25 m ≈ 13,3 m“ | 13,248 m ≈ 13,2 m | **Fehler** (gleiche Ursache) | `Ergebnis: S₁D ≈ 19,0 m, h′ ≈ 11,70 m, h ≈ 13,25 m ≈ 13,2 m (wer 11,7 + 1,55 rechnet, schreibt 13,3 m – beides gelten lassen, vgl. M5.5).` |
| material/M4.2-ab4-feder.md | Z. 150–154, Freigabe-Code | Tabelle ohne Zuordnung „welche Aufgabe“; A1–A3 verlangen ausdrücklich „berechne h“ | Richtige h-Werte 4,6 (A1) / 6,1 (A2) / 5,7 (A3) sind in M4.5 als Lockbuchstaben A / L / I angelegt; h aus A4 (4,3) ist dagegen Code-Buchstabe H | **Code** (Kollision richtig ↔ Lockbuchstabe) | Unter die Code-Tabelle einfügen: `\| Aufgabe \| 1: a \| 2: b \| 3: b \| 4: h \| 4: s \|` / `\|---\|---\|---\|---\|---\|---\|` / `\| Buchstabe \| \| \| \| \| \| \|` und Z. 150 ersetzen durch: `**Freigabe-Code:** Runde auf eine Nachkommastelle. Trage nur die Ergebnisse aus der Zeile „Aufgabe“ ein.` |
| material/M4.3-ab4-gewicht.md | Z. 120, Freigabe-Code | A4 verlangt „Berechne … s und die Höhe des Firsts“ | richtige Firsthöhe 6,354 m ≈ 6,4 m = Lockbuchstabe **M** (M4.5: „Firsthöhe statt s eingetragen“) | **Code** (Kollision) | Unter die Code-Tabelle einfügen: `\| Aufgabe \| 1: a \| 1: c \| 2: a \| 3: Zaun \| 4: s \|` / `\|---\|---\|---\|---\|---\|---\|` / `\| Buchstabe \| \| \| \| \| \| \|` |
| material/M4.4-ab4-doppelgewicht.md | Z. 90, Freigabe-Code | A1a verlangt „Berechne x und die Dachhöhe“ | richtige Dachhöhe 13,248 m ≈ 13,2 m = Lockbuchstabe **T** (M4.5: „Dachhöhe statt x eingetragen“) | **Code** (Kollision) | Unter die Code-Tabelle einfügen: `\| Aufgabe \| 1a: S₁L \| 1a: S₁D \| 1a: x \| 2: b \| 2: α \|` / `\|---\|---\|---\|---\|---\|---\|` / `\| Buchstabe \| \| \| \| \| \| \|` |
| material/M3.5-loesung-erwartung-std3.md | Z. 96–97, Forschungsfrage | 10 m: „±0,41 m“ · 11,7 m: „±0,41 m (kleinster Wert)“ | 10 m: ±0,414 m · 11,7 m: ±0,409 m (Minimum stimmt, ist aber bei 2 Stellen nicht sichtbar) | Hinweis | Z. 96: `\| 10 m \| 49,5° \| ±0,414 m \|` · Z. 97: `\| **11,7 m** \| **45°** \| **±0,409 m (kleinster Wert)** \|` |
| material/M4.6-hilfekarten-std4.md | Z. 11, Teil A „Zahlen“ | „α = 40°, β = 65°, b = 7,0 cm bzw. 30°/45°/15 m“ | Die Karten rechnen mit b = 7,5 cm, α = 44°, β = 58° (→ a ≈ 6,1 cm ✓) und d = 12,0 m, 42°/28° (→ 17,2 m ✓). Die genannten Werte sind die von ET4 – genau die sollten vermieden werden | Hinweis (Rechnungen auf den Karten richtig) | `\| **Zahlen** \| Parallelbeispiele mit **anderen** Werten als AB4 und ET4 (b = 7,5 cm, α = 44°, β = 58° bzw. d = 12,0 m, 42°/28°, Augenhöhe 1,60 m) \|` |
| material/M3.7-plan-b-regen.md | Z. 151, Trupp 4 | tan 27,8° = 0,5272403 | 0,5272402 (0,52724019) | Hinweis (Ergebnis 13,30 m unverändert) | `22 · 0,5272402 + 1,70 = 13,30 m` |
| material/M5.5-ab5-doppelgewicht.md / M5.8 | Teil A Z. 8 bzw. Teil D 2d | „13,2 m oder 13,3 m – beides richtig“ | 13,248 m ergibt korrekt gerundet 13,2 m; 13,3 m entsteht nur über 11,7 + 1,55 = 13,25 | Hinweis (Code L für beide Werte → kein Codeproblem) | keine Änderung nötig; ggf. ergänzen: `(korrekt gerundet 13,2 m; 13,3 m entsteht durch Runden des Zwischenergebnisses)` |

## Ohne Befund geprüft (Auswahl)

- **M1.4** (🪶/◼/◼◼ + Merkblatt): alle Werte inkl. Ablenker (z. B. 8,6 · cos(34 rad) = −7,30; 9,4 · sin(52 rad) = 9,27; sin(30 rad) = −0,988; sin(30 gon) = 0,454) ✓; Pythagoras-Kontrollen 4,8/5,5/7,3 und 6,5/7,2/9,7 exakt ✓.
- **M2.5**: alle drei Blätter, MWB-Items, Fehler-Detektiv (12 · sin(70 rad) = 9,29; 8 · sin 65° = 7,25) ✓; Steigung 12 %: 297,9 m bzw. 296,0 m ✓.
- **M3.5/M3.7**: Fehlertabelle ±1° (12,85 / 13,27 / 13,70 m), Fehlerbilder (20,7 / 6,2 / 10,8 / 13,4 / 13,6 / 13,7 m), Empfindlichkeit Zwei-Standpunkte (12,0 / 14,7 / 13,9 / 12,7 m), Plan-B-Mittelwerte aller 7 Trupps, Median 13,29 m, Mittelwert 13,30 m bzw. 13,86 m mit Ausreißer, Wartezeit-Code LOT ✓. M3.8 (13,8 m; 17,2 m) ✓.
- **M4.5** inkl. Sinussatz-Kontrollen, Fläche 431 m², Lot außerhalb (b = 9,443 cm, α = 27,9°) ✓.
- **M5.2/M5.8**: alle 30 Quotienten der 10 Entdeckerkarten (Winkelsumme jeweils 180°, Abweichung ≤ 0,56 %, Rundung auf 0,1 identisch), alle drei AB5-Lösungen ✓.
- **M6.6/M6.5**: alle 12 Stationen inkl. SSW (β₁ = 68,27°, AB₁ = 6,76 m, AB₂ = 2,61 m) und Laufkarten-Tabelle ✓.
- **M7.5** und Folien/Hilfekarten Std. 7 (4,71 km; 4,6 cm; 5,9 cm; 8,7 cm) ✓; Winkel aus SSS 100,1° / 46,3° / 33,6° ✓.
- **M8.5**: Turm 26,59 m (alle drei Wege), Brücke 54,20 m (Pythagoras 54,24 m; Sinussatz 54,20 m; Kosinussatz 54,20 m), Kanalbreite 51,5–51,6 m, Fehlerabschätzung 23,5 / 30,3 / 25,6 / 27,6 m ✓.
- **02-diagnose.md**: Vorwissen (8,1 / 9 / 6,0 / 21,1; RAD −0,99/−0,30; GRAD 0,45/0,81), ET1–ET8 alle Niveaus inkl. Fehlerwerte ✓.
- **klassenarbeit.md**: alle Lösungen (z. B. 6,0 / 9,1 / 26,9° / 9,0 cm; Block A 14,7 / 25,7 / 20,7° / 17,7 / 15,6 m; Block B 5,7 / 7,8 / 165 / 143,9 m, SSW 51,6°/128,4°, b₁ = 89,3 m, b₂ = 21,0 m; Block C 6,7 / 33,9 / 96,9 m, 94,9° / 38,0° / 47,1°, 10,5 m²), Notenschlüssel beider Modelle, Punktsummen ✓.
