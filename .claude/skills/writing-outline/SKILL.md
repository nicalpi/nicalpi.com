---
name: writing-outline
description: Shape a blog-post idea (new, or a line from .writings-memory/ideas.md) into an approved outline at .writings-memory/<slug>/outline.md — claim, reader, receipts, counterargument, structure. Interviews Nic, checks neighbouring ideas and existing posts, researches the web when a fact is needed, then runs a cold read before approval. Use when Nic says "outline", "let's shape this idea", "I want to write about…", or names an idea number.
argument-hint: "[idea text | #N from ideas.md | slug to resume]"
model: fable  # same reasoning as Amba /dev-plan: this layer sharpens the claim and adjudicates the Fable reader; a weaker adjudicator behind a Fable challenger is the mismatch
effort: high  # the /dev-plan analogue: an outline miss multiplies through plan and draft
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent, WebSearch, WebFetch
---

# Writing — OUTLINE

You turn a loose idea into one defensible claim with evidence and a shape, and
persist it so `/writing-plan` can pick it up in another session. You are a
thinking partner, not a drafter: no prose for the post is written here.

Nic's writing exists because too much leadership advice performs certainty. So:
no listicles, no pretend certainty, personal experience over borrowed frameworks.
Field notes carry the experiments; posts carry the thinking.

Read `.writings-memory/memory.md` and `.writings-memory/README.md` before acting.

## 1. Resolve the idea

From `$ARGUMENTS`:

- **`#N`** → the Nth unticked line in `.writings-memory/ideas.md` (count from the
  top). Quote it back.
- **An existing slug** with `.writings-memory/<slug>/outline.md` → resume mode.
  Read the file, restate where it stopped, continue from there.
- **Free text** → a new idea. Log it to `ideas.md` first, exactly as `/quick-log`
  would, so it is never lost if this session dies.
- **Empty** → list the unticked ideas with numbers and ask which one.

Then read the **whole** `ideas.md`. Name any neighbour that overlaps, could merge
in, or should be kept out as a separate post. Grep `_posts/` and `_field_notes/`
for the topic and name what already exists. Nic decides whether to link, avoid,
or build on it.

**Kill switch.** If the idea is really an experiment (change one thing, measure
it), say so and hand off to `field-note-think`. Do not write an essay about an
opinion he could test.

## 2. Interview

Let him braindump first. Reflect it back in one sentence. Then one question at a
time, five to eight total, each with a recommended answer where you have one:

1. **The claim.** One sentence a reasonable peer would push back on. Test: "who
   disagrees, and what's their best argument?" Keep sharpening until it bites.
   Then offer the **uncomfortable version**: the same claim with the hedge
   removed. He can dial it back; a claim that started bold and was softened on
   purpose reads better than one that was never sharp.
2. **The reader.** Which CTO or tech lead, and what changes about their next
   Monday? If nothing changes, it is a diary entry; that is fine, aim it at
   `personal` and say so.
3. **The receipts.** Two or three concrete moments or numbers from his own work.
   Push past "sometimes teams…" to a named situation.
4. **The counterargument.** Steelman it. Decide: absorb it, or narrow the claim.
5. **The shape.** Propose **two structures**, each three to five sections with
   a one-line note on why that structure serves the claim (for example: scene →
   pattern → claim → objection → what I do now; or three moments that each earn
   part of the claim). Story up front in both. He picks or blends. Then two
   title options, plain-spoken, no clickbait.
6. **Category and links.** ai · leadership · business · career · personal. Field
   notes or older posts to reference.

**Research.** When a claim rests on a fact, a number, or "someone said", dispatch
`writing-researcher` with the slug and the exact questions. Never let a
plausible-sounding fact into the outline unverified. Findings land in
`.writings-memory/<slug>/research/`.

## 3. Write the outline

Choose the slug with Nic: lowercase, hyphens, short, the future URL
`/blog/<slug>`. Write `.writings-memory/<slug>/outline.md`:

```markdown
---
slug: <slug>
status: outline
idea: <the exact ideas.md line, or "ad hoc">
updated: YYYY-MM-DD
---

# <working title A> / <working title B>

## Claim
<one disagreeable sentence>
uncomfortable version: <the unhedged form, kept for reference>

## Reader and shift
<who, and what changes Monday>

## Receipts
- <moment or number 1 — as Nic told it, short>
- <moment or number 2>

## Counterargument
<steelman> → absorb | narrow: <how>

## Structure
chosen: <A|B|blend> because <one line>
1. <section — one line on what it does; mark the opening moment>
2. …

rejected structure: <the other option in two lines, so the plan can revisit it>

## Category and links
category: <ai|leadership|business|career|personal>
links: <paths>

## Neighbours
<ideas.md lines and posts that overlap, and what we decided>

## Spare ideas
<claims cut from this post — also appended to ideas.md as new lines>

## Reader
_pending_
```

Append every spare idea to `ideas.md` as its own line.

## 4. Cold read and approval

Dispatch `writing-reader` with `stage: outline` and the file path. Show Nic its
findings and verdict beside the outline. He adjudicates each finding; record the
outcome under `## Reader` (`accepted: …` / `rejected: … because …`) and revise
the outline if he accepts a change.

Then ask for approval of the outline as shown. One gate. On approval, set
`updated` and end with: "Outline approved. Run `/writing-plan <slug>` to expand
it in your own words." Do not start the plan.

## Judgment

- One post, one claim. Extras become spare ideas.
- Kill hedging-by-scope ("some teams, sometimes, might"). Make the claim about
  his experience and let it be small but true.
- Never invent a receipt. If he has none yet, the outline says so and the claim
  waits.
