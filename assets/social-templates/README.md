# Social image templates — NicAlpi v3

HTML templates matching the site brand (JetBrains Mono, paper palette, blue
accent). Same tokens as `assets/main.css`, defined in `social.css`. Two
groups:

## 1. Generator templates (`{{…}}` placeholders)

Filled automatically by `scripts/generate-og.py` from front matter — these
produce every `og_image` under `assets/images/og/`.

| Template | Size | Fed by |
|---|---|---|
| `og-home.html` | 1200×630 | bespoke homepage brand card — static, the template is the content |
| `og-post.html` | 1200×630 | `_posts/*` front matter (title, subtitle/description, category, reading_time) |
| `og-field-note.html` | 1200×630 | experiment briefs (`home`-flagged metrics or `facts`) and progress notes (metrics) |
| `og-page.html` | 1200×630 | the `PAGES` list inside the script (home, writing, about, contact, field-notes index) |

```bash
pip3 install playwright                      # once; uses your installed Chrome
python3 scripts/generate-og.py               # regenerate every OG jpg
python3 scripts/generate-og.py intention exp-01   # only these slugs
python3 scripts/generate-og.py --examples         # render the promo-card gallery
python3 scripts/generate-og.py --check            # every page has og_image + file
```

Slugs come from each post's `og_image` filename. New post → set
`og_image: /assets/images/og/<slug>.jpg` in front matter, run the script,
commit the jpg. Twitter uses the same image (no `-twitter` variants).

## 2. Hand-edited promo cards

Open in a browser, edit the text in place, export with
`scripts/export-social.mjs` (Node + Playwright) or a screenshot at exact size.
Add `?theme=dark` to the URL for the dark variant.

| Template | Size | Use |
|---|---|---|
| `quote-square.html` | 1080×1080 | Quote card (Instagram, LinkedIn square) |
| `verdict-square.html` | 1080×1080 | Solid-accent card for when an experiment closes |
| `post-promo-portrait.html` | 1080×1350 | Blog post promo for portrait feeds |
| `newsletter-og.html` | 1200×630 | Newsletter / subscribe card |

## Conventions

- Keep the header strip / footer rule structure — that's the brand's frame.
- Metrics always read `before → now` with the "now" in accent.
- The verdict card is the only solid-accent surface; use it sparingly.
- OG images ship at 2× (2400×1260) for retina-crisp unfurls.

Full how-to (with a rendered example of every template): `docs/guide.md`.
