#!/usr/bin/env python3
"""
Baut PowerPoint-Präsentationen aus den Folientexten einer Einheit (material/M*.1-folien-*.md).

    python3 tools/praesentation_erstellen.py unterricht/mathematik-trigonometrie

Ergebnis in <einheit>/praesentationen/:
  klassisch/Std-1-….pptx   Design wie die Tafel der Lehrkraft (Karopapier, zentrierte Titel, Klebeband)
  lernpfad/Std-1-….pptx    neues, spielerisches Design (Lernpfad, XP, Level-Chips, Maskottchen „Theo“)

Folientext-Format: "### Folie n – Titel  ⏱ X Minuten", danach Inhalt (Absätze, Listen, Tabellen,
```dreieck-Blöcke, Inline-SVG), "*Moderation:* …" wird zur Sprechernotiz.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docx_erstellen as D  # noqa: E402  (SVG → PNG über Chromium)
from dreieck_svg import dreieck_svg  # noqa: E402

FOLIE = re.compile(r"^###\s+Folie\s+(\d+)\s*[–-]\s*(.*?)\s*$")
ZEIT = re.compile(r"⏱\s*([^|]*?)\s*$")


def inline_runs(text: str) -> list[dict]:
    """**fett**, *kursiv*, `code` → Liste von {text, bold, italic}."""
    runs = []
    for teil in re.split(r"(\*\*[^*]+\*\*|(?<!\*)\*[^*\s][^*]*\*(?!\*)|`[^`]+`)", text):
        if not teil:
            continue
        if teil.startswith("**"):
            runs.append({"text": teil[2:-2], "bold": True})
        elif teil.startswith("`"):
            runs.append({"text": teil[1:-1], "code": True})
        elif teil.startswith("*") and teil.endswith("*") and len(teil) > 2:
            runs.append({"text": teil[1:-1], "italic": True})
        else:
            runs.append({"text": teil})
    for r in runs:
        r["text"] = re.sub(r"<br\s*/?>", " · ", r["text"])
        r["text"] = re.sub(r"<[^>]+>", "", r["text"])
    return runs


def bild_aus_svg(svg: str, ordner: Path) -> dict:
    D.TMP = ordner
    name = "svg_" + __import__("hashlib").md5(svg.encode()).hexdigest()[:12] + ".png"
    D.SVG_AUFTRAEGE[name] = svg
    w = re.search(r'width="([\d.]+)', svg)
    h = re.search(r'height="([\d.]+)', svg)
    return {"typ": "bild", "pfad": str(ordner / name),
            "w": float(w.group(1)) if w else 300, "h": float(h.group(1)) if h else 200}


def parse_folien(md: str, bildordner: Path) -> list[dict]:
    folien, akt, modus, puffer, notiz_modus = [], None, None, [], False
    zeilen = md.splitlines()
    i = 0
    while i < len(zeilen):
        z = zeilen[i]
        m = FOLIE.match(z)
        if m:
            titel = m.group(2)
            zeit = ""
            zm = ZEIT.search(titel)
            if zm:
                zeit = zm.group(1).replace("Minuten", "Min.").replace("Minute", "Min.").strip()
                titel = titel[:zm.start()].strip()
            akt = {"nr": int(m.group(1)), "titel": titel, "zeit": zeit, "inhalt": [], "notizen": []}
            folien.append(akt)
            notiz_modus = False
            i += 1
            continue
        if akt is None or z.startswith("## ") or z.startswith("# "):
            if z.startswith("## ") and akt is not None:
                akt = None
            i += 1
            continue
        if z.startswith("### "):  # andere Zwischenüberschrift innerhalb einer Folie
            akt["inhalt"].append({"typ": "absatz", "runs": [{"text": z[4:].strip(), "bold": True}]})
            i += 1
            continue
        # Codeblöcke
        if z.lstrip().startswith("```"):
            art = z.strip()[3:].strip()
            block = []
            i += 1
            while i < len(zeilen) and not zeilen[i].lstrip().startswith("```"):
                block.append(zeilen[i])
                i += 1
            i += 1
            if art == "dreieck":
                akt["inhalt"].append(bild_aus_svg(dreieck_svg("\n".join(block)), bildordner))
            else:
                akt["inhalt"].append({"typ": "code", "text": "\n".join(block)})
            continue
        # Inline-SVG
        if "<svg" in z:
            block = [z]
            while "</svg>" not in block[-1] and i + 1 < len(zeilen):
                i += 1
                block.append(zeilen[i])
            i += 1
            akt["inhalt"].append(bild_aus_svg("\n".join(block), bildordner))
            continue
        # Moderation → Notizen
        if re.match(r"^\*Moderation:?\*:?", z.strip()) or z.strip().startswith("*Moderation"):
            notiz_modus = True
            akt["notizen"].append(re.sub(r"^\*Moderation:?\*:?\s*", "", z.strip()))
            i += 1
            continue
        if notiz_modus and z.strip():
            akt["notizen"].append(z.strip())
            i += 1
            continue
        notiz_modus = False if not z.strip() else notiz_modus
        # Tabellen
        if z.strip().startswith("|"):
            zeilen_tab = []
            while i < len(zeilen) and zeilen[i].strip().startswith("|"):
                zelle = [c.strip() for c in zeilen[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in zelle if c):
                    zeilen_tab.append([inline_runs(c) for c in zelle])
                i += 1
            akt["inhalt"].append({"typ": "tabelle", "zeilen": zeilen_tab})
            continue
        s = z.strip()
        if not s or s in ("---",) or s.startswith("<div") or s.startswith("</div") or s.startswith(":::"):
            i += 1
            continue
        lm = re.match(r"^(?:[-*•]|\d+[.)])\s+(.*)", s)
        einzug = len(z) - len(z.lstrip(" "))
        vorher = akt["inhalt"][-1] if akt["inhalt"] else None
        vorige_leer = i > 0 and not zeilen[i - 1].strip()
        if lm:
            akt["inhalt"].append({"typ": "punkt", "nummer": bool(re.match(r"^\d", s)), "ebene": 1 if einzug >= 2 else 0,
                                  "runs": inline_runs(lm.group(1))})
        elif vorher and vorher.get("runs") is not None and not vorige_leer and (einzug >= 2 or vorher["typ"] == "punkt"):
            vorher["runs"] += [{"text": " "}] + inline_runs(s)
        else:
            akt["inhalt"].append({"typ": "absatz", "runs": inline_runs(s.lstrip("> ").strip())})
        i += 1
    return folien


def grafiken(ordner: Path):
    """Karopapier-Hintergrund und Klebeband-Streifen für das klassische Design."""
    from PIL import Image, ImageDraw
    bg = ordner / "karopapier.png"
    if not bg.exists():
        w, h = 2000, 1250
        img = Image.new("RGB", (w, h), (249, 248, 238))
        d = ImageDraw.Draw(img)
        schritt = 34
        for x in range(0, w, schritt):
            d.line([(x, 0), (x, h)], fill=(214, 214, 205), width=2)
        for y in range(0, h, schritt):
            d.line([(0, y), (w, y)], fill=(214, 214, 205), width=2)
        img.save(bg)
    band = ordner / "klebeband.png"
    if not band.exists():
        w, h = 900, 110
        img = Image.new("RGB", (w, h), (31, 91, 79))
        d = ImageDraw.Draw(img)
        import math
        for i, x in enumerate(range(20, w, 46)):
            for j, y in enumerate((28, 80)):
                cx, cy, r = x + (23 if j else 0), y, 11
                farbe = (255, 255, 255) if (i + j) % 2 else (190, 214, 120)
                pts = []
                for k in range(10):
                    ang = math.pi / 2 + k * math.pi / 5
                    rr = r if k % 2 == 0 else r * 0.45
                    pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
                d.polygon(pts, fill=farbe)
        img.save(band)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    einheit = Path(sys.argv[1]).resolve()
    ziel = einheit / "praesentationen"
    bilder = ziel / ".bilder"
    bilder.mkdir(parents=True, exist_ok=True)
    grafiken(bilder)
    readme = einheit / "README.md"
    einheit_titel = readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip() if readme.exists() else einheit.name
    decks = []
    for p in sorted((einheit / "material").glob("M*.1-folien*.md"), key=D.P.natuerlich):
        md = p.read_text(encoding="utf-8")
        std = re.match(r"M(\d+)", p.name).group(1)
        thema = re.sub(r"^#\s*M[\d.]+\s*[–-]\s*", "", md.splitlines()[0]).strip()
        thema = re.sub(r"^Folien\s+(Std\.?|Stunde)\s*\d+\s*[–:-]?\s*", "", thema).strip()
        folien = parse_folien(md, bilder)
        decks.append({"std": int(std), "anzahl": None, "thema": thema, "folien": folien,
                      "datei": f"Std-{std}-{re.sub(r'[^a-z0-9]+', '-', thema.lower().translate(str.maketrans({'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss'}))).strip('-')[:45].strip('-')}"})
    D.TMP = bilder
    D.svgs_rendern()
    for d in decks:
        d["anzahl"] = len(decks)
    daten = ziel / ".decks.json"
    daten.write_text(json.dumps({"einheit": einheit_titel, "decks": decks, "ziel": str(ziel),
                                 "bilder": str(bilder)}, ensure_ascii=False), encoding="utf-8")
    import os
    umgebung = dict(os.environ)
    global_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    umgebung["NODE_PATH"] = os.pathsep.join(filter(None, [umgebung.get("NODE_PATH", ""), str(Path(__file__).resolve().parent / "node_modules"), global_root]))
    subprocess.run(["node", str(Path(__file__).resolve().parent / "praesentation_bauen.js"), str(daten)], check=True, env=umgebung)


if __name__ == "__main__":
    main()
