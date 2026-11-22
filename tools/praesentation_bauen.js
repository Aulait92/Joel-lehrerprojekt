// Baut die Präsentationen (klassisch + lernpfad) aus .decks.json (erzeugt von praesentation_erstellen.py).
const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");
const { imageSize } = (() => { try { return require("image-size"); } catch { return { imageSize: null }; } })();

const SKILL_THEME = "/root/.claude/skills/synced/d9e217d6-db34-4b2f-9a99-24230f08d023_51c8ad1a-1eb0-4567-9fbb-49523ed7f2ed/pptx/scripts/apply_theme.js";
let applyTheme = null;
try { applyTheme = require(SKILL_THEME).applyTheme; } catch { applyTheme = null; }

const daten = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const W = 10, H = 6.25; // LAYOUT_16x10

const THEMES = {
  klassisch: {
    name: "Klassisch Karopapier",
    headFontFace: "Arial", bodyFontFace: "Arial",
    colors: { dk1: "1A1A1A", lt1: "FFFFFF", dk2: "1F5B4F", lt2: "F9F8EE", accent1: "1F5B4F", accent2: "BED678",
      accent3: "C0392B", accent4: "2E6DA4", accent5: "7F7F7F", accent6: "D4A017", hlink: "2E6DA4", folHlink: "6D28D9" },
  },
  lernpfad: {
    name: "Lernpfad",
    headFontFace: "Calibri", bodyFontFace: "Calibri",
    colors: { dk1: "1E1B4B", lt1: "FFFFFF", dk2: "4C1D95", lt2: "F4F1FF", accent1: "7C3AED", accent2: "22C55E",
      accent3: "F59E0B", accent4: "0EA5E9", accent5: "EF4444", accent6: "A3E635", hlink: "7C3AED", folHlink: "4C1D95" },
  },
};

function textLaenge(items) {
  return items.reduce((n, it) => n + (it.runs ? it.runs.map(r => r.text).join("").length : (it.text || "").length), 0);
}

function runsZuText(runs, basis) {
  return runs.map(r => ({
    text: r.text,
    options: Object.assign({}, basis, r.bold ? { bold: true } : {}, r.italic ? { italic: true } : {},
      r.code ? { fontFace: "Courier New" } : {}),
  }));
}

function absaetze(items, groesse, farbe) {
  const out = [];
  items.forEach((it, idx) => {
    const letzte = idx === items.length - 1;
    if (it.typ === "code") {
      it.text.split("\n").forEach((zeile, j, arr) => out.push({ text: zeile || " ", options: { fontFace: "Courier New", fontSize: groesse - 3, color: farbe, breakLine: !(letzte && j === arr.length - 1) } }));
      return;
    }
    const basis = { fontSize: groesse, color: farbe };
    const runs = runsZuText(it.runs.filter(r => r.text !== ""), basis);
    if (!runs.length) return;
    const absatzOpt = it.typ === "punkt"
      ? { bullet: it.nummer ? { type: "number" } : true, paraSpaceAfter: 4, indentLevel: it.ebene || 0 }
      : { paraSpaceAfter: 6 };
    runs.forEach((r, j) => {
      Object.assign(r.options, absatzOpt);
      if (j === runs.length - 1 && !letzte) r.options.breakLine = true;
    });
    out.push(...runs);
  });
  return out;
}

function tabelle(slide, t, x, y, w, groesse, design, C) {
  const spalten = Math.max(...t.zeilen.map(z => z.length));
  const rows = t.zeilen.map((z, ri) => {
    const zellen = [];
    for (let i = 0; i < spalten; i++) {
      let runs = (z[i] || []).filter(r => r.text !== "");
      if (!runs.length) runs = [{ text: " " }];
      zellen.push({
        text: runsZuText(runs, { fontSize: groesse, color: design === "lernpfad" ? "1E1B4B" : "1A1A1A", bold: ri === 0 }),
        options: { fill: { color: ri === 0 ? (design === "lernpfad" ? "EDE9FE" : "E8EFE4") : "FFFFFF" } },
      });
    }
    return zellen;
  });
  const hoehe = Math.min(0.42 * rows.length, 4.2);
  slide.addTable(rows, { x, y, w, colW: Array(spalten).fill(w / spalten), border: { type: "solid", pt: 0.75, color: "9CA3AF" },
    fontFace: design === "lernpfad" ? "Calibri" : "Arial", valign: "middle", margin: 0.05, autoPage: false });
  return hoehe;
}

function texthoehe(items, groesse, breite) {
  const zeichenBreite = 0.5 * groesse / 72, zeilenHoehe = 1.3 * groesse / 72;
  let h = 0;
  items.forEach(it => {
    const n = it.runs ? it.runs.map(r => r.text).join("").length : 0;
    const zeilen = it.typ === "code" ? it.text.split("\n").length : Math.max(1, Math.ceil(n * zeichenBreite / Math.max(breite - 0.4, 1)));
    h += zeilen * zeilenHoehe + (it.typ === "punkt" ? 4 : 6) / 72;
  });
  return h + 0.3;
}

