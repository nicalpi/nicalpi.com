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

_None yet._

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

_None yet._
