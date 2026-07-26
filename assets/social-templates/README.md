# Social image templates — NicAlpi v3

Five HTML templates matching the site brand (JetBrains Mono, paper palette,
blue accent). Same tokens as `assets/main.css`, defined in `social.css`.

| Template | Size | Use |
|---|---|---|
| `og-field-note.html` | 1200×630 | Link card for a field note (OG, LinkedIn, X) — headline + live metrics column |
| `quote-square.html` | 1080×1080 | Quote card (Instagram, LinkedIn square) |
| `verdict-square.html` | 1080×1080 | Solid-accent card for when an experiment closes |
| `post-promo-portrait.html` | 1080×1350 | Blog post promo for portrait feeds (cover + title + pull quote) |
| `newsletter-og.html` | 1200×630 | Newsletter / subscribe card |

## Editing

Open the HTML file and edit the text in place — every block is plain markup.
Preview in a browser. Add `?theme=dark` to the URL for the dark variant.

## Exporting

```bash
npm i -D playwright && npx playwright install chromium   # once
node scripts/export-social.mjs                           # all templates, both themes, 2×
node scripts/export-social.mjs og-field-note             # a single template
```

PNGs land in `assets/images/social/`. Alternatively, one-off at 1×:

```bash
npx -y playwright screenshot --viewport-size="1200,630" \
  "assets/social-templates/og-field-note.html" og.png
```

## Conventions

- Keep the header strip / footer rule structure — that's the brand's frame.
- Metrics always read `before → now` with the "now" in accent.
- The verdict card is the only solid-accent surface; use it sparingly.
- Export at 2× (the script default) for retina-crisp uploads.