function bildMasse(b, maxW, maxH) {
  let w = b.w / 96, h = b.h / 96;
  const f = Math.min(maxW / w, maxH / h, 1.6);
  return { w: w * f, h: h * f };
}

// ---------------------------------------------------------------- Inhalt
function inhalt(slide, f, design, C, oben) {
  const texte = f.inhalt.filter(i => ["absatz", "punkt", "code"].includes(i.typ));
  const tabellen = f.inhalt.filter(i => i.typ === "tabelle");
  const bilder = f.inhalt.filter(i => i.typ === "bild" && fs.existsSync(i.pfad));
  const links = 0.55, unten = H - 0.55;
  const breite = W - 2 * links;
  const textBreite = bilder.length ? breite * 0.56 : breite;
  const n = textLaenge(texte) + tabellen.reduce((s, t) => s + t.zeilen.flat().map(c => c.map(r => r.text).join("")).join("").length * 0.6, 0);
  let groesse = n < 220 ? 22 : n < 400 ? 20 : n < 620 ? 18 : n < 850 ? 16 : 14;
  const farbe = design === "lernpfad" ? "1E1B4B" : "1A1A1A";
  let y = oben;
  const verfuegbar = unten - oben;
  const tabHoehe = tabellen.reduce((s, t) => s + Math.min(0.42 * t.zeilen.length, 4.2) + 0.15, 0);
  const platz = Math.max(verfuegbar - tabHoehe, 0.8);
  while (groesse > 14 && texthoehe(texte, groesse, textBreite) > platz) groesse -= 2;
  const textHoehe = Math.min(Math.max(texthoehe(texte, groesse, textBreite), 0.7), platz);
  if (texte.length) {
    const box = { x: links, y, w: textBreite, h: textHoehe, valign: "top", margin: design === "lernpfad" ? 0.15 : 0.05, isTextBox: true, fit: "shrink", objectName: "Inhalt" };
    if (design === "lernpfad") {
      slide.addShape("roundRect", { x: links - 0.05, y: y - 0.05, w: textBreite + 0.1, h: textHoehe + 0.1, rectRadius: 0.12,
        fill: { color: "FFFFFF" }, line: { color: "DDD6FE", width: 1 }, shadow: { type: "outer", color: "7C3AED", opacity: 0.12, blur: 6, offset: 2, angle: 90 }, objectName: "Karte" });
    }
    const par = absaetze(texte, groesse, farbe);
    if (par.length) slide.addText(par, box);
    y += textHoehe + 0.15;
  }
  tabellen.forEach(t => {
    const th = tabelle(slide, t, links, texte.length ? y : oben, textBreite, Math.max(groesse - 4, 12), design, C);
    y += th + 0.15;
  });
  if (bilder.length) {
    const bx = links + textBreite + 0.25, bw = breite - textBreite - 0.25;
    const proBild = (verfuegbar - 0.15 * (bilder.length - 1)) / bilder.length;
    let by = oben;
    bilder.forEach(b => {
      const m = bildMasse(b, bw, proBild);
      if (design === "lernpfad") {
        slide.addShape("roundRect", { x: bx + (bw - m.w) / 2 - 0.1, y: by - 0.1, w: m.w + 0.2, h: m.h + 0.2, rectRadius: 0.12,
          fill: { color: "FFFFFF" }, line: { color: "DDD6FE", width: 1 }, objectName: "Bildrahmen" });
      }
      slide.addImage({ path: b.pfad, x: bx + (bw - m.w) / 2, y: by, w: m.w, h: m.h, altText: "Skizze", objectName: "Skizze" });
      by += m.h + 0.25;
    });
  }
}

// ---------------------------------------------------------------- Designs
function theo(slide, x, y, s, C) {
  // Maskottchen „Theo“: ein freundliches rechtwinkliges Dreieck (eigenes Design)
  slide.addShape("rtTriangle", { x, y, w: s, h: s, fill: { color: "7C3AED" }, line: { color: "4C1D95", width: 1.5 }, objectName: "Theo" });
  slide.addShape("ellipse", { x: x + s * 0.18, y: y + s * 0.52, w: s * 0.2, h: s * 0.2, fill: { color: "FFFFFF" }, line: { color: "FFFFFF" }, objectName: "Theo-Auge" });
  slide.addShape("ellipse", { x: x + s * 0.42, y: y + s * 0.52, w: s * 0.2, h: s * 0.2, fill: { color: "FFFFFF" }, line: { color: "FFFFFF" }, objectName: "Theo-Auge" });
  slide.addShape("ellipse", { x: x + s * 0.25, y: y + s * 0.58, w: s * 0.09, h: s * 0.09, fill: { color: "1E1B4B" }, line: { color: "1E1B4B" }, objectName: "Theo-Pupille" });
  slide.addShape("ellipse", { x: x + s * 0.49, y: y + s * 0.58, w: s * 0.09, h: s * 0.09, fill: { color: "1E1B4B" }, line: { color: "1E1B4B" }, objectName: "Theo-Pupille" });
  slide.addShape("arc", { x: x + s * 0.24, y: y + s * 0.66, w: s * 0.32, h: s * 0.22, angleRange: [20, 160], line: { color: "FFFFFF", width: 2 }, objectName: "Theo-Lächeln" });
}

