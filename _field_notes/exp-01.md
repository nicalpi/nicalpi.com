---
kind: experiment
exp: 01
exp_id: exp-01
title: "Can I stop being the fastest path to an answer?"
lead: "I am the fastest path to an answer for twenty-two people, and that is the whole problem. For seven weeks I redirect every request that isn't mine — one line, no answer — and count whether the work finds its owner or just finds someone else."
description: "A seven-week experiment: I redirect every request that isn't mine and measure whether the work reaches its owner, or simply lands on the next available person."
theme_tag: boundaries
status: running
status_label: "running · since Aug"
started: "Aug 2026"
window: "Aug → Oct"
measure: "Off-lane share of requests reaching me"
next_label: "Sep checkpoint"
progress_pct: 5
permalink: /field-notes/exp-01/
og_image: /assets/images/og/exp-01.jpg
roadmap:
  - "8 Sep — checkpoint"
  - "5 Oct — verdict"
summary: "I redirect every request that isn't mine for seven weeks, and count whether the work finds its owner or just finds someone else."
facts:
  - label: baseline
    value: "10 working days, from logs"
  - label: window
    value: "7 weeks"
  - label: intervention
    value: "one line, no answer"
  - label: verdict
    value: "due in Oct"
    accent: true
metrics:
  - label: "Off-lane requests reaching me"
    home_label: "off-lane share"
    home: true
    before: "?"
    now: "?"
    target: "≤30%"
  - label: "Requests resolved without touching me"
    home_label: "resolved without me"
    home: true
    before: "~0"
    now: "?"
    target: "most, by week 6"
  - label: "My messages after 20:00, per week"
    home_label: "after 20:00"
    home: true
    before: "?"
    now: "?"
    target: "≤2"
  - label: "Median time to first support response"
    before: "?"
    now: "?"
    target: "no worse than baseline"
guardrails:
  - text: "stop if a decision slips more than 48h because I redirected"
    done: false
  - text: "stop if support first-response time doubles against baseline"
    done: false
  - text: "log where the work moved, every week"
    done: true
  - text: "publish the verdict even if the result is nothing"
    done: true
field_log:
  - date: "late Jul"
    strong: "Protocol published."
    text: "Baseline window chosen retrospectively so the counting can't change the behaviour it measures."
  - date: "early Aug"
    text: "Baseline counted from logs."
    planned: true
  - date: "8 Sep"
    text: "Checkpoint — first read on whether requests are reaching owners or just other people."
    planned: true
  - date: "5 Oct"
    text: "Verdict."
    planned: true
---

## The question

At 23:09 on a Thursday in July I ran a data reconciliation script by hand. It was the fifth run that day. I did it because nobody else on an eight-person engineering team could — not for want of skill, but because the script lives in my head and has never been written down.

Six weeks earlier our support lead posted a question and tagged two of us in it, me and the engineering lead, twice, sixty seconds apart. That isn't escalation. That's someone guessing which of us answers first. When I counted properly, twenty-two people had routed work to me over ninety days, and fourteen of them don't work in engineering.

For the baseline I counted ten working days, 29 June to 10 July, retrospectively from Slack rather than tallied forward. Two numbers: requests that reached me when a named owner already existed elsewhere, and requests that owner resolved without me. Counting from logs after the fact means there is no observer effect, and no chance of me quietly forgetting to count on a bad day.

## Hypothesis

> If I redirect instead of answering, off-lane requests reaching me fall below 30% within six weeks — without support first-response time getting worse.

## The protocol

- Any request on a lane with a named owner gets one line: who owns it, where to post it. No answer, not even a partial one.
- This applies in direct messages. The redirect is the entire reply.
- My lanes stay mine: security, vendor commercials, decisions only I can make.
- If no owner exists, I answer once, and that answer becomes a written entry or a ticket the same day.

## Measures

The before column stays at "?" until the baseline fortnight is counted. I'd rather publish an empty cell than a number I guessed.

One confound I can't design away: the engineering lead moves off delivery work and onto a support rotation inside the same window. If requests to me fall, that could be his rota rather than my redirecting. So the two are reported separately — requests I redirect measure my behaviour, requests that never reach me measure the system. If only the second moves, the honest finding is that the rota fixed this and I didn't.

{% include fn/metrics.html rows=page.metrics %}

## Guardrails

{% include fn/checklist.html items=page.guardrails %}

## Field log

{% include fn/field-log.html entries=page.field_log %}
