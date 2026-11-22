# Vorlage für eine Aufgabenpool-Datei (verbindliches Format)

Jede Datei behandelt **eine Kompetenz** in **5 Stufen × 3 Karten = 15 Karten**.

| Stufe (RLP) | Symbol | Bedeutung für die Schüler:innen |
|---|---|---|
| B | 🌰 | „Samen“ – Fundament (Grundschul-Niveau, für alle, die noch nicht sicher in C sind) |
| C | 🌱 | Keimling |
| D | 🌿 | Zweig |
| E | 🌳 | Baum |
| F | ⭐ | Stern – Profi-Herausforderung |

Karten-ID: `<CODE>-<Stufe><Nr>`, z. B. `VO-D2`. Die Codes stehen in `index.csv`.

## Aufbau der Datei

```
# Aufgabenpool <CODE>: <Kompetenz>

## Teil A – Für die Lehrkraft (nicht austeilen)
- Tabelle: Stufe | Symbol | „Ich kann …“ (schülernah) | typische Fehlerbilder (Kürzel aus 02-diagnose.md) | passt zu Material (M-Nr. der Einheit)
- 3–5 Sätze: Einsatz (Förderung nach Auswertung, Wiederholung, Drehtür, Vertretung), Hinweis „Karte der Stufe des nächsten Ziels wählen; wer 2 von 3 Karten einer Stufe sicher löst, geht eine Stufe höher“.

## Teil B – Aufgabenkarten (Kopiervorlagen, A6)
> ✂ ---------- <ID> <Symbol> ----------
### <ID> <Symbol> <kurzer Titel>
<Aufgabe: max. ca. 12 Zeilen, Operatoren fett, kurze Sätze, Platz zum Schreiben mit ______>
💡 Hilfe: <eine Zeile, Verweis auf Hilfekarte H-xx oder Werkzeugblatt M0.4>
(… 15 Karten in der Reihenfolge B1, B2, B3, C1 … F3)

## Teil C – Lösungen / Kontrollblatt (nicht mit austeilen)
| Karte | Lösung | häufiger Fehler → Fehlerbild |
```

## Regeln
- **Druckfertig:** KEINE Platzhalter wie „[Bild: …]“. Zeichnungen als Text-Grafik in Code-Blöcken (```), z. B. Streifen `▮▮▮▯`, Raster, Zahlenstrahl mit `|----|`. Max. 60 Zeichen breit.
- **Gleicher Kern, steigende Anforderung:** Stufe B anschaulich/mit Geld/Bildern, C einfache Zahlen, D Standardverfahren, E Verständnis/Mehrschritt/Begründen, F offen/verallgemeinern/beweisen. Innerhalb einer Stufe: Karte 1 leichter Einstieg, Karte 3 etwas anspruchsvoller.
- **Kontexte:** gern Alltag/Berlin/Späti, aber jede Karte muss ohne die Späti-Geschichte verständlich sein.
- **Keine Dopplung** mit Eingangstest, Exit-Tickets (02-diagnose.md) und Klassenarbeit (bewertung/klassenarbeit.md) – andere Zahlen verwenden.
- **Selbstkontrolle möglich:** eindeutige Lösungen oder klare Kriterien bei offenen Aufgaben.
- **Sprachsensibel:** Operatoren fett, Satzanfänge bei Begründungen („Ich weiß das, weil …“).
- Alle Lösungen **zweimal nachrechnen**.
