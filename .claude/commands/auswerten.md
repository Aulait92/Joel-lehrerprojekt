---
description: Wertet einen Test / ein Exit-Ticket / eine Klassenarbeit aus und leitet Förderung, Gruppenwechsel und Unterrichtsverbesserungen ab
argument-hint: <klasse> <test> [einheit] [Pfad zur CSV oder eingefügte Ergebnisse]
---

Werte aus: **$ARGUMENTS**

1. **Daten klären:** Liegt die Ergebnis-CSV in `klassen/<klasse>/`? Wenn nicht, hilf beim Erfassen (Vorlage aus `unterricht/<einheit>/auswertung/<test>.vorlage.csv` nach `klassen/<klasse>/<datum>_<test>.csv` kopieren oder eingefügte Daten umwandeln). Prüfe auf Klarnamen – ggf. stoppen. Trage den Test in `klassen/<klasse>/tests.csv` ein.
2. **lernfortschritt-analyst**: Skript `tools/lernauswertung.py test` (und `verlauf`, wenn ≥ 2 Tests im Index) laufen lassen und die Analyse schreiben.
3. Falls die Analyse einen Förderpaket-Auftrag enthält: **material-ersteller** erstellt die Pakete in `unterricht/<einheit>/material/foerderung/` (ohne Kürzel, nach Fehlerbild benannt).
4. **unterrichts-optimierer** mit dem *anonymen* Klassenbefund: Wirkung früherer Änderungen prüfen, max. 3 Verbesserungen umsetzen, Wiederholungsplan, `wissen/erkenntnisse.md` pflegen.
5. Fasse im Chat zusammen: Kernaussagen, was in der **nächsten Stunde** zu tun ist (Plenum-Impuls, Kleingruppen, Gruppenwechsel), welche Materialien geändert wurden.
