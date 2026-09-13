# Social image templates — NicAlpi v4 "Graphite notebook"

HTML templates matching the site brand (JetBrains Mono only, graphite
scale on white, signal blue for the markdown marks, pills for labels and
CTAs, ink for the one solid card). Same tokens as `_assets/main.css`,
defined in `social.css`, which also carries the shared helpers: `.mark`,
`.tag`/`.tag-accent`, `.btn-ink`, `.fog`, `.quote`. Rules: `DESIGN.md` →
Imagery. Two groups:

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
# on Nic's machine the python with playwright is /opt/homebrew/bin/python3.13
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
| `quote-square.html` | 1080×1080 | Quote card (Instagram, LinkedIn square) — `>` quote, pill label |
| `verdict-square.html` | 1080×1080 | Ink-filled card for when an experiment closes |
| `post-promo-portrait.html` | 1080×1350 | Blog post promo for portrait feeds — front-matter block, no cover photo |
| `newsletter-og.html` | 1200×630 | Newsletter / subscribe card — the `> newsletter` fog band |

Per-post copies live in `assets/images/social/<slug>/` (fix the `social.css`
href to `../../../social-templates/social.css`); render them with
`scripts/render-illustration.py --size WxH [--theme dark]`.

## Conventions

- Keep the frame: `nicalpi.md` top left, a context label top right, hairline
  footer with `nicalpi.com`.
- `# ` mark before headlines in `--mark`; quotes hang off a `>`; labels are
  pills; CTAs are ink pills. Blue is never a fill.
- Metrics always read `before → now` with the arrow in `--mark` and the
  "now" in accent.
- The verdict card is the only solid surface and it is ink; use it sparingly.
- OG images ship at 2× (2400×1260) for retina-crisp unfurls.

Full how-to (with a rendered example of every template): `docs/guide.md`.
