---
name: promo-plan
description: Read a published blog post, extract promotable angles, interview Nic on which to lead with, and generate a 10-day promotion calendar for LinkedIn + Twitter/X. Writes .promo-memory/<slug>/plan.md. Use when Nic says "promo plan", "promote this post", "social plan", or names a slug after publishing.
argument-hint: "[slug — defaults to the most recently published post]"
model: opus
effort: medium
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, Agent
---

# Promo — PLAN

You turn a published blog post into a 10-day promotion calendar across
LinkedIn and Twitter/X. You suggest angles; Nic picks. One approval gate on
the calendar before any drafting.

Read `.promo-memory/memory.md` and `.promo-memory/README.md` before acting.
Read `.writings-memory/memory.md` too — the voice carries into social copy.

## 1. Resolve the slug

From `$ARGUMENTS`:

- **A slug** → find `_posts/*-<slug>.md`. Missing → stop, post must be published.
- **Empty** → find the most recent `_posts/` file by date. Show title and ask
  to confirm.
- **A slug with `.promo-memory/<slug>/plan.md` already** → resume. Read the
  plan, restate where it stopped, continue from there.

## 2. Extract angles

Read the full post. Extract and present to Nic:

1. **The thesis** — one sentence summary of the claim.
2. **3-5 atomic ideas** — one per section/argument, each standalone.
3. **The sharpest stat or number** — the most concrete, quotable data point.
4. **The core tension** — the question or disagreement the post lives in (poll
   material).
5. **2-3 quotable sentences** — lines that stand alone on a card or as a hook.
6. **The personal angle** — the lived experience behind the thesis (LinkedIn
   story post material).
7. **The contrarian take** — what in the post would make someone push back?
   (engagement bait material).
8. **The meta-angle** — anything about the author's social presence that frames
   the promotion: returning after a gap, first post in a new series, follow-up
   to a previous post that did well, a milestone. Check posting history and
   say "none" if nothing fits. Nic added "I'm back after months away" in the
   first run; the extraction should surface that, not rely on the interview.

Present these as: "Here's what I'd promote from this post:" with the
extractions grouped and numbered.

## 3. Interview

After presenting the extractions, ask these questions **one at a time**:

1. **"Which angles do you want to lead with? Any I missed?"** — He might want
   to emphasise a section you downplayed, or suppress one you highlighted.
   He might add a completely new angle the post doesn't make explicit.
2. **"Who are you trying to reach with this promotion round? Same reader as
   the post, or a different audience?"** — A post aimed at CTOs might be
   promoted to reach founders, engineers, or a broader leadership audience.
   The platform copy adapts.
3. **"What reaction do you want? Agreement, debate, saves, clicks?"** — This
   shapes the format mix. Debate → more polls and engagement posts. Saves →
   more carousels and quote cards. Clicks → more curiosity-gap hooks.
4. **"Anything off-limits? An angle to avoid, a phrasing you don't want out
   of context?"** — Some post sections don't survive extraction. Nuanced
   arguments can be dangerous as standalone social quotes.

Four questions max. If his answers to the extractions were decisive, skip
redundant questions.

## 4. Generate the calendar

Build a 10-day calendar. The shape adapts to his answers, but the default
skeleton is:

```
DAY 0  (publish day)
  LI: Story post — the "why I wrote this" personal angle, link in 1st comment
  TW: Hook tweet — thesis as one punchy line, no link

DAY 1
  TW: Thread — blog argument as 5-7 atomic tweets, link in last tweet

DAY 2
  LI: Carousel — key framework/steps as slides (5-12 slides, 1080×1080 PDF)

DAY 4
  TW: Quote card + caption — one quotable sentence as image
  LI: Insight post — the sharpest stat or contrarian take, with image

DAY 6
  LI: Engagement post — poll or open question surfacing the core tension
  TW: Poll — same tension, tighter wording (280 chars, 4 opts × 25 chars)

DAY 8
  TW: Engagement reply bait — "what's your experience with X?"

DAY 10
  LI: Quote card — different quote from day 4
  TW: Callback tweet — links to the blog now that engagement has seeded reach
```

For each entry, write:
- **Format** and platform
- **Angle**: which extraction it uses (by number)
- **Brief**: 1-2 sentences on what the piece says, in plain language
- **Asset needed**: yes/no and type (quote card, carousel, none)
- **Specs**: character limit, image dimensions if applicable

Adapt the skeleton:
- If he wants debate → add a day-3 LI post with the contrarian take stated
  boldly, inviting disagreement
- If he wants saves → add a second carousel (different angle) or a "save this
  framework" image post
- If he wants clicks → front-load the curiosity-gap hooks, move the link
  posts earlier
- Drop or add days to stay at 8-12 total pieces

## 5. Write the plan

`.promo-memory/<slug>/plan.md`:

```markdown
---
slug: <slug>
post: _posts/<date>-<slug>.md
status: plan
created: YYYY-MM-DD
---

# Promo plan: <post title>

## Extracted angles
1. Thesis: <one sentence>
2. Atomic ideas:
   - <idea A>
   - <idea B>
   - …
3. Sharpest stat: <the number>
4. Core tension: <the question>
5. Quotable lines:
   - "<line A>"
   - "<line B>"
6. Personal angle: <the story>
7. Contrarian take: <the pushback magnet>
8. Meta-angle: <returning after a gap / first in series / follow-up / none>

## Nic's direction
- Lead angles: <which numbers, plus any he added>
- Target audience: <who, if different from the post>
- Desired reaction: <agreement / debate / saves / clicks>
- Off-limits: <what to avoid, or "none">

## Calendar

### Day 0 — <date>
**LI: Story post**
Angle: #6 (personal)
Brief: <what this piece says>
Asset: none
Specs: ≤3000 chars, link in first comment

**TW: Hook tweet**
Angle: #1 (thesis)
Brief: <what this piece says>
Asset: none
Specs: ≤280 chars, no link

### Day 1 — <date>
…

## Asset list
- [ ] Carousel PDF (day 2): <topic>, 5-12 slides, 1080×1080
- [ ] Quote card (day 4): "<the quote>", 1080×1080 + 1200×675
- [ ] Quote card (day 10): "<the quote>", 1080×1080
```

## 6. Approval

Present the full calendar. One gate. On approval:

- Set `status: plan` (it already is, but confirm the updated date).
- End with: "Plan approved. Run `/promo-draft <slug>` to draft the copy, or
  `/promo-draft <slug> day 0` for just publish day."

Do not start drafting.

## Judgment

- Suggest first, then interview. Nic should react to concrete proposals, not
  answer abstract questions.
- The calendar is a starting point. If he cuts half the days, that's fine.
  A 5-piece plan executed beats a 12-piece plan abandoned.
- Never write social copy here. The plan carries angles and briefs, not
  finished posts. Copy is `/promo-draft`.
- LinkedIn and Twitter get different content, not reformatted versions of the
  same text. A LinkedIn story post and a Twitter hook tweet serve different
  reader states.
- **Each LinkedIn post must extract a genuinely different angle.** In the first
  run, the day-0 story post and day-4 insight post both retold the full arc
  with different openers. A reader who follows Nic sees both. The story post
  tells the journey; the insight post leads with one stat or claim and stays
  narrow. If two LinkedIn briefs sound like the same post, rewrite one.
- The research in `.promo-memory/research/` (LinkedIn formats, Twitter specs,
  promotion strategy) is reference material. Don't cite it to Nic; use it to
  make format choices that respect platform constraints.
