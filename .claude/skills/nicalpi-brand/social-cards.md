# NicAlpi v4 Social Cards

The canonical templates live in `assets/social-templates/` — self-contained
HTML files sharing the site tokens via `social.css`. Don't rebuild cards from
scratch. Full usage doc: `docs/guide.md` (gallery + workflows) and
`assets/social-templates/README.md`. Brand spec: `DESIGN.md` → Imagery.

## OG images (generated — don't hand-edit the jpgs)

`scripts/generate-og.py` fills the placeholder templates from front matter
and screenshots them to `assets/images/og/<slug>.jpg` (1200×630 @2×, light
theme). Requires Python playwright driving the installed Chrome — on Nic's
machine use `/opt/homebrew/bin/python3.13`. Google Fonts must be reachable
(in Claude Code, run it outside the sandbox).

The script's front-matter parser only reads **block-style YAML lists**
(`- label: x` with indented keys) — inline `{ label: x, value: y }` entries
make it crash. Write field-note front matter block-style.

| Template | Fed by |
|---|---|
| `og-home.html` | bespoke homepage brand card: the `---` bio block + hero line + ink pill (static) |
| `og-post.html` | posts: title, subtitle/description, category (outlined pill), reading_time; slug from `og_image` |
| `og-field-note.html` | briefs: `home`-flagged metrics (or `facts`), status_label, verdict · progress notes: metrics, next_label. Header strip is a fog band with accent text |
| `og-page.html` | `PAGES` list in the script (writing, about, contact, field-notes index, styleguide, 404) |

Workflow for a new post or field note:
1. Set `og_image: /assets/images/og/<slug>.jpg` in front matter.
2. `/opt/homebrew/bin/python3.13 scripts/generate-og.py <slug>`
3. Commit the jpg. Twitter reuses the same image — no `-twitter` variants.

## Promo cards (hand-edited)

`quote-square` (1080×1080), `verdict-square` (1080×1080, **ink** fill),
`post-promo-portrait` (1080×1350, front-matter block instead of a cover
photo), `newsletter-og` (1200×630, the `> newsletter` fog band). Copy the
template next to the post (`assets/images/social/<slug>/`), edit text in
place, preview in a browser (`?theme=dark` for dark), render both themes
with `scripts/render-illustration.py --size WxH --theme dark`.

## Rules

- JetBrains Mono only, `-0.012em` tracking, 400/500/600/700. Never the serif
  in an image.
- Wordmark `nicalpi` 700 + `.md` 400 in `--faint`. Every card carries
  `nicalpi.com`.
- `# ` mark before headlines in `--mark` (`.mark`), never faint.
- Quotes hang off a mono `>` in `--mark` (`.quote`), italic, 600. No bar.
- Labels and categories are pills (`.tag`, `.tag-accent`). CTAs are ink
  pills (`.btn-ink`). Blue is never a fill.
- Metrics read `before → now`: before in ink, arrow in `--mark`, now in
  `--accent`.
- Fog panels (`.fog`) have no border and 12–20px corners; the card frame is
  the one 1px `--line` hairline.
- The verdict card is the only solid surface and it is ink. Verdicts are one
  word.
