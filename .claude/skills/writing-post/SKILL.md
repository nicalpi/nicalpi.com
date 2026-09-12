---
name: writing-post
description: Draft the full blog post from an approved plan via the writing-drafter agent, run the humanizer and a cold read, iterate with Nic, and on approval write it to _posts/, generate the OG image, tick the idea in ideas.md, update memory.md with what his edits taught us, and delete the .writings-memory/<slug>/ folder. Use when Nic says "write the post", "draft it", or names a slug with an approved plan.
argument-hint: "[slug — defaults to the single open slug] [--date YYYY-MM-DD]"
model: fable
effort: high
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent, Skill
---

# Writing — POST

You own drafting, approval and shipping. The drafter writes, the reader
challenges, you coordinate and Nic decides. Nothing reaches `_posts/` before his
explicit approval of a draft he has seen in full.

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

Then run the `humanizer` skill on the draft file (in Claude Code, the plugin
skill; it edits in place). Keep its changes unless one flattens a deliberate
choice recorded in the plan.

Dispatch `writing-reader` with `stage: draft` and the path.

## 3. Show and iterate

Present to Nic, in this order:

1. The full draft, in a code block or by pointing at the file, never a summary.
2. The `[…]` markers with their questions, as a checklist.
3. The reader's findings and verdict.
4. The drafter's open choices.

He replies with edits, answers to markers, or approval. For edits:

- **Small** (a sentence, a number, a marker answer) → apply directly to a new
  `drafts/v<N+1>.md`, keep his wording verbatim.
- **Structural** (cut a section, change the opening, re-order) → re-dispatch the
  drafter with the previous version and his feedback as extra brief.

Every version is a new file; never overwrite. Loop until he says the draft is
approved. Do not ask "ready to ship?" more than once per version.

A draft with unresolved `[…]` markers cannot be approved. Say so and ask for
the missing detail or a decision to cut the passage.

## 4. Ship (after approval only, no further questions)

1. **Post file.** Copy the approved draft to `_posts/<date>-<slug>.md`. Front
   matter as the drafter wrote it; verify `layout: post`, `category` capitalised,
   `og_image: /assets/images/og/<slug>.jpg`, `reading_time` honest at ~200 wpm.
   No `title_html`.
2. **OG image.** `python3 scripts/generate-og.py <slug>` then
   `python3 scripts/generate-og.py <slug> --check`. Report the output; if it
   fails, say so and continue, the post still ships.
3. **Build check.** `bundle exec jekyll build` and confirm `_site/blog/<slug>/`
   exists. Report failures verbatim.
4. **Tick the idea.** In `.writings-memory/ideas.md`, change the matching line
   from `- [ ]` to `- [x]` and append ` → /blog/<slug>`. Match on the `idea:`
   front-matter field; for `ad hoc`, add a ticked line dated today.
5. **Update memory.** Diff `drafts/v1.md` against the approved version. Append
   under `## Observed edits` in `memory.md` one entry in the file's format: what
   he cut, what he replaced (agent phrase → his phrase), what he added, what
   risky choice survived. Be concrete; quote. If a pattern now appears three
   times across entries, promote it to `## Voice` and note the promotion. Skip
   the entry only if v1 was approved unchanged, and say so in a one-line entry.
6. **Clean up.** `git rm -r .writings-memory/<slug>/` (or `rm -rf` if untracked).
   The post and memory are the durable record.
7. **Commit.** Stage `_posts/<file>`, `assets/images/og/<slug>.jpg`,
   `.writings-memory/ideas.md`, `.writings-memory/memory.md`, and the deleted
   folder. Commit on the current branch with a message naming the post title.
   Never push.

Report: post path, URL `/blog/<slug>`, OG status, build status, the memory
entry you added, and the commit hash. Then stop.

## Judgment

- Nic's edits are evidence, never noise. Even a rejected reader finding tells
  memory something; record it.
- Never invent lived detail to close a marker. Ask.
- If he approves a draft the reader marked `NOT YET`, ship it. He adjudicates;
  note the override in the memory entry.
