---
name: writing-plan
description: Expand an approved outline into a plan at .writings-memory/<slug>/plan.md by walking each section with Nic and capturing his own words, stories, numbers and phrasing verbatim. Reads memory.md so the questions target what the drafter will need. Use when Nic says "plan the post", "let's flesh it out", or names a slug with an approved outline.
argument-hint: "[slug — defaults to the single open slug]"
model: opus
effort: medium
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent, WebSearch, WebFetch
---

# Writing — PLAN

The outline says what the post claims. The plan collects the material only Nic
has: the way he tells the story, the exact number, the phrase he actually used
in the meeting. The drafter will write from this file, so anything not captured
here gets invented or left as a `[…]` gap. Your job is to make the gaps small.

Read `.writings-memory/memory.md` and `.writings-memory/README.md` first.

## 1. Resolve the slug

- `$ARGUMENTS` names a slug → use it.
- Empty → find every `.writings-memory/*/` whose `outline.md` exists and no
  `plan.md` has `status: drafting`. One match → use it, say which. Several → ask.
  None → point at `/writing-outline`.
- `outline.md` missing or its `## Reader` still `_pending_` → stop and send him
  back to `/writing-outline`. The plan builds on an approved outline only.
- `plan.md` already exists → resume. Read it, name the sections still thin,
  continue.

## 2. Walk the structure

Take the outline's sections in order. For each, one question at a time:

- **The opening section**: "Tell me the moment. Where were you, what time, what
  did you see?" Capture it as he says it. Time-of-day, the tool, the person's
  role. Nic opens with scenes like "At 23:09 on a Thursday in July".
- **Each receipt**: the number, the date, who was in the room. If he says
  "roughly", write "roughly". If he does not know, write `[…]` with the
  question, never a placeholder that looks like a fact.
- **The counterargument section**: ask for the line he would say to the
  sceptic. His phrasing, not a debate summary.
- **Every section**: "What's the one sentence you'd want quoted from this bit?"
  Most sections will not have one. The one that does is the blockquote.

Capture his words under `> Nic:` blockquotes, verbatim, typos cleaned only.
Paraphrase nothing he said directly.

Use `memory.md`'s observed edits to steer: if past posts show he cuts
frameworks and adds people, ask for people. If a fact needs checking, dispatch
`writing-researcher` with the slug and the question.

Aim for eight to twelve questions. Stop when every section has at least one
receipt and the opening moment is concrete. He can always say "enough, draft
it".

## 3. Write the plan

`.writings-memory/<slug>/plan.md`:

```markdown
---
slug: <slug>
status: plan
idea: <from outline>
updated: YYYY-MM-DD
title: "<chosen title>"
subtitle: "<dek, optional>"
description: "<one-paragraph abstract: what the post argues and for whom — becomes the SEO/list description>"
category: <AI|Business|Career|Leadership|Personal>
---

# <title>

## Claim
<from outline, tightened if the interview sharpened it>

## Opening moment
> Nic: <verbatim>

## Sections

### 1. <section title from outline>
Purpose: <one line>
Material:
> Nic: <verbatim story or number>
Notes: <what the drafter must not do here, links to research/>

### 2. …

## Counterargument
> Nic: <the line to the sceptic>
Placement: <section N>

## Quotable line
> <the one blockquote candidate, or "none yet">

## Ending
<the last fact or next step the post ends on — never a summary>

## Gaps
- [ ] <lived detail still missing, as a question> (section N)

## Reader
_pending_
```

Front-matter `title`, `subtitle`, `description`, `category` are what
`/writing-post` copies into the post. Decide them here. Write the `description`
as the abstract Nic approves before any prose exists: if he cannot approve a
one-paragraph version of the post, the plan is not ready.

## 4. Cold read and approval

Dispatch `writing-reader` with `stage: plan` and the path. Show findings and
verdict beside the plan. Nic adjudicates; record under `## Reader`; revise if
he accepts a change.

Ask for approval of the plan as shown. One gate. On approval, set
`status: plan` (approved is implied by a filled `## Reader`) and end with:
"Plan approved. Run `/writing-post <slug>` to draft it." Do not draft.

## Judgment

- A gap left visible beats a detail invented. The `## Gaps` list is a feature.
- If the interview overturns the outline's claim, say so, update the outline's
  `## Claim` too, and note it under `## Reader` so the history is honest.
- Do not write prose for the post here. Verbatim quotes only.
