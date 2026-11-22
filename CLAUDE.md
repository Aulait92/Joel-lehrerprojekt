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

## Befehle
- `/unterrichtsplanung <Fach> <Jg> <Schulform> <Thema>` – komplette Einheit mit allen Agenten
- `/differenziere-material <Datei|Text>` – vorhandenes Material in drei Niveaus umbauen
- `/klasse-analysieren <klassen/datei.md>` – Klassenprofil auswerten

## Regeln für alle Agenten
- **Sprache**: Deutsch, geschlechtergerecht (Doppelpunkt), schülernah in Materialien.
- **Datenschutz**: Nur Pseudonyme (S01 …). `klassen/` wird nicht committet.
- **Keine erfundenen RLP-Standards** – Quellen angeben, Unsicheres kennzeichnen.
- **Differenzierung ohne Stigmatisierung**: Symbole statt Leistungslabels, Gruppen flexibel.
- **Realismus**: 25–30 Schüler:innen, 45-Min.-Stunden, begrenzte Vorbereitungszeit.
- Ergebnisse unter `unterricht/<fach>-<thema>/` ablegen.
