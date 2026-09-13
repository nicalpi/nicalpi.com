---
name: nicalpi-brand
description: Apply the NicAlpi personal brand system for Nic Alpi (nicalpi.com). Use this skill whenever generating visual assets (social cards, blog headers, quote images, diagrams), writing or reviewing web code (HTML, CSS, Jekyll, Tailwind), writing or editing any content in Nic's voice (posts, field notes, newsletters, social copy, bios), or when asked about NicAlpi's design system, colour palette, typography, or voice. Trigger on any mention of: NicAlpi, nicalpi.com, the brand, brand guidelines, blog styling, social card, quote card, header image, field notes, "on-brand", or "in Nic's voice". Also trigger when writing CSS variables or design tokens for Nic's projects.
---

# NicAlpi Brand System — v4 "Graphite notebook"

> **v4 (13 Sep 2026).** The Field Notes devices below are unchanged, but the
> palette and shapes moved after a side-by-side with Expo's design system:
> a cool graphite neutral scale replaces warm paper; every control is a
> pill (buttons/inputs 36px, nav chips 24px, tags 9999px), content cards and
> the fm block are 12px, the newsletter 20px; the primary button is
> ink-filled (blue is never a button fill); tinted surfaces have no border
> and there is one hairline colour; two blues — `--accent #0072DE` for text
> links and running state, `--mark #0090FF` rationed to `#`/`##` marks,
> `---` fences, `- [x]` and `>` kickers. Mono carries -0.012em tracking.
> Weight (600 mono vs 400 serif) does hierarchy; sizes are compact (hero
> 30px, post h1 28px, page h1 26px, section h2 16px/600, prose 18px/1.75,
> prose h2 1.1em/600 with a hairline). Current tokens: see the table below
> (v4 column) and `_assets/main.css`. Where the older prose in this file
> says 4px radius, warm paper, or `#1E4FD8`, read the v4 values instead.

| Token | v4 light | v4 dark | Use |
|-------|---------|---------|-----|
| `--panel` / `--canvas` | `#FFFFFF` | `#0F1114` | page surface |
| `--side` | `#F0F0F3` | `#1A1D22` | fog: fm block, newsletter, code, chip hover |
| `--raise` | `#F7F7F9` | `#15181C` | card/row hover |
| `--ink` | `#1C2024` | `#F2F3F5` | headings, strong, primary button fill |
| `--body` | `#2A2E34` | `#C9CCD2` | body text |
| `--muted` | `#60646C` | `#8B8F98` | graphite: meta, nav at rest |
| `--faint` | `#80838D` | `#6B6F78` | steel: column labels, EOF, `.md` |
| `--line` / `--line2` | `#D9D9E0` | `#2A2E35` | the one hairline |
| `--accent` | `#0072DE` | `#6DB8FF` | text links, running state |
| `--mark` | `#0090FF` | `#3DA5FF` | markdown marks, fences, checkboxes, kickers |
| `--accent-soft` / `--accent-line` | `#EAF4FF` / `#B9DBFF` | `#14233A` / `#2B4A73` | tint surfaces, at-rest underlines |
| `--on-ink` / `--on-accent` | `#FFFFFF` | `#0F1114` | text on ink / accent |

---

## v3 "Field Notes" reference (devices still current; palette and radii superseded above)

Personal brand for Nic Alpi — CTO at an age-tech company in Bristol, UK.
Sold his 20-person Rails consultancy (CookiesHQ) in 2021. HYROX athlete,
three kids, hard 4pm stop. Writes in public.

**Core positioning:** the public CTO lab. "Change one thing. Measure it.
Publish the result." Honest, measured, anti-performative. Field notes are
experiments (baseline → protocol → guardrails → verdict), not essays.
Verdicts get published even when the answer is "this did nothing".

**Art direction:** rendered markdown. Faint `#`/`##` marks before headings,
`- [ ]` / `- [x]` checklists kept as text, monospace everything, thin rules,
one blue accent, warm paper surfaces. Light and dark themes are first-class.

**Companion docs in this skill:**
- `voice.md` — how Nic writes: register, sentence rules, vocabulary, AI-tells to avoid. Read it before writing any prose as Nic.
- `components.md` — every site component with markup (repo work).
- `social-cards.md` — OG images and promo card templates.

---

