---
name: promo-asset
description: Generate visual assets for an approved promo plan — quote cards, carousel PDFs, and insight images using the v4 brand templates. Use when Nic says "make the assets", "generate the carousel", or names a day that needs a visual.
argument-hint: "[slug] [day N | all]"
model: opus
effort: medium
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent, Skill
---

# Promo — ASSET

You generate visual assets for social promotion using the v4 "Graphite
notebook" brand system. Templates and rendering are documented in the
`social-image` skill, `docs/guide.md` §1-2, and `assets/social-templates/`.

Read `.promo-memory/<slug>/plan.md` to see which days need assets and what
they contain.

## Asset types

### Quote card (1080×1080 for LinkedIn/Instagram, 1200×675 for Twitter)

Uses `assets/social-templates/quote-square.html` as the base. One quotable
sentence from the blog post, attributed to Nic. On-brand: `nicalpi.md`
wordmark, `# ` mark before the quote, hairline footer with `nicalpi.com`.

1. Copy the template to `.promo-memory/<slug>/assets/quote-dayNN.html`
2. Edit the quote text and any labels
3. Render both sizes:
   ```bash
   /opt/homebrew/bin/python3.13 scripts/render-illustration.py <file> --size 1080x1080 --out <file>-square.png
   /opt/homebrew/bin/python3.13 scripts/render-illustration.py <file> --size 1200x675 --out <file>-landscape.png
   ```
4. Render dark variants if Nic wants them (append `--theme dark`)

### Carousel (1080×1080 or 1080×1350 PDF, 5-12 slides)

No template exists yet for carousels. Build as a self-contained HTML file
with one `<section>` per slide at the target dimensions, then render each
slide to a PNG and combine into a PDF.

Carousel design rules (from the research):
- 1080×1080 (square) or 1080×1350 (portrait) — pick one per carousel
- 14pt minimum body text
- One idea per slide
- Slide 1: hook (the claim or question)
- Slides 2-N: one point each, with a visual hierarchy
- Last slide: CTA or the blog URL
- On-brand: same tokens as quote cards, JetBrains Mono headings, pills for
  labels, `nicalpi.md` wordmark on slide 1 and last slide

Build the HTML in `.promo-memory/<slug>/assets/carousel-dayNN.html` as one
stacked file with a `?slide=N` param that removes every slide but the Nth:

```html
<script>
  const q = new URLSearchParams(location.search);
  if (q.get('theme') === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
  addEventListener('DOMContentLoaded', () => {
    const n = parseInt(q.get('slide'), 10);
    if (!n) return;
    document.querySelectorAll('.slide').forEach((el, i) => { if (i + 1 !== n) el.remove(); });
  });
</script>
```

**Render one slide at a time.** Do not render the full stacked strip and crop
it: at `device_scale_factor=2` a 8×1080px strip is 17280px tall, past Chrome's
16384px texture limit, and the lower slides come back corrupted (slide content
bleeding across tile boundaries). `render-illustration.py` cannot pass
`?slide=`, so loop Playwright directly:

```bash
/opt/homebrew/bin/python3.13 -c "
from playwright.sync_api import sync_playwright
from pathlib import Path
src = Path('.promo-memory/<slug>/assets/carousel-dayNN.html').resolve()
out = src.parent
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, channel='chrome')
    pg = b.new_page(viewport={'width':1080,'height':1080}, device_scale_factor=2)
    for n in range(1, 9):
        pg.goto(src.as_uri() + f'?slide={n}', wait_until='networkidle')
        pg.evaluate('() => document.fonts.ready')
        pg.screenshot(path=str(out / f'slide-{n:02d}.png'), type='png',
                      clip={'x':0,'y':0,'width':1080,'height':1080})
    b.close()
"
```

Then combine to PDF (ImageMagick is installed):
```bash
cd .promo-memory/<slug>/assets && magick slide-*.png -quality 92 carousel-dayNN.pdf
```

Always open at least the first and last rendered slide with Read to confirm
nothing clipped before declaring the carousel done.

### Insight image (1080×1080 with a stat or data point)

Same approach as quote card, but the content is a number or stat rather than
a quote. Use the quote-square template as a base, replacing the quote block
with a large number + context line.

## Workflow

1. Read the plan's `## Asset list` to see what's needed
2. Read the draft copy for each day (the carousel slide text, the quote to
   use) from `.promo-memory/<slug>/drafts/`
3. Generate each asset, showing Nic a preview (the HTML in a browser or a
   description of the layout)
4. Ask for approval of each asset — he may want a different quote, a
   different slide order, or a tweak to the layout
5. Render final PNGs/PDFs

Mark completed assets in the plan's `## Asset list` with `[x]`.

When all assets are done, end with: "Assets ready. The full promo calendar
is drafted and designed — post when ready. Run `/promo-status <slug>` to
see the checklist."

## Judgment

- Use the existing v4 templates. Do not design from scratch.
- The carousel is the highest-effort asset. If Nic wants to skip it, that's
  fine — text posts with a quote card already cover most of the calendar.
- Quote cards use actual lines from the post, never invented or paraphrased.
- Rendering needs Chrome and the Python script — if those fail, provide the
  HTML and tell Nic to screenshot at 100% zoom as a fallback.
- Dark variants are optional. Generate them if he's posting to platforms where
  his audience is likely in dark mode (most of Twitter).
