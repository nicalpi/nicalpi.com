---
name: nicalpi-brand
description: Apply the NicAlpi personal brand system for Nic Alpi (nicalpi.com). Use this skill whenever generating visual assets (social cards, blog headers, quote images, diagrams), writing or reviewing web code (HTML, CSS, Jekyll, Tailwind), creating any on-brand content, or when asked about NicAlpi's design system, colour palette, typography, or voice. This replaces the Calm CTO brand entirely. Trigger on any mention of: NicAlpi, nicalpi.com, the brand, brand guidelines, blog styling, social card, quote card, header image, or "on-brand". Also trigger when writing CSS variables or design tokens for Nic's projects.
---

# NicAlpi Brand System

Personal brand for Nic Alpi — CTO, agency founder, HYROX athlete, writer. Based in Bristol, UK.

**Core positioning:** "Not a navy seal." — honest, relatable tech leadership content. Anti-aspirational. Real experience without the LinkedIn performance.

---

## Quick Reference

| Token | Value |
|-------|-------|
| Accent | `#3B82F6` (Blue) |
| Accent dark | `#1A4FA8` |
| Accent light | `#EFF6FF` |
| Accent mid | `#BFDBFE` |
| Ink | `#111111` |
| Body text | `#3A3A3A` |
| Muted | `#717171` |
| Border | `#E3E1DD` |
| Off-white | `#F5F4F1` |
| White | `#FFFFFF` |
| Heading font | DM Sans 800 |
| Pre-heading font | Caveat 600 |
| Body font | DM Sans 400 |

---

## Colour System

```css
:root {
  /* Core */
  --white:      #FFFFFF;
  --off-white:  #F5F4F1;  /* section bands, NOT page background */
  --ink:        #111111;  /* headings, dark sections */
  --body:       #3A3A3A;  /* body text */
  --muted:      #717171;  /* meta, secondary */
  --border:     #E3E1DD;  /* dividers, card borders */

  /* Accent — Blue */
  --blue:       #3B82F6;  /* buttons, blockquote border, highlights, CTAs */
  --blue-dark:  #1A4FA8;  /* small text on white — 7.2:1 WCAG AA */
  --blue-light: #EFF6FF;  /* section tints, blockquote bg, tag bg */
  --blue-mid:   #BFDBFE;  /* borders on tinted sections, highlight bg */
}
```

