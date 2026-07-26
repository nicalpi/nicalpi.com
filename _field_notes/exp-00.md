---
kind: experiment
exp: 0
exp_id: exp-00
title: "A hard 4pm stop, ninety days later"
short_title: "hard 4pm stop"
lead: "Phone down at 4pm, non-negotiable. Ninety days of data on whether anything actually broke."
description: "A ninety-day experiment: hard stop at 4pm, phone down, non-negotiable. What broke, what didn't, and why the rule is now permanent."
theme_tag: boundaries
status: closed
status_label: "closed · kept"
verdict: kept
started: "Feb 2026"
window: "Feb → May"
measure: "evenings reclaimed, incidents caused"
progress_pct: 100
permalink: /field-notes/exp-00/
og_image: /assets/images/og/exp-00.jpg
summary: "Phone down at 4pm, non-negotiable. Ninety days of data on whether anything actually broke."
facts:
  - label: window
    value: "Feb → May"
  - label: evenings reclaimed
    value: "78 / 90"
  - label: incidents caused
    value: "0"
  - label: verdict
    value: "kept, permanently"
    accent: true
metrics:
  - label: "evenings reclaimed"
    before: "0 / 90"
    now: "78 / 90"
    target: "> 70"
  - label: "incidents caused by absence"
    before: "—"
    now: "0"
    target: "0"
  - label: "messages sent after 4pm"
    before: "~14 / wk"
    now: "2 / wk"
    target: "< 5"
guardrails:
  - text: "stop if a production incident waits on me past 9am the next day"
    done: true
  - text: "stop if the team starts holding decisions for the morning"
    done: true
  - text: "publish the verdict even if the result is nothing"
    done: true
field_log:
  - date: "Feb"
    strong: "Rule announced."
    text: "Phone in a drawer at 4pm. The team gets an escalation path: call twice and I pick up."
  - date: "Mar"
    strong: "First real test."
    text: "A deploy went sideways at 4:20pm. The team rolled it back without me. Nobody called."
  - date: "May"
    strong: "Ninety days done."
    text: "78 evenings kept, zero incidents caused, and the escalation path was used once — for something that genuinely needed it."
---

## The question

For years my evenings absorbed whatever the day didn't finish. The theory was that being reachable made the team safer. I never tested the theory; I just paid for it.

So: what actually breaks if I stop at 4pm — completely, phone down, every working day, for ninety days?

## Hypothesis

> Nothing breaks. The team escalates the one genuine emergency a quarter by phone, everything else waits until morning, and I get my evenings back at zero cost to delivery.

## The protocol

- Hard stop at 4pm. Phone in a drawer, laptop closed.
- One escalation path: call twice in a row and I pick up. Anything else waits.
- No "quick checks" in the evening. A check is a breach, and breaches get logged.
- Count three things: evenings kept, incidents caused by my absence, after-4pm messages sent.

## Results

{% include fn/metrics.html rows=page.metrics caption="Ninety working days, one team, one CTO. The 12 lost evenings were planned exceptions — releases and one conference — not slips." %}

## Verdict — kept, permanently

The escalation path was used once in ninety days, for something that justified it. Zero incidents waited on me overnight. The after-4pm messages that used to look urgent turned out to be ambient noise that resolved itself by morning.

The rule survived contact with a real quarter, so it stopped being an experiment. It's now just how I work — and the reason this site talks about boundaries with a straight face.

## Field log

{% include fn/field-log.html entries=page.field_log %}
