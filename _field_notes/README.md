---
published: false
---

# Field notes — authoring guide

Field notes are the public CTO lab: experiments run on Nic's own work, each
with a baseline, a protocol, guardrails and a published verdict. Two document
kinds live in this collection.

## 1. Experiment brief — `_field_notes/exp-NN.md`

The top-level page for an experiment (`/field-notes/exp-NN/`). Uses
`layout: field_note` (the collection default).

```yaml
---
kind: experiment
exp: 2                      # number, used for ordering
exp_id: exp-02              # stable id, referenced by progress notes
title: "Can AI review replace my first pass on pull requests?"
short_title: "ai first pass"   # sidebar label once closed (optional)
lead: "One-paragraph dek under the title."
description: "SEO description."
theme_tag: ai               # attention | boundaries | delivery | ai …
status: running             # running | closed
status_label: "running · since Oct"
verdict: kept               # only when closed: kept | dropped | inconclusive
started: "Oct 2026"
window: "Oct → Nov"
measure: "review turnaround time"
next_label: "Nov checkpoint"
progress_pct: 10            # drives the progress bar while running
permalink: /field-notes/exp-02/
roadmap:                    # future steps, dimmed in the sidebar
  - "Nov — checkpoint"
  - "Dec — verdict"
summary: "One-liner for the index card."
facts:                      # right-hand column of the index card
  - { label: baseline, value: "9h turnaround" }
  - { label: verdict, value: "due in Dec", accent: true }
metrics:                    # before / now / target table
  - { label: "review turnaround", before: "9h", now: "6h", target: "< 2h" }
guardrails:
  - { text: "stop if a regression ships that review would have caught", done: false }
field_log:
  - { date: "early Oct", strong: "Protocol live.", text: "Team briefed." }
  - { date: "Dec", text: "Verdict.", planned: true }
---
```

Body: markdown. The structured blocks are rendered wherever you place them:

```liquid
## Measures
{% raw %}{% include fn/metrics.html rows=page.metrics %}{% endraw %}

## Guardrails
{% raw %}{% include fn/checklist.html items=page.guardrails %}{% endraw %}

## Field log
{% raw %}{% include fn/field-log.html entries=page.field_log %}{% endraw %}
```

Every `##` heading automatically appears in the sidebar "on this page" list.

## 2. Progress note — `_field_notes/exp-NN/<slug>.md`

A dated child update (`/field-notes/exp-NN/<slug>/`). Uses
`layout: progress_note` (set it explicitly in front matter).

```yaml
---
layout: progress_note
kind: progress
experiment: exp-01          # parent exp_id
note_id: fn-01.2            # fn-<exp>.<n>
nav_label: "Sept — checkpoint"   # sidebar tree label
title: "…"
lead: "…"
date: 2026-09-20
published_label: "late Sept 2026"
status_label: "still running"
reading_time: 4
next_label: "Oct verdict"
permalink: /field-notes/exp-01/<slug>/
metrics: [ … ]              # same shape as the brief
adjustments: [ … ]          # checklist items
guardrail_check:            # checklist items, `note:` adds a muted suffix
  - { text: "…", note: "…", done: true }
---
```

## Queue

Planned experiments live in `_data/field_notes.yml` and render in the
"queued" box on `/field-notes/` and the home lab band. Promote one by
creating its brief here.
