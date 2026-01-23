---
layout: post
title: "If You Can't Explain the Code, AI Is Not Helping You"
title_html: "If You Can't Explain the Code,<br><span class='text-coral'>AI Is Not Helping You</span>"
subtitle: "AI made code output cheap. Value moved from writing code to owning outcomes."
description: "AI made code output cheap. 'I shipped a lot' means less now. Value moved from writing code to owning outcomes—deciding what matters, explaining trade-offs, taking responsibility."
category: AI
reading_time: 9
date: 2026-01-17
og_image: /assets/images/og/ai-code-explain.jpg
---

I've been quiet for three years.

Not because I stopped thinking. I stopped publishing. Life happened. A company acquisition, some personal stuff. I went heads down and rebuilt things.

Meanwhile, AI pulled software into a new phase. Now I watch people talk about it in a way that bothers me. They're missing the real change.

AI isn't a new tool in the toolbox. It changes what the toolbox is worth.

## Output got cheap

AI made output cheap. Code, tests, docs, first drafts of features. Whole chunks of product, sometimes.

When output gets cheap, output stops being a strong signal. "I shipped a lot this week" doesn't mean what it used to. Anyone can ship a lot when a machine drafts the work.

That's the shift. Not "developers are doomed". Not "we're all ten times faster". Value just moved somewhere else.

Here's what I think: if you can't explain the code, AI is not helping you.

It might feel like help. You moved faster. The diff is bigger. But if you can't explain what you just shipped, you didn't gain leverage. You lost ownership.

So what does "explain" actually mean? I'm not talking about describing the folder structure.

## What "explain" actually means

I mean you can answer basic questions without hesitating:

- What does this code do?
- What does it depend on?
- What assumptions does it make?
- What could break it?
- How would you notice?
- What would you do about it?

That's the bar. That's engineering with the theatre cut out.

![Can you explain your code? Six questions checklist](/assets/images/ai-code-explain/six-questions.jpg)

For most of my career, nobody asked these questions. Or at least, not consistently. The industry rewarded something else.

## The old deal

For a long time, teams rewarded implementation speed. Take a ticket, make it real, move on. That made sense when implementation was the bottleneck.

Even average implementation had value because it took time, focus, effort. A lot of careers were built on being the person who reliably turns requirements into working code. I know because I hired those people for eleven years. Good people. Solid people.

That deal is changing. Worth being specific about which parts AI actually touches.

## What AI replaces

AI replaces drafting and pattern matching.

It replaces the loop of "search, paste, tweak until it compiles". It replaces writing the boring parts. It replaces the first version of almost everything.

That's not bad. It's progress. But it wipes out work that used to separate "productive" from "stuck". So the market re-prices that work.

Here's where people get confused. They see AI writing code and assume it's doing the whole job. It's not. Not even close.

## What AI doesn't replace

AI doesn't replace responsibility.

It doesn't carry the context of your system's history. It doesn't feel the pain of a production incident at 2am. It doesn't own the trade-offs when a quick fix creates a long-term mess.

It generates implementations. It doesn't decide what matters.

That decision is where value moved.

![What AI replaces vs what it doesn't](/assets/images/ai-code-explain/replaces-vs-not.jpg)

This sounds abstract. Here's a real example.

## Verification debt

Here's what people miss.

AI makes confident-looking code cheap. It compiles. It reads well. It sounds like a strong engineer wrote it. Teams lower their guard because the output looks professional.

But real systems fail in places you don't see in a clean demo. Weird data shapes. Partial outages at 3am. Retry logic nobody tested under load.

If you ship AI-assisted code you can't explain, you create verification debt. You borrow certainty now. You pay later in bugs, rework, incidents. Slow loss of trust in the codebase. Slow loss of trust in the team.

AI lets you generate that debt faster than most teams are ready for.

![Verification debt flow](/assets/images/ai-code-explain/verification-debt.jpg)

I watched a team ship an AI-generated authentication flow last month. It looked clean. Passed code review. Two weeks later, a race condition in the session handling took down their checkout for six hours.

Nobody on the team could explain why the code handled token refresh that way. Because nobody had decided it should. They'd accepted what the machine offered. Seemed reasonable at the time.

Now, there's a different concern I hear from developers. Not about debt or quality. About identity.

## "But is it even my code?"

This question keeps coming up.

Developers feel weird about using AI. Feels like cheating. If Claude generates the implementation, if Cursor writes the tests, if the AI drafts most of the file... what did you actually contribute?

I get it. I've felt it too. But it's the wrong question.

## The director problem

Nobody debates whether a Spielberg film is "his". He doesn't operate the camera. Doesn't build the sets. Doesn't edit the footage.

Yet you can feel his fingerprints everywhere. In what the film focuses on. What it cuts. What the scene refuses to waste time on.

The camera operator executes with technical skill. Spielberg decides what to point the camera at. When to cut. What the scene needs to achieve.

That's authorship. Nobody questions it belongs to him.

## What this means for your code

When I use AI to build a feature, AI might write most of the code.

But the architecture is mine. The constraints are mine. The boundaries are mine.

The spec that told AI what to build came from twenty years of watching things go wrong. The judgment about why this approach fits our team, our codebase, our risks? Mine.

AI is the camera crew. I'm the director.

The code is mine because the decisions are mine. The trade-offs are mine. The responsibility when it breaks? That's on me.

If you can explain those decisions, the code is yours. If you can't, you're not the director. You're hoping the camera crew guessed what scene you needed.

![The director problem - AI is the camera crew, you're the director](/assets/images/ai-code-explain/director-metaphor.jpg)

So what does this mean for your career? What actually makes a developer valuable now?

## What valuable looks like now

A valuable developer isn't "the fastest typist". Never really was, honestly. We just measured output because output was easy to count.

Now? It's the person who can own outcomes. Someone who turns vague requirements into a clear problem. Who decides what matters before anyone asks. Who spots risk before it ships.

Someone who can explain what they built. Why it won't fall over under real pressure. Why this approach and not another.

AI doesn't remove that person. It makes them more dangerous.

## The line

AI didn't kill developer value. It moved it.

If you can't explain the code, AI is not helping you. It's hiding the gap until production finds it.

If you can explain it, AI becomes leverage. You keep authorship. You ship faster without guessing.

That's the line.

![The line - can't explain vs can explain](/assets/images/ai-code-explain/the-line.jpg)

---

*I'm Nic Alpi. After 20 years in tech and building a consultancy to £1M+ revenue before acquisition, I help technical leaders build sustainable systems. Writing weekly on boring technology, calm execution, and working without burning out.*
