---
description: Plant eine komplette differenzierte Unterrichtseinheit mit dem gesamten Agenten-Team (Lehrplan → Diagnose → Kreativ-Ideen → Struktur → Material → Inklusion → Bewertung → Qualitätsprüfung)
argument-hint: <Fach> <Jahrgang> <Schulform> <Thema> [Stundenzahl] [Klassenprofil-Datei]
---

Plane eine differenzierte Unterrichtseinheit für: **$ARGUMENTS**

Fehlen Fach, Jahrgang, Schulform (Grundschule / ISS / Gymnasium / Gemeinschaftsschule) oder Thema, frage einmal kurz nach. Sonst lege los mit sinnvollen Annahmen (Standard: 6 Stunden à 45 Min., 3 Niveaugruppen) und nenne diese Annahmen.

Lege den Ordner `unterricht/<fach>-<thema>/` an (Kleinbuchstaben, Bindestriche) und führe das Team in dieser Reihenfolge aus. Gib jedem Agenten die relevanten Ergebnisse der vorherigen Schritte mit und speichere jedes Ergebnis als Datei:

0. Lies `wissen/erkenntnisse.md` und gib relevante Erkenntnisse an alle folgenden Agenten weiter.
1. **lehrplan-analyst** → `01-lehrplanbezug.md`
2. Parallel:
   - **lernstand-diagnostiker** → `02-diagnose.md` (Eingangsdiagnose; falls ein Klassenprofil in `klassen/` angegeben ist, auch Gruppenvorschlag)
   - **kreativ-impulsgeber** → `03-kreative-ideen.md`
3. **differenzierungs-architekt** (mit 01–03) → `04-verlaufsplanung.md`
4. **material-ersteller** (mit 04) → `material/`
5. Parallel:
   - **inklusion-sprachfoerderung** → prüft und ergänzt `material/`, Notizen in `05-inklusion.md`
   - **bewertungs-feedback-coach** → `bewertung/`
   - Zu allen Tests/Exit-Tickets/Klassenarbeiten Schlüsseldateien in `auswertung/` anlegen (für `/auswerten`).
6. **qualitaets-pruefer** → `06-qualitaetspruefung.md`
7. Arbeite die 🔴/🟡-Punkte der Qualitätsprüfung selbst ein (oder mit dem jeweiligen Agenten).

Schreibe zum Schluss `README.md` im Einheitsordner: Kurzüberblick, Stundenübersicht, Materialliste, Vorbereitungs-Checkliste für die Lehrkraft. Fasse im Chat in wenigen Sätzen zusammen, was entstanden ist und welche Punkte die Lehrkraft selbst prüfen sollte (v. a. nicht verifizierte RLP-Zitate).
