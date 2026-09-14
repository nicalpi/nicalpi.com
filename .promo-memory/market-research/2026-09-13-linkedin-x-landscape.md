# Market research: LinkedIn and X.com — 13 Sep 2026

## Summary

The conversation has shifted from "AI makes us faster" to "AI made us faster
and everything broke." Five threads dominate:

1. **Acceleration Whiplash** — Faros AI report (22k devs, 4k teams): +66%
   epics but +242% incidents, +861% code churn, 31% more unreviewed PRs.
   Everyone cites it; almost nobody describes a working solution from a real
   team.
2. **Tokenmaxxing died** — Meta killed its internal AI leaderboard, Uber
   burned its budget by April, Amazon told staff to stop using AI for the sake
   of it. Forbes ran "You're Measuring The Wrong Thing" on 3 Sep 2026. The
   vacuum: what DO you measure instead?
3. **Code review is the bottleneck of 2026** — AI-generated PRs: 32.7%
   acceptance vs 84.4% human. Median review time +441%. GitHub shipped stacked
   PRs to cope. Problem described everywhere; solutions almost nowhere.
4. **Andrew Ng's "PM bottleneck"** — when code builds 100x faster, deciding
   what to build is the constraint. 1-10 person generalist teams. Theoretical
   so far; Nic has lived it with no PM on an 8-person team.
5. **"Machine pace" burnout** — 56% tech burnout (up from 45%), 96% heavy AI
   users say role expanded. Meta CTO said AI gains mean "more work, not more
   time off" and got ratio'd. Sustainable-pace counter-narrative has no
   credible CTO voice yet.

Nic's "We're Measuring the Wrong Thing" post (12 Sep) landed in the middle of
threads 1-2. His shaping-first workflow is the structural answer to thread 3.
His daily life is the counter-narrative to thread 5.

---

## Findings

### 1. The Faros "Acceleration Whiplash" report is the data set of the season

