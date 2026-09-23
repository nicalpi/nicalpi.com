# NicAlpi — Style Reference
> a working CTO's notebook, rendered as markdown: mono chrome, serif reading, one graphite scale, and signal blue only where the markdown marks go.

**Version:** v4 "Graphite notebook" (13 Sep 2026)
**Theme:** light and dark, first-class
**Source of truth:** `_assets/main.css` (`:root` = light, `[data-theme="dark"]` = dark). Never hard-code hex in templates; outside the repo (mockups, artifacts, Claude Web) copy the token block below verbatim.

nicalpi.com is a personal site for Nic Alpi, CTO at Amba in Bristol, who writes in public about leading teams, AI without losing ownership, and useful work without another system. The design idea is **rendered markdown made literal**: the wordmark is `nicalpi.md`, the home hero and every post open with a `---` fenced front-matter block, post lists are a directory listing under an `ls -t _posts/` line, beliefs are `- [x]` items, the newsletter is a `> newsletter` band, prose quotes hang off a mono `>`, and the footer ends in `EOF`. One device per section, never two stacked.

Visually it borrows from precision developer tools (Expo, Linear, Vercel): a near-monochrome graphite scale on white, separation by tonal step and a single hairline rather than borders or shadows, pill-shaped controls, weight-first compact type. What keeps it Nic's: JetBrains Mono for everything that is chrome or heading, Source Serif 4 for everything you read at length, and the markdown devices above.

---

## Tokens — Colours

| Name | Light | Dark | Token | Role |
|------|-------|------|-------|------|
| Canvas | `#FFFFFF` | `#0F1114` | `--panel` (`--canvas` alias) | Page surface. Everything sits directly on it |
| Fog | `#F0F0F3` | `#1A1D22` | `--side` | The tonal step: front-matter block, newsletter band, code blocks, chip/nav hover, tag fills |
| Fog half-step | `#F7F7F9` | `#15181C` | `--raise` | Card and row hover |
| Mist | `#D9D9E0` | `#2A2E35` | `--line`, `--line2` | The one hairline: section rules, directory rows, outlined pills, card borders, image borders |
| Ink | `#1C2024` | `#F2F3F5` | `--ink` | Headings, strong text, the primary button fill, the verdict card |
| Body | `#2A2E34` | `#C9CCD2` | `--body` | Running serif text |
| Graphite | `#60646C` | `#8B8F98` | `--muted` | Meta, dates, nav links at rest, secondary copy, footer |
| Steel | `#80838D` | `#6B6F78` | `--faint` | Column labels, `EOF`, the `.md` in the wordmark, read-time, disabled. Decorative and labels only, never body copy |
| Deep signal | `#0072DE` | `#6DB8FF` | `--accent` | Text links, directory category word, "now" in metrics, running state, kickers. AA on white |
| Signal blue | `#0090FF` | `#3DA5FF` | `--mark` | The markdown marks only: `#`/`##`, `---` fences, `- [x]`, `>` kickers, the `→` in metrics. Never text, never a fill |
| Accent soft | `#EAF4FF` | `#14233A` | `--accent-soft` | Tint surfaces: contact email band, accent tags |
| Accent line | `#B9DBFF` | `#2B4A73` | `--accent-line` | At-rest link underline, borders on tinted surfaces |
| On ink / on accent | `#FFFFFF` | `#0F1114` | `--on-ink`, `--on-accent` | Text on ink or accent fills |

**Rules.** Two blues, two jobs: `--accent` is for things you click or read, `--mark` is punctuation. Blue is never a button fill. Ink is the only colour allowed to fill a whole control. Tinted surfaces (fog, accent-soft) carry no border. There are no shadows, gradients or blur.

## Tokens — Typography

### JetBrains Mono — chrome and headings · `--font-mono`
- **Weights:** 400 (marks, meta), 500 (nav, tags, chips, column labels), 600 (buttons, section titles, prose h2–h4), 700 (page and post titles, wordmark)
- **Tracking:** `-0.012em` on everything mono; titles tighten to `-0.02em`
- **Used for:** wordmark, top bar, every heading, front-matter blocks, directory rows, buttons, chips, kickers, footer, code, all social images and illustrations (images are mono-only)
- **Substitute:** `ui-monospace, SFMono-Regular, Menlo, monospace`

