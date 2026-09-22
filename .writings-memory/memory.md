# Writing memory — how Nic writes

Read by `writing-drafter`, `writing-reader` and `/writing-plan` before any prose.
Two sections. **Voice** is the stable guide, seeded from
`.claude/skills/nicalpi-brand/voice.md` (that file stays canonical for brand
work; this one adds what only shipping posts can teach). **Observed edits** is
evidence: what Nic changed between the agent's draft and the version he
approved. `/writing-post` appends there after every post. When an observed
pattern repeats three times, promote it into Voice and say so in the entry.

## Who is writing

A working CTO, not a commentator. French, in the UK since 2008. Co-founded
CookiesHQ (Rails consultancy, 20 people, £1m+ revenue), sold it to Amba in
2021, now leads an 8-person team building software for elderly care. Burned out
once; rebuilt deliberately. HYROX at 5:30am, three kids, hard 4pm stop. Writes
in public because too much leadership advice performs a certainty the author
doesn't have. The reader is a technical leader with too much on: peers, not
students. Canonical version: `.claude/skills/nicalpi-brand/voice.md`.

## Voice

- First person, plain words, short paragraphs (1–3 sentences). Reads spoken.
  British English.
- Open with the concrete moment, not the thesis. The claim lands after the
  reader has seen the evidence.
- Confident about what he saw, honest about what he doesn't know. Hedges like
  "small sample, one team, one month" are brand, not weakness.
- Specific numbers over adjectives. "20 people and over £1 million", never
  "a successful agency".
- Dry, occasionally. Never snark, never guru register, no exclamation marks.
- `##` headings, sentence case, short. One blockquote at most, for the
  quotable line. Lists only when a list is genuinely the shape.
- 800–1800 words. When in doubt, shorter. End on the last fact or the next
  step, never a summary.
- Never invent facts, numbers or stories about his life. Leave a visible
  `[…]` marker instead.
- Short paragraphs, but connected thought. Sentences carry on from each other
  with "so", "because", "and then". No run of one-line fragments for effect.
