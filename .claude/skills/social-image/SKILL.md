---
name: social-image
description: Create or regenerate a social/OG image for a nicalpi.com post, page, field note, quote or thought using the v3 templates. Use when Nic asks for a social card, OG image, quote card, verdict card, LinkedIn/Instagram image, or wants to promote a post or field note visually.
---

# Social image

You produce on-brand social images for nicalpi.com using the v3 template
system — never a from-scratch design. Full reference: `docs/guide.md` §1–2
and `assets/social-templates/README.md`.

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
python3 scripts/generate-og.py <slug> [...]   # regenerate specific cards
python3 scripts/generate-og.py --check        # every page has a card
```

Slug = the `og_image` filename. If a new page lacks `og_image`, add
`og_image: /assets/images/og/<slug>.jpg` to its front matter first. Field
note cards pull their stats column from `home:`-flagged `metrics` (or
`facts`); if the card looks stale, update the front matter numbers and
regenerate.

## 3. Hand-edited promo cards

1. Copy the text into the template (edit the HTML in place — every block is
   plain markup). Keep the frame: header strip / footer rule, lowercase
   `nicalpi` wordmark, metrics as `before → now` with "now" in accent.
2. Writing for cards: one idea per card; quotes come from the actual post or
   note (never invent); verdicts are one word; every card carries
   `nicalpi.com`.
3. Export:
   ```bash
   node scripts/export-social.mjs <template-name>     # light + dark, 2×
   ```
   or preview in a browser (`?theme=dark` for dark) and screenshot at exact
   size.

## 4. On Claude Web (no repo)

Build the card as a **self-contained HTML artifact** at the exact pixel
size, using these tokens (light): canvas `#E4E2DC` · panel `#FCFCFA` · raise
`#F5F3ED` · ink `#191917` · body `#4A4A45` · muted `#77776E` · faint
`#C4C2B8` · line `#E4E2DA` · accent `#1E4FD8` · accent-soft `#EAF0FE` ·
on-accent `#FFFFFF`. Dark: canvas `#0C0E11` · panel `#171A1F` · ink
`#F1F1ED` · body `#BFC2BE` · muted `#8B8F96` · faint `#4B505A` · line
`#272B32` · accent `#82A9FF` · accent-soft `#182339` · on-accent `#0C0E11`.
Font: JetBrains Mono (400/700, Google Fonts). Reproduce the template
layouts (blue header strip, `# ` faint mark before headlines, footer rule),
then tell Nic to screenshot it at 100% or paste the HTML into
`assets/social-templates/` and export properly later.

## Judgment

- OG jpgs are generated artefacts: never hand-edit them, never design a
  bespoke one-off when a template fits.
- The verdict card is the only solid-accent surface — closing experiments
  only.
- If asked for a card for content that doesn't exist yet, say so and point
  at the think/write skills first.
