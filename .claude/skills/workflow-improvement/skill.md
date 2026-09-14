---
name: workflow-improvement
description: Apply an improvement to the writing or promo workflow skills. Takes a finding (what went wrong or could be better) and edits the skill files directly. Use when Nic says "improve the workflow", "fix this in the skill", "the outline should…", "next time the drafter should…", or names a specific improvement. Also use when you spot something yourself mid-session.
argument-hint: "[description of what to improve — a finding, a pattern, a rule]"
model: opus
effort: medium
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion
---

# Workflow improvement

You take one improvement finding and apply it directly to the skill files.
No intermediate file, no backlog — straight into the skills.

## 1. Understand the finding

From `$ARGUMENTS` or the conversation context, extract:

- **What happened** — the concrete problem or missed opportunity.
- **Which stage** — which skill or agent was responsible.
- **The fix** — what should change, and where.

If the finding is vague ("the outline was slow"), ask one question to make it
actionable: "What specifically should change?" Don't proceed until you have a
concrete fix.

If no argument is given, scan the current conversation for any moments where:
- Nic corrected an approach ("no, don't do that", "that's not what I meant")
- A skill produced something that needed rework
- A step took longer than it should have
- Something was caught late that should have been caught early
- A pattern repeated that should be codified

Present what you found and ask which to apply.

## 2. Locate the target

The workflows and their files:

**Writing pipeline:**
- `.claude/skills/writing-outline/skill.md` — idea → claim + structure
- `.claude/skills/writing-plan/skill.md` — outline → Nic's words verbatim
- `.claude/skills/writing-post/skill.md` — plan → drafted + approved post
- `.claude/skills/writing-publish/skill.md` — approved → live on site
- `.claude/skills/writing-brainstorm/skill.md` — finding what to write
- `.claude/skills/quick-log/skill.md` — one-line idea capture
- `.claude/agents/writing-drafter.md` — the drafting agent
- `.claude/agents/writing-reader.md` — the cold-read agent
- `.claude/agents/writing-researcher.md` — the research agent
- `.writings-memory/memory.md` — voice + observed edits

**Promo pipeline:**
- `.claude/skills/promo-plan/skill.md` — post → angles + calendar
- `.claude/skills/promo-draft/skill.md` — calendar → platform copy
- `.claude/skills/promo-asset/skill.md` — copy → visual assets
- `.claude/skills/promo-status/skill.md` — checklist view
- `.claude/agents/promo-drafter.md` — the social copy agent
- `.promo-memory/memory.md` — social voice + what works

**Shared:**
- `.claude/skills/social-image/skill.md` — v4 brand image generation
- `.claude/skills/nicalpi-brand/` — brand system

Read the target file before editing. Always.

## 3. Apply the fix

Make surgical edits to the skill files. Rules:

- **Add, don't rewrite.** Insert the new guidance at the natural point in the
  skill — after the step it improves, or in the Judgment section if it's a
  general principle.
- **One finding, one edit location.** If a fix applies to multiple skills
  (like "mine the interview for ideas" applied to outline, plan, and post),
  edit each one, but keep each edit self-contained.
- **Match the file's voice.** Skill files are terse instructions, not
  documentation. Write the fix the way the rest of the file reads.
- **Include the why.** A one-line parenthetical with the problem: "(In the
  first run, the day-0 and day-4 LinkedIn posts both retold the full arc.)"
  Future readers need the reason to know when the rule applies and when to
  break it.
- **If the fix is about voice or Nic's preferences**, it goes in
  `.writings-memory/memory.md` (under `## Rules Nic added` with today's date)
  or `.promo-memory/memory.md` (under `## Social voice`), not the skill file.
- **If the fix is a new extraction, question, or format**, it goes in the
  skill file.

## 4. Report

After editing, report in this format:

```
**Improvement:** <one-line summary>
**Files edited:**
- `<path>` — <what changed, one line>
- `<path>` — <what changed, one line>
**Why:** <the problem it fixes, one line>
```

No follow-up questions after applying. The improvement is live.

## Judgment

- If Nic names a rule about his voice ("don't do X in my posts"), save it to
  `memory.md` under `## Rules Nic added` with today's date — that's where
  the drafter reads it. Only put it in the skill if it changes the workflow's
  *structure*, not just the output's *tone*.
- Never delete existing guidance to make room for new guidance. If two rules
  conflict, flag it to Nic.
- An improvement that would change the pipeline's shape (adding a new stage,
  removing an approval gate, changing which agent does what) needs Nic's
  confirmation before applying. A fix within an existing stage does not.
- Don't batch. One finding per invocation. If there are five things to fix,
  call the skill five times or list them and let Nic pick.
