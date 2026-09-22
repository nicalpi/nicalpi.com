# Ideas

One line per idea, newest at the bottom. Format:

`- [ ] YYYY-MM-DD · <one line, Nic's words> · #tag #tag`

Ticked (`[x]`) when the post ships, with ` → /blog/<slug>` appended.
`/quick-log` appends here. `/writing-outline` reads the whole list before
shaping one, so neighbouring ideas can merge or split.

- [x] 2026-09-12 · ai leadership in Amba · #ai #leadership #business → /blog/ai-measuring-wrong-thing
- [ ] 2026-09-12 · the AI workflow in detail: shaping → building → review, how each phase works · #ai #business · receipt (2026-09-22): agents plan fine, they plan for the wrong question — the "you want X, tell me more" interview step (Blain Thomas reply on LinkedIn), today's epic scoping: napkin split → challenge round → adjudication → 8 children
- [ ] 2026-09-12 · AI and the death of the product manager: when your AI workflow does what a PM used to do · #ai #leadership
- [x] 2026-09-12 · the delegation instinct: why CTOs who delegate to people find AI workflows natural · #ai #leadership #career · receipt (2026-09-22): seniors didn't resist the AI, they resisted delegating — "they trust their brain, they were never used to delegating a plan to someone else" (Brett Knapik reply on LinkedIn) → /blog/nobody-taught-developers-to-delegate
- [ ] 2026-09-12 · I was wrong — I thought introducing AI was about picking the winning tool, turns out the tool didn't matter · #ai #leadership
- [ ] 2026-09-12 · onboarding new developers in the agentic era (field-note candidate) · #ai #leadership #business
- [ ] 2026-09-14 · "typing code was never the hard part" — what the hard part actually looks like with AI · #ai #business
  Hook: Dave Farley's LinkedIn post (284 reactions, 27 reposts) landed the line and everyone agreed. But nobody replied with what the hard part looks like from inside a team using AI daily. Not the methodology (BDD, SDD, "waterfall in 15 minutes") — the mess. When the spec is wrong. When a dev pushes back on the spec. When AI technically meets the spec but misses the point. When you realise the spec was the wrong question. A response to the most-engaged AI engineering post on LinkedIn right now, framed around the stories the methodology people skip.
  See: .promo-memory/market-research/2026-09-13-linkedin-x-landscape.md — LinkedIn section, Dave Farley post
- [ ] 2026-09-13 · the review bottleneck everyone's talking about — and how we accidentally solved it · #ai #business
  Hook: Faros data says code review is the bottleneck of 2026 (+441% review time, 32.7% AI-PR acceptance vs 84.4% human). Our shaping-first workflow meant the review happens against a known spec, not open-ended "does this look right?" 50+ tickets, low rejection rate. Frame as: "My team didn't experience the review bottleneck. Here's why." Responds to the hottest eng-leadership thread right now.
  See: .promo-memory/market-research/2026-09-13-linkedin-x-landscape.md #3, #6
  receipt (2026-09-22): left side fixed, QA is where the work hides now — Amba QA acceptance rewritten from the named-user POV ("the resident gets out of bed at 03:20"), developer-steps block, QA warm-up, phased delivery gates; LinkedIn reply "now we're attacking the right side"
- [ ] 2026-09-13 · sustainable pace in the machine-pace era — everyone's burning out from AI, my team isn't · #ai #leadership #career
  Hook: 56% tech burnout (up from 45%), Meta CTO said AI gains = "more work, not more time off" and got ratio'd. Nic is the opposite: hard 4pm stop, HYROX at 5:30am, burned out once, rebuilt deliberately. Team ships with AI daily at a sustainable pace. Nobody in CTO-writing-about-AI space combines both. Personal + contrarian = high engagement on both platforms.
  See: .promo-memory/market-research/2026-09-13-linkedin-x-landscape.md #5
