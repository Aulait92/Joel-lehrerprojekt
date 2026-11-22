---
description: Zeigt die Lernentwicklung einer Klasse über alle erfassten Tests und plant Förderung und Wiederholung
argument-hint: <klasse>
---

Lernverlauf für Klasse **$ARGUMENTS**:

1. **lernfortschritt-analyst**: `python3 tools/lernauswertung.py verlauf --index klassen/<klasse>/tests.csv --out klassen/<klasse>/auswertungen/verlauf.md`, dann interpretieren: Wer holt auf (was hat geholfen?), wer fällt zurück (Ursachen prüfen, nicht vorschnell urteilen), hartnäckige Fehlerbilder, Entwicklung der Schere. Ergebnis: `klassen/<klasse>/auswertungen/verlauf-analyse.md` mit Maßnahmen je Kürzel.
2. **unterrichts-optimierer**: aus dem anonymen Befund einen **Wiederholungsplan** für die nächsten 4 Wochen (verteilte 5-Min.-Einstiege zu den hartnäckigen Fehlerbildern) und Erkenntnisse für `wissen/erkenntnisse.md`.
3. Kurzfazit im Chat: 3 wichtigste Beobachtungen, 3 Maßnahmen.
