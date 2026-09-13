---
name: social-image
description: Create or regenerate a social/OG image for a nicalpi.com post, page, field note, quote or thought using the v4 "Graphite notebook" templates. Use when Nic asks for a social card, OG image, quote card, verdict card, LinkedIn/Instagram image, or wants to promote a post or field note visually.
---

# Social image

You produce on-brand social images for nicalpi.com using the v4 template
system — never a from-scratch design. Full reference: `docs/guide.md` §1–2,
`assets/social-templates/README.md`, and `DESIGN.md` → Imagery for the
rules (mono only, `# ` mark in signal blue, pills for labels, ink for the
one solid card, never a blue fill).

## 1. Pick the template

| Want | Template | Size | Route |
|---|---|---|---|
| Link card for a post / page / field note / progress note | `og-post` / `og-page` / `og-field-note` / `og-home` | 1200×630 | **generated** from front matter |
| A quote or one thought, square feed | `quote-square.html` | 1080×1080 | hand-edit |
| An experiment just closed (verdict) | `verdict-square.html` | 1080×1080 | hand-edit |
| Promote a post in portrait feeds | `post-promo-portrait.html` | 1080×1350 | hand-edit |
| Newsletter push | `newsletter-og.html` | 1200×630 | hand-edit |

## 2. Generated OG cards (link previews)

These come from front matter — the fix is in the *content*, not the image.

```bash
/opt/homebrew/bin/python3.13 scripts/generate-og.py <slug> [...]   # regenerate specific cards
/opt/homebrew/bin/python3.13 scripts/generate-og.py --check        # every page has a card
```
(Needs Chrome and Google Fonts — run outside the Claude Code sandbox.)

Slug = the `og_image` filename. If a new page lacks `og_image`, add
`og_image: /assets/images/og/<slug>.jpg` to its front matter first. Field
note cards pull their stats column from `home:`-flagged `metrics` (or
`facts`); if the card looks stale, update the front matter numbers and
regenerate.

## 3. Hand-edited promo cards

1. Copy the template to `assets/images/social/<slug>/` (fix the `social.css`
   href to `../../../social-templates/social.css`) and edit the text in place
   — every block is plain markup. Keep the frame: `nicalpi.md` wordmark top
   left, hairline footer with `nicalpi.com`, `# ` mark (`.mark`) before the
   headline, quotes as `.quote`, labels as `.tag`, CTAs as `.btn-ink`,
   metrics as `before → now` with the arrow in `--mark` and "now" in accent.
2. Writing for cards: one idea per card; quotes come from the actual post or
   note (never invent); verdicts are one word; every card carries
   `nicalpi.com`.
3. Export both themes:
   ```bash
   /opt/homebrew/bin/python3.13 scripts/render-illustration.py <file.html> --size 1080x1080 --out <file>.png
   /opt/homebrew/bin/python3.13 scripts/render-illustration.py <file.html> --size 1080x1080 --theme dark --out <file>-dark.png
   ```
   or preview in a browser (`?theme=dark` for dark) and screenshot at exact
   size.

## 4. On Claude Web (no repo)

Build the card as a **self-contained HTML artifact** at the exact pixel
size, using these tokens (light): panel `#FFFFFF` · fog `#F0F0F3` · line
`#D9D9E0` · ink `#1C2024` · body `#2A2E34` · muted `#60646C` · faint
`#80838D` · accent `#0072DE` · mark `#0090FF` · accent-soft `#EAF4FF` ·
on-ink `#FFFFFF`. Dark: panel `#0F1114` · fog `#1A1D22` · line `#2A2E35` ·
ink `#F2F3F5` · body `#C9CCD2` · muted `#8B8F98` · faint `#6B6F78` · accent
`#6DB8FF` · mark `#3DA5FF` · accent-soft `#14233A` · on-ink `#0F1114`.
Font: JetBrains Mono (400/500/600/700, Google Fonts), `-0.012em` tracking.
Reproduce the template layouts (1px hairline frame, `nicalpi.md` top left,
`# ` mark in `#0090FF` before headlines, pills for labels, ink pill CTA,
hairline footer with `nicalpi.com`), then tell Nic to screenshot it at 100%
or paste the HTML into `assets/images/social/<slug>/` and render properly
later.

## Judgment

- OG jpgs are generated artefacts: never hand-edit them, never design a
  bespoke one-off when a template fits.
- The verdict card is the only solid surface, and it is ink — closing
  experiments only. Blue is never a fill.
- If asked for a card for content that doesn't exist yet, say so and point
  at the think/write skills first.
