---
name: writing-publish
description: Take an approved draft from .writings-memory/<slug>/approved.md and make it a published nicalpi.com page — the _posts/ file, the generated OG image, optional on-brand inline illustrations and promo cards, a build and preview check, the ideas.md tick, workspace clean-up and a commit. Use when Nic says "publish", "ship it", "put it on the site", or a draft has status: approved.
argument-hint: "[slug — defaults to the single approved slug] [--date YYYY-MM-DD] [--no-illustrations] [--no-promo]"
effort: high
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent, Skill
---

# Writing — PUBLISH

The words are approved. Nothing here changes them. This lane turns
`approved.md` into a page that is on-brand, has its link card, is illustrated
where an illustration helps, builds cleanly and is committed. One question round
for the optional visuals, then run to the end without asking again.

Read `.writings-memory/README.md`, `.claude/skills/nicalpi-brand/SKILL.md`
(tokens, art direction) and `.claude/skills/social-image/SKILL.md` before acting.

## 1. Resolve

- Slug from `$ARGUMENTS`, else the single `.writings-memory/*/approved.md`.
  Several → ask. None → point at `/writing-post`.
- `plan.md` must read `status: approved`. Anything else → stop, send him to
  `/writing-post`.
- Date: `--date`, else the `date:` in `approved.md`, else today. State it.
- Re-check `approved.md` has no `[…]` markers. If it has, stop; the draft is not
  approved.

## 2. Post file

Copy `approved.md` to `_posts/<date>-<slug>.md`. Verify front matter:
`layout: post`, `title`, `description`, `category` capitalised from the five,
`reading_time` honest at ~200 wpm, `date`, `og_image:
/assets/images/og/<slug>.jpg`. No `title_html`. Body untouched except for the
illustration lines added in step 4.

## 3. OG image (always)

```bash
python3 scripts/generate-og.py <slug>
python3 scripts/generate-og.py --check
```

The card is generated from front matter. If it reads badly (title wraps into
four lines, subtitle truncated), the fix is a shorter `subtitle` or
`short_title`, never a hand-edited jpg. Report the outcome.

## 4. Illustrations (offer, then do)

Skip when `--no-illustrations`. Otherwise read the post once as an art director
and find where a picture would carry meaning that prose carries badly: a flow,
a before/after, a comparison, a checklist the reader will screenshot. Most posts
need none or one. Never more than three. Never a decorative header image, never
stock or AI-generated photography; the brand is rendered markdown.

Present the candidates in one message: for each, the section, what it shows, one
line on why a picture beats the paragraph. He picks, or says none.

For each picked illustration:

1. Write `assets/images/<slug>/<name>.html`: self-contained, 1200×630 unless
   the content wants square, linking `../../social-templates/social.css` for
   tokens. JetBrains Mono only. Faint `#` marks, thin rules, one accent. Text
   comes from the post verbatim. Light theme by default (posts render the jpg
   in both themes; paper surfaces read fine on dark).
2. Render: `/opt/homebrew/bin/python3.13 scripts/render-illustration.py assets/images/<slug>/<name>.html`
   (add `--size WxH` for non-default sizes; that Python has Playwright, the
   default `python3` does not; it launches system Chrome, so it runs outside
   the Bash sandbox).
3. Insert into the post at the agreed spot:
   `![<alt that says what the picture shows>](/assets/images/<slug>/<name>.jpg)`
   on its own line, after the paragraph it illustrates. The post layout adds the
   lightbox.
4. Read the jpg back (Read tool renders images) and check it: nothing clipped,
   contrast fine, text readable at half size. Fix and re-render if not.

Commit both the `.html` source and the `.jpg`.

## 5. Promo cards (offer, then do)

Skip when `--no-promo`. Offer at most two, based on what the post has:

- **Quote card** (`quote-square.html`) when the post has a blockquote or a
  line the reader would repost. Text verbatim from the post.
- **Portrait promo** (`post-promo-portrait.html`) for the title + dek + one
  hook line, verbatim.

He picks, or says none. For each: copy the template to
`assets/images/social/<slug>/<template>.html`, fix its stylesheet link to
`../../../social-templates/social.css`, edit the text in place, then render
both themes with `scripts/render-illustration.py` (`--size 1080x1080` or
`1080x1350`; `--theme dark` for the second; `--out …/<template>.png` and
`<template>-dark.png`). The site templates stay untouched. Read one exported
PNG back and check it. Social copy that goes with the
cards is out of scope here; that is a separate project.

## 6. Build and preview

```bash
bundle exec jekyll build
test -d _site/blog/<slug>/ && echo built
```

Paste any failure verbatim and fix front matter if that is the cause. Read the
rendered page's key checks from `_site/blog/<slug>/index.html`: title present,
every illustration `src` resolves to a file, OG meta points at the jpg. If a
local server is running, tell him the URL.

## 7. Close the loop

1. **Tick the idea.** In `.writings-memory/ideas.md`, the line matching the
   plan's `idea:` field goes `- [ ]` → `- [x]` with ` → /blog/<slug>` appended.
   For `ad hoc`, add a ticked line dated today.
2. **Clean up.** `git rm -r .writings-memory/<slug>/` (or `rm -rf` if
   untracked) and `rm -f _drafts/<slug>.md`. Memory was already updated at
   approval by `/writing-post`; do not touch `memory.md` here.
3. **Commit.** Stage the post, `assets/images/og/<slug>.jpg`, any
   `assets/images/<slug>/`, any `assets/images/social/<slug>/`,
   `.writings-memory/ideas.md`, the deleted folder. One commit on the current
   branch, message naming the post title. Never push; publishing to origin is
   Nic's call.

Report, then stop: post path, `/blog/<slug>`, OG status, illustrations and
cards produced (paths), build status, commit hash, and the one line he needs to
run to push.

## Judgment

- The words are frozen. A typo spotted here is reported, not fixed silently;
  he decides, and the fix goes in the same commit if he says so.
- One question round covers illustrations and promo together. Then no more
  questions.
- A post with no illustrations is a normal outcome. Do not manufacture one.
