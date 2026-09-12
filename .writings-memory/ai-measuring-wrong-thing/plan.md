---
slug: ai-measuring-wrong-thing
status: approved
idea: "- [ ] 2026-09-12 · ai leadership in Amba · #ai #leadership #business"
updated: 2026-09-12
title: "If You're Measuring AI by Speed, You're Measuring the Wrong Thing"
subtitle: "The productivity gain no one talks about"
description: "Most teams measure AI's value by how fast it writes code. After a four-month experiment with my eight-person development team, I found the real gain was elsewhere: in shaping, delivery planning, and the quality of what gets shipped. The speed you save writing code, you reinvest into planning. That's the point."
category: AI
---

# If You're Measuring AI by Speed, You're Measuring the Wrong Thing

## Claim
If you're measuring AI's value by how fast it writes code, you're measuring the wrong thing. The biggest AI productivity gain isn't code generation — it's the shaping and delivery planning that happens before anyone writes a line of code. The time you save writing code, you put back into planning. That's the point.

## Opening moment
> Nic: The initial conversation was with Stuart, my CEO, on one of our regular catchups over video call. Early 2026. I was explaining that I was going to delay our tech hiring plan because I wanted to make sure I fully understood what the impact of AI would be on our team. Initially, I didn't know or even envisaged that we would be, seven months later, talking about having an almost fully automated workflow helping us deliver.
>
> Stuart is a sharp CEO, ex-engineer, and well versed in AI — I don't want to frame it as him only seeing the cost-saving angle, because that's far from the truth. But the productivity question was mandatory, and initially I didn't have a realistic answer. I didn't know what the result of our experiment would be.
>
> Post-experiment, I was clearer about our direction. When I introduced the developer-attended workflow, the obvious question about productivity impact came again. Stuart half-joked, based on what people say on the internet, "Oh, so now each developer can be 10x developer and produce more?" I understood the joke, but I said I wasn't massively interested in "10x productivity" improvement. Maybe we would, optimistically, improve productivity by 1.25 or 1.5, because now we had autonomous agents dealing with smaller items. But I reinstated that my biggest KPI and driver was precision and problem solving for our customers. I didn't want us to push more tickets — I wanted us to spend more relative time on a ticket, and when a ticket was pushed it would be solving more and better.

## Sections

### 1. The investor conversation
Purpose: Open with the concrete moment — Nic proposing the AI workflow to leadership, the "10x" joke, and his answer. The question everyone asks ("how much faster?") is the wrong one. Scene first, thesis earned.
Material:
> Nic: [see Opening moment above — same scene, same exchange]
Notes: Stuart is CEO, ex-engineer, well versed in AI. Don't caricature him as a bean-counter. The "10x" joke is his, the "1.25 or 1.5" is Nic's honest number. The hiring delay is the setup — Nic chose to understand before scaling.

### 2. The sensor API story
Purpose: What "better" looks like instead of "faster." A real problem surfaced, traced, fixed, and shipped — with a bonus escape hatch that was never needed.
Material:
> Nic: We'd had a hunch for a few weeks that we had issues on one of our partner sensor's token refresh logic — it would sometimes leave sensor tokens as dead tokens. The only solution when it happened was to regenerate a new token, but we didn't expose any option in the interface for customer support to do that. They had to manually disconnect and reconnect the sensor on our platform.
>
> The hunch was confirmed when we investigated exposing a "regenerate token" option. We found a race condition between token generation and consumption that could leave tokens dead. It was silent because the sensor would still be sending data and we could ingest it, but we couldn't access deeper data via the API.
>
> Within the same couple of days we had the hunch of a problem, and then support exposing us the problem because they needed to regenerate tokens regularly.
>
> I used our newly done AI workflow to expose the issues, gave it the API endpoints we needed to integrate, and together we traced the issues and decided on the plan of attack — fixing the issue as much as possible and giving support the option, in app, to regenerate the token if it happened again.
>
> The irony is that our fix is now solid, and that option to regenerate token has, so far, never needed to be used.
Notes: The irony is the punchline — the fix was so good the escape hatch sits unused. Don't over-explain the technical detail; the reader needs to feel "silent bug found, fixed properly, shipped" — not understand the token refresh protocol. The workflow agent wrote the entire code. Nic shaped the solution and traced the issue; the agent built the fix. The "couple of days" was the discovery window: the team had a hunch about token issues, and within the same couple of days support raised the need for token regeneration (their need was caused by the same underlying bug). The build itself was fast once the plan was set.

