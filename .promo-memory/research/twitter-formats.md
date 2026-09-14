# Twitter/X formats and best practices, 2025-2026

## Internal sources

No file in `_posts/` or `_field_notes/` covers Twitter/X promotion strategy.
`_posts/2024-07-18-the-ctos-wardrobe.md` mentions Twitter once, in passing,
as a place to follow thought leaders — not a promotion tactic. Nothing to
link or avoid repeating.

## 1. Post formats — limits and specs

**Text limit.** Free accounts cap posts at 280 characters. Premium
subscribers get up to 25,000 characters ("long-form posts"). Verified.
Source: [Publora, "X (Twitter) Character Limit in 2026"](https://publora.com/blog/twitter-character-limit) —
"X still caps free posts at 280 characters - Premium raises it to 25,000."

**Links cost 23 characters** regardless of pasted length (t.co shortener);
each emoji counts as 2 characters. Verified, same source.

**Long-form Articles** (rich formatting, headings, embeds) are a separate,
more restricted tier: Premium+ ($16/mo) or Verified Organizations only, distinct
from the 25K-character "long-form post." Source: X user citing a Grok query, Jan 2026 —
["Long-form posts... available to all X Premium subscribers... Articles...
currently still restricted to Premium+ subscribers"](https://x.com/MichealCodes/status/2012802486805897696).
Treat this one as inferred/lower-confidence — it's a screenshotted AI answer,
not an X help-center page, though it's consistent with other reporting on the
$1M article prize (Social Media Today, 2026) which required "at least 1,000
words" and judged on "Verified Home Timeline impressions."

**Images.** Up to 4 images per post. Recommended single-image size ~1200×675
(16:9). Multi-image grids reflow: 2 images render side-by-side at 7:8 each;
3 images render as one 7:8 + two 4:7. Desktop allows any ratio between 2:1
and 1:1; mobile also allows 3:4. Max file size 2MB (JPG/PNG/GIF). Source:
[Metricool, "Twitter Image Sizes 2025"](https://metricool.com/twitter-image-size/)
and [Influencer Marketing Hub, "X Image Sizes for 2026"](https://influencermarketinghub.com/twitter-image-size/).
Verified via aggregation of these vendor guides — no single X help-center page
was located with all grid ratios; treat exact grid math as inferred from
consistent secondary reporting.

**Video.** Free accounts: up to 140 seconds (2:20), 512MB. Premium: up to 4
hours. Recommended resolution 1280×720 or 1920×1080; max 1920×1200, min
32×32. Supports 16:9, 1:1, 9:16, and any ratio between 1:3 and 3:1. MP4
(H.264/AAC) recommended. Verified, aggregated from
[Nemovideo](https://www.nemovideo.com/blog/twitter-video-specs-guide-2026) and
[Buzzvoice, "X Video Length Limits 2026"](https://buzzvoice.com/blog/how-long-can-twitter-videos-be).

**Polls.** 2-4 options, 25 characters each, duration 5 minutes to 7 days.
Source: [Woobox, "X Poll Best Practices"](https://woobox.com/articles/twitter-x-poll-best-practices).
Strategic guidance (1 day for a recurring question, 2-3 days for a real
decision, diminishing returns past 3 days) is inferred/opinion from vendor
content, not an X specification.

**Spaces (live audio).** No hard specs found beyond practical guidance:
45-90 minutes is commonly cited as the engagement sweet spot, up to 2 hours
for workshops. Guest co-hosts expose the Space to the guest's followers.
This is practitioner consensus across multiple SEO/vendor blogs, not an X
official doc — treat as inferred.

**Thread mechanics.** A thread is a chain of individually-posted replies to
your own tweet; each tweet still obeys the 280-character limit (unless using
long-form). No official cap on thread length; practitioner guidance below.

## 2. Algorithm — what's actually documented vs. what's inferred

**Primary source: X's open-sourced ranking code**, `twitter/the-algorithm-ml`
repo, `recap/README.md`. Released March 2023; this is the one verifiable,
primary-source artifact in this research (dated code, not guaranteed current
in 2026, but it's the only place actual weight numbers are published).
Quoted weights (as documented in that file):

- `scored_tweets_model_weight_fav: 0.5`
- `scored_tweets_model_weight_retweet: 1.0`
- `scored_tweets_model_weight_reply: 13.5`
- `scored_tweets_model_weight_reply_engaged_by_author: 75.0`
- `scored_tweets_model_weight_negative_feedback_v2: -74.0`
- `scored_tweets_model_weight_report: -369.0`

Final score = weighted sum of predicted-engagement-probability × weight per
type. Source: [github.com/twitter/the-algorithm-ml, recap README](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md).
**Verified** — read directly.

Note the discrepancy: this primary source shows retweet weight at 1.0 (not
0.5, i.e., 2x a favorite) and no bookmark line at all (bookmarks as a ranking
signal were added to the platform after this file's last public update).
Multiple 2026 vendor blogs claim "retweet 20x, bookmark 10x, reply 13.5x,
profile click 12x, link click 11x" — these numbers are **inferred/unverified**:
no vendor cited a dated, primary source for the 20x/10x/12x/11x figures, and
they don't match the one primary document found. Treat any specific weight
beyond the reply=13.5x-a-fav figure (confirmed in the actual repo) as
unconfirmed marketing-content repetition, likely uncritically copied between
SEO blogs.

**Reply weight is the one number with real backing**: reply (13.5) is 27x
favorite (0.5), and author-engaged reply (75.0) is 150x a favorite. This
supports the general claim that posts provoking author replies get ranked
far higher than posts that only collect likes — verified from the primary
source math, not merely asserted.

**Counter-evidence / caveat**: the repo is from March 2023 and X's ranking
stack has reportedly been rebuilt multiple times since (vendor blogs claim a
"Grok-powered transformer model" replaced it in January 2026, processing
"500 million daily tweets" and "5 billion ranking decisions per day" —
source: [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works)).
No primary source (X engineering blog, official announcement) was found to
confirm this rebuild or its specifics. **Inferred at best** — could be
fabricated/hallucinated content common to SEO-optimized "2026 guide" pages
that recur across many of the search results. Any post citing exact
algorithm mechanics from 2026 should flag this uncertainty rather than
present these numbers as current fact.

**Link penalty.** Widely repeated claim across vendor blogs: posts with
external links get suppressed (~30-50% less reach per one source, "up to 80%"
per another), so the practitioner workaround is posting the link in a reply,
not the main post. One source claims "X officially said it removed the
penalty in October 2025 but the data says otherwise" — source:
[dkodetech.com](https://dkodetech.com/does-the-twitter-x-algorithm-downrank-your-links-what-small-businesses-should-know/).
No primary X statement was located either confirming or denying a link
penalty. This entire claim is **inferred** — treat as commonly-believed
practitioner lore, not verified fact. It is nonetheless the single most
consistent, repeated claim across all algorithm sources found, which raises
its credibility as directionally true even without a primary citation.

**Dwell time / read-through**, repeatedly cited as "the most heavily weighted
signal," has no primary-source confirmation found (not in the 2023 repo
README, which lists explicit engagement-probability weights but not a dwell
metric by that name). Inferred/unverified.

**Format vs. distribution claim**: one source states "X's algorithm now
treats single long-form posts... more favourably than multi-tweet threads for
distribution" — source: [teract.ai](https://www.teract.ai/resources/twitter-thread-writing-2026).
No primary confirmation; contradicts other sources claiming threads (4-8
tweets) are "the best format for complex insights." These two claims are in
direct tension across the vendor-content ecosystem — a sign that no one
actually knows, or that it depends on account size/niche. Flag both as
inferred and mutually contradicting.

## 3. Blog-to-Twitter conversion / the "atomic idea" approach

**Core practice, consistently repeated**: extract one thesis from the blog
post, then pull 8-12 supporting points/stats/insights, one per tweet. "One
idea per tweet" — cramming two thoughts kills rhythm; if a tweet has an "and
also," split it. Source: [Circleboom, "How to convert a blog post to a
Twitter thread"](https://circleboom.com/blog/how-to-convert-a-blog-post-to-a-twitter-thread)
and [RePurpose](https://repurpose.ws/blog/how-to-turn-blog-into-x-thread).
This is inferred/practitioner-consensus, not backed by platform data, but it
is the dominant framing across every "atomic idea" / "lean writing" source
found, including Ship 30 for 30's essay on the technique:
["Lean Writing On Twitter: How To Turn A Tweet Into A Thread Into An Atomic
Essay"](https://www.ship30for30.com/post/lean-writing-on-twitter-how-to-turn-a-tweet-into-a-thread-into-an-atomic-essay).

**Manual restructuring, not paragraph-splitting**: "a blog rewards depth and
gradual development, while a thread rewards density and hooks... restructuring
the content for a different reading context." Source: same Circleboom
article. Inferred/opinion, widely repeated.

**Closing pattern**: numbered tweets (1/12, 2/12), end with either a
restated main point, an engagement ask, or a link back to the full post.
Source: [Tugan.ai, "How to Write a Twitter Thread"](https://tugan.ai/blog/how-to-write-a-twitter-thread).
Inferred/practitioner consensus.

## 4. Thread-specific best practices

**Tweet length inside a thread**: keep tweets under ~250 characters even
though the limit is 280; "tweets with 250+ characters feel dense... long
tweets also perform worse algorithmically." Some sources claim the sweet spot
for likes is actually 240-259 characters ("near-max"), which contradicts the
"keep it short" advice above — another internal contradiction across sources.
Source: [teract.ai](https://www.teract.ai/resources/twitter-thread-writing-2026).
Inferred, contradictory.

**Optimal thread length**: 4-8 tweets is repeatedly cited as best for
"complex insights," with the claim that "a 7-tweet thread keeps someone
reading for 2-3 minutes" and dwell time is rewarded. Source: same. Inferred,
no primary confirmation of the dwell-time mechanism (see algorithm section).

**Hook pattern**: first tweet should use "specific numbers or contrarian
statements to create immediate curiosity," and should not give away the
punchline. Example cited: "I spent $50K on content marketing experiments.
Here's what actually worked (and what was a complete waste of money)."
Source: [Tugan.ai](https://tugan.ai/blog/how-to-write-a-twitter-thread). Inferred/opinion.

**Progressive build**: save the strongest insight for tweets 6-8, not the
opener, to sustain read-through across the thread. Source: teract.ai.
Inferred, unverified mechanism.

**When threads beat single tweets**: no primary source draws this line
cleanly. Vendor consensus: threads for "complex, multi-point" ideas; single
tweets (or single long-form posts, per Premium) for a single sharp claim.
This is inferred, and directly conflicts with the "long single posts now beat
threads for distribution" claim noted above — flag the tension if referenced.

## 5. Posting frequency and timing

**Best days/times, widely repeated but not attributed to X data**:
Tuesday-Thursday, roughly 9-11am or 12-6pm. One source: "Wednesday is the
single best day to post... 17% higher engagement than weekly average" and
"Wednesday at 9am is the single best time." Source:
[Sprout Social, "Best Times to Post on Twitter (X) in 2026"](https://sproutsocial.com/insights/best-times-to-post-on-twitter/).
Sprout Social does run its own aggregated-customer-data studies historically,
so this is a somewhat more credible source than pure SEO content, but the
specific "17%" figure could not be independently verified in this session —
treat as inferred pending direct read of Sprout's methodology.

**Thought-leadership-specific timing**: threads recommended at lunch
(12-1pm) or commute hours (5-6pm) "when people have dedicated reading time."
Inferred/opinion, no data cited.

**Frequency**: brand/business accounts, 1-3 posts/day is the commonly cited
ceiling before "diluting engagement per post." Creator accounts, 3-5
posts/day "across different formats" is cited as the 2026 sweet spot for
growth. Consistency (5-7 days/week) is claimed to matter more than exact
timing, training "the algorithm to surface your content more reliably."
Source: [RecurPost, "Best Time to Post on Twitter/X in 2026"](https://recurpost.com/schedule-tweets/best-time-to-post-on-twitter/)
and related vendor round-ups. All inferred, no primary data cited by any
source found.

**Spacing between tweets about the same topic**: no reliable source found.
Tried: "twitter posting spacing same topic algorithm penalty," folded into
the frequency searches above; no source directly addressed spacing multiple
posts about one topic/story. This is an open gap — no reliable source found.

## Summary of what's actually verified vs. inferred

Verified (read from a primary or first-party source):
- 280-char free limit / 25,000-char Premium long-form limit.
- The 2023 Heavy Ranker weight file's exact numbers (fav 0.5, retweet 1.0,
  reply 13.5, author-engaged reply 75.0, negative feedback -74.0, report
  -369.0), and that reply-with-author-engagement is 150x a favorite.
- Video: 140-second/512MB free cap, 4-hour Premium cap.
- Poll: 2-4 options, 25 chars each, 5-min to 7-day duration.

Everything else in this document — algorithm-in-2026 rebuild claims, the
retweet=20x/bookmark=10x figures, link-penalty percentages, dwell-time
primacy, optimal thread length, hook formulas, best posting times/frequency —
is inferred from repeated but uncorroborated vendor/SEO content. Multiple
sources contradict each other on thread-length-vs-long-form-post
distribution and on ideal tweet character count, which is itself worth
noting: the practitioner consensus is not settled.
