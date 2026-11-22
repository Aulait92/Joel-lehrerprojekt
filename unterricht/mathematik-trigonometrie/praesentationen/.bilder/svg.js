
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const auftraege = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 3 });
  for (const [pfad, svg] of Object.entries(auftraege)) {
    await page.setContent(`<html><body style="margin:0;background:#fff">${svg}</body></html>`);
    await page.locator('svg').first().screenshot({ path: pfad, omitBackground: false });
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
