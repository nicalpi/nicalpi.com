# NicAlpi v3 Social Cards

The canonical templates live in `assets/social-templates/` — self-contained
HTML files sharing the site tokens via `social.css`. Don't rebuild cards from
scratch. Full usage doc: `docs/guide.md` (gallery + workflows) and `assets/social-templates/README.md`.

## OG images (generated — don't hand-edit the jpgs)

`scripts/generate-og.py` fills the placeholder templates from front matter
and screenshots them to `assets/images/og/<slug>.jpg` (1200×630 @2×, light
theme). Requires Python playwright (`pip3 install playwright`; drives the
installed Chrome).

| Template | Fed by |
|---|---|
| `og-home.html` | bespoke homepage brand card (static) |
| `og-post.html` | posts: title, subtitle/description, category, reading_time; slug from `og_image` |
| `og-field-note.html` | briefs: `home`-flagged metrics (or `facts`), status_label, verdict · progress notes: metrics, next_label |
| `og-page.html` | `PAGES` list in the script (home, writing, about, contact, field-notes index) |

Workflow for a new post or field note:
1. Set `og_image: /assets/images/og/<slug>.jpg` in front matter.
2. `python3 scripts/generate-og.py <slug>`
3. Commit the jpg. Twitter reuses the same image — no `-twitter` variants
   (head.html no longer rewrites the filename).

## Promo cards (hand-edited)

`quote-square` (1080×1080), `verdict-square` (1080×1080, solid accent),
`post-promo-portrait` (1080×1350), `newsletter-og` (1200×630). Edit text in
place, preview in a browser (`?theme=dark` for dark), export with
`scripts/export-social.mjs` (Node playwright) at 2×.

## Rules

- JetBrains Mono only. Faint `# ` mark before headlines.
- Wordmark is lowercase `nicalpi`, 700, no coloured letters.
- Metrics read `before → now`: before in ink, arrow in `--faint`, now in accent.
- The verdict card is the only solid-accent surface. Verdicts are one word.
- Every card carries `nicalpi.com` (or `nicalpi.com / field notes`).
