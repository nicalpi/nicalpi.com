---
slug: nobody-taught-developers-to-delegate
status: outline
approved: 2026-09-22
idea: "- [ ] 2026-09-12 · the delegation instinct: why CTOs who delegate to people find AI workflows natural · #ai #leadership #career · receipt (2026-09-22): seniors didn't resist the AI, they resisted delegating"
updated: 2026-09-22
---

# Nobody taught developers to delegate / Button-pushers are made, not hired

## Claim
Developers are becoming button-pushers not because AI replaced their thinking, but because nobody ever taught them to delegate: to plan for someone else, then check what came back. Their managers just told them to press enter instead.

Delegation here has two halves and the post must carry both: (1) write a plan another person could execute; (2) check what came back at the right touch points. Voxium's complaint is about the second half being denied.

Key distinction (reader finding 1): a **senior IC** has led code but never led people. Someone who has **actually handed work to another human and lived with the result** is a different animal, whatever their title. The Amba seniors who quietly resisted were the first kind; the CTOs who find agents natural are the second. Say this in section 2 or the opening argues against the thesis.

uncomfortable version: "AI burnout" is a CTO failure. If your team is pressing enter 13 hours a day, you handed them a subordinate and never taught them to manage one.

## Reader and shift
The CTO or head of engineering who has rolled out coding agents, reads voxium's thread and recognises a bit of their own team in it. Monday shift: stop measuring the rollout by how fast people press enter; look instead at whether each developer can write a plan another person could execute, and whether they are given the time to check what came back. If not, that is the coaching (and the budgeting) to do before buying more tooling.

## Receipts
- **Voxium's thread** (X, 20 Sep 2026, ~7M views, ~43K likes, ~5.4K reposts, ~1.8K replies): two weeks into a big-company role, everything from PRDs to tests made by Claude Code, management says "pushing code is not a bottleneck, so why are we slow?", people working 12–13 hours "just to press enter", "nobody is thinking anymore". Key line: he would not mind "if we were at least given the time to check out the code". Obie Fernandez already replied with a "your resentment won't extend the runway" essay — the guru response is taken. Numbers and the "time to check out the code" line verified by direct read of the page on 22 Sep 2026; press (Business Insider, dev.by) confirms the main quotes and had "nearly 5 million views" on Monday morning. See research/sources.md.
- **Nic's own overwhelm, current**: Jev, released 15 Sep 2026 by TypeSafe AI (a "System One Model" returning typed values with confidence scores — NOT a coding LLM, don't frame it as a Claude Code rival; TechCrunch 18 Sep). He "immediately felt behind" and spent a few hours reading docs to work out whether it fits the product or the workflow. He has been in voxium's camp too.
- **The quiet resistance at Amba**: no loud "I won't". Seniors simply ignored the workflow and the tools and kept working their own way. It sounded like: "I don't see why we need to change our process, I've been doing it this way for years and it's worked fine." They wanted to feel in control. Months later, the same people said they were doing a better job (see last post).
- **The plan-in-the-head pattern**: before the workflow, "we knew what we wanted to build but didn't have a granular plan"; developers built, hit new things, the plan morphed, rework and delays followed. `[…] no single ticket named — either find one before the plan stage, or the post says plainly "I can't name one, it was every ticket"`
- **The workflow taught delegation — receipt needed (reader finding 2)**: `[…] plan-stage task: one plan a developer wrote that the agent or a colleague executed without a conversation. The "doing a better job" line is borrowed from the last post and is not enough on its own. If none exists, the post says so plainly.`
- **Nic's own words to keep**: "they were formalising a plan before, but only to be consumed by themselves"; "building things is the fun part, delegating is not fun, it isn't taught in school, it's learned through experience and often too late"; "the best way to learn delegation is to be put in a position where you have no choice"; seniors/CTOs "have learned to smell the right touch points, when to step in and when to step back"; they "don't delegate by saying 'AI, do this for me'. They delegate by intensely thinking about the problem, planning THEIR solution, and using the tool to execute the plan."
- **The bet, hedged honestly**: "My role as a CTO is to look forward. My bet (and I accept I can be wrong) is that writing code by hand will be less and less valuable."