### Source Serif 4 — reading · `--font-serif`
- **Weights:** 400, 600 (`strong`), 400 italic (quotes); optical sizes on
- **Used for:** post prose, leads, deks, beliefs, directory titles (600), form help. Never in headings, never in images
- **Substitute:** `Georgia, 'Times New Roman', serif`
- Default font smoothing (no `antialiased`): the thin rendering washed the serif out on Mac

### Type scale

| Role | Face / weight | Size / line | Notes |
|------|---------------|-------------|-------|
| Hero title (home) | Mono 700 | 38px / 1.18 | `-0.02em`; the first thing on the page; 28px on phones, `<br>` dropped |
| Post title (h1) | Mono 700 | 32px / 1.22 | `# ` mark in `--mark`; 26px on phones |
| Post dek | Serif 400 | 20px / 1.55 | `--muted`, the post `subtitle`; 44px below; 17px on phones |
| Page title (writing, about, 404) | Mono 700 | 26px / 1.3 | |
| Section title (h2 in layouts) | Mono 600 | 16px / 1.4 | `## ` mark |
| Prose h2 | Mono 600 | 1.1em / 1.4 | hairline below, `0.4em` padding |
| Prose h3 / h4 | Mono 600 | 1em / 0.95em | |
| Body / prose | Serif 400 | 18px / 1.75 | 17px / 1.7 on phones |
| Hero lead | Serif 400 | 19px / 1.65 | `--body` |
| Section lead | Serif 400 | 17px / 1.7 | `--muted` |
| Beliefs | Serif 400 | 17px / 1.7 | `- [x]` mono 13px in `--mark` |
| Quote (prose blockquote) | Serif 400 italic | 1.05em / 1.6 | mono `>` hanging left in `--mark`, no bar |
| Directory title | Serif 600 | 17.5px / 1.4 | the one serif in a row of mono columns; 17px on phones |
| Directory meta, nav, meta lines | Mono 400–500 | 13px | |
| Front-matter block | Mono 400 | 13.5px / 1.85 | keys `--muted`, values `--ink`, fences `--mark` |
| Kickers, column labels | Mono 500 | 11px, uppercase, `0.08em` | `--faint` |
| Footer, fine print | Mono 400 | 11.5–12px | `--muted` |

Hierarchy comes from weight and face before size. The scale is deliberately compact: only the hero (38px) and post title (32px) go above 30px.

## Tokens — Spacing & Shapes

**Base unit:** 4px. **Density:** comfortable in reading, compact in chrome.

| Name | Value | Use |
|------|-------|-----|
| section gap | 40px | padding above and below each `.sheet-section` |
| sheet padding | 32px top · 72px sides · 56px bottom | 40px sides under 1080px, 20px on phones |
| card padding | 16–20px | front-matter block 16×20, xcard 16×18 |
| newsletter padding | 28×32px | |
| element gap | 8px | between buttons, chips, form controls |
| row padding | 13px | directory rows |

### Radii

| Element | Radius |
|---------|--------|
| Buttons, inputs | 36px (pill) |
| Nav link chips, article-foot links | 24px |
| Filter chips, tags, theme toggle | 9999px |
| Front-matter block, cards, code blocks, images, offers | 12px |
| Newsletter band, email band | 16–20px |
| Inline code | 6px |
| Focus ring | 2px accent outline, 2px offset |

Nothing interactive has a sharp corner. Nothing structural has a shadow.

### Layout

- **Frame:** sticky, borderless 64px top bar → centred 1024px `<main class="sheet">` (880px inner) → one-line footer above a hairline. One surface, no canvas behind the page.
- **Home and list pages span the sheet.** Titles, cards, list rows and the newsletter run the full 880px.
- **Posts read in a centred column.** `--measure: 700px` (~75 characters at 18px) caps the path line, fm, h1, dek, prose, article foot and prev/next cards, centred in the sheet; wide `pre` and tables may break out. Full-width posts (13–23 Sep 2026) ran ~100 characters a line.
- **Two-column moments above 800px:** beliefs (intro left 0.8fr and sticky under the top bar, list right 1.2fr, 48px gap) and the newsletter (copy left, 380–400px form right).
- **Phone (≤640px):** 56px top bar with four chips and the theme toggle, 20px side padding, directory rows stack (date · read / title / category), buttons go full-width, hero `<br>` removed.

---

## Components