## Design tokens

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--canvas` | `#E4E2DC` | `#0C0E11` | page surround, outside the frame |
| `--panel` | `#FCFCFA` | `#171A1F` | main page surface |
| `--side` | `#F5F3ED` | `#13161A` | sidebar surface |
| `--raise` | `#F9F8F4` | `#1D2127` | raised bands, table heads |
| `--ink` | `#191917` | `#F1F1ED` | headings, strong text |
| `--body` | `#4A4A45` | `#BFC2BE` | body text |
| `--muted` | `#77776E` | `#8B8F96` | meta, secondary |
| `--faint` | `#C4C2B8` | `#4B505A` | md marks, big numbers — decorative only |
| `--line` | `#E4E2DA` | `#272B32` | primary borders |
| `--line2` | `#EDEBE4` | `#1F232A` | subtle row dividers |
| `--accent` | `#1E4FD8` | `#82A9FF` | links, running state, CTAs |
| `--accent-soft` | `#EAF0FE` | `#182339` | accent tint surfaces |
| `--accent-line` | `#BDCDF5` | `#2E4368` | borders on accent surfaces, at-rest link underlines |
| `--on-accent` | `#FFFFFF` | `#0C0E11` | text on accent |

**Fonts (since 13 Sep 2026):** two faces, clearly split by role.
- **JetBrains Mono** — 400/500/700 — every heading, the wordmark, nav, meta
  lines, kickers, chips, buttons, footer, code, front-matter blocks,
  directory rows, and the `#`/`##` marks (in the accent). All images and
  social cards stay mono-only.
- **Source Serif 4** — 400/600 + italic, optical sizes — running text
  only: post prose at 19.5px/1.7 full width, leads, beliefs, form help.
  `strong` is 600. Never in headings, never in images. Body ink is
  `#33332E` light / `#CFD2CE` dark. Default font smoothing (no
  `antialiased`).
- In prose, headings are em-based so they keep rank over the serif: h2 is
  1.32em with a hairline below, h3 1.12em, h4 1em; every level's mark is
  in the accent.
History: mono everywhere at the v3 launch read as friction in long posts;
IBM Plex Sans (Sep 2026) tested worse for Nic when tuned heavier, and the
serifs won a side-by-side lab — Source Serif 4 first, Spectral a close
second (20.5px). v2's DM Sans and Caveat stay retired.

**Layout (since Sep 2026):** one sticky top bar (wordmark · writing ·
about · work with me · theme), then a centred 1024px `.sheet`, then a
one-line footer — all on the panel surface; the canvas token is no longer
shown behind the page (Nic found the grey surround flat). Blocks use the
sheet's 880px inner width; running text caps at `--measure` (640px): prose
18px/1.7 Plex, about 78 characters a line; `strong` 600; the quotable
blockquote 18.5px 600 with a 3px accent bar. Code, images and tables run
the full column. Above 800px the beliefs block is intro-left/list-right
and the newsletter is copy-left/form-right. No sidebar, no drawer, no
breadcrumbs. Field notes are paused (`output: false`); their layouts and
`fn/` components stay in the repo for when the lab returns.

**Signature devices (direction "Front matter", 13 Sep 2026).** The
rendered-markdown idea is now literal — one device per section, never two
stacked: wordmark `nicalpi.md` (`.md` in `--faint`); a `---` fenced
front-matter block (`.fm`: `--side` fill, hairline, mono 14px, fences in
the accent, keys muted, values ink) opens the home hero and every post —
the post block is built from real front matter under a `_posts/<file>.md`
path line; post lists are a directory listing (date · category · title ·
read, mono, uppercase column labels, an `ls -t _posts/ · N files` line);
belief lists use `- [x]` in the accent; the newsletter is a `> newsletter`
band (`accent-soft` fill, 3px accent left bar, square left edge) — still
the one tinted surface; prose blockquotes carry a mono `> `; the footer
ends in a faint `EOF`. Same devices, same restraint, in images and social
cards.

In the repo, tokens live in `_assets/main.css` (`:root` = light,
`[data-theme="dark"]` = dark); Tailwind maps them in `tailwind.config.js`
(`text-ink`, `bg-panel`, `border-line`, `text-accent`, `bg-accent-soft`,
`border-accent-line`, `rounded-brand` = 4px …). Never hard-code hex values
in templates — outside the repo (mockups, artifacts), copy the token block
verbatim.

## Theming

