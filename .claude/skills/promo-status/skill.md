---
name: promo-status
description: Show the promotion calendar for a post with checklist status — what's drafted, approved, posted. Use when Nic says "promo status", "where am I with promotion", or wants to see what's left.
argument-hint: "[slug — defaults to the single open promo plan]"
model: haiku
effort: low
allowed-tools: Read, Grep, Glob
---

# Promo — STATUS

Show where a promotion calendar stands. Read-only, no edits.

## 1. Resolve

- Slug from `$ARGUMENTS`, else find every `.promo-memory/*/plan.md`. One → use
  it. Several → list them with post titles and dates, ask which. None → "No
  active promo plans. Run `/promo-plan <slug>` after publishing a post."

## 2. Display

Read `plan.md` and scan `drafts/` and `assets/`. Show:

```
# Promo: <post title>
Post: <date> · /blog/<slug>/
Status: <plan | drafting | approved | done>

| Day | Date       | Platform | Format         | Copy | Asset | Posted |
|-----|------------|----------|----------------|------|-------|--------|
|  0  | YYYY-MM-DD | LI       | Story post     | ✓    | —     | ○      |
|  0  | YYYY-MM-DD | TW       | Hook tweet     | ✓    | —     | ○      |
|  1  | YYYY-MM-DD | TW       | Thread (6 tw)  | ✓    | —     | ○      |
|  2  | YYYY-MM-DD | LI       | Carousel       | ✓    | ○     | ○      |
…

Copy: ✓ drafted  ○ not yet
Asset: ✓ rendered  ○ needed  — not needed
Posted: ✓ done  ○ not yet

Next action: /promo-asset <slug> day 2  (carousel still needs rendering)
```

Derive "Copy" from file existence in `drafts/`. Derive "Asset" from the
plan's asset list and file existence in `assets/`. "Posted" is tracked by
`✓ posted` markers in the plan (Nic adds these manually or tells the skill).

End with the next recommended action — whichever step is blocking progress.

## 3. Mark as posted

If Nic says "I posted day 0" or similar, update the plan's calendar entries
for that day with `✓ posted` and show the updated table.

When every entry is marked posted, set `status: done` in `plan.md` and say:
"Promo complete for <title>. The `.promo-memory/<slug>/` folder can be
cleaned up whenever you like."