### Top bar
64px, no border, sits on the canvas. Wordmark `nicalpi` mono 700 15px with `.md` in `--faint` (hidden on phones). Right cluster: `writing · about · work with me` as nav chips, then the theme toggle. Gap between chips 4px.

### Nav link chip
Mono 500 13px `--muted`, padding 7×12px, radius 24px. Hover and `aria-current="page"`: fog background, ink text. No underline anywhere in the bar.

### Theme toggle
32px pill, 1px mist border, sun icon 12px + "light"/"dark" label (label hidden ≤440px). Hover: fog fill, ink text. Shortcut ⌥T.

### Front-matter block `.fm`
The signature device. Fog fill, 12px radius, no border, mono 13.5px/1.85. `---` fences in `--mark`, keys `--muted`, values `--ink`, linked values `--accent`. On the home page it is the credentials card under the headline, lead and buttons (the claim comes first). On posts `.fm-post` is unfilled and metadata only (category, date, reading_time) under a `_posts/<file>.md` path line, 28px above the h1: title and subtitle render once, as the h1 and dek, never repeated in the block.

### Primary button `.btn`
40px pill (44px on phones), ink fill, `--on-ink` text, mono 600 13px, padding 0×18px, optional trailing `→`. Hover: 0.9 opacity. The only surface ink fills entirely.

### Ghost button `.btn-ghost`
Transparent, no border, `--muted` text. Hover: fog fill, ink text. Pairs with the primary. Home hero: primary "Start reading →", ghost "Get new posts by email" (the newsletter band lower down is the main signup).

### Outline button `.btn-outline`
Transparent, 1px mist border, ink text. Used when a secondary action needs an edge (stacked phone CTAs).

### Filter chip `.chip`
30px pill, 1px mist border, mono 500 12.5px `--muted`, padding 0×13px. Active `.chip-solid`: ink fill, `--on-ink` text. Hover: fog fill.

### Directory listing `.dir-row`
Grid `96px 88px 1fr 56px`, 20px gaps, 13px padding, mist hairline below. Column labels (`.dir-head`) mono 11px uppercase `--faint`. Date `--muted`, **category a plain lowercase word in `--accent`** (not a pill), title **Source Serif 600 17.5px** ink (the columns stay mono so the row still reads as `ls`), read-time `--faint` right-aligned. Hover: title turns `--accent`, no underline, no arrow. Header line: `ls -t _posts/ · N files` in `--faint`.

### Section head
`## Title` mono 600 16px with the mark in `--mark`, a mono 12px `--faint` command on the right (`ls -t _posts/ · 9 files`), baseline aligned.

### Beliefs
Serif 17px/1.7 `--body`, `strong` 600 ink; each item prefixed by a mono `- [x]` 13px in `--mark`, 52px hanging indent, 10px row gap.

### Newsletter band
Fog card, 20px radius, no border, 28×32px padding. `> newsletter` kicker mono 12.5px in `--mark`, section title, serif lead in `--body`, 40px pill input (mist border, canvas fill) + ink pill button, fine print mono 11.5px `--muted`. Two-column above 800px.

### Cross-link card `.xcard`
Prev/next. 1px mist border, 12px radius, 16×18px padding, kicker mono 11.5px `--muted`, title mono 600 14px. Hover: `--raise` fill.

### Prose
Serif 18px/1.75 `--body`. Headings mono 600 with `##`/`###` marks in `--mark`; h2 has a hairline below. Links `--accent` with a hairline underline in `--accent-line` at rest, full accent on hover. Blockquote italic, `>` mark hanging left, no bar. Inline code fog fill 6px radius; `pre` fog fill 12px radius no border; images 1px mist border 12px radius; tables hairline heads; `hr` solid mist. GFM task lists render as `- [ ]`/`- [x]` text with the checked mark in `--mark`.

### Footer
One line, mist hairline above, mono 12px `--muted`: © left, `writing · about · linkedin · twitter/x · rss` right, ending in `EOF` in `--faint`.

### Field-note components (paused, `_includes/fn/`)
Metrics table (`before → now → target`, arrow in `--mark`, now in `--accent`), checklist (`- [ ]`/`- [x]`), field log, experiment card (12px), meta block (mist rules), progress bar (3px). All token-driven; nothing to restyle when the lab returns.

---

## Do's and Don'ts