- Honest hedges stay ("small sample, one team"). Scope hedges go ("some teams,
  sometimes, might"). Nothing reads like a press release or a keynote.
- Strip AI-tells: delve, crucial, pivotal, landscape, journey, unpack,
  game-changer, leverage, seamless, cutting-edge, unlock, paradigm shift,
  robust, empower; rule-of-three padding; "it's not X, it's Y"; inflated
  symbolism ("a testament to"); more than ~2 em-dashes per paragraph. The
  `humanizer:humanizer` plugin skill is the full checklist and runs on every
  draft in `/writing-post`.

## Rules Nic added

_When Nic says a draft sounds off and names why, the rule goes here the same
day, dated. No three-times threshold for a rule he states himself._

- 2026-09-12 · **Timeline should flow, not bounce.** When a post covers months
  of work, the reader needs to follow one line forward. Jumping to a later
  moment for dramatic effect and then back for context cost three draft
  versions on ai-measuring-wrong-thing. Default to chronological when the
  post is a journey.
- 2026-09-15 · **Introduce before you reference.** Don't mention a concept
  (a workflow, a tool, a process) as if the reader already knows what it is.
  If you name it, you've earned a sentence explaining what it is first.
  Caught on a LinkedIn post that said "50-odd tickets through the workflow"
  when no prior line said a workflow had been built.
- 2026-09-12 · **Real numbers over poetic abstractions.** "The 50-odd tickets
  we've built with the workflow and the low rejection rate" beats "the quality
  of the tickets, the confidence of the team." The first is evidence; the
  second sounds like a speech. Extends the existing "specific numbers over
  adjectives" rule to lists of proof, not just individual claims.

- 2026-09-22 · **Read it aloud before he does; transitions are part of the
  draft.** After approval of nobody-taught-developers-to-delegate, Nic re-read
  the published page and said "overall the post feels a bit strange to read".
  The specifics: the opening named the workflow, then explained it in the next
  sentence ("through our new workflow. The workflow is…"), then said the wait
  twice ("some way into implementation… after more than a week"); and a short
  reaction sentence ("So I didn't tell them off.") sat on its own between two
  longer ones. Three causes to check on every version: a thing introduced
  after it is used, the same beat said twice in one paragraph, and a one-line
  sentence dropped between paragraphs that don't hand off to it. A flow read
  (paragraphs, transitions, repetition) is a distinct pass from the claims read
  and should run before Nic sees v1.

## Post shape

story → claim earned → counterargument absorbed → last fact.

## Calibration posts

Read one in full before drafting. `/writing-post` adds a shipped post here when
Nic's edit load was light (v1 or v2 approved), because a post that landed with
few edits is the best evidence of the voice. Keep the list under six; drop the
oldest when it grows.

- `_posts/2026-01-17-if-you-cant-explain-the-code-ai-is-not-helping.md` — the
  current register.
- `_posts/2024-10-03-feeling-like-a-failure.md` — the personal register.
- `_posts/2026-09-22-nobody-taught-developers-to-delegate.md` — the management-failure register: a scene, a mechanism from his own past, outside evidence handled without judging it, the workflow as what happens.

## Observed edits

_Appended by `/writing-post` after each approval. Format:_

```
### YYYY-MM-DD · <slug> · edit load: light|medium|heavy (vN approved)
- cut: <what he removed, and the pattern it suggests>
- replaced: "<agent phrase>" → "<his phrase>"
- added: <what he put in that the draft lacked>
- kept: <a risky choice the draft made that survived — worth repeating>
- reader: <findings he accepted / overrode, one line>
```

### 2026-09-12 · ai-measuring-wrong-thing · edit load: heavy (v4 approved)
- cut: entire defensive Stuart paragraph ("I don't want to paint him as the man who only saw the cost-saving angle") — the fair portrayal was already in the writing. Also cut guru paragraph ("I'm not saying the workflow will do that thinking for them… prepare them for the world we're now in") — keynote register, weakened the absorb line before it.
- replaced: "the quality of the tickets, the confidence of the team, the sensor fix that never needed its escape hatch" → "the 50-odd tickets we've built with the workflow and the low rejection rate that came with them, and a clear sense from the wider team that we're doing a good job" (real numbers over poetic abstractions). "They're right" → "That's right" (dangling pronoun). "empowered" removed (AI-tell, even though it was his word from the plan interview).
- added: "A few months in, just as the workflow was becoming stable, we had our first real test" — he wanted the sensor section to mark a turning point. Also repositioned "the oddest thing for a CTO to say" as a hook *before* the answer rather than a comment after it. Stuart framed as "sharp, an ex-engineer, and he obviously knew the 10x thing is an internet joke. But the productivity question is his job as CEO" — sharper, fairer, no defensiveness.
- restructured: entire post reordered from misconception-led (structure B) to chronological. v1 bounced Jan → July → June/July → Jan-April → May-June. v4 flows Jan → Jan-April → May-June → June/July → post-experiment → today. Stuart's question moved from opening to after the evidence. This was the main edit: the timeline is the story when the post covers months of work.
- kept: the "new team joining" analogy survived all versions. "I assumed, and I was wrong" survived. The honest "no metric" concession survived and got stronger with real numbers. The blockquote placement survived.
- reader: findings 2 (speed contradiction) and 3 (guru paragraph) accepted and applied. Finding 1 (hypothetical ticket section) partially addressed — reframed from "Say the team…" to pattern in past tense, but no specific named integration available. Reader verdict was NOT YET; Nic approved anyway after the chronological restructure improved the thesis section's positioning.

### 2026-09-13 · about-page (a page, not a post) · edit load: medium (v4 approved)
- cut: the whole scene opener ("In January 2026 I froze my team's hiring plan… That's roughly how I work"). On the About page he wanted a plain chronological start ("I started CookiesHQ… in 2011"), not a moment. The "open with the moment" rule is for posts; pages can open on the fact.
- cut (before drafting): co-founder detail, HYROX, kids, hard 4pm, "calm CTO", "public CTO lab". Keep the *idea* of a designed, sustainable pace ("a bad week stays a bad week"), lose the lifestyle specifics.
- replaced: the old copy's "Catherine" was wrong — never carry a name from old site copy without checking. Years: he confirmed "30 years, 15 of them as a CTO" (homepage said 20+; fixed to match).
- added: "board advisor to software agencies" (new fact, his words). Blog posts are still called "field notes" even with the lab paused.
- kept: buyer-facing paragraph once, after the writer identity, ending on the email as the single next step (research-backed; he didn't push back). The fm block carries the CV so the prose never lists credentials.
- reader: all three findings accepted (pick opening B; cut the receipt-less beliefs section; fix the "this" referent in "I've run teams through this") — then he cut opening B too.
- method: research agent → plan with his verbatim answers → drafter → humanizer → cold read → three versions. Worked for a page as well as a post.

### 2026-09-22 · nobody-taught-developers-to-delegate · edit load: light (v4 approved; four versions, every change sentence-level, no structural move)
- cut: every optional `[…]` marker rather than filling it (CookiesHQ hand-over, named ticket, restart outcome, start date). When Nic says "can't recall" in the plan, the drafter should not leave a marker for it; cut the line. Also cut "I can't point at one ticket for it, because it was how every feature went" (the plan-sanctioned honesty line) — he prefers to state the pattern and move on rather than confess the missing example. Cut the Business Insider attribution ("What I can say is that when Business Insider followed up with him,") — the source is in the thread link, no need to name the outlet in prose.
- replaced: "[month or season]" → "In the first few weeks of me introducing our AI workflow" (dates the scene relative to his own action, not the calendar).
- added: nothing new of his own; every fix came from his markers or the reader.
- kept: the uncomfortable line "you handed them a subordinate and never taught them to manage one" survived, as did the bet one-liner next to it and the single blockquote "Button-pushers are made, not hired." The "different animal" distinction (senior IC vs someone who has delegated to a human) survived. The workflow written as what happens, not a framework, survived unedited.
- reader: all three accepted on request ("Fix what the reader found"): removed the judgement of v0xium's managers two sentences after "I can't say anything about his experience"; cut the hedged "Consider a developer… may struggle… may feel overwhelmed" restatement before the blockquote; introduced "two halves" once at the end of section 2 before it is referenced. Kept section 3 as a section (his verbatim words) rather than folding it into section 2 as the reader suggested — he didn't ask for the fold.
- pattern to watch (2/3): he cuts hedged restatements of the claim that sit just before the blockquote (also cut on ai-measuring-wrong-thing: the guru paragraph before the absorb line). Once more and it goes into Voice: "the paragraph before the quotable line is the first to go".
