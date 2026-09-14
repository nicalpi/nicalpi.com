---
layout: post
title: "If You're Measuring AI by Speed, You're Measuring the Wrong Thing"
subtitle: "The productivity gain no one talks about"
short_title: "Measuring AI by speed"
description: "A seven-month AI experiment with an eight-person development team, and why I told my CEO I wasn't chasing 10x. The gain showed up in ticket quality and delivery planning, not in how fast we wrote code."
category: AI
reading_time: 8
date: 2026-09-12
og_image: /assets/images/og/ai-measuring-wrong-thing.jpg
---

In January I froze our tech hiring plan. I told Stuart, our CEO, that I wanted to understand what AI was going to do to my eight-person development team before I added people to it. I didn't have a prediction. I didn't know what we'd find.

What followed was seven months of figuring it out.

## What we tried first

The first four months were open exploration. Two months where people could try the tools they wanted, then two months to decide which one would be our primary tool and apply, at the very least, proper security measures to it.

I assumed, and I was wrong, that the finding was going to be about which tool won. Pick the winner between the four coding agents we were trialling, then go along with it "naked".

The output depended a lot on the developer using the tool. Some were extremely sharp with them and doing an OK job. Some trusted the tools too much and sent back mountains of code we had to reject.

Reviewing all that output is when we realised the naked approach was going to be the problem for us. These tools are good at writing code, but **they had no idea how we wanted them to work**.

So we spent the next couple of months building a workflow around the agent: a set of structured commands and agents that told it how to scope a ticket, plan delivery, write code to our standards, and hand work back for review. I approached it almost as if I was documenting for a team of new project managers, business analysts, developers and QA who were about to join us, explaining to each of them how we wanted them to work with us.

## Where the gain actually sits

Here's what tickets looked like before the workflow. The team needed to integrate a new sensor for data already in our catalogue. The ticket would be "Integrate with Sensor X", a link to the API documentation, and five or ten lines on what we knew about the integration and the data ingestion that should happen. That was about it.

The assumption was that a couple of conversations with the developer, plus the fact that we already had the data points in our catalogue, was enough to make all the decisions. We don't have a dedicated product manager, so this was how tickets got written.

The reality, and we knew it, was that developers were often confused midway through because there were unexpected decisions to make. QA had no clear acceptance criteria and no context on what the sensor was doing. And more importantly, we were probably skipping the part that would have pushed us to think about what this integration meant for the product as a whole.

Today, if we tell the workflow we need to integrate with this sensor, here's the documentation and here's the blurb about what we know, the flow reads the full documentation with our code as context. It builds a multi-card epic: connecting the sensor to the platform, then data ingestion, then data rendering. It writes user stories for every sub-ticket and QA acceptance criteria to go with them.

Then it helps the developer turn that scope into a locked-in delivery plan, ticket by ticket.

**Not one line of that is code.** All of it is the work that used to get done badly, or not at all, before anyone opened an editor. The workflow does what good ticket-writing would always have done, except now it's the default rather than something you get when someone has the time.

## What better looks like

A few months in, just as the workflow was becoming stable, we had our first real test. We'd had a hunch about one of our partner sensors: its token refresh logic would sometimes leave a token dead, and the only fix was to regenerate a new one manually. Within the same week, support came to us with the same problem. There was a race condition between token generation and consumption, silent because the sensor kept sending data. What we lost was access to the deeper data through the API, which is the kind of thing nobody notices until someone goes looking.

I used our workflow to expose the issue. I gave it the API endpoints we needed to integrate, and together we traced the problem and decided on a plan of attack: fix the race condition as far as we could, and give support an option in the app to regenerate the token if it ever happened again.

The agent wrote all of the code. I shaped the solution and traced the issue with it.

The irony is that the fix is solid, and the regenerate option has, so far, never been used.

The build was quick once the plan was set. But the value was in the tracing and the deciding, and the fact that a silent bug got fixed properly rather than patched around. That's the kind of ticket I want us pushing.

## The question everyone asks

When I came back to Stuart with results, he half-joked: "Oh, so now each developer can be a 10x developer and produce more?"

Stuart is sharp, an ex-engineer, and he obviously knew the 10x thing is an internet joke. But the productivity question is his job as CEO, and it was fair.

My answer was the oddest thing for a CTO to say about a tool everyone sells on speed.

I told him I wasn't interested in 10x. Maybe 1.25, maybe 1.5, because we now had autonomous agents dealing with smaller items. The number I cared about was precision: how well we solved problems for our customers.

> I didn't want us to push more tickets. I wanted us to spend more relative time on a ticket, and when a ticket was pushed, for it to be solving more and better.

The feedback from the team backed this up. It came at different times and in different moments, all from senior developers, and I don't remember it word for word. But every single developer, including the ones who resisted the introduction because they liked to "feel in control", said after a few months that they saw real benefits.

The part I hold on to is that they feel they're doing a better job with it, and that **they haven't lost ownership of what gets built**.

That last point matters to me. I wrote in January that [if you can't explain the code, AI isn't helping you](/blog/if-you-cant-explain-the-code-ai-is-not-helping). That was about the individual developer. This is what it looks like when you try to make it true for a whole team.

## Yes, this is what seniors always did

The fair pushback is that I've been writing software for 30 years, 15 of them as a CTO, so of course shaping is where I add value. For a mid-level developer, the speed of code generation is the win, and I'm just describing what senior engineers have always done and calling it an AI workflow.

Yes. That's right. And that's the whole point.

Writing code entirely by hand is becoming less prevalent as a developer, at least while AI is around. Being able to understand a problem and translate it into a clear plan was a very desirable skill in a developer before. It's now mandatory if they want to be productive with AI.

**Scoping is my job. Delivery planning is the developer's job**, and that's exactly where the workflow changed how they behave, because it forces the planning conversation whether or not the developer would have had it on their own.

The harder pushback is that I've swapped a bad metric for no metric. That one lands.

I don't have clear metrics yet, only what's in front of me day to day: the 50-odd tickets we've built with the workflow and the low rejection rate that came with them, and a clear sense from the wider team that we're doing a good job. We're working on embedding those metrics into the workflow now.

Until then, what I see is enough to know the direction is right, and **the time we've saved on writing code is going back into planning what we write**.

## Where we are now

The workflow is out of beta and used by the whole development team. It's going through small refinements as we find ways to improve it, but we're out of the "improve it all the time" phase and into the stable one.

We can pair with it in attended mode, and we can dispatch autonomous tasks to it straight from our GitHub board, so it does everything we want for the moment.

What's left is a human problem: us getting more proficient with it.

And since we've reopened the hiring process and will soon have new developers joining, my next step is working out how to introduce a new developer to a team that works this way.
