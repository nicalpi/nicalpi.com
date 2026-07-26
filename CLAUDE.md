# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- `bundle install` — install Ruby dependencies
- `yarn install` — install node dependencies (Tailwind)
- `yarn css` — compile CSS (`_assets/main.css` → `assets/main.css`, minified). **Run after any CSS/template class change**; the compiled file is committed.
- `yarn css:watch` — recompile CSS on change during development
- `bundle exec jekyll serve` — local dev server (http://localhost:4000)
- `bundle exec jekyll build` — build to `_site/`

CSS is compiled by the Tailwind CLI, not a Jekyll plugin. (jekyll-postcss was
removed: it talks to a hardcoded localhost:8124 compile server, which breaks
with parallel checkouts and caused stale-CSS bugs.)

## Architecture

Jekyll 4.4. Brand: **NicAlpi v3 "Field Notes"** — JetBrains Mono, warm paper
palette, blue accent, light/dark themes via CSS variables and `data-theme` on
`<html>`. See `.claude/skills/nicalpi-brand/` for the full system and
`/styleguide/` for live components.

- `_assets/main.css` — token + component CSS **source** (edit this, then `yarn css`)
- `assets/main.css` — compiled output (committed, don't hand-edit)
- `tailwind.config.js` — maps Tailwind colours to the CSS variables
- `assets/js/site.js` — theme toggle (⌥T), mobile contents drawer
- `_layouts/` — `default` (shell), `post`, `field_note` (experiment brief), `progress_note`
- `_includes/` — `nav-top`, `sidebar` (desktop column / mobile drawer, parameterised by `context`), `mobile-bar`, `newsletter`, `footer`, `lightbox`, and `fn/*` field-note components (metrics, checklist, field-log, exp-card, xcard, follow-cta, meta-block)
- `_posts/` — blog posts (`YYYY-MM-DD-title.md`, permalink `/blog/:slug`)
- `_field_notes/` — the experiments collection (see below)
- `_data/field_notes.yml` — queued experiments
- `assets/social-templates/` — social image templates: OG generator templates (filled by `scripts/generate-og.py` → `assets/images/og/*.jpg`) + hand-edited promo cards (exported with `scripts/export-social.mjs`). See its README.
- `styleguide.html` → `/styleguide/` — living component reference (noindex)

## Field notes collection

Two document kinds, both in `_field_notes/`:

- **Experiment brief** — `_field_notes/exp-NN.md`, `kind: experiment`, URL `/field-notes/exp-NN/`
- **Progress note** — `_field_notes/exp-NN/<slug>.md`, `kind: progress`, `layout: progress_note`, URL `/field-notes/exp-NN/<slug>/`

Full front-matter schema and authoring guide: `_field_notes/README.md`.
Structured blocks (metrics, guardrails, field log) are front-matter data
rendered with `{% include fn/... %}` inside the markdown body, so section
order is free and every `##` heading lands in the sidebar "on this page" list.

`future: true` is set in `_config.yml` because launch content is dated ahead.

## Creating Posts

`_posts/YYYY-MM-DD-title.md` with front matter:

```yaml
---
layout: post
title: "Post Title"
subtitle: "Optional dek shown under the title"
description: "SEO + list description"
category: AI            # one of: AI, Business, Career, Leadership, Personal
reading_time: 9
date: YYYY-MM-DD
og_image: /assets/images/og/slug.jpg
---
```

Optional: `cover_image`, `cover_caption`, `short_title` (sidebar label).
Don't use `title_html` (retired with the v2 brand).

After creating a post (or field note), generate its OG image:
`python3 scripts/generate-og.py <slug>` (slug = the `og_image` filename).
Twitter reuses the OG image — no `-twitter` variants.

## Notes

- The site renders inside a 1280px panel; inner pages have a sidebar that
  becomes a contents drawer under 900px.
- Portrait/photo slots on home + about read `site.portrait_image` from
  `_config.yml`; until it's set they show an on-brand placeholder.
- `node_modules/` is committed (pre-existing choice); don't prune it in
  unrelated PRs.