Source: [Faros AI Engineering Report 2026](https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways),
covered by [ADTmag](https://adtmag.com/articles/2026/04/22/more-code-more-bugs.aspx),
[Defract](https://defract.dev/blog/ai-code-acceleration-whiplash),
[Hyrax](https://hyrax.dev/blog/review-gap-measurable-faros-ai-telemetry-2026).

22,000 developers, 4,000+ teams. Under high AI adoption: epics completed per
developer +66%, task throughput +33.7%, PR merge rate +16.2%. But: bugs per
developer +54%, incidents-to-PR ratio +242.7%, median review time +441.5%,
code churn +861%, unreviewed PRs merged +31.3%.

### 2. Tokenmaxxing rose and fell — the "what should we measure" vacuum

Sources: [The Pragmatic Engineer](https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/),
[LeadDev](https://leaddev.com/ai/tokenmaxxing-and-the-search-for-ai-metrics-that-matter),
[Fortune (Meta killed its dashboard)](https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/),
[Forbes (Sep 3 2026)](https://www.forbes.com/councils/forbestechcouncil/2026/09/03/software-engineering-productivity-youre-measuring-the-wrong-thing/).

Meta created "Claudeonomics" — 85k employees ranked by token consumption,
titles like "Token Legend" and "Cache Wizard." Uber burned its 2026 AI budget
by April. Amazon told staff to stop using AI just to use AI. Only 19% rate
token metrics as effective (LeadDev); 57% say they fail to gauge value.

### 3. Code review is the acknowledged bottleneck — few describe solutions

Sources: [Dominic Elm on X](https://x.com/elmd_/status/2033454836822286393),
[Codacy](https://blog.codacy.com/ai-breaking-code-review-how-engineering-teams-survive-pr-bottleneck),
[DEV Community](https://dev.to/code-board/code-review-is-the-real-bottleneck-of-2026-and-most-teams-dont-see-it-5eed),
[FlowVerify](https://www.flowverify.co/blog/ai-code-review-bottleneck-2026-data).

AI-generated PRs: 32.7% acceptance rate vs 84.4% human. Wait 4.6x longer
before pickup. GitHub launched stacked PR support (Apr 2026) to address this.

### 4. Andrew Ng's "product management bottleneck" thesis

Sources: [Andrew Ng on X](https://x.com/AndrewYNg/status/2043742105852621052),
[Pandaily](https://pandaily.com/andrew-ng-ai-agent-data-architecture-jun2026),
[Forbes](https://www.forbes.com/sites/josipamajic/2026/08/16/andrew-ng-maps-the-ai-skills-that-decide-which-startups-ship/).

When code builds 10-100x faster, deciding what to build becomes the
bottleneck. Teams of 1-10 "high-context generalists." Quote: "When a prototype
can be built in a single day, waiting a week for user feedback is really
painful."

### 5. "Machine pace" burnout — the backlash is real

Sources: [Charter Works](https://www.charterworks.com/how-the-machine-pace-of-work-is-burning-out-your-best-employees/),
[Meta CTO on TechRadar](https://www.techradar.com/pro/meta-chief-technology-officer-andrew-bosworth-says-ai-productivity-gains-should-now-mean-were-all-doing-more-work-not-taking-time-off),
[Garry Tan on X](https://x.com/garrytan/status/2080699367883980924),
[Forbes](https://www.forbes.com/sites/pauladavis/2026/06/11/sustainable-performance--ai-accelerated-work-5-questions-every-leader-must-ask/),
[Psychology Today](https://www.psychologytoday.com/us/blog/pressure-proof/202606/ai-accelerated-work-demands-new-leadership-questions).

56% tech burnout (up from 45%). 96% heavy AI users say role expanded. Meta CTO
Bosworth: "more work, not more time off" — walked it back after backlash.
Garry Tan: "Be prepared for this to take 10 years not 2."

### 6. Spec-driven development goes mainstream — mostly theoretical

Sources: [Microsoft Developer Blog](https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/),
[Addy Osmani](https://addyosmani.com/blog/ai-coding-workflow/),
[Augment Code](https://www.augmentcode.com/guides/what-is-spec-driven-development).

SDD is now a named methodology. Microsoft published an official post. Osmani
calls it "waterfall in 15 minutes." GitHub reports ~10x fewer regeneration
cycles with specs. Nic's shaping phase IS SDD arrived at organically.

### 7. Junior developer hiring crisis

Sources: [CodeConductor](https://codeconductor.ai/blog/future-of-junior-developers-ai/),
[AIExposure](https://www.aiexposure.org/analysis/coding-jobs-ai-2026),
[Nucamp](https://www.nucamp.co/blog/the-junior-developer-hiring-crisis-in-2026-how-to-get-your-first-full-stack-job).

Junior hiring down 35%, bootcamp enrollment down 40%, AI engineer roles up
300%. 70% of hiring managers believe AI can do intern-level work. AWS CEO Matt
Garman called this "one of the dumbest things I've ever heard."

### 8. METR perception gap — developers think AI helps but data says otherwise

Sources: [METR study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
[METR 2026 update](https://metr.org/blog/2026-02-24-uplift-update/),
[DX newsletter](https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity).

Controlled study of 16 experienced OSS devs: AI made them 19% SLOWER.
Developers expected +24% speed and even after the slowdown believed it had
sped them up by 20%. METR is redesigning the experiment because devs refused
to participate without AI tools.

### 9. Code quality declining — duplication and maintainability data

Sources: [LeadDev](https://leaddev.com/ai/code-maintainability-plummets-in-the-ai-coding-era),
[Codemanship: "Slow The F**k Down"](https://codemanship.wordpress.com/2026/05/10/slow-the-fk-down/).

Code duplication +81%. Code reuse (refactoring commits) down 70%. Legacy
refactoring down 74%. Error masking up 47%. Functional connectivity down 35%.

---

## LinkedIn-specific posts (browsed 14 Sep 2026)

What's actually getting engagement from real people on the platform, not just
articles about trends.

### Code review bottleneck — the dominant LinkedIn conversation

- **Dave Farley** (Continuous Delivery co-author, 2nd connection) — 3 weeks
  ago — **284 reactions, 32 comments, 27 reposts**. "For CTOs, Engineering
  Leads, and technology decision-makers, the current AI revolution presents an
  incredibly seductive trap: the belief that AI coding assistants will
  magically solve your delivery bottlenecks. But typing code was never the hard
  part of software engineering. The real challenge has always been, and still
  is, exploring the problem, building a deep understanding of customer needs,
  and translating that into clear requirements. AI coding assistants don't help
  us with that exploration." Linked article: "Is BDD with AI - The 5th
  Generation of Programming?"
  → **Highest engagement** found across all searches. His thesis is exactly
  Nic's lived experience. A response post would enter a proven conversation.

- **Karel Becerra** — 1 week ago — "AI Hasn't Solved Software Engineering. It
  Has Moved the Bottleneck." Opening line: "I love vibe coding — except when
  it's running the Boeing 737 MAX I'm flying home on."

- **Rob Allen** (LIFT.Corp founder) — 3 weeks ago — "AI Code Review Is Finding
  Real Bugs. Now Humans Are the Bottleneck" newsletter article.

- **Oleksandr Pavlenko** (Head of AI, NOVA GROUP) — 3 weeks ago — "The
  headline numbers around AI coding make it sound like software delivery has
  been solved: 10x faster implementation, higher acceptance rates, and soaring
  commit volumes..." — comic showing AI-generated PR #4521 with "Estimated
  Review Time: 18 days."

- **"LGTM, but did anyone actually read it?"** — article from
  theintelligentcommit.com — 16 reactions — about rubber-stamp reviews.

- **Toni Ruokolainen** — "AI Solved the Easy Part of Software Engineering. Now
  We Have to Fix the Hard Part." — 11 reactions, 10 comments. "Typing syntax
  was never the true constraint. Understanding domain logic, maintaining
  architecture, and verifying correctness always was."

### Spec-driven development — emerging but lower engagement

- **Rafael Ramos** (Principal AI Engineer, AWS Developer Transformation) —
  1 week ago — **90 reactions, 6 comments, 6 reposts**. "The Attestation
  Model: Continuous Integration for AI-Native SDLC." Works on helping
  engineering orgs adopt AI across their SDLC.

- **John Crickett** — 2 weeks ago — "I spoke to Anton Arhipov about
  Spec-Driven Development at JetBrains' KotlinConf earlier this year..." —
  JetBrains pushing SDD at conferences.

- **Jose Santos** — Data Engineer — "Spec-Driven Development" newsletter. "AI
  coding tools have shifted the bottleneck in software delivery from writing
  code to specifying what to build and verifying what gets generated — PR
  review time has surged 91% in high-AI-adoption teams." Low engagement (2
  reactions) but sharp framing.

### Tokenmaxxing / measuring AI productivity

- **Andrew Palmer** (Bartleby columnist, The Economist) — 3 weeks ago — **60
  reactions, 4 comments, 9 reposts**. "Stop tokenmaxxing. Concentrate on
  outcomes-based metrics. Track quality. Expect productivity to dip before it
  rises. Decide how you want to use time savings. And measure how well your
  organisation is managing change." Sharing Economist article "How to measure
  returns on AI."

- **Jess Ramos** (650K+ followers, Data/AI creator) — "Tokenmaxxing is DEAD
  and Valuemaxxing is IN. Tokenmaxxing has been KILLING enterprises not just
  with cost but also..." — major account pushing back.

- **Stephen Fahey** — "Meta Pushes Its New AI Agent on Employees - but Backs
  Off on..." — 8 reactions, 3 comments.

### AI burnout / sustainable pace

- **Hugo Lu** (Founder, Orchestra) — 2 weeks ago — **63 reactions, 6 comments,
  6 reposts**. "Data Teams are burning out." Article: "AI's Chokehold: How to
  build a Data Team without AI Burnout."

- **Eleanor Warnock** (journalist, ex Sifted/WSJ/Atomico) — 6 months ago —
  "Going to wade into this AI pacing debate and then log out of LinkedIn for a
  few days because I am getting as tired as I feel like those AI researchers on
  TV..." — even the press is fatigued by the debate.

### What this tells Nic

1. **The code review bottleneck is the #1 engagement topic.** Dave Farley's
   post (284 reactions) is the clear proof. His conclusion — "typing code was
   never the hard part" — is the opening for a practitioner response: "I agree.
   Here's how my team prevented the bottleneck."

2. **SDD posts get engagement from authority accounts (AWS, JetBrains) but
   low engagement from the crowd.** The methodology is still being named, not
   yet lived. A practitioner's messy version would stand out.

3. **Tokenmaxxing/metrics posts get solid engagement** (60 reactions for the
   Economist share) — the "what should we measure" question is open. Nic's
   "part two" post would land in a live conversation.

4. **Burnout posts get personal engagement** (63 reactions for Hugo Lu). The
   sustainable-pace angle is underserved in the CTO-who-uses-AI space — most
   burnout posts come from ICs or data teams, not CTOs running AI workflows.