- `data-theme` on `<html>`; set pre-paint by an inline script in
  `_includes/head.html` (localStorage → `prefers-color-scheme` fallback).
- `assets/js/site.js` handles the toggles (`[data-theme-toggle]`), the ⌥T
  shortcut, the mobile contents drawer, and the newsletter form.
- Because every colour is a token, components need zero dark-mode variants.

## Typography scale

| Role | Size / weight |
|---|---|
| Page title (h1) | 30px / 700, `letter-spacing:-0.02em`, faint `# ` mark (24px mobile) |
| Hero title (home) | 36px / 700 (25px mobile) |
| Section heading (h2) | 17px / 700, faint `## ` mark |
| Lead paragraph | 15px / 1.85 |
| Body prose | 14.5px / 1.9 (13.5px mobile) |
| Card titles | 15.5–21px / 700 |
| Meta, crumbs | 12–12.5px |
| Kickers | 11px, uppercase, `letter-spacing:0.12em` |
| Sidebar labels | 10.5px / 700, uppercase |

## Layout system

- The site is a **1280px panel** (`.site-frame`) centred on the warm canvas;
  full-bleed below 1280px.
- **Home** is full-width with a top nav (`nav-top.html`).
- **Inner pages** use a 248px sidebar (`sidebar.html`, `.with-sidebar` grid)
  with a breadcrumb bar (`.crumbs`) on the main column.
- Sidebar section order is fixed: context nav first ("on this page",
  experiment tree), then field notes, then **writing pinned to the bottom**
  (`mt-auto`) directly above the meta links (about / work with me / rss).
- Below 900px the sidebar becomes an off-canvas **contents drawer** (same
  markup) behind a burger button; inner pages get a sticky `mobile-bar.html`.
- Radius: 4px (`rounded-brand`) everywhere; 6px only on preview panels.
- Rules and borders do the structure; **no shadows**.

## Links (the affordance system)

- **Inline text links**: accent colour with a hairline underline in
  `--accent-line` at rest — that faint underline is the "this is a link"
  cue — strengthening to `--accent` on hover (1px, `text-underline-offset:
  4px`).
- **Block links** (list rows, cards): `.link-block` on the `<a>`,
  `.link-title` on the title. Only the title underlines on hover; an accent
  `→` after the title fades in with a slight bounce (`link-arrow-in`
  keyframes; space reserved so nothing reflows; disabled under reduced
  motion).
- Buttons, chips, sidebar links and cards never underline — they signal
  hover with border or colour shifts.
- Big cards that need to be obviously readable also carry an explicit
  accent text link, e.g. "read the full brief — question, protocol,
  guardrails →".

## Voice (summary — full guide in `voice.md`)

- Lowercase for nav, labels, meta ("field notes", "work with me").
  Sentence case for headings and body. No exclamation marks.
- First person, plain words, short paragraphs. British English.
- Numbers carry the story: `before → now` with "now" in accent.
- Verdicts are one word: kept / dropped / inconclusive.
- Honest hedges stay in ("small sample, read the direction, not the
  decimals"). No pretend certainty, no guru register.

## Accessibility

- WCAG AA: ink on panel 15.9:1, body 9.4:1, muted 4.6:1, accent on panel
  6.8:1 (light); equivalents hold in dark.
- `--faint` is decorative only (md marks, index numbers) — never for copy.
- Focus: 2px accent outline (`:focus-visible`). Reduced motion respected
  globally (kills the link-arrow bounce too).
- Drawer: `aria-expanded`, Escape closes, focus moves to the close button.

## Where things live (repo work)

| Thing | Path |
|---|---|
| Design tokens + component CSS (source) | `_assets/main.css` → compile with `yarn css` to `assets/main.css` (committed) |
| Tailwind token mapping | `tailwind.config.js` |
| Components (live examples) | `/styleguide/` (`styleguide.html`) |
| Component reference | `components.md` in this skill |
| Social image templates | `assets/social-templates/` + `social-cards.md` |
| Field notes authoring guide | `_field_notes/README.md` |
| Newsletter | Kit form 5638226; `_includes/newsletter.html` + `[data-newsletter-form]` handler in `site.js` (inline success, plain-POST fallback) |

**On Claude Web** (no repo): apply the tokens, type scale and voice directly;
output complete files or snippets and say what still needs doing in the repo
(compile CSS, generate OG image). Never claim files were created.
