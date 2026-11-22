#!/usr/bin/env python3
"""
Erzeugt maßstabsgetreue Dreiecks-Skizzen als SVG aus einem einfachen Textblock.

In Markdown-Materialien:

    ```dreieck
    winkel_A: 34          # Innenwinkel bei A in Grad (A liegt links unten)
    winkel_B: 56          # Innenwinkel bei B (B liegt rechts unten); C ergibt sich
    namen: A B C          # optional andere Eckpunktnamen, z. B. "C D E"
    seiten: AB="c = 8,6 cm" AC="b" BC="a"      # Beschriftung der Seiten (Namen wie bei 'namen')
    winkel: A="α = 34°" B="β"                  # Beschriftung der Winkelbögen
    rechter_winkel: auto  # auto (Standard) | nein – Quadrat-Zeichen bei 90°
    breite: 300           # Breite in Pixeln (Standard 300)
    spiegeln: nein        # ja = Spitze nach unten
    ```

Hat ein Winkel 90°, wird automatisch das Zeichen für den rechten Winkel (Viertelkreis mit Punkt,
wie in den Arbeitsblättern) gesetzt; dort wird kein Winkelbogen gezeichnet.
"""
from __future__ import annotations

import math
import re
import shlex


def _parse(text: str) -> dict[str, str]:
    werte = {}
    for zeile in text.splitlines():
        zeile = zeile.split("#", 1)[0].strip() if not re.search(r'"[^"]*#', zeile) else zeile.strip()
        if ":" in zeile:
            k, v = zeile.split(":", 1)
            werte[k.strip().lower()] = v.strip()
    return werte


def _paare(text: str) -> dict[str, str]:
    erg = {}
    for teil in shlex.split(text or ""):
        if "=" in teil:
            k, v = teil.split("=", 1)
            erg[k.strip()] = v.strip()
    return erg


