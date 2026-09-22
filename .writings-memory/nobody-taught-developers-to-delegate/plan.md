---
slug: nobody-taught-developers-to-delegate
status: approved
idea: "- [ ] 2026-09-12 · the delegation instinct: why CTOs who delegate to people find AI workflows natural · #ai #leadership #career · receipt (2026-09-22): seniors didn't resist the AI, they resisted delegating"
updated: 2026-09-22
title: "Nobody Taught Developers to Delegate"
subtitle: "Coding agents didn't make developers into button-pushers. Never being asked to delegate did."
description: "A senior developer on my team was handed a plan built for coding agents and spent a week typing it out by hand. Not out of defiance: nobody had ever asked them to delegate. I think that's the skill behind most \"AI turned us into button-pushers\" stories. Writing a plan someone else can execute, then checking what comes back, was never part of a developer's job. Here's how I saw the gap, why I think it's a management failure rather than a tooling one, and how our workflow forces the delegation the job never asked for."
category: Leadership
---

# Nobody Taught Developers to Delegate

Alternative title kept for the drafter: "Button-pushers are made, not hired" — now the blockquote, so not the title.

## Claim
Developers are becoming button-pushers not because AI replaced their thinking, but because nobody ever taught them to delegate: to plan for someone else, then check what came back. Their managers just told them to press enter instead.

Two halves, both carried: (1) a plan another person could execute; (2) checking what came back at the right touch points. Distinction the post must draw in section 2: a senior IC has led code, never people; someone who has handed work to a human and lived with the result is different, whatever the title.

Uncomfortable version (Nic can dial to): "AI burnout" is a CTO failure. If your team is pressing enter 13 hours a day, you handed them a subordinate and never taught them to manage one.

## Opening moment
Two-fold scene. A senior developer was handed a well-formed scope through the new workflow. Roughly a working week later, the team was asking why nothing was visible yet.

> Nic: The developer was handed a well formed plan using the new workflow, and after some implementation time, we were questioning why it was taking so long to see results. When having a catchup with them, it was clear that, while they were following the plan, they were still doing everything manually, and not leveraging the new workflow to its full potential.

> Nic: Maybe a working week after the task was started. We would have expected seeing something within a few days of implementation, and after more than a week, we were still at the "it's coming together" stage.

> Nic: In the catchup they were very open about the fact that they were struggling with the idea of forming the plan and delegating, so they reverted to manual code writing.

What happened next (the success half — plan reader finding 1):
> Nic: I decided to do some pair teaching on how to use the workflow better with him, and the ticket was restarted from the beginning.

Notes for the drafter: this is NOT a discipline story. They followed the plan. They executed by hand a plan written to be delegated, like a good IC would. Their honesty in the catch-up is the beat that makes it a delegation story. Nic's response was to sit with them and teach the delegation, not to tell them off: pair teaching, ticket restarted from scratch, regular check-ins. No name, no ticket detail. Nic's earlier words: "we decided to provide additional training and resources… and set up regular check-ins". `[…]` month or season, if Nic wants one. `[…]` how the restarted ticket went: time to first visible result vs the by-hand week, and whether it shipped through the phase stops — ask Nic in /writing-post if he has it; otherwise the post ends the scene on the restart and says the rest honestly.

## Sections

### 1. The senior who did it by hand
Purpose: open on the scene above; the quiet form resistance takes. No fight, just "it's coming together".
Material: the three quotes above. Plus the general shape of the quiet resistance from the outline interview:
> Nic: The resistance I experienced was more subtle, and it was about the senior developer wanting to feel in control of the process. They would simply ignore the workflow and AI tools for their development tasks, and continue to work in their own way. The resistance sounded like, "I don't see why we need to change our process, I've been doing it this way for years and it's worked fine."
Notes: one scene, not two. The "I've been doing it this way for years" line can be the composite voice of the resistance; the by-hand developer is the specific moment.

### 2. People who have managed humans find this natural
Purpose: the observation and the distinction (senior IC vs has-delegated-to-humans). Nic is the receipt.
Material:
> Nic: My first delegation started as I started to hire developers in my agency. It was a learning experience delegating things to other people. Most of delegation fails, in my opinion, because of a lack of understanding. The person delegating assumes that the person receiving the plan will make certain decisions, so those decisions are never surfaced (example, use this code pattern, or achieve X this way). When the person receives the delegated task and implements it, they don't have all this context and make their own decisions. This, most of the time, creates divergence between what's requested and what's produced.
Timeline: CookiesHQ, roughly 2012 — Nic: "or just say 15 years ago". `[…]` one specific hand-over where an assumed decision came back different — Nic: "can't recall". The drafter writes the mechanism in Nic's own words above and does not invent a feature; it may lean on the by-hand developer's scene as the concrete instance instead.
> Nic: Those seniors/CTOs have learned to delegate. They have learned to formalise a plan, and hand it over to other team members to execute. They have learned to trust their team members to make decisions and take ownership of their work. And most importantly they have learned to smell the right touch points, and to know when to step in and when to step back.
> Nic: They don't delegate by saying "AI, do this for me." They delegate by first intensely thinking about the problem, planning THEIR solution, and using the AI tool to execute the plan.
Notes: the "unsurfaced decisions" paragraph is the mechanism of the whole post. With a human colleague, the missing decisions at least get asked about; with an agent they get made silently. Draw that contrast.

