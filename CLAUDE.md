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

Jekyll 4.4. Brand: **NicAlpi v3 "Field Notes"** — JetBrains Mono for
headings and chrome, IBM Plex Sans for body copy (since Sep 2026), warm paper
palette, blue accent, light/dark themes via CSS variables and `data-theme` on
`<html>`. See `.claude/skills/nicalpi-brand/` for the full system and
`/styleguide/` for live components.

**Layout (Sep 2026 simplification):** `_layouts/default.html` wraps every
page in one frame — sticky top bar (`nav-top`) → a centred 1024px
`<main class="sheet">` → one-line `footer`, all on a single panel surface
(no canvas). Blocks span the sheet's 880px inner width — titles, cards,
code, images, tables, list rows, the newsletter band — while running text
(`.prose > p/ul/ol/blockquote/h2…`) caps at `--measure` (640px; prose is
18px/1.7 IBM Plex Sans ≈ 78 characters a line). Above 800px, post rows put
meta on the right, the beliefs list goes two-column and the newsletter is
copy-left/form-right. Pages and layouts only provide what goes inside the
sheet. There is no sidebar, drawer or breadcrumb bar any more; the old
includes live in `_retired/` for reference.

- `_assets/main.css` — token + component CSS **source** (edit this, then `yarn css`)
- `assets/main.css` — compiled output (committed, don't hand-edit)
- `tailwind.config.js` — maps Tailwind colours to the CSS variables; `font-mono` / `font-sans`
- `assets/js/site.js` — theme toggle (⌥T), newsletter form
- `_layouts/` — `default` (frame), `post`, `field_note`, `progress_note` (the last two are sheet-based but unused while field notes are paused)
- `_includes/` — `nav-top`, `footer`, `post-row` (one post in a list; home + `/blog/`), `newsletter`, `lightbox`, `head`, and `fn/*` field-note components (metrics, checklist, field-log, exp-card, xcard, follow-cta, meta-block — `xcard` is also the post prev/next card)
- `_retired/` — `field-notes.html`, `sidebar.html`, `mobile-bar.html`: not processed by Jekyll, kept for the day the lab returns
- `_posts/` — blog posts (`YYYY-MM-DD-title.md`, permalink `/blog/:slug`)
- `_field_notes/` — the experiments collection, **paused**: `output: false` in `_config.yml` (see below)
- `_data/field_notes.yml` — queued experiments
- `assets/social-templates/` — social image templates: OG generator templates (filled by `scripts/generate-og.py` → `assets/images/og/*.jpg`) + hand-edited promo cards (exported with `scripts/export-social.mjs`). See its README.
- `styleguide.html` → `/styleguide/` — living component reference (noindex)
- `docs/guide.md` — **maintainer guide**: social images, template gallery, components how-to, field-note/progress-note authoring (excluded from the build)
- `.claude/skills/` — authoring skills: think/write pairs for field notes (`field-note-think`/`field-note-write`) and progress notes (`progress-think`/`progress-write`), the blog-post pipeline (`quick-log` → `writing-outline` → `writing-plan` → `writing-post`, state in `.writings-memory/`, agents `writing-researcher`/`writing-reader`/`writing-drafter` in `.claude/agents/`), plus `social-image`. Re-package for Claude Web with `scripts/package-skills.sh` → `dist/claude-web-skills/`.
- `.writings-memory/` — committed working state for the post pipeline: `ideas.md` inbox, `memory.md` (Nic's voice + observed edits, read by every drafter), one `<slug>/` per post in flight. See its README.

## Field notes collection

**Paused since Sep 2026.** The site is posts-only for now: the collection has
`output: false`, the `/field-notes/` index and the nav/footer links are gone,
and the homepage no longer has the lab band. Nothing was deleted — flip
`output` to `true`, restore `_retired/field-notes.html`, and add the links
back to bring it online. The `field_note` / `progress_note` layouts already
render inside the new sheet.

Two document kinds, both in `_field_notes/`:

- **Experiment brief** — `_field_notes/exp-NN.md`, `kind: experiment`, URL `/field-notes/exp-NN/`
- **Progress note** — `_field_notes/exp-NN/<slug>.md`, `kind: progress`, `layout: progress_note`, URL `/field-notes/exp-NN/<slug>/`

Full front-matter schema and authoring guide: `_field_notes/README.md`.
Structured blocks (metrics, guardrails, field log) are front-matter data
rendered with `{% include fn/... %}` inside the markdown body, so section
order is free and every `##` heading lands in the sidebar "on this page" list.

`future: true` is set in `_config.yml` because launch content is dated ahead.

## Writing blog posts — the workflow

Blog posts go through a four-stage pipeline, modelled on the shape of Amba's
ai-workflow: thin skills own the protocol and the approval gates, fresh-context
agents own the judgment, and files are the only state. Target: two posts a week.

```
/writing-brainstorm        → 5–8 candidates from his week → picked ones land in ideas.md
/quick-log <idea>          → .writings-memory/ideas.md            (no questions)
/writing-outline [#N|text] → .writings-memory/<slug>/outline.md   (interview + cold read → approve)
/writing-plan [slug]       → .writings-memory/<slug>/plan.md      (Nic's words verbatim + cold read → approve)
/writing-post [slug]       → drafts/vN.md … → approve → approved.md (memory.md learns from the edits)
/writing-publish [slug]    → _posts/ + OG image + optional illustrations/promo cards → build → tick, clean up, commit
```

Rules that hold across the pipeline:

- **Brainstorming is its own verb.** Finding what to write about is where Nic
  stalls most, so `/writing-brainstorm` is divergent only: it mines field
  notes, recent commits (here and in the Amba checkout, read-only, no customer
  detail), old posts and the inbox, asks up to five moment-prompts, and lands
  picked candidates in `ideas.md`. It never shapes a post. The session hook
  nudges towards it when fewer than four ideas are open.
- **Every skill and agent pins its model.** Sessions default to Opus, but
  nothing inherits: each front matter names the best model for its role.
  Fable where the stage's judgment compounds into later stages
  (`writing-outline`, `writing-post`, `writing-drafter`, `writing-reader`);
  Opus for conversational lanes where Nic filters the output
  (`writing-brainstorm`, `writing-plan`); Sonnet for retrieval and mechanical
  work (`writing-researcher`, `writing-publish`); Haiku for `quick-log`. Effort
  is pinned alongside, with the reason as a comment.
- **Preview without shipping.** In `/writing-post`, the `preview` pass copies
  the current draft to `_drafts/<slug>.md` (gitignored); `bundle exec jekyll
  serve --drafts` renders it at `/blog/<slug>/` in the real layout.

- **Capture is dumb.** When Nic drops an idea, `/quick-log` it. Never shape it
  inline; shaping is `/writing-outline`.
- **One approval gate per stage**, on a file Nic has seen in full. After
  approval the skill finishes its stage without asking "continue?" again.
- **Nothing reaches `_posts/` before draft approval.** Drafts live in
  `.writings-memory/<slug>/drafts/`, one file per version, never overwritten.
  `/writing-post` freezes the approved text as `approved.md`; only
  `/writing-publish` writes `_posts/`, and it never changes the words.
- **Publishing is visual work, not editing.** `/writing-publish` generates the
  OG card from front matter (fix the front matter, never the jpg), offers at
  most three inline illustrations as brand-token HTML rendered with
  `scripts/render-illustration.py` (needs `/opt/homebrew/bin/python3.13`, the
  one with Playwright), and optional quote/portrait promo cards from the social
  templates. No stock or AI-generated photography. One question round for the
  visuals, then it runs to the commit.
- **Never invent lived detail.** A visible `[…]` marker with the question
  inside is the correct output when a story, number or name is missing.
- **Read `.writings-memory/memory.md` before writing any post prose**, in any
  skill or ad hoc. It holds who is writing, the stable voice, rules Nic added,
  calibration posts, and observed edits: what Nic cut, replaced and added
  between agent drafts and the versions he approved. `/writing-post` appends
  there after every ship; a pattern seen three times is promoted into Voice.
- **The memory grows two ways.** Every time a draft sounds off and Nic says
  why, the rule goes into memory the same day. Every time a post ships with
  light edits, it joins the calibration list. Voice is learned from evidence,
  not asserted.
- **Every draft goes through the `humanizer:humanizer` plugin skill** inside
  `/writing-post`, after the drafter and before the cold read. Ad hoc post prose
  written outside the pipeline gets the same pass before Nic sees it.
- **Options before commitment.** The outline offers two structures, the claim
  gets an "uncomfortable version" Nic can dial back, and the drafter returns
  alternative titles and openings. The first option is rarely the best.
- **Agents have one write surface each.** `writing-researcher` (Sonnet, web +
  repo, writes `<slug>/research/`), `writing-reader` (Fable, read-only cold read:
  three findings max, one verdict line, Nic adjudicates), `writing-drafter`
  (Fable, writes `<slug>/drafts/` only). Skills do every other write.
- **`.writings-memory/` is committed.** The `<slug>/` folder is deleted on ship;
  the post, the ticked idea line and the memory entry are the durable record.
- The SessionStart hook `.claude/hooks/writing-context.sh` prints open ideas and
  in-flight slugs with their next command (registered in `.claude/settings.json`).
- An idea that is really an experiment (change one thing, measure it) is
  redirected to `field-note-think`, not written as an essay.

`post-think` and `post-write` are retired; the pipeline replaces them.

## Creating Posts

`/writing-post` writes the file; the shape below is what it must produce, and
what to use when a post is written by hand.


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

- Every page is a 1024px column under a sticky top bar, on one panel
  surface; blocks span it, paragraphs cap at `--measure` (640px). Four nav
  links fit a phone width, so there is no drawer.
- Portrait/photo slots on home + about read `site.portrait_image` from
  `_config.yml`; until it's set they show an on-brand placeholder.
- `node_modules/` is committed (pre-existing choice); don't prune it in
  unrelated PRs.
