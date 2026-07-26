---
layout: progress_note
kind: progress
experiment: exp-01
note_id: fn-01.1
nav_label: "Aug — progress"
title: "The questions moved, but the decisions did not"
lead: "Two weeks in, the interruptions are down by a third and I have the mornings back. What I do not have is any evidence that the team is deciding more on its own."
description: "Two weeks into the question-firewall experiment: interruptions down a third, mornings reclaimed — and no evidence yet that the team is deciding more on its own."
date: 2026-08-24
published_label: "late Aug 2026"
status_label: "still running"
reading_time: 4
next_label: "Sept checkpoint"
permalink: /field-notes/exp-01/the-questions-moved/
metrics:
  - label: "unplanned interruptions / wk"
    before: "31"
    now: "19"
    target: "< 12"
  - label: "strategic hours / wk"
    before: "3.5"
    now: "5.0"
    target: "9.5"
  - label: "median decision latency"
    before: "4h"
    now: "9h"
    target: "< 24h"
  - label: "questions resolved without me"
    before: "12%"
    now: "41%"
    target: "> 60%"
adjustments:
  - text: "add a second measure: decisions made without me, counted in 1:1s"
    done: true
  - text: "ask the two loudest sceptics what the rule costs them"
    done: true
  - text: "keep the protocol otherwise untouched until the Sept checkpoint"
    done: false
guardrail_check:
  - text: "no decision has slipped past 48 hours"
    note: "closest was 31h"
    done: true
  - text: "juniors still asking"
    note: "volume flat, which is the point"
    done: true
  - text: "where the work moved"
    note: "unclear, this is the Sept question"
    done: false
---

## What changed

The written filter did the obvious thing: it made asking slightly expensive, so fewer people asked. Two answering windows a day turned out to be the part that mattered — not the channel rule.

The mornings are genuinely quiet now. I have had three uninterrupted 90-minute blocks a week, which is three more than before.

## The numbers so far

{% include fn/metrics.html rows=page.metrics caption="Small sample, one team, two weeks. Read the direction, not the decimals." %}

## What I got wrong

> I measured whether questions reached me. I never measured whether anyone decided anything without me.

Most of the drop is one senior developer batching her questions into a single afternoon message. That is a person adapting, not a system working. If she is on holiday in Sept, I expect the number to bounce straight back.

## What I'm adjusting

{% include fn/checklist.html items=page.adjustments %}

## Guardrail check

{% include fn/checklist.html items=page.guardrail_check %}
