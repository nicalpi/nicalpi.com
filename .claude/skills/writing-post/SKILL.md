---
name: writing-post
description: Draft the full blog post from an approved plan via the writing-drafter agent, run humanizer:humanizer and a cold read, iterate with Nic through versioned drafts, and on approval freeze the text as .writings-memory/<slug>/approved.md and record what his edits taught us in memory.md. Publishing (the _posts/ file, images, commit) is /writing-publish. Use when Nic says "write the post", "draft it", or names a slug with an approved plan.
argument-hint: "[slug — defaults to the single open slug] [--date YYYY-MM-DD]"
model: fable  # edits prose in Nic's voice, arbitrates humanizer vs plan, and writes the memory entry every future draft inherits
effort: high  # applies Nic's edits in his voice and writes the memory diff
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent, Skill
---

# Writing — POST

You own drafting and approval. The drafter writes, the reader challenges, you
coordinate and Nic decides. This lane never writes to `_posts/`; it ends with a
frozen `approved.md` that `/writing-publish` turns into a page.

Read `.writings-memory/memory.md` and `.writings-memory/README.md` first.

## 1. Resolve

- Slug from `$ARGUMENTS`, else the single `.writings-memory/*/plan.md` whose
  `## Reader` is not `_pending_`. Several → ask. None → point at `/writing-plan`.
- `plan.md` missing or unapproved → stop, send him to `/writing-plan`. Never
  draft from an outline alone.
- Date: `--date` if given, else today. Confirm it in one line; it becomes the
  file name and the `date:` field.
- `drafts/` already holds versions → resume. Read the latest, restate its open
  markers and Nic's last feedback, continue at step 3.

Set `status: drafting` in `plan.md`.

## 2. Draft

Dispatch `writing-drafter` with: slug, draft version (`v1`, or next), date. It
reads plan, outline, memory and calibration posts itself. It returns the path,
word count, `[…]` markers and open choices.

Then run the **`humanizer:humanizer`** plugin skill (via the `Skill` tool) on
the draft file. It edits in place. Keep its changes unless one flattens a
deliberate choice recorded in the plan or a verbatim `> Nic:` quote; revert
those and say so. This pass is mandatory for every version that Nic sees.

Dispatch `writing-reader` with `stage: draft` and the path.

## 3. Show and iterate

Present to Nic, in this order:

1. The full draft, in a code block or by pointing at the file, never a summary.
2. The `[…]` markers with their questions, as a checklist.
3. The reader's findings and verdict.
4. The drafter's alternative titles and opening, and its open choices.
5. The **read-aloud check**, three questions for him: does any paragraph sound
   like a press release; is anything hedged that he actually believes; is
   there a sentence he would never say out loud?

He replies with edits, answers to markers, a named pass, or approval. For edits:

- **Small** (a sentence, a number, a marker answer) → apply directly to a new
  `drafts/v<N+1>.md`, keep his wording verbatim.
- **A named pass** → run only that pass, nothing else, into a new version.
  Offer these when he says "make it better" without saying how:
  `opening` (more provocative, reader slightly challenged) · `hedges` (strip
  scope hedges, keep honest ones) · `active` (passive voice → active) ·
  `cut` (remove 15% by weakest paragraph first) · `titles` (five alternatives)
  · `end` (replace any summary with the last fact).
- **Structural** (cut a section, change the opening, re-order) → re-dispatch
  the drafter for **that section only**, with the previous version, the plan's
  material for the section and his feedback as brief. Splice the result.
- **`preview`** → copy the current version to `_drafts/<slug>.md` (gitignored,
  built only with `--drafts`) and tell him: `bundle exec jekyll serve --drafts`
  then `http://localhost:4000/blog/<slug>/`. Refresh the copy on every new
  version once he has asked for it once. This never touches `_posts/`.
- **"It sounds off"** → ask what, in one question. His answer becomes a dated
  line under `## Rules Nic added` in `memory.md` immediately, before the next
  version is drafted.

Every version is a new file; never overwrite. Loop until he says the draft is
approved. Do not ask "ready to ship?" more than once per version.

A draft with unresolved `[…]` markers cannot be approved. Say so and ask for
the missing detail or a decision to cut the passage.

## 4. Freeze (after approval only, no further questions)

1. **Approved copy.** Copy the approved version to
   `.writings-memory/<slug>/approved.md`, byte for byte. Set `status: approved`
   and `updated` in `plan.md`. `_posts/` is not touched here.
2. **Update memory.** Diff `drafts/v1.md` against `approved.md`. Append under
   `## Observed edits` in `memory.md` one entry in the file's format: edit load
   (`light` = v1 or v2 approved with sentence-level changes, `medium` = one
   structural change, `heavy` = more), what he cut, what he replaced (agent
   phrase → his phrase), what he added, what risky choice survived, which reader
   findings he accepted or overrode. Be concrete; quote. If a pattern now
   appears three times across entries, promote it to `## Voice` and note the
   promotion. If the edit load was `light`, add the future post path
   `_posts/<date>-<slug>.md` to `## Calibration posts` (keep the list under
   six). Skip the diff only if v1 was approved unchanged, and say so in a
   one-line entry.
3. **Commit** `.writings-memory/<slug>/` and `memory.md` on the current branch,
   message "Approve draft: <title>". Never push.

Report the approved path, the memory entry you added, and end with: "Run
`/writing-publish <slug>` to put it on the site." Do not start publishing.

## Judgment

- Nic's edits are evidence, never noise. Even a rejected reader finding tells
  memory something; record it.
- Never invent lived detail to close a marker. Ask.
- If he approves a draft the reader marked `NOT YET`, freeze it. He
  adjudicates; note the override in the memory entry.
