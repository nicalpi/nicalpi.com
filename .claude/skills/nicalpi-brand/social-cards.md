# NicAlpi v3 Social Cards

The canonical templates live in `assets/social-templates/` — self-contained
HTML files sharing the site tokens via `social.css`. Don't rebuild cards from
scratch; copy a template and edit the text.

| Template | Size | Use |
|---|---|---|
| `og-field-note.html` | 1200×630 | Field-note link card (OG/LinkedIn/X): accent header strip, `#` headline, metrics column |
| `quote-square.html` | 1080×1080 | Quote card: accent-ruled blockquote, exp footer |
| `verdict-square.html` | 1080×1080 | Experiment-close card: solid accent, one-word verdict, 2-stat grid |
| `post-promo-portrait.html` | 1080×1350 | Post promo: cover, category tag, `#` title, pull quote |
| `newsletter-og.html` | 1200×630 | Subscribe card on `--raise` |

## Rules

- JetBrains Mono only. Faint `# ` mark before headlines.
- Wordmark is lowercase `nicalpi`, 700, no coloured letters.
- Metrics read `before → now`: before in ink, arrow in `--faint`, now in accent.
- The verdict card is the only solid-accent surface. Verdicts are one word.
- Every card carries `nicalpi.com` (or `nicalpi.com / field notes`).
- Dark variants: append `?theme=dark` when previewing/exporting.

## Export

```bash
npm i -D playwright && npx playwright install chromium   # once
node scripts/export-social.mjs                           # all cards, both themes, 2×
node scripts/export-social.mjs quote-square              # one card
```

Output: `assets/images/social/<name>[-dark].png`.

## Legacy

The old OG sources in `assets/images/og/*.html` and per-post folders
(`assets/images/ai-code-explain/` …) predate v3 (sage/DM Sans era and the v2
blue). Regenerate from the v3 templates when a post's card is next needed;
don't copy their styles.