function pfad(slide, akt, gesamt, x, y, breite) {
  const n = Math.min(gesamt, 18);
  const schritt = breite / Math.max(n - 1, 1);
  slide.addShape("line", { x, y: y + 0.06, w: breite, h: 0, line: { color: "DDD6FE", width: 2.5 }, objectName: "Pfadlinie" });
  for (let i = 0; i < n; i++) {
    const fertig = i < akt, jetzt = i === akt;
    slide.addShape("ellipse", { x: x + i * schritt - 0.07, y: y - 0.01, w: 0.14, h: 0.14,
      fill: { color: jetzt ? "F59E0B" : fertig ? "22C55E" : "FFFFFF" }, line: { color: jetzt ? "B45309" : fertig ? "15803D" : "C4B5FD", width: 1 }, objectName: "Pfadpunkt" });
  }
}

function chip(slide, text, x, y, w, fuell, schrift) {
  slide.addShape("roundRect", { x, y, w, h: 0.34, rectRadius: 0.17, fill: { color: fuell }, line: { color: fuell }, objectName: "Chip" });
  slide.addText(text, { x, y, w, h: 0.34, fontSize: 12, bold: true, color: schrift, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: "Chip-Text" });
}

function bauen(deck, design) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x10";
  const T = THEMES[design];
  pres.theme = { headFontFace: T.headFontFace, bodyFontFace: T.bodyFontFace };
  pres.title = `${daten.einheit} – Std. ${deck.std}`;
  pres.author = "Lehrerprojekt";
  const C = pres.SchemeColor;
  const bg = path.join(daten.bilder, "karopapier.png");

  if (design === "klassisch") {
    pres.defineSlideMaster({ title: "KLASSISCH_INHALT", background: { path: bg },
      objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.25, w: 9.0, h: 0.85, align: "center", valign: "middle", fontSize: 32, color: "1A1A1A", fontFace: "Arial" }, text: "" } }],
      slideNumber: { x: 9.2, y: 5.85, w: 0.5, h: 0.3, fontSize: 10, color: "7F7F7F" } });
    pres.defineSlideMaster({ title: "KLASSISCH_TITEL", background: { path: bg },
      objects: [{ placeholder: { options: { name: "title", type: "title", x: 1.5, y: 0.5, w: 7.0, h: 1.4, align: "center", valign: "middle", fontSize: 32, color: "1A1A1A", fontFace: "Arial" }, text: "" } }] });
  } else {
    pres.defineSlideMaster({ title: "LERNPFAD_INHALT", background: { color: "F4F1FF" },
      objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.55, y: 0.5, w: 6.6, h: 0.75, align: "left", valign: "middle", fontSize: 28, bold: true, color: "1E1B4B", fontFace: "Calibri" }, text: "" } }],
      slideNumber: { x: 9.2, y: 5.85, w: 0.5, h: 0.3, fontSize: 10, color: "6B7280" } });
    pres.defineSlideMaster({ title: "LERNPFAD_TITEL", background: { color: "4C1D95" },
      objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.7, y: 1.6, w: 5.8, h: 1.6, align: "left", valign: "middle", fontSize: 36, bold: true, color: "FFFFFF", fontFace: "Calibri" }, text: "" } }] });
  }

  pres.addSection({ title: `Stunde ${deck.std}` });
  const gesamt = deck.folien.length;
  {
    const t = pres.addSlide({ masterName: design === "klassisch" ? "KLASSISCH_TITEL" : "LERNPFAD_TITEL", sectionTitle: `Stunde ${deck.std}` });
    if (design === "klassisch") {
      t.addText("Herzlich Willkommen im Mathematikunterricht!", { placeholder: "title" });
      t.addText([{ text: `Trigonometrie – Stunde ${deck.std}`, options: { fontSize: 24, bold: true, breakLine: true } },
                 { text: deck.thema, options: { fontSize: 18 } }],
        { x: 1.0, y: 2.6, w: 8.0, h: 1.6, align: "center", valign: "middle", color: "1A1A1A", isTextBox: true, objectName: "Untertitel" });
      t.addImage({ path: path.join(daten.bilder, "klebeband.png"), x: -0.5, y: 2.3, w: 3.4, h: 0.42, rotate: -58, objectName: "Klebeband" });
      t.addImage({ path: path.join(daten.bilder, "klebeband.png"), x: 7.1, y: 2.3, w: 3.4, h: 0.42, rotate: 58, objectName: "Klebeband" });
    } else {
      t.addText(`Trigonometrie – Level ${deck.std}`, { placeholder: "title" });
      chip(t, `LEVEL ${deck.std} / ${deck.anzahl}`, 0.7, 0.8, 1.6, "F59E0B", "1E1B4B");
      t.addText(deck.thema, { x: 0.7, y: 3.25, w: 5.8, h: 0.9, fontSize: 20, color: "EDE9FE", valign: "top", margin: 0, isTextBox: true, objectName: "Untertitel" });
      t.addText("Sammle heute XP: ★-Aufgaben 10 XP · Bonus 15 XP · Profi-Challenge 25 XP", { x: 0.7, y: 4.4, w: 5.8, h: 0.5, fontSize: 14, color: "C4B5FD", margin: 0, isTextBox: true, objectName: "XP-Hinweis" });
      theo(t, 6.9, 1.4, 2.4, C);
    }
  }
  deck.folien.forEach((f, idx) => {
    const istTitel = false;
    const istEnde = idx === gesamt - 1 && /geschafft|pause|ende|glückwunsch|abschluss/i.test(f.titel + JSON.stringify(f.inhalt));
    const master = design === "klassisch" ? (istTitel ? "KLASSISCH_TITEL" : "KLASSISCH_INHALT") : (istTitel ? "LERNPFAD_TITEL" : "LERNPFAD_INHALT");
    const slide = pres.addSlide({ masterName: master, sectionTitle: `Stunde ${deck.std}` });
    slide.addText(f.titel, { placeholder: "title" });

    if (design === "klassisch") {
      if (istTitel || istEnde) {
        slide.addImage({ path: path.join(daten.bilder, "klebeband.png"), x: -0.55, y: 0.45, w: 2.4, h: 0.3, rotate: -40, objectName: "Klebeband" });
        slide.addImage({ path: path.join(daten.bilder, "klebeband.png"), x: 8.15, y: 0.45, w: 2.4, h: 0.3, rotate: 40, objectName: "Klebeband" });
      }
      if (f.zeit) slide.addText(`ca. ${f.zeit}`, { x: 0.5, y: 1.08, w: 3, h: 0.35, fontSize: 16, color: "1A1A1A", margin: 0, isTextBox: true, objectName: "Zeit" });
      inhalt(slide, f, design, C, istTitel ? 2.2 : 1.5);
    } else {
      if (istTitel) {
        chip(slide, `LEVEL ${deck.std} / ${deck.anzahl}`, 0.7, 0.8, 1.6, "F59E0B", "1E1B4B");
        theo(slide, 6.9, 1.4, 2.4, C);
        const rest = Object.assign({}, f, { inhalt: f.inhalt });
        const unter = absaetze(rest.inhalt.filter(i => i.runs && i.runs.some(r => r.text.trim())), 16, "EDE9FE");
        if (unter.length) slide.addText(unter, { x: 0.7, y: 3.3, w: 5.8, h: 2.2, valign: "top", margin: 0, isTextBox: true, fit: "shrink", objectName: "Untertitel" });
      } else {
        pfad(slide, idx, gesamt, 0.6, 0.2, 5.5);
        chip(slide, `Level ${deck.std}`, 7.35, 0.13, 1.0, "EDE9FE", "4C1D95");
        if (f.zeit) chip(slide, `⏱ ${f.zeit}`, 8.45, 0.13, 1.05, "FEF3C7", "92400E");
        if (istEnde) theo(slide, 7.9, 3.9, 1.6, C);
        inhalt(slide, f, design, C, 1.4);
      }
    }
    const notiz = f.notizen.join("\n").replace(/\*\*/g, "");
    if (notiz) slide.addNotes(notiz);
  });
  return pres;
}

(async () => {
  for (const design of ["klassisch", "lernpfad"]) {
    const ordner = path.join(daten.ziel, design);
    fs.mkdirSync(ordner, { recursive: true });
    for (const deck of daten.decks) {
      const pres = bauen(deck, design);
      const datei = path.join(ordner, deck.datei + ".pptx");
      await pres.writeFile({ fileName: datei });
      if (applyTheme) {
        try { await applyTheme(datei, THEMES[design]); } catch (e) { console.warn("Theme nicht angewendet:", e.message); }
      }
      console.log("PPTX:", datei);
    }
  }
})().catch(e => { console.error(e); process.exit(1); });