### 3. Why ICs don't have it
Purpose: trained to do; building is the fun part; the plan in their head was only for themselves.
Material:
> Nic: Developers, ICs, were trained to DO. They were trained to write code, to implement features, to fix bugs. They were proud of their ability to produce tangible results. But, until a certain level, ICs were not trained to delegate.
> Nic: They were formalising a plan before, but only to be consumed by themselves. And most likely the plan was a rough outline of the steps to follow, not a detailed plan that can be handed over to someone else.
> Nic: Delegating, as a developer, is not a natural skill. Mostly because, for a lot of developers, building things is the fun part. It's spawned out of a desire to create, and the act of creating is what makes it fun. Delegating is not fun, and it is not a skill that is taught in school. It is a skill that is learned through experience, and it is a skill that is often learned too late in a developer's career. The best way to learn delegation is to be forced to do it.
The plan-in-the-head pattern, pre-workflow:
> Nic: We knew what we wanted to build, but we didn't have a granular plan in place. The developers would start to build, and as they went along, they would encounter new challenges and opportunities that would cause the plan to change. This often led to confusion and delays, as the team would have to constantly adjust their approach and rework parts of the codebase. It cost us time.
Notes: `[…]` no single ticket for the pattern. Nic could not name one; the post may say so plainly ("I can't point at one, it was how every feature went"). Do not invent a feature.

### 4. The extreme case: voxium's thread
Purpose: same tool, opposite experience. Management skipped the teaching, asked for volume, denied checking time.
Material (thread; quotes verified, see research/sources.md): posted 20 Sep 2026, ~7M views / ~43K likes / ~5.4K reposts on 22 Sep. "everything is made by Claude Code"; management: "pushing code is not a bottleneck, so why are we slow?"; "People are working 12 to 13 hours a day just to press enter"; "In reality, nobody is thinking anymore"; "I would not mind it, to be honest, if we were at least given the time to check out the code and see what is going where. But no, the goal is to just ship."
Cut (plan reader finding 3, Nic agreed): the Jev weekend. FOMO about model news is not the button-pusher experience; it is its own post, already logged in ideas.md ("keeping up with new models is a real cost for a CTO"). Do not use it here. Nic's general "I can feel like I'm constantly behind" line may survive as one clause of empathy, no more.
Notes: Nic will not judge voxium's experience (see Counterargument). The thread is evidence, not the frame. Prior art not to repeat: Obie Fernandez's "your resentment won't extend the runway"; Chamath's slot-machine framing; Chollet's "Delegate coding. Never delegate understanding."

### 5. The claim lands
Purpose: button-pushers are made, not hired. Nobody taught them to delegate, and the manager told them to press enter.
Material:
> Nic: This is why you see a lot of very senior developers or CTOs encouraging everyone to jump on the AI bandwagon and struggle to understand why their teams are not as productive as they expected.
> Nic: Consider a developer that was always on the receiving end of instructions, and was never trained to delegate. They may struggle to understand how to effectively leverage AI tools, and may feel overwhelmed. In my opinion this is why we are seeing a lot of developers struggling to leverage AI tools effectively or feeling like they are becoming button pushers.
> Nic: The last thing I want is for my team to become button pushers, mindlessly approving what the AI suggests without critical thinking or understanding. But it's a fine line to walk on.
Blockquote here: "Button-pushers are made, not hired."

