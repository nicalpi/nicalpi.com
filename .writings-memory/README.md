# .writings-memory

Working state for the writing workflow (`/writing-brainstorm` → `/quick-log` →
`/writing-outline` → `/writing-plan` → `/writing-post` → `/writing-publish`). Committed on purpose: the history of how a
post was shaped is worth keeping, and it works across machines.

```
ideas.md            inbox — one line per idea, ticked when published
memory.md           how Nic writes: stable voice + observed edits, read by every drafter
<slug>/
  outline.md        /writing-outline — claim, reader, receipts, structure (status: outline)
  plan.md           /writing-plan — outline expanded with Nic's own words (status: plan)
  research/         optional web/reading notes from writing-researcher
  drafts/           v1, v2 … from /writing-post until approved
  approved.md       the frozen approved text (status: approved) — input to /writing-publish
```

`/writing-post` ends at approval: it writes `approved.md` and the `memory.md`
entry (the diff between v1 and approved is the evidence). `/writing-publish`
then creates `_posts/…`, images and the commit, ticks the idea line in
`ideas.md`, and deletes the `<slug>/` folder.

Front-matter on `outline.md` and `plan.md`:

```yaml
---
slug: <slug>
status: outline | plan | drafting | approved
idea: <the exact line from ideas.md, or "ad hoc">
updated: YYYY-MM-DD
---
```

"The current open slug" = the single `<slug>/` whose latest file is not
`published`. If more than one is open, the skills ask which.
