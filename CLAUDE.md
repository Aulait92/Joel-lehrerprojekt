# Lehrerprojekt – differenzierte Unterrichtsplanung (Berlin)

Dieses Projekt unterstützt eine Lehrkraft in Berlin bei der Planung von Unterricht für
**heterogene Lerngruppen** auf Basis des **Rahmenlehrplans Berlin-Brandenburg (RLP 1–10, Niveaustufen A–H)**.

## Agenten-Team (`.claude/agents/`)
| Agent | Rolle |
|---|---|
| `lehrplan-analyst` | RLP-Standards, Niveaustufen, Teil A/B/C – immer zuerst |
| `lernstand-diagnostiker` | Eingangsdiagnosen, Auswertung, flexible Lerngruppen |
| `kreativ-impulsgeber` | Lebensweltbezug Berlin, Gamification, Projekte, Lernorte |
| `differenzierungs-architekt` | Stundenverlauf und Lernwege auf mehreren Niveaus |
| `material-ersteller` | druckfertige Arbeitsblätter 🌱/🌿/🌳, Hilfekarten, Lösungen |
| `inklusion-sprachfoerderung` | DaZ, Förderbedarf, LRS, Hochbegabung |
| `bewertungs-feedback-coach` | Kompetenzraster, differenzierte Tests, Feedback |
| `qualitaets-pruefer` | kritische Endkontrolle – immer zuletzt |
| `lernfortschritt-analyst` | wertet Tests/Klassenarbeiten aus, nächste Schritte je Kürzel |
| `unterrichts-optimierer` | setzt Befunde in Unterricht um, prüft Wirkung, pflegt `wissen/` |
| `schueler-tester` | prüft jedes Blatt aus Schülersicht: ohne Nachfragen ausfüllbar? bessert nach |

## Befehle
- `/unterrichtsplanung <Fach> <Jg> <Schulform> <Thema>` – komplette Einheit mit allen Agenten
- `/differenziere-material <Datei|Text>` – vorhandenes Material in drei Niveaus umbauen
- `/klasse-analysieren <klassen/datei.md>` – Klassenprofil auswerten
- `/auswerten <klasse> <test> [einheit]` – Test/Klassenarbeit auswerten → Förderung + Verbesserung
- `/lernverlauf <klasse>` – Entwicklung über alle Tests, Wiederholungsplan

## Verbesserungskreislauf
Planen → Unterrichten → Ergebnisse erfassen (`klassen/<klasse>/*.csv`) → `tools/lernauswertung.py` →
`lernfortschritt-analyst` (Förderung je Kürzel) → `unterrichts-optimierer` (Material ändern, Wirkung prüfen,
`wissen/erkenntnisse.md`) → nächste Planung liest den Erfahrungsspeicher.

## Regeln für alle Agenten
- **Sprache**: Deutsch, geschlechtergerecht (Doppelpunkt), schülernah in Materialien.
- **Datenschutz**: Nur Pseudonyme (S01 …). `klassen/` wird nicht committet. In `unterricht/` und `wissen/` nur anonyme Klassenbefunde.
- **Auswertung**: Zahlen immer mit `tools/lernauswertung.py` berechnen, nicht schätzen. Kein Urteil über ein Kind aus einem einzelnen Test.
- **Keine erfundenen RLP-Standards** – Quellen angeben, Unsicheres kennzeichnen.
- **Differenzierung ohne Stigmatisierung**: Symbole statt Leistungslabels, Gruppen flexibel.
- **Realismus**: 25–30 Schüler:innen, begrenzte Vorbereitungszeit. **Stundenlänge und Niveausymbole stehen im Auftrag der Einheit** (`00-auftrag.md`, z. B. 60 Min. und 🪶/◼/◼◼) – sonst 45 Min. und 🌱/🌿/🌳.
- **Vorgaben der Lehrkraft** (`00-auftrag.md`, `vorhandenes-material/`) haben Vorrang vor den Standardannahmen der Agenten.
- **Geometrie-Skizzen**: Dreiecke als ` ```dreieck `-Block (siehe `tools/dreieck_svg.py`), andere Skizzen als Inline-SVG – keine Bild-Platzhalter.
- Ergebnisse unter `unterricht/<fach>-<thema>/` ablegen.
- Nach Änderungen an Materialien die Ausgaben neu erzeugen:
  - `python3 tools/pdf_erstellen.py unterricht/<einheit>` – PDFs (klassisch) inkl. Sammel-PDFs
  - `python3 tools/lernpfad_design.py unterricht/<einheit>` – PDFs im Lernpfad-Design + Lernpass
  - `python3 tools/docx_erstellen.py unterricht/<einheit>` – Word-Dateien
  - `python3 tools/praesentation_erstellen.py unterricht/<einheit>` – PowerPoint (klassisch + Lernpfad) aus `M*.1-folien-*.md`
  - Einmalig für PowerPoint: `cd tools && npm install`