## Counterargument
1. **(main, reader finding 3)** "Your developers may plan fine. The button-pusher is made when nobody budgets time to check what came back." Voxium says it himself: he would not mind if he had time to check the code. → absorb: delegation is planning *and* verification. Nic's "smell the right touch points, when to step in and when to step back" is the second half. A workflow that forces the plan but not the check is half a workflow; Amba is "attacking the right side" (QA, release) now for exactly this reason.
2. "The problem in voxium's thread is the 13-hour day, not the missing plan." → absorb: management owns the workload. A 13-hour day means work is being assigned and prioritised badly. The workflow *is* the management decision: the time saved on typing goes into planning and checking, not into more tickets (links to the last post).
3. "You're a 30-year veteran describing what seniors always did." → one line and a link to the last post, where it was already absorbed. Not re-argued here.

Prior art to be aware of, not repeat: François Chollet, "Delegate coding. Never delegate understanding" (x.com/fchollet/status/2102166631439053014); Obie Fernandez's reply; Chamath's "slot machine" framing. Nic (22 Sep): prominent people will land on similar thoughts; the post's angle is a team and a workflow, not a maxim.

Misconception corrected: resistance to AI workflows is assumed to be loud and about fear of replacement. At Amba it was silent and about control.

## Structure
chosen: B because every section is about one skill and the viral thread becomes evidence, not the frame.
1. **Opening moment**: a senior developer, quietly not using the workflow. "I've been doing it this way for years and it's worked fine." No fight; they just carried on.
2. The observation: people who have actually managed other humans take to agents naturally and can't understand why their teams don't. Draw the line here: senior IC (led code, never led people) vs someone who has handed work over and lived with the result. What the second group has: plan → hand over → check touch points → step back. Both halves.
3. Why ICs don't have it: trained to DO; building is the fun part; the plan in their head was only ever for themselves, a rough outline that morphed as they built. `[…]` pattern receipt.
4. The extreme case: voxium's thread. Same tool, opposite experience. Management skipped the teaching, asked for volume, and denied the checking time. Nic's own Jev evening sits here too: he knows the overwhelm from the inside.
5. The claim lands: button-pushers are made, not hired. Nobody taught them to delegate (plan for someone else, then check), and the manager told them to press enter.
6. What Amba did instead: the workflow as the position where you have no choice but to plan before you build. Not "AI, do this", but think, plan your solution, hand it over. `[…]` one concrete plan-handed-over receipt. Seniors came round because the work felt better, not because they were told to.
7. Counterarguments: it's the checking time, not the planning (yes — delegation is both, and that is the half we're building now); it's the 13-hour day (yes, and that's management's job, and the workflow is how you spend the saved time); seniors always did this (one line, link).
8. Last fact: the bet, and that he accepts he may be wrong.

rejected structure: A — open on voxium and the Jev evening side by side ("I've been in both camps"), then Amba, then the claim. Reader meets the misery first, the diagnosis second. Kept in case the plan stage finds the opening in B too quiet.

## Category and links
category: leadership
links: /blog/ai-measuring-wrong-thing (workflow, "seniors always did this" pushback, scoping vs delivery planning); /blog/if-you-cant-explain-the-code-ai-is-not-helping (the individual principle this extends); the voxium thread https://x.com/v0xium/status/2101526107128529120

## Neighbours
- `_posts/2026-09-12-ai-measuring-wrong-thing.md` treats the resistance as a one-paragraph footnote to the metric argument. This post makes it the whole subject; link, don't repeat.
- ideas.md "the best hiring signal I've found is a 30-minute plan for a fake checkout" — the hiring side of the same skill, next week's post. One foreshadowing sentence at most.
- ideas.md "it's too long to read, I'll have to trust you" — where delegation fails for the delegator. Keep out; separate post.
- ideas.md "onboarding new developers in the agentic era" — field-note candidate; keep out.

## Spare ideas
- Every developer is becoming a mini team of their own, from scoping to QA to testing, each handing better input to the next person in the chain. (Nic's phrase; too big for this post.)
- Keeping up with models, tools and frameworks is a real cost for a CTO, and nobody budgets for it. (The Jev evening as its own personal post.)

## Reader
verdict: NOT YET (2026-09-22) — all three findings accepted by Nic and applied; outline approved by Nic 2026-09-22.
- accepted 1: opening vs section 2 contradiction → senior IC / has-managed-humans distinction added to Claim and section 2.
- accepted 2: mechanism has no receipt → plan-stage task added to Receipts and section 6 (`[…]` one plan handed over and executed without a conversation).
- accepted 3: voxium's complaint is verification, not planning → claim widened to both halves of delegation; new main counterargument; "seniors always did this" reduced to a link.
- Nic: "Obviously there will be prominent people that will have the same thoughts" — Chollet et al noted as prior art, not a reason to change the angle.
