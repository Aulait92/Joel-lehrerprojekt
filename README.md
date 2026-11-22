# Agenten-Team für differenzierten Unterricht 🍎

Ein Team aus 8 spezialisierten KI-Agenten für **Claude Code**. Es plant auf Basis des
**Rahmenlehrplans Berlin-Brandenburg** Unterricht für Klassen mit sehr unterschiedlichen Lernniveaus.

## Warum das gut zum Berliner RLP passt
Der RLP 1–10 beschreibt Kompetenzen in **Niveaustufen A–H** statt starr pro Jahrgang.
Eine 7. Klasse kann also am selben Thema auf Stufe C, D und E arbeiten – genau dafür baut das Team die Lernwege.

## So arbeitet das Team

```
           ┌──────────────────────┐
           │  lehrplan-analyst    │  Welche Standards & Niveaustufen?
           └──────────┬───────────┘
          ┌───────────┴────────────┐
┌─────────▼──────────┐  ┌──────────▼─────────┐
│lernstand-diagnostik│  │ kreativ-impulsgeber│  Wo stehen die Kinder? / Was motiviert?
└─────────┬──────────┘  └──────────┬─────────┘
          └───────────┬────────────┘
           ┌──────────▼───────────┐
           │differenzierungs-     │  Stundenverlauf, Lernwege 🌱🌿🌳
           │architekt             │
           └──────────┬───────────┘
           ┌──────────▼───────────┐
           │  material-ersteller  │  Arbeitsblätter, Hilfekarten, Lösungen
           └──────────┬───────────┘
          ┌───────────┴────────────┐
┌─────────▼──────────┐  ┌──────────▼─────────┐
│inklusion-sprach-   │  │bewertungs-feedback-│  DaZ/Förderbedarf / faire Bewertung
│foerderung          │  │coach               │
└─────────┬──────────┘  └──────────┬─────────┘
          └───────────┬────────────┘
           ┌──────────▼───────────┐
           │  qualitaets-pruefer  │  Ampel-Check vor dem Einsatz
           └──────────────────────┘
```

## Schnellstart
1. Dieses Repository in Claude Code öffnen (Terminal, Desktop-App oder claude.ai/code).
2. Optional: RLP-Fachteil als PDF in `lehrplan/` legen (für exakte Zitate).
3. Optional: Klassenprofil aus `vorlagen/klassenprofil.md` nach `klassen/` kopieren und **pseudonymisiert** ausfüllen.
4. Befehl eingeben, z. B.:

```
/unterrichtsplanung Mathematik 7 ISS "Brüche und Dezimalzahlen" 8 Stunden klassen/7b.md
/unterrichtsplanung Deutsch 4 Grundschule "Sachtexte verstehen"
/differenziere-material unterricht/mein-arbeitsblatt.md Biologie 8
/klasse-analysieren klassen/7b.md
```

Du kannst Agenten auch einzeln ansprechen:
> „Lass den kreativ-impulsgeber 5 Ideen für das Thema Photosynthese in Klasse 8 sammeln.“

## Ergebnis einer Planung
```
unterricht/mathematik-brueche/
├── README.md                  ← Überblick + Vorbereitungs-Checkliste
├── 01-lehrplanbezug.md
├── 02-diagnose.md
├── 03-kreative-ideen.md
├── 04-verlaufsplanung.md
├── 05-inklusion.md
├── 06-qualitaetspruefung.md
├── material/                  ← druckfertige Arbeitsblätter 🌱🌿🌳 + Lösungen
└── bewertung/                 ← Kompetenzraster, Test, Feedbackbögen
```

## Wichtige Hinweise
- **Datenschutz**: Niemals Klarnamen oder sensible Schülerdaten eingeben. `klassen/` ist per `.gitignore` vom Upload ausgeschlossen.
- **Fachliche Verantwortung** bleibt bei dir: Prüfe RLP-Zitate (die Agenten kennzeichnen Unsicheres) und passe das Material an deine Klasse an.
- **Anpassen**: Jeder Agent ist eine einfache Markdown-Datei in `.claude/agents/` und kann frei bearbeitet werden, z. B. für schulinterne Curricula oder bevorzugte Methoden.
