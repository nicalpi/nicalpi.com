# .writings-memory

Working state for the writing workflow (`/quick-log` → `/writing-outline` →
`/writing-plan` → `/writing-post`). Committed on purpose: the history of how a
post was shaped is worth keeping, and it works across machines.

```
ideas.md            inbox — one line per idea, ticked when published
memory.md           how Nic writes: stable voice + observed edits, read by every drafter
<slug>/
  outline.md        /writing-outline — claim, reader, receipts, structure (status: outline)
  plan.md           /writing-plan — outline expanded with Nic's own words (status: plan)
  research/         optional web/reading notes from writing-researcher
  drafts/           v1, v2 … from /writing-post until approved
```

A `<slug>/` folder is deleted by `/writing-post` once the post is approved and
written to `_posts/`. Its idea line in `ideas.md` is ticked in the same step and
`memory.md` gains what the approval edits taught us.

Front-matter on `outline.md` and `plan.md`:

```yaml
---
slug: <slug>
status: outline | plan | drafting
idea: <the exact line from ideas.md, or "ad hoc">
updated: YYYY-MM-DD
---
```

"The current open slug" = the single `<slug>/` whose latest file is not
`published`. If more than one is open, the skills ask which.