### 6. What we do instead: the workflow as the position where you have no choice
Purpose: show delegation in both halves built into steps. This is the receipt the cold read asked for, in structural form.
Material:
> Nic: It starts with a scope. A team lead or myself will write a ticket scope: a series of explanations of what this ticket introduces, for whom, the problem we want to solve and how we envisage solving it, followed by a series of user acceptance criteria.
> Nic: This is what the developer receives, and is introduced to it with a catch-up meeting to make sure that: 1. the problem understanding is clear, 2. the outcome understanding is clear, 3. we are aligned on the plan forward.
> Nic: Then the developer runs our /dev-plan command on the issue. The dev-plan command requires the developer to explain HOW they would approach the task, in which order, the gotchas, the things not to miss and which pattern/libraries they may decide to use. The /dev-plan command has the responsibility to encode the developer's thinking, before passing it to builder agents.
> Nic: When agents are done with one of the phases of the plan, they stop and ask the developer to review the code. They won't progress without approval. This is the occasion for the developer to steer, phase by phase, the shape of the feature.
> Nic: In the final part, one agent is responsible for running a visual Q&A of the implementation and asks the developer to check the implementation as well.
> Nic: Our workflow has been designed in a way that it will enforce some critical thinking time and input from the team and individuals. We leverage the tools, but we don't delegate the decision-making to them.
Map for the drafter (do not write it as a framework, write it as what happens): scope + three-point catch-up = the unsurfaced decisions get surfaced; dev-plan = the developer's plan written for someone else, the thing ICs never had to do; phase stops = the touch points, the checking half voxium was denied; visual QA = last check. Introduce each before referencing it (memory rule 2026-09-15).
Then the outcome, from the last post, one line with link: the 50-odd tickets, low rejection rate, seniors who resisted saying they do a better job.
`[…]` one named ticket that went scope → dev-plan → phases → accepted, if Nic wants it; otherwise the process description carries the section.

### 7. Counterarguments
See below. Order: checking time (main), the 13-hour day, "seniors always did this" (one line + link).

### 8. Ending
See Ending.

## Counterargument
Main: "Your developers may plan fine. The button-pusher is made when nobody budgets time to check what came back." Absorb: delegation is planning and checking; the phase stops are the checking half; Amba is building the right side (QA, release) now.
> Nic: I can't say anything about his experience really. I personally don't understand their management team's experience. I would have a lot to say to them really. If your team is unhappy, why are you not trying to change the way of working, adapting to keep morale up?
Second: "It's the 13-hour day, not the missing plan."
> Nic: Management has to be responsible for the workloads and their impact on the team. If management is demanding a 13-hour day, it indicates a deeper issue with how work is being assigned and prioritised.
Absorb, concretely (restored from outline): the workflow is the management decision about where the saved time goes. At Amba the time saved on typing went into planning and checking, not into more tickets — link to /blog/ai-measuring-wrong-thing ("the time we've saved on writing code is going back into planning what we write"). Not into 13-hour days.
Third: "You're a 30-year veteran describing what seniors always did." One line, link to /blog/ai-measuring-wrong-thing where it was absorbed. Not re-argued.
Placement: section 7, after the workflow.

## Quotable line
> Button-pushers are made, not hired.

## Ending
Two new developers are joining the team soon. Nic will have to teach delegation from day one and does not yet know what that looks like.
> Nic: We're soon getting 2 new developers to join our team, so we will see what it looks like. In the past, it was easy: you would give them some small/light tickets that you know would touch a broad surface of the app, to let them loose and discover. No idea what it will look like today.
(From his LinkedIn reply, 16 Sep 2026.) `[…]` start date, if he wants one.
The bet stays available as a one-liner earlier, not the ending:
> Nic: My role as a CTO is to look forward. My bet (and I accept I can be wrong) is that writing code by hand is a skill that will be less and less valuable in the future.

## Gaps
- [ ] Month or season of the by-hand scene, if Nic wants to date it (section 1)
- [ ] How the restarted ticket went after the pair teaching: time to first visible result, did it ship through the phase stops (section 1 → carries into section 6)
- [ ] One CookiesHQ hand-over where an assumed decision came back different — Nic can't recall; drafter must not invent (section 2)
- [ ] One named ticket for the pre-workflow plan-morphed pattern, or the post says plainly it can't pick one (section 3)
- [ ] Start date of the two new developers (ending)

## Reader
verdict: NOT YET (2026-09-22) — three findings, all accepted by Nic and applied. Plan approved by Nic 2026-09-22.
- accepted 1 (no success moment): added what happened after the catch-up — pair teaching, ticket restarted from the beginning. Outcome of the restart is a named gap for /writing-post, not an invention.
- accepted 2 (mechanism on a date, not a moment): asked; Nic can't recall a specific CookiesHQ hand-over. Recorded as a gap with a no-invent instruction; the by-hand scene stands in as the concrete instance.
- accepted 3 (Jev argues a different thing): Jev cut from this post, kept for its own (already in ideas.md). Concrete absorb for the 13-hour-day counterargument restored with the link to the last post.
- Nic (unprompted): description must not reference the viral thread. Description and subtitle rewritten to open on the by-hand developer instead.