### Do
- Keep every interactive element a pill: 36px on buttons and inputs, 24px on nav chips, 9999px on tags and toggles.
- Use fog (`--side`) as the surface step. Fog surfaces have no border and 12–20px corners.
- Use one hairline colour (`--line`) for every rule, row divider and outlined edge.
- Reserve `--mark` for markdown punctuation and `--accent` for links and the running state. Two blues, two jobs.
- Fill only with ink: the primary button, the active filter chip, the verdict card.
- Let weight carry hierarchy (mono 600/700 over serif 400) before reaching for size.
- Apply `-0.012em` tracking to all mono; leave the serif alone.
- Keep the markdown joke light: one device per section, never two in one block.
- Keep images mono-only and built from these tokens; no stock or AI photography.

### Don't
- Don't use blue as a button or card fill. Blue punctuates, it never dominates.
- Don't add shadows, gradients, blur or a canvas behind the sheet.
- Don't put a border on a tinted surface, or a left accent bar on a rounded box.
- Don't turn the directory category into a pill. It is a word in `--accent`.
- Don't use `--faint` for copy anyone must read.
- Don't exceed 30px for any chrome type (hero 38px and post h1 32px are the only titles above it) or drop body copy under 17px.
- Don't repeat the post title or subtitle inside the post front-matter block.
- Don't reintroduce the warm paper palette (v3) or the sidebar, drawer and breadcrumbs (v2).
- Don't use a third typeface. Inter, DM Sans and Caveat are all retired.

## Surfaces

| Level | Name | Light | Dark | Purpose |
|-------|------|-------|------|---------|
| 0 | Canvas | `#FFFFFF` | `#0F1114` | Page and card surface |
| 1 | Fog | `#F0F0F3` | `#1A1D22` | Front matter, newsletter, code, hover |
| 1½ | Fog half-step | `#F7F7F9` | `#15181C` | Card/row hover |
| 2 | Mist hairline | `#D9D9E0` | `#2A2E35` | Every rule and outlined edge |
| solid | Ink | `#1C2024` | `#F2F3F5` | Primary button, active chip, verdict card |

## Elevation

None. Depth is a tonal step (canvas → fog) or a hairline. Nothing floats; the page reads like a printed notebook, not a layered app.

## Imagery

No photography, no illustration in the drawn sense, no emoji. Every image is HTML built from these tokens and rendered with Playwright: OG cards from front matter (`scripts/generate-og.py`), promo cards from `assets/social-templates/`, inline post illustrations rendered with `scripts/render-illustration.py`. Images are **mono-only** (Source Serif 4 never appears in an image), carry the wordmark `nicalpi.md` and `nicalpi.com`, use the same devices (a `# ` mark before headlines, `---` front matter, `>` quotes, `before → now` metrics with the arrow in `--mark` and now in `--accent`), and never a blue fill. The verdict card is the one solid surface and it is ink. Icons, where needed, are 1.5px stroke SVG in `--muted` or `--ink`. Client logos render greyscale at 0.75 opacity (inverted in dark).

## Voice in the UI

Lowercase for nav, labels, kickers and meta (`writing`, `work with me`, `> newsletter`). Sentence case for headings and copy. British English. No exclamation marks. Verdicts are one word: kept / dropped / inconclusive. Full writing guide: `.claude/skills/nicalpi-brand/voice.md`.

## Accessibility

WCAG AA on white: ink 16.1:1, body 13.4:1, graphite 5.7:1, deep signal 4.9:1. Steel (3.4:1) is for labels and decoration only. Focus is a 2px accent outline. `prefers-reduced-motion` kills the one animation (the retired link arrow). Theme is set pre-paint from `localStorage` then `prefers-color-scheme`.

---

## Agent prompt guide

**Quick colour reference (light)**
- text: `#1C2024` · body: `#2A2E34` · muted: `#60646C` · label: `#80838D`
- background: `#FFFFFF` · surface step: `#F0F0F3` · hairline: `#D9D9E0`
- link / running: `#0072DE` · markdown mark: `#0090FF`
- primary action: ink `#1C2024` fill, white text, 36px pill. Never blue.

