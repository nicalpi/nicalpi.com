---
name: nicalpi-brand
description: Apply the NicAlpi personal brand system for Nic Alpi (nicalpi.com). Use this skill whenever generating visual assets (social cards, blog headers, quote images, diagrams), writing or reviewing web code (HTML, CSS, Jekyll, Tailwind), writing or editing any content in Nic's voice (posts, field notes, newsletters, social copy, bios), or when asked about NicAlpi's design system, colour palette, typography, or voice. Trigger on any mention of: NicAlpi, nicalpi.com, the brand, brand guidelines, blog styling, social card, quote card, header image, field notes, "on-brand", or "in Nic's voice". Also trigger when writing CSS variables or design tokens for Nic's projects.
---

# NicAlpi Brand System — v4 "Graphite notebook"

Personal brand for Nic Alpi — CTO at Amba, an age-tech company in Bristol,
UK. Sold his 20-person Rails consultancy (CookiesHQ) in 2021. HYROX athlete,
three kids, hard 4pm stop. Writes in public.

**Core positioning:** a working CTO writing after the fact. "What worked,
what failed, and what I'm changing next." Honest, measured,
anti-performative. Field notes (paused) are experiments with a baseline, a
protocol, guardrails and a one-word verdict, published even when the answer
is "this did nothing".

**Art direction:** rendered markdown, made literal. The wordmark is
`nicalpi.md`; the home hero (after its headline) and every post carry a
`---` front-matter block; post lists are a directory listing under `ls -t _posts/`; beliefs are
`- [x]`; the newsletter is a `> newsletter` band; the footer ends in `EOF`.
Mono for everything that is chrome or heading, a serif for everything read
at length, one graphite grey scale, and signal blue only where the markdown
marks go. Light and dark are first-class.

**The full spec is `DESIGN.md` at the repo root** — tokens, type scale,
radii, every component, do's and don'ts, agent prompts. This skill is the
working summary plus the rules that bite. Companion docs in this folder:

- `voice.md` — how Nic writes. Read it before writing any prose as Nic.
- `components.md` — every site component with markup (repo work).
- `social-cards.md` — OG images and promo card templates.

---

## Tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--panel` (`--canvas`) | `#FFFFFF` | `#0F1114` | page surface |
| `--side` | `#F0F0F3` | `#1A1D22` | fog: fm block, newsletter, code, hover, tag fills |
| `--raise` | `#F7F7F9` | `#15181C` | card/row hover |
| `--line` / `--line2` | `#D9D9E0` | `#2A2E35` | the one hairline |
| `--ink` | `#1C2024` | `#F2F3F5` | headings, strong, primary button fill |
| `--body` | `#2A2E34` | `#C9CCD2` | running serif text |
| `--muted` | `#60646C` | `#8B8F98` | graphite: meta, nav at rest, footer |
| `--faint` | `#80838D` | `#6B6F78` | steel: column labels, `EOF`, `.md`, read-time — labels only |
| `--accent` | `#0072DE` | `#6DB8FF` | text links, category word, "now", running state |
| `--mark` | `#0090FF` | `#3DA5FF` | `#`/`##`, `---`, `- [x]`, `>`, `→` — punctuation only |
| `--accent-soft` / `--accent-line` | `#EAF4FF` / `#B9DBFF` | `#14233A` / `#2B4A73` | tint surfaces, at-rest underlines |
| `--on-ink` / `--on-accent` | `#FFFFFF` | `#0F1114` | text on fills |

Two blues, two jobs. Blue is never a fill. Ink is the only fill (primary
button, active chip, verdict card). Tinted surfaces have no border. No
shadows, gradients or blur.

In the repo, tokens live in `_assets/main.css` (`:root` = light,
`[data-theme="dark"]` = dark); Tailwind maps them in `tailwind.config.js`
(`text-ink`, `bg-side`, `border-line`, `text-accent`, `text-mark`,
`rounded-brand` = 12px …). Never hard-code hex values in templates — outside
the repo (mockups, artifacts, Claude Web), copy the token block from
`DESIGN.md` verbatim.

## Type

- **JetBrains Mono** 400/500/600/700, `letter-spacing: -0.012em` — wordmark,
  top bar, every heading, front-matter blocks, directory rows, buttons,
  chips, kickers, footer, code, and **every image**. 600 for buttons,
  section titles and prose h2–h4; 700 for page/post titles.
- **Source Serif 4** 400/600 + italic, optical sizes — post prose, leads,
  the post dek, beliefs, directory titles (600), form help. Never in
  headings, never in images. Default font smoothing.
- Scale is compact and weight-led: hero 38px, post h1 32px (dek 20px serif
  `--muted`), page h1 26px, section h2 16px/600, prose 18px/1.75 with h2 at
  1.1em/600 plus a hairline, directory titles 17.5px serif, meta 13px,
  labels 11px uppercase. Only the hero and post h1 go above 30px.

## Shapes and layout

- Buttons and inputs 36px pills (40px tall, 44px on phones). Nav link chips
  24px. Filter chips, tags and the theme toggle 9999px. Front-matter block,
  cards, code blocks, images 12px. Newsletter band 20px. Focus: 2px accent.