### 3. What we tried first
Purpose: The free-exploration phase. Let people discover tools, mixed results, the "naked" approach was the real problem. Sets up why the workflow was necessary.
Material:
> Nic: The exploration phase was structured on a four-month window. Two months where people would try the tools they wanted, and two months to decide which tool would be our primary tool and apply, at the very least, proper security measures to the chosen tools. Initially — and I was wrong — I assumed our initial finding was going to be about finding the winning tool between Claude Code, Codex, Gemini and Copilot and then going along with it "naked."
>
> The output was very depending on the developer using the tool. Some were extremely sharp at using them and were doing an OK job, but some developers were trusting the tools too much and sending back to us mountains of code we had to reject.
>
> As we were reviewing all these tools and their output, this is when we realised that the "naked" approach was going to be the issue for us. Because these tools, while good at writing code, had no idea how we wanted them to work. So I approached my workflow creation almost as if I was documenting for a team of new project managers, business analysts, developers and QA to join our team — explaining to each of them how we wanted them to work with us.
Notes: "I was wrong" is important — he admits the initial assumption. "Mountains of code we had to reject" is the visceral detail. The "new team" analogy is a candidate quotable line. Don't name the tools that lost — the post isn't a tool review.

### 4. Where AI actually helps
Purpose: Shaping and delivery planning, not code generation. The before/after of ticket quality. Developer retro feedback.
Material — the "before":
> Nic: Before, say our team has been talking about integrating a new sensor for data already in our catalogue. The "ticket" and scope would probably have looked something like: "Integrate with Sensor X" — a link to API documentation, five or ten lines of what we know about the integration and the data ingestion that should happen. And that was about it.
>
> This was assuming that a couple of conversations with the developer about this work, and the fact that we already had the data points in our catalogue, was enough to make all decisions.
>
> The reality — and we knew about it — was that developers were often confused midway through the ticket because there were obviously unexpected decisions to make. QA had no clear acceptance criteria and no context of what the sensor was doing. And more importantly, we were probably skipping the part that would push us to think more about this new integration and what it would mean for the product as a whole.

Material — the "after":
> Nic: Today, if we tell our workflow we need to integrate with this sensor, here's the documentation and the blurb about what we know — the flow will actually read the full documentation with our code as context reference, build us a multi-card epic about the new integration starting with connecting the sensor to the platform, then data ingestion, then data rendering. It creates clear user stories for every sub-ticket and clear QA acceptance criteria. Following that scoping part, it helps the developers create a locked-in delivery plan, ticket per ticket.

Material — developer feedback:
> Nic: It was different feedback times and moments, all by senior developers. I don't remember word for word, but every single developer in my team — even the ones that were resistant initially about the workflow introduction because they liked to "feel in control" — all said after a few months that they saw massive benefits. To me, the best feedback is still that they felt empowered and feel like they are doing a better job with it, while not losing ownership of what is built.
Notes: No word-for-word developer quotes — don't invent them. The resistance-to-buy-in arc ("feel in control" → "empowered") is the story. The before/after ticket contrast is the proof. No dedicated PM on the team — that's context, not a complaint. The workflow does what good ticket-writing would have done, but makes it the default.

### 5. The reinvestment
Purpose: The time you save writing code, you put back into planning. Own the fact that there are no hard metrics yet — that's the honest position, and it's temporary. End on what's next.
Material:
> Nic: [the "1.25 or 1.5" number from the opening — not 10x, but honest]
> Nic: I don't have clear metrics yet, only what's in front of me day to day. But we're working on getting those metrics embedded now in the workflow.
Notes: The honest hedge is the receipt here: "I don't have clear metrics yet" is stronger than pretending. The fact that they're actively building measurement into the workflow is the forward motion. Don't dress it up — own it. Fold the reinvestment principle into section 4's ending rather than making it a standalone argument if the drafter finds this section thin. The outline's "delivery planning is the developer's job, and that's where the workflow changed their behaviour" is the sharper counterargument line — keep it.

