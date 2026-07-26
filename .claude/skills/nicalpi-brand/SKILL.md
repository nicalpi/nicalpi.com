---
name: nicalpi-brand
description: Apply the NicAlpi personal brand system for Nic Alpi (nicalpi.com). Use this skill whenever generating visual assets (social cards, blog headers, quote images, diagrams), writing or reviewing web code (HTML, CSS, Jekyll, Tailwind), creating any on-brand content, or when asked about NicAlpi's design system, colour palette, typography, or voice. Trigger on any mention of: NicAlpi, nicalpi.com, the brand, brand guidelines, blog styling, social card, quote card, header image, field notes, or "on-brand". Also trigger when writing CSS variables or design tokens for Nic's projects.
---

# NicAlpi Brand System — v3 "Field Notes"

Personal brand for Nic Alpi — CTO, agency founder, HYROX athlete, writer.
Based in Bristol, UK.

**Core positioning:** the public CTO lab. "Change one thing. Measure it.
Publish the result." Honest, measured, anti-performative. Field notes are
experiments (baseline → protocol → guardrails → verdict), not essays.

**Art direction:** rendered markdown. Faint `#`/`##` marks before headings,
`- [ ]` / `- [x]` checklists kept as text, monospace everything, thin rules,
one blue accent. Light and dark themes are first-class.

---

## Quick Reference

| Token | Light | Dark |
|-------|-------|------|
| `--canvas` (page surround) | `#E4E2DC` | `#0C0E11` |
| `--panel` (page surface) | `#FCFCFA` | `#171A1F` |
| `--side` (sidebar) | `#F5F3ED` | `#13161A` |
| `--raise` (bands, table heads) | `#F9F8F4` | `#1D2127` |
| `--ink` (headings) | `#191917` | `#F1F1ED` |
| `--body` (body text) | `#4A4A45` | `#BFC2BE` |
| `--muted` (meta) | `#77776E` | `#8B8F96` |
| `--faint` (md marks, big numbers) | `#C4C2B8` | `#4B505A` |
| `--line` (borders) | `#E4E2DA` | `#272B32` |
| `--line2` (row dividers) | `#EDEBE4` | `#1F232A` |
| `--accent` | `#1E4FD8` | `#82A9FF` |
| `--accent-soft` (tints) | `#EAF0FE` | `#182339` |
| `--accent-line` (tint borders) | `#BDCDF5` | `#2E4368` |
| `--on-accent` | `#FFFFFF` | `#0C0E11` |

**Font:** JetBrains Mono only — 400 body, 500 medium, 700 bold. Loaded from
Google Fonts. No DM Sans, no Caveat (v2 is retired).

Tokens live in `_assets/main.css` (`:root` = light, `[data-theme="dark"]` =
dark). Tailwind maps them in `tailwind.config.js` (`text-ink`, `bg-panel`,
`border-line`, `text-accent`, `bg-accent-soft`, `border-accent-line`,
`rounded-brand` = 4px …). Never hard-code hex values in templates.

## Theming

- `data-theme` attribute on `<html>`; set pre-paint by an inline script in
  `_includes/head.html` (localStorage → `prefers-color-scheme` fallback).
- `assets/js/site.js` handles toggles (`[data-theme-toggle]`), the ⌥T
  shortcut, and the mobile contents drawer.
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
  with a breadcrumb bar (`.crumbs`) on top of the main column.
- Below 900px the sidebar becomes an off-canvas **contents drawer** (same
  markup) behind a burger button; inner pages get a sticky
  `mobile-bar.html` header.
- Radius: 4px (`rounded-brand`) everywhere; 6px only on preview panels.
- Rules and borders do the structure; shadows are not used.

## Voice

- Lowercase for nav, labels, meta ("field notes", "work with me").
- Sentence case for headings and body. No exclamation marks.
- Numbers carry the story: `before → now` with "now" in accent.
- Verdicts are one word: kept / dropped / inconclusive.
- Honest hedges stay in ("small sample, read the direction, not the decimals").

## Accessibility

- WCAG AA: ink on panel 15.9:1, body 9.4:1, muted 4.6:1, accent on panel 6.8:1
  (light); equivalents hold in dark.
- `--faint` is decorative only (md marks, big index numbers) — never for copy.
- Focus: 2px accent outline (`:focus-visible`). Reduced motion respected.
- Drawer: `aria-expanded`, Escape closes, focus moves to close button.

## Where things live

| Thing | Path |
|---|---|
| Design tokens + component CSS (source) | `_assets/main.css` → compiled by `yarn css` to `assets/main.css` |
| Tailwind token mapping | `tailwind.config.js` |
| Components (live examples) | `/styleguide/` (`styleguide.html`) |
| Component reference | `components.md` in this skill |
| Social image templates | `assets/social-templates/` + `social-cards.md` |
| Field notes authoring guide | `_field_notes/README.md` |