- Frame: borderless sticky 64px top bar (wordmark left; `writing · about ·
  work with me` chips + theme pill right) → centred 1024px `.sheet` (880px
  inner) → one-line footer over a hairline. One surface, no canvas behind it.
- Home and list pages span the sheet. **Posts read in a centred 700px
  column** (`--measure`, ~75 characters): path line, fm, h1, dek, prose,
  article foot and prev/next cards share that edge. (Full-width posts ran
  13–23 Sep 2026 at ~100 characters a line and were pulled back.)
- Home order: headline → lead → buttons (primary "Start reading →", ghost
  email) → fm credentials card → "worked with" logos (per-shape optical
  heights: `.logo-wide` 17px, `.logo-mid` 24px, `.logo-block` 32px) →
  writing → beliefs → newsletter. The claim comes before the bio.
- Beliefs and the newsletter go two-column above 800px; the beliefs intro
  is sticky. Phone: 20px gutters, directory rows stack, buttons full-width.
- No sidebar, drawer or breadcrumbs (retired with v2; includes in `_retired/`).

## Signature devices (one per section, never two stacked)

- Wordmark `nicalpi.md` (`.md` in `--faint`, hidden on phones).
- `.fm` front-matter block: fog fill, 12px, no border, mono 13.5px/1.85,
  fences `--mark`, keys `--muted`, values `--ink`. The home credentials card
  under the headline. On posts `.fm-post` is unfilled and metadata only
  (category, date, reading_time) under a `_posts/<file>.md` line, 28px
  above the h1 — **never repeat the title or subtitle in it**; they render
  once as the h1 and dek.
- Directory listing: `date · category · title · read` (title in serif 600,
  the other columns mono), uppercase `--faint`
  column labels, an `ls -t _posts/ · N files` line. **Category is a plain
  lowercase word in `--accent`, not a pill** (Nic tried the pill and reverted
  it, 13 Sep 2026). Title turns `--accent` on hover, no underline, no arrow.
- Beliefs: `- [x]` in `--mark`. Newsletter: fog card, `> newsletter` kicker
  in `--mark`, pill input + ink button. Prose quotes: italic serif with a
  mono `>` hanging left in `--mark`, no bar. Footer ends in `EOF`.

## Links

Inline text links: `--accent` with a hairline underline in `--accent-line`
at rest, full accent on hover. Nav chips, buttons, chips, cards and
directory rows never underline — they shift background or colour.

## Images

All images are HTML on these tokens, rendered with Playwright, mono-only,
with the `nicalpi.md` wordmark and `nicalpi.com`, the `# ` mark before
headlines, `before → now` metrics (arrow `--mark`, now `--accent`), pills for
labels, ink for the one solid card (verdict). No photography, no blue fills.
See `social-cards.md`.

## Voice (summary — full guide in `voice.md`)

- Lowercase for nav, labels, meta ("writing", "work with me"). Sentence
  case for headings and body. No exclamation marks.
- First person, plain words, short paragraphs. British English.
- Numbers carry the story: `before → now` with "now" in accent.
- Verdicts are one word: kept / dropped / inconclusive.
- Honest hedges stay in ("small sample, read the direction, not the
  decimals"). No pretend certainty, no guru register.

## Accessibility

WCAG AA on white: ink 16.1:1, body 13.4:1, muted 5.7:1, accent 4.9:1.
`--faint` is for labels and decoration only. Focus ring 2px accent. Reduced
motion respected. Theme set pre-paint (`localStorage` → `prefers-color-scheme`).

## Where things live (repo work)

| Thing | Path |
|---|---|
| Full spec | `DESIGN.md` |
| Tokens + component CSS (source) | `_assets/main.css` → `yarn css` → `assets/main.css` (committed) |
| Tailwind token mapping | `tailwind.config.js` |
| Components (live) | `/styleguide/` (`styleguide.html`) |
| Component reference | `components.md` |
| Social templates + `social.css` | `assets/social-templates/` + `social-cards.md` |
| OG generator / illustration renderer | `scripts/generate-og.py`, `scripts/render-illustration.py` (`/opt/homebrew/bin/python3.13`) |
| Newsletter | Kit form 5638226; `_includes/newsletter.html` + `[data-newsletter-form]` in `site.js` |
| Design canvas (chosen direction + rejected blends) | https://claude.ai/code/artifact/45b46ca1-4d7c-467b-bb94-47a0f0a77edf |

**History.** v2 "Calm CTO" (DM Sans + Caveat, sage, sidebar) → v3 "Field
Notes" (Jul 2026 mono + warm paper; Sep 2026 single sheet, Source Serif 4,
front-matter direction) → **v4 "Graphite notebook"** (13 Sep 2026: Expo's
graphite scale and pill controls blended in; warm paper retired).

**On Claude Web** (no repo): apply the tokens, type scale and voice directly;
output complete files or snippets and say what still needs doing in the repo
(compile CSS, generate OG image). Never claim files were created.