**Example component prompts**
1. A primary button: `#1C2024` fill, white text, JetBrains Mono 600 13px, 40px tall, 0×18px padding, 36px radius, trailing `→`.
2. A nav chip: JetBrains Mono 500 13px `#60646C`, 7×12px padding, 24px radius; active state `#F0F0F3` fill and `#1C2024` text.
3. A front-matter block: `#F0F0F3` fill, 12px radius, no border, JetBrains Mono 13.5px/1.85, `---` lines in `#0090FF`, keys `#60646C`, values `#1C2024`.
4. A directory row: grid `96px 88px 1fr 56px`, 20px gaps, 13px vertical padding, 1px `#D9D9E0` rule below; date `#60646C` mono 13px, category lowercase `#0072DE` mono, title Source Serif 4 600 17.5px `#1C2024`, read-time `#80838D` mono right.
5. A post page: a centred 700px column. `_posts/<file>.md` path in Mono 12px `#60646C`, an unfilled front-matter block with one meta line (category, date, reading_time), 28px, `# Title` Mono 700 32px with the mark in `#0090FF`, dek Source Serif 4 20px `#60646C`, 44px, prose Source Serif 4 18px/1.75 `#2A2E34`, h2 Mono 600 1.1em with a `#D9D9E0` rule below.
6. An OG card 1200×630: white card with 1px `#D9D9E0` frame, 56×64px padding, `nicalpi.md` top-left, category as an outlined pill top-right, `# Title` Mono 700 54px, dek Mono 22px `#2A2E34`, hairline footer `Nic Alpi · CTO, Bristol` / `nicalpi.com`.

## Similar brands
- **Expo** — the graphite scale, pill radii, borderless top bar and ink-filled CTA were adopted from its system in Sep 2026.
- **Linear / Vercel** — same monochrome-first restraint and single accent used sparingly.
- Where NicAlpi departs: a serif for reading, mono everywhere else, and the literal-markdown devices.

## Quick start

### CSS custom properties

```css
:root {
  --canvas: #FFFFFF; --panel: #FFFFFF; --side: #F0F0F3; --raise: #F7F7F9;
  --ink: #1C2024; --body: #2A2E34; --muted: #60646C; --faint: #80838D;
  --line: #D9D9E0; --line2: #D9D9E0;
  --accent: #0072DE; --mark: #0090FF;
  --accent-soft: #EAF4FF; --accent-line: #B9DBFF;
  --on-accent: #FFFFFF; --on-ink: #FFFFFF;
  color-scheme: light;
}
[data-theme="dark"] {
  --canvas: #0F1114; --panel: #0F1114; --side: #1A1D22; --raise: #15181C;
  --ink: #F2F3F5; --body: #C9CCD2; --muted: #8B8F98; --faint: #6B6F78;
  --line: #2A2E35; --line2: #2A2E35;
  --accent: #6DB8FF; --mark: #3DA5FF;
  --accent-soft: #14233A; --accent-line: #2B4A73;
  --on-accent: #0F1114; --on-ink: #0F1114;
  color-scheme: dark;
}

/* Type */
--font-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;   /* letter-spacing: -0.012em */
--font-serif: 'Source Serif 4', Georgia, 'Times New Roman', serif;

/* Radii */
--radius-pill: 36px;     /* buttons, inputs */
--radius-nav: 24px;      /* nav chips */
--radius-full: 9999px;   /* tags, filter chips, theme toggle */
--radius-card: 12px;     /* fm block, cards, code, images */
--radius-band: 20px;     /* newsletter */
```

Google Fonts: `Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400` and `JetBrains+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400`.

### Where things live

| Thing | Path |
|---|---|
| Tokens + component CSS (source) | `_assets/main.css` → `yarn css` → `assets/main.css` (committed) |
| Tailwind token mapping | `tailwind.config.js` (`text-ink`, `bg-side`, `border-line`, `text-accent`, `text-mark`, `rounded-brand` = 12px) |
| Live components | `/styleguide/` (`styleguide.html`) |
| Brand skill (rules, components, voice, social cards) | `.claude/skills/nicalpi-brand/` |
| Social templates + shared `social.css` | `assets/social-templates/` |
| OG generator / illustration renderer | `scripts/generate-og.py`, `scripts/render-illustration.py` (`/opt/homebrew/bin/python3.13`) |
| Design canvas (the chosen direction + rejected blends) | https://claude.ai/code/artifact/45b46ca1-4d7c-467b-bb94-47a0f0a77edf |

**History.** v1 (2022) default theme · v2 "Calm CTO" (DM Sans + Caveat, sage green, sidebar) · v3 "Field Notes" (Jul 2026: mono + warm paper; Sep 2026: single sheet, Source Serif 4, front-matter direction) · **v4 "Graphite notebook"** (13 Sep 2026: this document).
