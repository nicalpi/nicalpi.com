---
name: quick-log
description: Log a blog-post idea in one line to .writings-memory/ideas.md so it is never lost. No interview, no shaping, no questions — fire and forget. Use when Nic says "log this", "idea:", "I should write about…", or drops a thought mid-conversation. Shaping an idea into a post is /writing-outline.
argument-hint: "<idea in Nic's words>"
allowed-tools: Read, Edit
---

# Quick-log

You log. You never shape. This lane exists so that capturing an idea costs one
message and zero decisions. If you find yourself wanting to ask what the claim is,
stop: that is `/writing-outline`'s job.

## Protocol

1. Read `.writings-memory/ideas.md`.
2. If `$ARGUMENTS` is empty, use the last thing Nic said in this conversation that
   reads as an idea. If nothing does, ask once: "What's the idea, in one line?"
3. **Near-duplicate check.** If an existing unticked line covers the same idea,
   do not add a new one. Say which line matches and offer to append a note to it
   instead (` · note: <text>`). Different angle on the same topic is not a
   duplicate; log it and mention the neighbour.
4. Append one line at the bottom, today's date, Nic's wording kept (trim filler,
   never rewrite the thought), one to three `#tags` from the categories he uses:
   `#ai #leadership #business #career #personal`, plus any topic word.

   ```
   - [ ] YYYY-MM-DD · <one line, Nic's words> · #tag #tag
   ```

5. Reply with the line you added and the count of open ideas. One or two
   sentences, nothing else.

## Rules

- Never invent detail Nic did not say. A half-thought is a valid entry.
- Two ideas in one message → two lines. Say so.
- Never tick, delete or reorder existing lines here. `/writing-post` ticks.
- If the idea is an experiment (change something, measure it) log it anyway and
  add `#experiment` so `/writing-outline` can redirect to `field-note-think`.
