# LinkedIn formats and best practices, 2025-2026

Internal search: no prior Nic writing on LinkedIn strategy found in `_posts/` or
`_field_notes/`. Nothing to link or avoid repeating.

General caveat that applies to nearly every finding below: almost all sources
are SEO/marketing blogs run by social-media scheduling tools (Buffer,
ContentIn, Postiv AI, Sendible, SocialPilot, etc.), not LinkedIn itself. Their
numbers come from self-reported "studies" of unclear methodology, and several
contradict each other on the same question (see posting frequency, below).
Treat specific percentages as industry lore, not fact, unless marked verified
against an official LinkedIn source.

## 1. All LinkedIn post formats

**Text-only / single image / multi-image** — verified.
Source: ContentIn, "LinkedIn Post Specs 2026," last verified June 2026.
https://contentin.io/blog/linkedin-post-specs/
Quote: "Posts: 3,000 characters total... Supported aspect ratio: 3:1 to 4:5.
Recommended: 1080×1080 (square) or 1080×1350 (portrait)... Up to 20 images per
post."
Also: link-preview thumbnails render at 1.91:1, 1200×627px, and must be 200+
px wide or LinkedIn shrinks them to a small thumbnail (same source).

**Video** — verified (same source).
Quote: "Duration: 3 seconds–15 minutes (desktop); 10 minutes (mobile app); 10
minutes (Company Pages)... Aspect ratio: 1:2.4 to 2.4:1... Format: MP4 (H.264
codec)... File size: 75 KB minimum; ~5 GB practical maximum."
Quote: "Native uploads autoplay in the feed and consistently outperform link
embeds on reach" (same source, no independent verification found — treat as
inferred, not confirmed by LinkedIn).

**Carousel / document post** — verified.
Same source. Quote: "Max file size: 100 MB... Max pages: Up to 300...
Formats: PDF, DOC, DOCX, PPT, PPTX (PDF most reliable)... Recommended design
size: 1080×1080 or 1080×1350... Minimum font: 14 pt for body text."
Slide count for engagement: Oktopost, "LinkedIn carousel best practices for
2026." https://www.oktopost.com/blog/linkedin-carousel-pdf-best-practices/
Inferred summary from search aggregation: "Most high-performing B2B carousels
use 5 to 15 slides." No single verbatim quote captured — flag as inferred,
not a direct quote.

**Polls** — verified.
Source aggregated from multiple posts citing LinkedIn's own poll help page
and third-party guides (authoredup.com, "LinkedIn Polls," 2026;
LinkedIn Help, "LinkedIn Polls – FAQ," https://www.linkedin.com/help/linkedin/answer/a527270).
Poll question: 140 characters. Up to 4 options, 30 characters each. Duration:
1 or 2 weeks (fixed choices, no custom range). This matches LinkedIn's own
help page structure, so treated as verified for the mechanical limits; the
"keep accompanying text to 300-600 characters" advice is inferred (a
third-party recommendation, not a LinkedIn spec).

**Articles** — verified for length limits, inferred for reach mechanics.
Source: multiple 2026 guides citing the same range (e.g., linkedgrow.ai,
"How to Write a LinkedIn Article in 2026"). Reported max ~110,000-125,000
characters; recommended 800-1,500 words. No official LinkedIn spec page was
directly fetched, so treat the character ceiling as inferred (repeated across
sources but not confirmed on a LinkedIn help page).

**Newsletters** — verified for setup mechanics, inferred for reach claim.
Source: LinkedIn Help, "LinkedIn Newsletters best practices."
https://www.linkedin.com/help/linkedin/answer/a517940
Cover photo 1920×1080px, logo 300×300px, one edition per 24 hours — these are
LinkedIn's own stated constraints (verified by nature of being on
linkedin.com/help, though I did not fetch the page body directly and am
relying on secondary citation — mark as inferred pending direct fetch).
Reach mechanic, inferred (third-party framing, not an official LinkedIn
statement): "The platform delivers newsletter content directly to subscriber
inboxes and notifications, bypassing the feed algorithm entirely for
subscribers... links inside newsletters aren't downranked the way links in
regular posts often are."

**Events** — inferred.
Multiple 2026 guides (LeadsBridge, Converve, Writio) describe events as
auto-generating a feed post identical in reach mechanics to a normal post,
with the event's comment section usable for attendee communication. No
official LinkedIn source directly fetched; treat as inferred consensus.
Quote (Writio, 2026, secondary source): "this post gets the same reach and
discovery benefits as any regular LinkedIn post."

## 2. Algorithm preferences in 2025-2026

