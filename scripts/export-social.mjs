#!/usr/bin/env node
/**
 * Export the social image templates to PNG (both themes, 2× scale).
 *
 * Setup (once):   npm i -D playwright && npx playwright install chromium
 * Usage:          node scripts/export-social.mjs [template-name] [out-dir]
 *   node scripts/export-social.mjs                 # export everything → assets/images/social/
 *   node scripts/export-social.mjs og-field-note   # one template, both themes
 */
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const templatesDir = path.join(root, 'assets', 'social-templates');

const TEMPLATES = {
  'og-field-note':       { w: 1200, h: 630 },
  'quote-square':        { w: 1080, h: 1080 },
  'verdict-square':      { w: 1080, h: 1080 },
  'post-promo-portrait': { w: 1080, h: 1350 },
  'newsletter-og':       { w: 1200, h: 630 },
};

const only = process.argv[2];
const outDir = process.argv[3] || path.join(root, 'assets', 'images', 'social');
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
for (const [name, { w, h }] of Object.entries(TEMPLATES)) {
  if (only && name !== only) continue;
  for (const theme of ['light', 'dark']) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    const url = `file://${path.join(templatesDir, name + '.html')}?theme=${theme}`;
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(outDir, `${name}${theme === 'dark' ? '-dark' : ''}.png`);
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h } });
    console.log('✓', path.relative(root, out));
    await page.close();
  }
}
await browser.close();
