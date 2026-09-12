---
slug: ai-measuring-wrong-thing
status: outline-approved
idea: "- [ ] 2026-09-12 · ai leadership in Amba · #ai #leadership #business"
updated: 2026-09-12
---

# If You're Measuring AI by Speed, You're Measuring the Wrong Thing / The AI Productivity Gain No One Talks About

## Claim
If you're measuring AI's value by how fast it writes code, you're measuring the wrong thing.
uncomfortable version: The biggest AI productivity gain isn't code generation — it's the shaping and delivery planning that happens before anyone writes a line of code. The time you save writing code, you put back into planning. That's the point.

## Reader and shift
Tech leaders, CTOs, or CEOs of small companies (10–30 people) who are introducing AI tools or wondering why their AI introduction isn't delivering. After reading: they stop chasing velocity metrics and start looking at their ticket-writing and delivery-planning process. They reallocate saved time into shaping, not more output.

## Receipts
- The sensor API story: customer support made an urgent request for a couple of APIs on an already-integrated sensor. Scoped with the workflow in the morning, discovered a silent token-refresh bug in the existing implementation along the way, delegated the build in the afternoon, deployable by evening. Nic didn't write the code but shaped the solution — and still felt ownership. 15 years of delegating plans to people meant delegating to the workflow felt natural.
- The "before" pattern: no dedicated product manager, so developers wrote tickets assuming full context. Most of the time, the builder lacked detail. Time lost at build stage as context was uncovered, and at QA when missed opportunities surfaced.
- The investor framing: when Nic proposed the AI workflow internally, the initial expectation was "more productive." He made the KPI clear upfront — not velocity, but precision. Fewer rejects, fewer half-built features, the extra mile on what they shipped. [...no hard before/after numbers — lean on qualitative team feedback and the honest hedge: "I don't have a dashboard to prove it."]
- Developer retro feedback: team members commented that the workflow forces them to think more at the delivery-planning stage — not because it gets in the way, but because it understands how they work and what matters to them.

## Counterargument
"You're a CTO with 15 years of experience — of course shaping is where you add value. For a mid-level developer, code generation speed IS the win. You're just describing what senior engineers have always done, but calling it an AI workflow."
→ absorb: Yes, it is what senior engineers have always done. But the workflow makes it the default for everyone, not just the person with 15 years of experience. Developers confirmed in retros that the workflow forces better delivery planning at their level too. The counterargument is fair for scoping (CTO's job), but delivery planning is the developer's job — and that's where the workflow changed their behaviour.

## Structure
chosen: B (the misconception) because it leads with what the reader gets wrong and they recognise themselves immediately. Faster to the point than the chronological journey.

1. **The investor conversation** — open with the concrete moment: Nic proposing the AI workflow to leadership, and setting the KPI as precision, not velocity. The question everyone asks ("how much faster?") is the wrong one. Scene first, thesis earned.
2. **The sensor API story** — what "better" looks like instead of "faster." Scoped in the morning, found a silent bug along the way, built in the afternoon, deployable by evening. Ownership without writing code. The detail that makes "precision over speed" concrete.
3. **What we tried first** — the free-exploration phase. No mandates, let people discover tools. Mixed results: some embraced, some didn't. PRs varied wildly. The missing-context ticket problem (no PM, assumptions about context, time lost at build and QA). Not a leadership failure to let people explore — but someone needs to look at it holistically.
4. **Where AI actually helps** — shaping and delivery planning, not code generation. The workflow: shaping (hybrid, developer-led, AI-assisted) → building (AI writes, humans review) → review gate. The bulk of the work is pre-code. Developer retro quotes: the workflow forces better delivery planning because it understands how we work.
5. **The reinvestment** — the time you save writing code, you put back into planning. Not a measured stat — a principle. "I don't have a dashboard to prove it, but the retros tell me something changed." The workflow encapsulates years of good engineering practices, just leveraged with AI. It feels like proper pair programming from beginning to end, not a tool you adapt to.

rejected structure: A (the journey) — chronological, opens with sensor API story then walks through the full experience. Warmer start but takes longer to reach the claim. Could work for a longer piece or a series, but for a single post, B is tighter.

## Category and links
category: ai
links: _posts/2026-01-17-if-you-cant-explain-the-code-ai-is-not-helping.md (companion — individual developer angle vs. this leadership angle)

## Neighbours
- "ai leadership in Amba" (ideas.md #1) — this post
- if-you-cant-explain-the-code-ai-is-not-helping — distinct: that post is about individual developers understanding their code, this one is about how leaders introduce AI to teams. Natural link, no overlap in claim.

## Spare ideas
- The AI workflow in detail: shaping → building → review, the tooling specifics, how each phase works (separate "how-to" post, not this one)
- AI and the death of the product manager: when your AI workflow does what a PM used to do (ticket quality, context capture) — what does that mean for the role?
- The delegation instinct: why CTOs who are used to delegating to people find AI workflows natural, and why individual-contributor developers might struggle with it differently

## Reader
cold read 2026-09-12, stage: outline

1. "50% rule has no receipt" → accepted: softened to a principle ("the time you save, you put back into planning"), not a measured stat. No false precision.
2. "Precision KPI stated but never shown" → accepted: marked gap with [...], will lean on qualitative team feedback and the honest hedge "I don't have a dashboard to prove it."
3. "Opening overlaps with January post" → accepted: section 1 now opens with the investor conversation (a scene), not the thesis. The January post becomes a companion link, not a repeat.