**Dwell time is a real, LinkedIn-confirmed ranking signal** — verified.
Source: Siddharth Dangi (LinkedIn Staff Software Engineer), with Johnson
Jia, Manas Somaiya, Ying Xuan. "Understanding dwell time to improve LinkedIn
feed ranking." LinkedIn Engineering Blog, 12 May 2020.
https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time
Quote: "Dwell time is a more reliable indicator of engagement" than clicks or
"viral actions" like likes/shares, because dwell time is continuous and
always measurable, while clicks are binary and noisier.
Note the date: this is a 2020 post, not 2025/2026 — it establishes that
dwell time has been an official LinkedIn signal for years, but the specific
"30-second threshold" and "60-90 second golden zone" numbers circulating in
2026 blogs are not confirmed by this or any other LinkedIn-authored source
found.

**Specific 2026 thresholds (30-second interest signal, comments weighted
15x likes)** — inferred, unconfirmed by LinkedIn.
Source: aggregated secondary 2026 blogs (meet-lea.com, dataslayer.ai,
teract.ai) citing each other and Richard van der Blom's "Algorithm Insights
Report." No official LinkedIn document with these exact multipliers was
found. Quote (as reported, uncertain original source):
"initial engagement quality (first-hour comments, weighted at 15x the value
of likes)."
Counter-evidence: a separate secondary source (via Hootsuite aggregation)
cites a different, non-comment metric as the top signal: "a save can drive
around five times the reach of a like... roughly twice the reach of a
comment" — i.e., saves, not comments, are described elsewhere as the
strongest signal. The two claims (comments > everything vs. saves > comments)
are not reconcilable from what was found; the field's numbers are
inconsistent.

**"Golden hour"** — inferred, and explicitly not an official LinkedIn term.
Source: ContentIn, "What Is the Golden Hour on LinkedIn?"
https://contentin.io/glossary/golden-hour/
Quote: "it is a creator-coined term: LinkedIn has never officially defined or
confirmed a specific time window, though it confirms engagement data shapes
feed ranking."
Counter-evidence / internal inconsistency: other 2026 sources claim the
window has already changed shape — one describes a "Momentum Model: a 3 to 8
hour evaluation phase" replacing the older 60-90 minute test window. Since
neither claim is LinkedIn-sourced, both should be treated as unverified
creator theory, not fact.

**Big architecture shift (official, verified)**: LinkedIn replaced its
ranking stack with a 150-billion-parameter model called 360Brew.
Source: Hristo Danchev, "Engineering the next generation of LinkedIn's
Feed," LinkedIn Engineering Blog, 12 March 2026.
https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed
(Confirmed via search aggregation citing this exact title/author/date; I did
not fetch the full body text directly, so mark the existence and date of the
post as verified, but the specific mechanism description — "many-shot
in-context learning, feeding 2-3 months of a member's activity... retrieval
and ranking... under 50 milliseconds" — as inferred pending a direct read.)
This is the most load-bearing fact for any "what does the algorithm actually
reward" claim: LinkedIn's 2026 ranking is now a single large sequence model
trained on recent behavior, not a hand-tuned formula of "comments beat
likes." Any post asserting fixed point-multipliers (15x, 5x, etc.) is
describing outputs of a black-box model observed by outside marketers, not a
disclosed formula.

## 3. Blog-to-LinkedIn repurposing patterns

**Do not repost verbatim; rewrite the opening for the LinkedIn reader** —
verified.
Source: Irina Maltseva, Growth Lead at Aura. Buffer,
"How I Repurpose Blog Content into LinkedIn Posts to Expand My Reach," 21
Mar 2024. https://buffer.com/resources/repurpose-blog-content-linkedin/
Quote: "Avoid simply reposting your blog content verbatim. The introduction
and opening paragraphs especially should be tweaked to better align with
your audience."

**Put the external link in the first comment, not the post body** —
verified (same source, same author/date).
Quote: "Putting your external link in the comments section and encouraging
the reader to click it with the 'check the first comment' CTA navigates this
problem" — the "problem" being LinkedIn's suppression of posts containing
outbound links.
Counter-evidence: LinkedIn's own 2026 architecture change (360Brew, a
learned model rather than hand-coded link penalties) makes it unclear
whether an explicit "outbound link penalty" still exists as a distinct rule
in 2026, versus being an emergent, weaker preference inside the model. No
source directly tested this in 2026.

**Distill into stats/visual points; carousels turn dense blog sections into
scannable slides** — verified (same source).
Quote: "Distill your post into key statistics, talking points, or visual
assets shared horizontally."

