---
name: writing-brainstorm
description: Divergent session to find what Nic should write about next — mines his recent work, field notes, existing posts and the ideas inbox, asks a handful of prompts that surface lived material, and produces 5–8 candidate post one-liners with the receipt each would need. Picked candidates land in .writings-memory/ideas.md. Use when Nic says "what should I write about", "brainstorm", "I have nothing to write", "queue is low", or at the start of a writing week.
argument-hint: "[theme or constraint, optional — e.g. 'something on AI and juniors', 'personal register']"
allowed-tools: Read, Grep, Glob, Bash, AskUserQuestion, Agent, WebSearch, WebFetch, Edit
---

# Writing — BRAINSTORM

This is the stage Nic skips most, so it has to be cheap to start and produce
something concrete in under fifteen minutes. You are not shaping a post. You are
finding the two or three ideas worth shaping, out of the dozen that are in his
week already. Divergent first, then pick, then stop. `/writing-outline` does the
convergent work.

Read `.writings-memory/memory.md` (who is writing, what the reader wants) and
`.writings-memory/ideas.md` before anything else.

## 1. Mine before asking

Do this silently and fast, then present it as a short "what I found" list. He
should react to material, not face a blank question.

- **Ideas inbox**: every unticked line. Cluster them; a cluster of three weak
  ideas is often one good post.
- **Field notes**: `_field_notes/**` field logs and progress notes since the
  last shipped post. A logged observation is a receipt waiting for a claim.
- **Existing posts**: `_posts/` titles and dates. Gaps in the categories he
  writes in; posts old enough to revisit with "what I got wrong".
- **Recent work**: `git log --since='14 days ago' --oneline` here, and if
  `/Users/nicolas/code/amba` exists, its `git log --since='14 days ago'
  --oneline --no-merges | head -40` and `.ai-work/*/progress.md` files touched
  in that window. Commit messages and rulings are where "what I changed my mind
  on" hides. Read-only. Never quote customer names or anything commercial;
  extract the engineering or leadership pattern only.
- **What his readers are arguing about** (optional, when `$ARGUMENTS` names a
  theme or the inbox is thin): dispatch `writing-researcher` for two or three
  current takes in that space, with links. Purpose: something to disagree with.

## 2. Ask, one at a time, at most five

Pick from this bank the questions the mining did not already answer. Each is a
prompt for a moment, not an opinion:

- What annoyed you this week that you have said out loud to someone?
- What did you change your mind on in the last month, and what changed it?
- What did someone on the team ask you twice?
- Which number surprised you recently?
- What did you do at 23:00 that you should not have?
- What advice do you keep giving that you have never written down?
- What did you read or hear recently that you think is wrong?
- Which old post of yours would you argue with today?

Take his answers as raw material. Reflect each back in one line. Do not
evaluate yet.

## 3. Generate candidates

Produce five to eight one-liners. For each:

```
N. <one line in Nic's words — a claim, not a topic>
   receipt: <the moment, number or story from the mining or his answers>
   angle: <contrarian | what I got wrong | the number | the conversation | field-note spin-off | reply to something read>
   why now: <one line>
   register: <ai|leadership|business|career|personal>
```

Vary the angles; two contrarian takes in a row is a rut. Include at least one
`personal` and at least one that spins off a field note. Mark any candidate
that is really an experiment with `→ field-note-think`.

Also offer one **uncomfortable candidate**: the thing he might not want to
publish. It is often the best one.

## 4. Pick and land

Ask him to pick, kill or merge. Then:

- Each picked candidate becomes one line in `ideas.md`, in `/quick-log` format,
  today's date, his wording, tags, plus ` · receipt: <short>` so the outline
  starts with material.
- Candidates he killed are not logged. Ones he is unsure about are logged with
  `#maybe`.
- End with the count of open ideas and: "Run `/writing-outline #N` on the one
  you want to shape first." Do not start the outline.

## Judgment

- Speed over completeness. Fifteen minutes, then stop, even with three
  candidates.
- Never propose a topic he has no receipt for. "Thoughts on remote work" is
  not a candidate; "the Tuesday I cancelled the standup and nobody noticed" is.
- If the inbox already has six or more strong unticked ideas, say so first and
  offer to skip straight to `/writing-outline`.
- Two posts a week is the target. If it is Monday and nothing is in flight, the
  session should end with at least two ideas landed.