def _esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def dreieck_svg(text: str) -> str:
    w = _parse(text)
    a = float(w.get("winkel_a", "60").replace(",", "."))
    b = float(w.get("winkel_b", "60").replace(",", "."))
    if a <= 0 or b <= 0 or a + b >= 180:
        raise ValueError(f"Ungültige Winkel: A={a}, B={b} (Summe muss < 180 sein)")
    g = 180 - a - b
    namen = (w.get("namen") or "A B C").split()
    if len(namen) != 3:
        namen = ["A", "B", "C"]
    nA, nB, nC = namen
    breite = float(w.get("breite", "300"))
    spiegeln = w.get("spiegeln", "nein").lower() in ("ja", "true", "1")
    rw_auto = w.get("rechter_winkel", "auto").lower() != "nein"
    seiten = _paare(w.get("seiten", ""))
    winkel = _paare(w.get("winkel", ""))

    # Geometrie: A=(0,0), B=(1,0), C über Sinussatz
    ra, rb = math.radians(a), math.radians(b)
    ac = math.sin(rb) / math.sin(ra + rb)
    P = {nA: (0.0, 0.0), nB: (1.0, 0.0), nC: (ac * math.cos(ra), ac * math.sin(ra))}
    xs = [p[0] for p in P.values()]
    ys = [p[1] for p in P.values()]
    rand = 34
    s = (breite - 2 * rand) / (max(xs) - min(xs))
    hoehe = (max(ys) - min(ys)) * s + 2 * rand

    def px(p):
        x = (p[0] - min(xs)) * s + rand
        y = (max(ys) - p[1]) * s + rand if not spiegeln else (p[1] - min(ys)) * s + rand
        return (x, y)

    Q = {k: px(v) for k, v in P.items()}
    sx = sum(q[0] for q in Q.values()) / 3
    sy = sum(q[1] for q in Q.values()) / 3
    teile = []
    pts = " ".join(f"{Q[n][0]:.1f},{Q[n][1]:.1f}" for n in namen)
    teile.append(f'<polygon points="{pts}" fill="none" stroke="black" stroke-width="1.6"/>')

    winkelgrad = {nA: a, nB: b, nC: g}
    for n in namen:
        x, y = Q[n]
        andere = [m for m in namen if m != n]
        v = []
        for m in andere:
            dx, dy = Q[m][0] - x, Q[m][1] - y
            lae = math.hypot(dx, dy)
            v.append((dx / lae, dy / lae))
        bis = (v[0][0] + v[1][0], v[0][1] + v[1][1])
        bl = math.hypot(*bis) or 1
        bis = (bis[0] / bl, bis[1] / bl)
        ist_rechter = rw_auto and abs(winkelgrad[n] - 90) < 0.01
        if ist_rechter:
            r = 13
            p1 = (x + v[0][0] * r, y + v[0][1] * r)
            p2 = (x + v[1][0] * r, y + v[1][1] * r)
            teile.append(f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 0 {_sweep(v[0], v[1])} '
                         f'{p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="black" stroke-width="1"/>')
            d = (x + bis[0] * r * 0.55, y + bis[1] * r * 0.55)
            teile.append(f'<circle cx="{d[0]:.1f}" cy="{d[1]:.1f}" r="1.6"/>')
        elif n in winkel:
            r = 24 if winkelgrad[n] > 35 else 34
            p1 = (x + v[0][0] * r, y + v[0][1] * r)
            p2 = (x + v[1][0] * r, y + v[1][1] * r)
            teile.append(f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 0 {_sweep(v[0], v[1])} '
                         f'{p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="black" stroke-width="1"/>')
            lr = r + 8 + 3.2 * len(winkel[n])
            lx, ly = x + bis[0] * lr, y + bis[1] * lr + 4
            teile.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle">{_esc(winkel[n])}</text>')
        # Eckpunktname außen
        ox, oy = x - sx, y - sy
        ol = math.hypot(ox, oy) or 1
        teile.append(f'<text x="{x + ox / ol * 14:.1f}" y="{y + oy / ol * 14 + 4:.1f}" text-anchor="middle">{_esc(n)}</text>')

    for schluessel, label in seiten.items():
        if len(schluessel) < 2:
            continue
        # Seitenname aus zwei Eckpunktnamen (auch mehrbuchstabig getrennt durch '-')
        teile_namen = schluessel.split("-") if "-" in schluessel else [schluessel[0], schluessel[1:]]
        if len(teile_namen) != 2 or any(t not in Q for t in teile_namen):
            continue
        p, q = Q[teile_namen[0]], Q[teile_namen[1]]
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        nx, ny = -(q[1] - p[1]), q[0] - p[0]
        nl = math.hypot(nx, ny) or 1
        nx, ny = nx / nl, ny / nl
        if (mx + nx - sx) ** 2 + (my + ny - sy) ** 2 < (mx - sx) ** 2 + (my - sy) ** 2:
            nx, ny = -nx, -ny
        # Text außen neben die Seite setzen: Ausrichtung nach der Richtung der Normalen
        if nx < -0.3:
            anker, tx = "end", mx + nx * 8 - 2
        elif nx > 0.3:
            anker, tx = "start", mx + nx * 8 + 2
        else:
            anker, tx = "middle", mx
        ty = my + ny * 8 + (12 if ny > 0.3 else (-2 if ny < -0.3 else 4))
        teile.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anker}">{_esc(label)}</text>')

    return (f'<svg width="{breite:.0f}" height="{hoehe:.0f}" viewBox="0 0 {breite:.0f} {hoehe:.0f}" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, DejaVu Sans, sans-serif" '
            f'font-size="13">' + "".join(teile) + "</svg>")


def _sweep(v0, v1) -> int:
    kreuz = v0[0] * v1[1] - v0[1] * v1[0]
    return 1 if kreuz > 0 else 0


DREIECK_BLOCK = re.compile(r"^```dreieck[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def ersetze_dreiecke(md: str) -> str:
    def ersatz(m):
        try:
            return dreieck_svg(m.group(1))
        except Exception as fehler:  # sichtbar machen statt abbrechen
            return f"**[Dreieck fehlerhaft: {_esc(str(fehler))}]**"
    return DREIECK_BLOCK.sub(ersatz, md)


if __name__ == "__main__":
    import sys
    print(dreieck_svg(sys.stdin.read()))
