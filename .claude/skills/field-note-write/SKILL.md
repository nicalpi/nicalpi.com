---
name: field-note-write
description: Turn a finished experiment frame (from field-note-think, or any braindump) into a new field-note collection page for nicalpi.com — front matter, markdown body, queue update and OG image. Use when Nic says "write the field note", "create the experiment page", "new field note page", or hands over a FIELD NOTE FRAME.
---

# Field note — WRITE

You write the experiment brief page for Nic's public CTO lab from a FIELD
NOTE FRAME (produced by `field-note-think`) or a sufficiently complete
braindump. If key pieces are missing (baseline, hypothesis, guardrails,
window), ask for just those — don't restart the whole interview.

## Voice

First person, plain, measured. Sentence case headings, no exclamation marks,
no hype. Numbers carry the story. Honest hedges stay in ("small sample, read
the direction, not the decimals"). Verdicts are one word: kept / dropped /
inconclusive. It reads like an engineer's lab notebook, not a productivity
blog.

## The page

File: `_field_notes/exp-NN.md` (URL `/field-notes/exp-NN/`). Follow the full
schema in `_field_notes/README.md`; model on `_field_notes/exp-01.md`
(running) or `exp-00.md` (closed).

Front matter (all of it):

```yaml
---
kind: experiment
exp: NN
exp_id: exp-NN
title: "<the question>"
lead: "<one-paragraph dek under the title>"
description: "<SEO description>"
theme_tag: <theme>
status: running
status_label: "running · since <Mon>"
started: "<Mon YYYY>"
window: "<Mon → Mon>"
measure: "<the headline metric>"
next_label: "<Mon> checkpoint"
progress_pct: 5
permalink: /field-notes/exp-NN/
og_image: /assets/images/og/exp-NN.jpg
roadmap:
  - "<Mon> — checkpoint"
  - "<Mon> — verdict"
summary: "<index-card one-liner>"
facts:            # index-card right column, 3–4 rows
  - { label: baseline, value: "<…>" }
  - { label: verdict, value: "due in <Mon>", accent: true }
metrics:          # 2–4 rows; flag up to 3 with home: true (+ short home_label)
  - { label: "<metric>", home_label: "<short>", home: true, before: "<?>", now: "<?>", target: "<…>" }
guardrails:
  - { text: "<stop condition>", done: false }
  - { text: "log where the work moved, every week", done: true }
  - { text: "publish the verdict even if the result is nothing", done: true }
field_log:
  - { date: "early <Mon>", strong: "Protocol published.", text: "<…>" }
  - { date: "<Mon>", text: "<checkpoint>", planned: true }
---
```

Body — markdown sections in this order, structured blocks via includes:

```markdown
## The question
<the itch, as a story, 2 short paragraphs; end with what was counted for the baseline>

## Hypothesis
> <If …, then …, without …>

## The protocol
- <intervention bullets>

## Measures
{% include fn/metrics.html rows=page.metrics %}

## Guardrails
{% include fn/checklist.html items=page.guardrails %}

## Field log
{% include fn/field-log.html entries=page.field_log %}
```

Metrics `before` values stay "?" until the baseline fortnight is counted —
that's honest, say so in the body if relevant.

## After writing the file

Working in the repo (Claude Code):
1. Create the file, then remove the experiment from `_data/field_notes.yml`
   if it was queued.
2. `python3 scripts/generate-og.py exp-NN` then
   `python3 scripts/generate-og.py --check`
3. `bundle exec jekyll build` to confirm it renders; offer a commit.

On Claude Web (no repo access): output the complete file as one markdown
code block with the exact path as a heading, plus this reminder list
(queue removal, OG generation command, --check). Never pretend you created
files you couldn't.
