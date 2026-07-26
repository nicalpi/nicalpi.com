---
name: progress-write
description: Turn a PROGRESS FRAME (from progress-think, or a debrief braindump) into a progress-note page under an experiment on nicalpi.com — front matter, body, brief updates and OG image. Use when Nic says "write the progress note", "publish the checkpoint", or hands over a PROGRESS FRAME.
---

# Progress — WRITE

You write a progress note — a short, numbers-first child page of a running
experiment — from a PROGRESS FRAME (`progress-think`) or an equivalent
debrief. Progress notes are ~4 min reads: tighter and more candid than the
brief. Model: `_field_notes/exp-01/the-questions-moved.md`; full schema in
`_field_notes/README.md`.

## Voice

Same lab-notebook register as the brief, but this is the honest middle:
lead with what's true *now*, including the uncomfortable part. The title is
a finding, not a status ("The questions moved, but the decisions did not" —
never "Exp-01 update #1"). One quotable admission sits in a blockquote.

## The page

File: `_field_notes/exp-NN/<slug>.md` — slug from the title
(URL `/field-notes/exp-NN/<slug>/`).

```yaml
---
layout: progress_note
kind: progress
experiment: exp-NN
note_id: fn-NN.N
nav_label: "<Mon> — progress"
title: "<the finding>"
lead: "<two sentences: the good number, then the doubt>"
description: "<SEO>"
date: YYYY-MM-DD
published_label: "<early|mid|late Mon YYYY>"
status_label: "still running"
reading_time: 4
next_label: "<Mon> checkpoint"
permalink: /field-notes/exp-NN/<slug>/
og_image: /assets/images/og/<slug>.jpg
metrics:            # same rows as the brief, now filled in
  - { label: "<metric>", before: "<…>", now: "<…>", target: "<…>" }
adjustments:
  - { text: "<change>", done: true }
guardrail_check:    # note: adds the muted suffix
  - { text: "<guardrail>", note: "<evidence>", done: true }
---
```

Body order (headings feed the sidebar "on this page" list):

```markdown
## What changed
<mechanism, not just direction — what actually did the work; 2 short paragraphs>

## The numbers so far
{% include fn/metrics.html rows=page.metrics caption="Small sample, one team, <period>. Read the direction, not the decimals." %}

## What I got wrong
> <the quotable admission>

<the story behind it, and what it implies for the rest of the window>

## What I'm adjusting
{% include fn/checklist.html items=page.adjustments %}

## Guardrail check
{% include fn/checklist.html items=page.guardrail_check %}
```

## Update the parent brief too

- `field_log`: add a dated entry for this note (strong = the headline).
- `progress_pct`: bump to match the window elapsed.
- `roadmap`: drop the step this note fulfils.
- If a guardrail was breached and the frame says stop: that's a verdict
  conversation, not a progress note — say so and stop.

## After writing

In the repo (Claude Code):
1. Create the note, apply the brief updates above.
2. `python3 scripts/generate-og.py <slug>` then `--check`.
3. `bundle exec jekyll build`; offer a commit.

On Claude Web: output both files' changes as complete markdown/code blocks
(note file in full; brief front-matter diff) plus the OG commands as a
to-do list. Never claim to have written files you couldn't.