Material — the counterargument response (weave in, don't make a separate section):
> Nic: My view is that writing code entirely by hand is becoming less prevalent as a developer, at least while AI is around. So my role as a CTO is to empower my team to understand what's happening and make sure they are ready for this change. Even if I was already spending time before helping them become sharper planners and delegators, it is now mandatory for them to become extremely good at this skill. Being able to understand the problem and translate it into a clear actionable plan was a very desirable skill in a developer — but it's now becoming mandatory if they want to be productive with AI. I'm not saying the workflow will do that for them, but it will help them see things they might have missed. It's my role as the CTO to up-skill my team and prepare them for the new world we're in.
Notes: Use the outline's sharper absorb line too: "delivery planning is the developer's job, and that's where the workflow changed their behaviour." The harder counter is "you swapped a bad metric for no metric" — absorb it honestly: no dashboard yet, working on it, but what he sees day to day (ticket quality, developer confidence, the sensor fix) is enough to know the direction is right.

Material — ending:
> Nic: Right now our workflow is out of beta and is used by our entire development team. It's going through small refinements as we find ways to improve it, but we're out of the "improve it all the time" phase. We're in the stable phase — we can pair program with it in attended mode, we can dispatch autonomous tasks to it directly from our GitHub board, so it's doing everything we want for the moment. Now it's a human problem of us becoming more proficient with it. And as we've reopened our hiring process and will soon get new developers joining the team, my next step is understanding how to introduce new developers to the team in the new agentic era.
Notes: End on "my next step is understanding how to introduce new developers in the new agentic era" — forward-looking, concrete, not a summary. The counterargument absorbs "that's just what senior engineers do" and turns it into the thesis: yes, and the workflow makes it the default for everyone. Nic has 30 years of software development experience, 15 as a CTO — get the number right.

## Counterargument
> Nic: Yes, they are absolutely right. And that's the whole point. Writing code entirely by hand is becoming less prevalent. My role as a CTO is to empower my team to understand what's happening. Being able to understand the problem and translate it into a clear actionable plan was a very desirable skill — it's now mandatory if you want to be productive with AI. The workflow helps them see things they might have missed, but it's my role to up-skill my team and prepare them for the new world we're in.
Placement: woven into section 5, not a standalone section. The harder counter ("you swapped a bad metric for no metric") is absorbed honestly: no dashboard yet, working on embedding metrics, but what he sees day to day is enough to know the direction.

## Quotable line
Candidates (drafter picks in context):
1. "I didn't want us to push more tickets — I wanted us to spend more relative time on a ticket, and when a ticket was pushed it would be solving more and better."
2. "I approached my workflow creation almost as if I was documenting for a team of new project managers, business analysts, developers and QA to join our team."

## Ending
The workflow is stable. The next problem is human: how to onboard new developers into a team that works this way. End on that — forward-looking, concrete, no summary.

## Gaps
- [x] "I don't have a dashboard to prove it" — Nic: no additional retro detail; owns the gap honestly, they're embedding metrics now. (section 5)
- [x] Companion post link — inline mention is enough. (section 4 or 5)
- [x] Sensor API: who wrote the code — the workflow agent wrote the entire code. Nic shaped and traced. (section 2)
- [x] Sensor API timeline — "couple of days" was the discovery window (hunch → support raising the need), not the build timeline. (section 2)

## Reader
cold read 2026-09-12, stage: plan

1. "Section 5 (reinvestment) has no receipt" → accepted: Nic has no hard numbers. Owns the gap honestly ("I don't have clear metrics yet, we're embedding them now"). Drafter may fold into section 4 if thin.
2. "Counterargument dodges the harder version (swapped bad metric for no metric)" → accepted: plan now absorbs the harder counter directly, keeps outline's sharper line ("delivery planning is the developer's job").
3. "Sensor API: who wrote the code, real timeline" → resolved: workflow agent wrote all the code, couple of days was discovery not build.
