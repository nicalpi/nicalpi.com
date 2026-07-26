---
kind: experiment
exp: 1
exp_id: exp-01
title: "Can a question firewall give me back strategic time?"
lead: "A four-week experiment to reduce reactive interruptions without becoming inaccessible, delaying decisions, or moving the burden onto somebody else."
description: "A four-week experiment to cut reactive interruptions without becoming inaccessible. Baseline, protocol, guardrails — and a verdict published either way."
theme_tag: attention
status: running
status_label: "running · since Aug"
started: "Aug 2026"
window: "Aug → Sept"
measure: "strategic hours per week"
next_label: "Sept checkpoint"
progress_pct: 23
permalink: /field-notes/exp-01/
og_image: /assets/images/og/exp-01.jpg
roadmap:
  - "Sept — planned"
  - "Oct — verdict"
summary: "A four-week test to cut reactive interruptions without becoming inaccessible or moving the burden onto somebody else."
tags:
  - "interruption log n=62"
  - "calendar audit"
  - "team pulse"
facts:
  - label: baseline
    value: "31 interrupts/wk"
  - label: now
    value: "19"
  - label: target
    value: "+6 strategic hrs"
  - label: verdict
    value: "due in Oct"
    accent: true
metrics:
  - label: "unplanned interruptions / wk"
    home_label: "interrupts/wk"
    home: true
    before: "31"
    now: "19"
    target: "< 12"
  - label: "strategic hours / wk"
    home_label: "strategic hrs"
    home: true
    before: "3.5"
    now: "5.0"
    target: "9.5"
  - label: "median decision latency"
    before: "4h"
    now: "9h"
    target: "< 24h"
  - label: "questions resolved without me"
    home_label: "resolved w/o me"
    home: true
    before: "12%"
    now: "41%"
    target: "> 60%"
guardrails:
  - text: "stop if any decision slips more than 48 hours"
    done: false
  - text: "stop if juniors stop asking altogether"
    done: false
  - text: "log where the work moved, every week"
    done: true
  - text: "publish the verdict even if the result is nothing"
    done: true
field_log:
  - date: "early Aug"
    strong: "Protocol published to the team."
    text: "Two people said it would never hold. Noted, for the verdict."
  - date: "mid Aug"
    strong: "Interruptions down from 31 to 19."
    text: "Most of the drop is one person batching. Not yet a system."
  - date: "Sept"
    text: "Mid-point check on decision latency."
    planned: true
  - date: "Oct"
    text: "Verdict — kept, dropped, or inconclusive."
    planned: true
---

## The question

I am the default answer in my company. That felt like leadership for a long time. It is closer to a bottleneck: the fastest route to an answer runs through one person, so it keeps running through that person.

Before changing anything, I counted. Two weeks of tagging every unplanned interruption with who, what, and whether it actually needed me.

## Hypothesis

> If questions must pass a written filter before reaching me, then two thirds will resolve without me, and I will recover six strategic hours a week — without slowing any decision by more than a day.

## The protocol

- Questions go to a shared channel first, never DM.
- The asker states what they tried and what they'd do if I were away.
- I answer twice a day, 11:00 and 16:30 — nothing in between.
- Anything genuinely urgent uses a phone call. No guilt.

## Measures

{% include fn/metrics.html rows=page.metrics %}

## Guardrails

{% include fn/checklist.html items=page.guardrails %}

## Field log

{% include fn/field-log.html entries=page.field_log %}
