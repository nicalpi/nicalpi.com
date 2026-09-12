# Writing workflow — improvements

Observed during sessions. Each entry names the stage, the problem, and a fix.

## /writing-outline

### Push harder on "before" receipts
**Problem:** When Nic says "there were too many examples" of a pattern, the interview tends to accept the general description instead of pressing for one named story. The cold reader then flags thin receipts — but the interview is the right place to surface them, not the review.
**Fix:** When a receipt is a pattern ("we always had this problem"), follow up once with: "Pick one. A feature name, a sprint, a week — what happened and how much time was lost?" If he genuinely can't name one, mark it `[…]` immediately rather than carrying a vague receipt into the outline.

### Read neighbour posts, don't just list them
**Problem:** The neighbour check grepped filenames and matched on keywords but didn't read the actual content. The cold reader found a direct overlap at line 142 of the January post that the outline interview missed entirely.
**Fix:** When the grep finds a neighbour, read at least the opening and the claim section of that post. Name the specific overlap or distinction before moving on. Two minutes of reading saves a finding at cold-read stage.

### Lighter structure pitches
**Problem:** The two-structure choice came with a full paragraph each. Nic knew immediately which one was right — the detail slowed the moment down.
**Fix:** Two lines per structure: the shape and why it serves the claim. Save the detail for whichever one is picked. The rejected structure still gets recorded in the outline for the plan to revisit.

### Structure choice needs a timeline test
**Problem:** The outline for ai-measuring-wrong-thing chose structure B (misconception-led, proof-before-explanation) over A (chronological). Four draft versions later, Nic restructured the whole post chronologically because the timeline was bouncing between January, July, January-April, May-June. When a post tells a journey (introducing a process over months), chronological is almost always right. The misconception structure works when the reader's wrong assumption IS the opening, not when the story has a natural arc.
**Fix:** After picking a structure, ask: "Is this post a journey with a timeline? If yes, default to chronological. The drafter should argue for non-chronological, not the other way around."

## /writing-plan

### Ask for receipts on the thesis section during the interview, not after
**Problem:** The cold reader caught that section 5 ("the reinvestment") had no receipt — just a recycled number and a hedge. The interview had eight chances to ask "show me a moment where planning took longer and was better for it" and never did. The cold read is a safety net, not the primary place to surface missing material.
**Fix:** After walking all sections, before writing the plan, scan the outline's claim and check: does the interview material contain at least one moment that directly demonstrates the claim? If not, ask for it explicitly. One targeted question at the end is cheaper than a cold-read finding that sends us back to Nic.

### Draft the description yourself, then confirm
**Problem:** Question 10 asked Nic to approve a description — but by that point he'd already given everything needed to write it. The question felt like a formality, not a real decision point.
**Fix:** Write the description draft silently after question 8 or 9. Present it as "here's the description, does this land?" rather than an open question. Nic can still rewrite it, but the default should be a concrete proposal, not a prompt.

### First-person in all reader-facing front matter
**Problem:** The first description draft referred to Nic in third person ("Nic Alpi found the real gain"). He corrected it to first person. Reader-facing text (description, subtitle) should always be first person — the blog is his.
**Fix:** All front-matter fields that end up visible to the reader (description, subtitle) use first person. Third person only in internal notes and drafter instructions.

## /writing-post

### Don't open with the reframe when the evidence earns it
**Problem:** The drafter for ai-measuring-wrong-thing put Stuart's "10x?" question at the opening (structure B). It landed much better after the sensor story and ticket section, because by then the reader already knows the answer is wrong. When a question has an obvious wrong answer, placing it after the evidence is stronger than leading with it.
**Fix:** When the drafter places a question or reframe at the opening, check: "Does the reader need to see the evidence before the reframe hits?" If yes, move it later. The Stuart scene went from opening to section 5 and the post improved immediately.

## General — all stages

### Mine the interview for new ideas before closing
**Problem:** During the ai-measuring-wrong-thing plan interview, Nic's answers surfaced two new post ideas ("I was wrong — I thought it was about the tool" and "onboarding devs in the agentic era") that would have been lost if he hadn't asked. The interview is the richest source of raw material and it's the moment Nic is thinking out loud — ideas surface naturally.
**Fix:** After approval at every stage (outline, plan, draft), scan the interview for claims, analogies, or next-steps that aren't covered by the current post and could stand alone. Log them to `ideas.md` via `/quick-log` format. Present them to Nic ("these came up — worth logging?") rather than logging silently, so he can filter. One question, not a gate.

### Suggest a new session between stages
**Problem:** Nic had to ask whether to continue or start fresh. The workflow should proactively recommend it when a stage boundary is a natural break point.
**Fix:** After a stage is approved (outline, plan, draft), suggest starting a new session for the next stage when: (1) the conversation is already long with interview material that the next stage doesn't need in context, (2) the next stage involves a fresh interview or cold read that benefits from clean context, or (3) the persisted files already capture everything needed to pick up. Say it in one line — "I'd start a new session for the plan, everything's saved in the slug folder" — not a paragraph.