- [ ] 2026-09-13 · what I actually measure after seven months of AI coding agents · #ai #business
  Hook: natural part two of "We're Measuring the Wrong Thing." Tokenmaxxing died (Meta, Uber, Amazon), Forbes ran the same headline last week, LeadDev says 68% of orgs cite lack of clear metrics as biggest challenge. Everyone asks "what should we measure?" — Nic has 7 months of data and a specific answer: precision over speed, rejection rate, whether work holds in production. The audience from yesterday's post is already primed for this.
  See: .promo-memory/market-research/2026-09-13-linkedin-x-landscape.md #2, #8
- [ ] 2026-09-13 · my team is 3-5 seniors plus AI — here's what we lost and what we gained · #ai #leadership #business
  Hook: Andrew Ng describes 1-10 person generalist teams, Garry Tan projects 400x productivity. Nic is living it: 8-person team, elderly care (regulated sector, "move fast" has consequences), no dedicated PM. What it actually looks like, costs and gains, told honestly — not a projection from a VC deck.
  See: .promo-memory/market-research/2026-09-13-linkedin-x-landscape.md #4, #7
- [ ] 2026-09-13 · AI works differently when people can get hurt — building elderly care software with AI agents · #ai #business #leadership
  Hook: nobody in the AI-coding conversation is talking about high-consequence sectors from the practitioner side. Production incidents tripled industry-wide (Faros); in elderly care that means real people. The sensor fix that never needed its escape hatch. The intersection of AI agents and "the user is 85 and lives alone" is territory no other CTO writing publicly can claim. Most differentiated angle available.
  See: .promo-memory/market-research/2026-09-13-linkedin-x-landscape.md #1, #9
- [ ] 2026-09-15 · I froze hiring and it scared me — the emotional side of the decision everyone writes about as strategy · #personal #career · receipt: 7 months of not knowing, the stress of needing authority outside the job, the LinkedIn comeback post that almost didn't happen
- [ ] 2026-09-15 · the workflow is the product, not the code — everyone talks about AI writing code, we built a workflow where code is the easy part · #ai #business · receipt: 50+ Amba tickets, Amba commits showing the workflow itself evolving weekly (review packages, decision policies, visual context bridging)
- [ ] 2026-09-15 · I've been quiet for two years and I nearly didn't come back — about writing itself, not about AI · #personal #career · receipt: the silence, the fear, the LinkedIn post he almost didn't send; the number (2026-09-22): 23,943 impressions, 43 reactions, 14 comments, 2 reposts on the comeback post
- [ ] 2026-09-15 · I'm building authority because I'm afraid my job won't exist — the thing no CTO is saying out loud · #career #personal · receipt: the side business instinct, the stress about where he fits in the AI era
- [ ] 2026-09-22 · the best hiring signal I've found is a 30-minute plan for a fake checkout · #leadership #career · receipt: recent recruitment round, candidates asked for a dev plan for an e-commerce basket checkout, under 30 min, AI welcome — "eye opening the difference in quality"; Michael Dameron asked for the signal on LinkedIn, the reply had 40 impressions
- [ ] 2026-09-22 · the workflow caught nothing, because nobody ran it · #ai #leadership · receipt: Copilot found 4 things on one Amba PR the workflow should have caught; audit showed zero review ran (coordinator wrote a standard inline); fix was a hard stop at the ship step, not more prose — prose gates get skipped, deterministic stops don't
- [ ] 2026-09-22 · "it's too long to read, I'll have to trust you" — the delegation failure I warned seniors about, done by me · #leadership #personal · receipt: 2026-09-22 epic split, 3 drafts + challenge round, 8 child issue drafts approved unread
- [ ] 2026-09-22 · every developer is becoming a mini team of their own — scoping to QA to testing, each handing better input to the next person in the chain · #ai #leadership · receipt: spare from nobody-taught-developers-to-delegate interview
- [ ] 2026-09-22 · keeping up with new models is a real cost for a CTO and nobody budgets for it · #personal #career · receipt: the Jev evening, a few hours reading docs to see whether it fits the product or the workflow