**Reach non-overlapping audience** — inferred.
Source: aggregated from LinkDeck AI, "How to Repurpose Blog Posts Into
LinkedIn Carousels," 2026. https://www.linkdeckai.com/blog/how-to-repurpose-blog-posts-into-linkedin-carousels
Quote (as reported): "only 5-10% of your blog readers are also active on
LinkedIn, so repurposing reaches entirely new people." No methodology given
for the 5-10% figure — treat as an unverified industry estimate.

**Selection criteria: validated posts, opinionated posts** — inferred.
Same aggregated search, multiple sources: posts with numbered steps/lists
convert best to one-idea-per-slide carousels; posts that "take a stance"
reportedly outperform neutral explainer content as carousels. No single
quote with clean attribution was captured for this specific claim.

## 4. Carousel/document posts specifically

**Dimensions** — verified. See section 1 above: 1080×1080 or 1080×1350,
PDF preferred, up to 300 pages / 100MB, 14pt minimum body font (ContentIn,
2026, cited above).

**Engagement claims vs other formats** — inferred, inconsistent across
sources.
One secondary source (aggregated from Writio/event-marketing search) claims:
"Carousel posts (document posts) are the best format for LinkedIn posts in
2026, generating 5.85-6.60% average engagement rates and 3.5x more reach
than text-only posts." Another aggregated source (Hootsuite-cited) says
plainly: "Documents, or carousels, turned out to be the most valuable assets
in terms of reach" (attributed to "Shubham Davey, SEO Copywriter," 2026).
Both point the same direction (carousels > text), but neither is a primary
LinkedIn-published number — no official confirmation was found that
carousels systematically outperform other formats. Treat as directionally
consistent industry consensus, not verified fact.

**Slide count** — inferred. 5-15 slides commonly cited (Oktopost, cited
above); a separate source in the events context recommends 8-12 slides for
event-teaser carousels. No exact optimum was confirmed by LinkedIn.

## 5. Posting frequency and timing

This is the area with the sharpest direct contradiction found in the
research, worth flagging explicitly for the drafter.

**Claim A — more is (almost) always better.**
Source: Buffer, "How Often Should You Post on LinkedIn in 2026? Data From 2
Million+ Posts." https://buffer.com/resources/how-often-to-post-on-linkedin/
Quote: "The short answer: no. Our analysis shows that posting more often
helps your performance on LinkedIn." And: "posting 6 to 10 times weekly
pushes the gains further with +5,001 more impressions per post... At 11+
posts per week, the lift is dramatic with nearly 17,000 more impressions per
post." Study basis: "2+ million LinkedIn posts from 94,000+ accounts,"
z-score and fixed-effects regression, per the same Buffer piece.

**Claim B — more than ~5/week hurts per-post performance and cannibalizes
distribution.**
Source: Seth Horne, Full Throttle Media, "Why Posting More on LinkedIn
Stopped Working," 1 May 2026.
https://www.fullthrottlemedia.com/2026/05/why-posting-more-on-linkedin-stopped.html
Quote: "When you publish a second post inside that window, the system
effectively interrupts the first one." And: "Beyond five posts per week,
per-post engagement drops in the range of eighteen to thirty-two percent."
And on lead quality specifically: "The qualified DMs, demo requests, and
inbound replies... tend to peak around three to four posts per week and
decline past that." This piece explicitly frames itself as a rebuttal of
"post daily" advice, citing three unnamed independent studies converging on
2-5 posts/week as optimal.

These two do not describe the same metric (Buffer: aggregate impressions
scale with volume; Full Throttle: per-post engagement rate and lead quality
degrade with volume) — both could be true simultaneously (more posts, each
one individually weaker, still nets more total reach). Any post citing one
without the other is telling half the story.

**Convergent, less contested number: 2-3x/week for thought leadership.**
Multiple sources agree on this range without direct contradiction: "the
recommended posting frequency is two to three times per week" and "the
optimal range is 2 to 5 times per week" (aggregated across Buffer,
salesandmarketingengineers.co.uk, connectsafely.ai, all 2026). Treat as
inferred consensus rather than a single verified figure.

**Timing ("golden hour" of day, not the engagement-window "golden hour")**
— inferred, weakly sourced.
One aggregated Hootsuite-derived source claims: "best time to post on
LinkedIn is between 4 AM and 6 AM on Tuesdays and Wednesdays" with "posting
weekly generates a 2x engagement lift versus sporadic posting." No
methodology given; contradicts the intuitive assumption that professional
audiences engage during business hours. Flag as suspect — likely an
artifact of a specific dataset's timezone mix rather than a universal rule.