### WCAG Compliance
| Combination | Ratio | Pass |
|-------------|-------|------|
| Ink on White | 19.1:1 | AA + AAA |
| Blue Dark on White | 7.2:1 | AA + AAA |
| White on Blue (#3B82F6) | 3.0:1 | Large text / buttons only |
| White on Ink | 19.1:1 | AA + AAA |
| Muted on White | 5.3:1 | AA |

### Usage rules
- **White** is the default page background. Never use off-white as a page background.
- **Off-white (#F5F4F1)** is used as full-width section bands to create rhythm (about section, alternating sections). Not for cards on a white page.
- **Blue (#3B82F6)** on dark backgrounds: use the full value — never a pale/muted variant.
- On dark backgrounds, body text should be **white (#FFFFFF)**, not grey. Secondary items (nav links, captions) can be `rgba(255,255,255,0.65)` maximum — never lower.
- **Blue is the single accent.** One moment of blue per section. It's a signal, not a pattern.

---

## Typography

```html
<!-- Always import both fonts -->
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&family=Caveat:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Font roles
| Role | Font | Weight | Size | Tracking |
|------|------|--------|------|----------|
| Display hero | DM Sans | 800 | clamp(52px, 7vw, 88px) | -2.5px |
| H1 | DM Sans | 800 | 36–40px | -1px |
| H2 | DM Sans | 700–800 | 28px | -0.5px |
| H3 | DM Sans | 700 | 20px | -0.3px |
| Body | DM Sans | 400 | 17px | 0 |
| Small/meta | DM Sans | 400 | 13px | 0 |
| Label (uppercase) | DM Sans | 700 | 11px | +2.5px |
| Pre-heading | Caveat | 600 | 18–22px | 0 |
| Annotation/signature | Caveat | 500–600 | 16–20px | 0 |

### Rules
- **DM Sans 800** for all headings, always. No other weight for headings.
- **Caveat** for pre-headings (above H1/H2), personal annotations, signatures, and human moments. Use sparingly — once per section maximum.
- Never use Caveat for body text or UI labels.

---

## Wordmark

```
NicAlpi
```

- One word. DM Sans 800. Plain ink or plain white. **No coloured letters.**
- The blue lives in components only — never in the wordmark.
- Min size: 18px on screen.
- Never separate into two words. Never add icons or marks.

```css
.wordmark {
  font-family: 'DM Sans', system-ui, sans-serif;
  font-weight: 800;
  font-size: 22px;
  color: #111111; /* or #FFFFFF on dark */
  letter-spacing: -0.5px;
  line-height: 1;
}
```

---

## Taglines (in priority order)

1. **"Not a navy seal."** — preferred, homepage hero and social bios
2. **"Real work. Real life."** — secondary, works beneath the primary
3. **"Honest about it."** — versatile, bio closers, subheadlines
4. **"Less bullshit, more building."** — reserve for individual contrarian posts

---

## Components

For full component CSS, see `references/components.md`.

### Blockquote — Light
```css
border-left: 4px solid #3B82F6;
background: #EFF6FF;
padding: 24px 28px;
border-radius: 0 12px 12px 0;
/* Quote text: DM Sans 700, 18–20px, #111111 */
/* Attribution: Caveat 600, 17px, #717171 */
```

### Blockquote — Dark
```css
background: #111111;
border-radius: 12px;
padding: 32px;
/* Large decorative quote mark: DM Sans 800, 120px, #3B82F6 at 15% opacity */
/* Quote text: DM Sans 700, 20px, #FFFFFF */
/* Attribution: Caveat 600, 17px, rgba(255,255,255,0.65) */
```

### Buttons
```css
/* Primary (on light bg) */
.btn-primary { background: #111111; color: #FFFFFF; }

/* Blue (on light OR dark bg — same value both places) */
.btn-blue { background: #3B82F6; color: #FFFFFF; }

/* Ghost */
.btn-ghost { background: transparent; border: 2px solid #E3E1DD; color: #111111; }

/* Shared */
font-size: 15px; font-weight: 700; padding: 13px 24px;
border-radius: 8px; border: none; cursor: pointer;
```

### Tags/Labels
```css
/* Default */   background: #F5F4F1; color: #3A3A3A; border: 1px solid #E3E1DD;
/* Blue */      background: #EFF6FF; color: #1A4FA8; border: 1px solid #BFDBFE;
/* Dark */      background: #111111; color: #FFFFFF;
font-size: 12px; font-weight: 600; padding: 6px 14px; border-radius: 100px;
```

### Post Card
```css
background: #FFFFFF; border: 1px solid #E3E1DD;
border-radius: 12px; padding: 24px 28px;
/* Hover: border-color → #BFDBFE, box-shadow: 0 4px 20px rgba(59,130,246,0.08) */
```

### Inline Highlights
```css
/* Background chip */  background: #BFDBFE; padding: 2px 6px; border-radius: 4px;
/* Underline */        border-bottom: 3px solid #3B82F6; color: #1A4FA8;
```

---

## Page Layout

```css
/* Section bands */
.section-white    { background: #FFFFFF; }
.section-offwhite { background: #F5F4F1; border-top: 1px solid #E3E1DD; border-bottom: 1px solid #E3E1DD; }
.section-dark     { background: #111111; }

/* Max widths */
--max-article: 640px;   /* body text, prose */
--max-page:    960px;   /* page wrapper */

/* Spacing scale */
--sp-xs:  4px;  --sp-sm: 8px;   --sp-md: 16px;
--sp-lg:  24px; --sp-xl: 32px;  --sp-2xl: 48px;
--sp-3xl: 64px; --sp-4xl: 80px;
```

### Section rhythm (homepage)
```
White    — nav + hero
Off-white — about / featured sections (full-width band)
White    — posts / reading list
White    — blockquote interlude
Dark     — newsletter CTA (full-width, no card rounding)
White    — footer
```

---

## Voice & Tone

**Write like this:**
- Short sentences. One idea per paragraph.
- First person, specific. "I did this. Here's what happened."
- Honest about uncertainty. "I'm not sure this is right."
- Concrete details. "8 people, not 'a small team'."
- Most important thing first.

**Never:**
- Hyperbole — "game-changing", "revolutionary", "transformative"
- Navy seal / elite framing
- Vague inspiration — "find your why"
- Performing certainty you don't have
- Bullet lists as a substitute for thinking

**Example contrast:**
- ❌ "As a seasoned technology executive with over two decades of experience..."
- ✓ "I've been running dev teams for 20 years. Here's what I learned — mostly by getting it wrong first."

---

## Social Cards

Three styles. Full specs in `references/social-cards.md`.

| Style | Background | Use |
|-------|-----------|-----|
| Dark | `#111111` | Bold takes, hot opinions |
| Light | `#FFFFFF` + blue top border | How-to, practical content |
| Blue | `#3B82F6` | Manifestos, statements |

**Dimensions:**
- OG / Twitter: 1200 × 630px
- LinkedIn: 1200 × 627px
- Instagram square: 1080 × 1080px

Wordmark on all cards: plain ink or plain white. No coloured letters.

---

## Generating Visual Assets (HTML → Image)

For social cards, blog headers, and quote images:

1. Build HTML using the colour system and typography above
2. Export using Playwright:

```bash
python3 scripts/export_image.py input.html output.jpg --width 1200 --height 630
```

Options: `--width`, `--height`, `--quality` (default 95), `--scale` (default 2 for retina)

See `references/social-cards.md` for ready-to-use HTML templates for each card style.

---

## Using This Skill in Claude Code (Jekyll Projects)

When working on `nicalpi.com` (Jekyll blog), apply these rules:

### CSS Custom Properties
Always define brand tokens as CSS custom properties at `:root` level. See the Colour System section above for the full token set.

### Jekyll-specific patterns
- `_sass/` or `assets/css/` — put brand tokens in `_variables.scss` or `_tokens.css`
- Post layouts should max-width article body to `640px`
- Use `font-display: swap` on Google Fonts `<link>` tags
- Pre-heading pattern: `<span class="pre-heading">Caveat text</span>` above `<h2>`

### What to apply where
| Jekyll file | Brand application |
|-------------|------------------|
| `_layouts/default.html` | Font imports, base CSS variables |
| `_layouts/post.html` | Article max-width 640px, body 17px/1.75 |
| `_includes/header.html` | Wordmark (plain ink, DM Sans 800), nav links |
| `_includes/footer.html` | Wordmark (plain ink or white), muted text |
| `_sass/_variables.scss` | All CSS custom properties |
| `_sass/_typography.scss` | Heading + body scale |
| `_sass/_components.scss` | Cards, blockquotes, tags, buttons |
| `assets/css/main.css` | Root :root block, global resets |

### Checklist when rebranding
- [ ] Font import updated (DM Sans + Caveat, both weights)
- [ ] CSS variables set at `:root`
- [ ] Body background: `#FFFFFF` (never off-white as global bg)
- [ ] Headings: DM Sans 800, correct tracking
- [ ] Pre-headings: Caveat 600, blue-dark colour
- [ ] Wordmark: plain ink, no coloured letter
- [ ] Off-white used only for full-width section bands
- [ ] Blue buttons consistent on light and dark backgrounds
- [ ] Body text on dark: `#FFFFFF` (not grey)
- [ ] Article max-width: 640px

---

## Reference Files

- `references/components.md` — Full CSS for every component with copy-paste code
- `references/social-cards.md` — HTML templates for all three social card styles
