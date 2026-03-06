# NicAlpi Components — Full CSS Reference

Complete, copy-paste ready CSS for every component in the NicAlpi design system.

---

## CSS Custom Properties (always include at :root)

```css
:root {
  --white:      #FFFFFF;
  --off-white:  #F5F4F1;
  --ink:        #111111;
  --body:       #3A3A3A;
  --muted:      #717171;
  --border:     #E3E1DD;
  --blue:       #3B82F6;
  --blue-dark:  #1A4FA8;
  --blue-light: #EFF6FF;
  --blue-mid:   #BFDBFE;

  --font-heading: 'DM Sans', system-ui, sans-serif;
  --font-body:    'DM Sans', system-ui, sans-serif;
  --font-hand:    'Caveat', cursive;

  --max-article: 640px;
  --max-page:    960px;

  --sp-xs:  4px;
  --sp-sm:  8px;
  --sp-md:  16px;
  --sp-lg:  24px;
  --sp-xl:  32px;
  --sp-2xl: 48px;
  --sp-3xl: 64px;
  --sp-4xl: 80px;
}
```

---

## Base Reset & Body

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font-body);
  background: var(--white);
  color: var(--body);
  font-size: 17px;
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
}
```

---

## Typography Scale

```css
/* Pre-heading (Caveat — above H1 or H2) */
.pre-heading {
  font-family: var(--font-hand);
  font-weight: 600;
  font-size: 20px;
  color: var(--blue-dark);
  display: block;
  margin-bottom: 6px;
}

/* Display hero */
.display {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: clamp(52px, 7vw, 88px);
  line-height: 1.0;
  letter-spacing: -2.5px;
  color: var(--ink);
}

h1 {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: clamp(34px, 4.5vw, 42px);
  letter-spacing: -1px;
  line-height: 1.1;
  color: var(--ink);
  margin-bottom: 22px;
}

h2 {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 28px;
  letter-spacing: -0.5px;
  line-height: 1.2;
  color: var(--ink);
  margin-bottom: 16px;
}

h3 {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 20px;
  letter-spacing: -0.3px;
  line-height: 1.25;
  color: var(--ink);
  margin-bottom: 12px;
}

p {
  font-size: 17px;
  line-height: 1.75;
  color: var(--body);
  margin-bottom: 16px;
  max-width: var(--max-article);
}

/* Labels / category tags (uppercase) */
.label {
  font-family: var(--font-heading);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--blue-dark);
}

/* Meta / timestamps */
.meta {
  font-size: 13px;
  color: var(--muted);
}

/* Annotation (handwritten aside) */
.annotation {
  font-family: var(--font-hand);
  font-size: 18px;
  font-weight: 500;
  color: var(--muted);
}
```

---

## Wordmark

```css
.wordmark {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 22px;
  color: var(--ink);
  letter-spacing: -0.5px;
  line-height: 1;
  text-decoration: none;
}

.wordmark--on-dark {
  color: var(--white);
}
```

```html
<!-- Light background -->
<a href="/" class="wordmark">NicAlpi</a>

<!-- Dark background -->
<a href="/" class="wordmark wordmark--on-dark">NicAlpi</a>
```

---

## Navigation

```css
.nav {
  height: 64px;
  padding: 0 var(--sp-2xl);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--white);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav__links {
  display: flex;
  gap: 28px;
  list-style: none;
}

.nav__links a {
  font-size: 14px;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.15s;
}

.nav__links a:hover { color: var(--ink); }

.nav__cta {
  font-size: 13px;
  font-weight: 700;
  color: var(--white);
  background: var(--blue);
  padding: 8px 18px;
  border-radius: 7px;
  text-decoration: none;
}
```

---

## Buttons

```css
/* Shared button base */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-body);
  font-size: 15px;
  font-weight: 700;
  padding: 13px 24px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: opacity 0.15s;
}
.btn:hover { opacity: 0.9; }

/* Primary — ink on light bg */
.btn--primary { background: var(--ink); color: var(--white); }

/* Blue — use on BOTH light and dark backgrounds */
.btn--blue { background: var(--blue); color: var(--white); }

/* Ghost */
.btn--ghost {
  background: transparent;
  color: var(--ink);
  border: 2px solid var(--border);
}

/* Ghost on dark */
.btn--ghost-dark {
  background: rgba(255,255,255,0.08);
  color: rgba(255,255,255,0.65);
  border: none;
}
```

---

## Blockquotes

```css
/* Light blockquote */
.blockquote {
  padding: 24px 28px;
  border-left: 4px solid var(--blue);
  background: var(--blue-light);
  border-radius: 0 12px 12px 0;
  margin: 24px 0;
}

.blockquote p {
  font-weight: 700;
  font-size: 19px;
  color: var(--ink);
  line-height: 1.45;
  letter-spacing: -0.2px;
  max-width: none;
  margin-bottom: 10px;
}

.blockquote cite {
  font-family: var(--font-hand);
  font-size: 17px;
  color: var(--muted);
  font-style: normal;
}

/* Dark blockquote */
.blockquote--dark {
  padding: 32px;
  background: var(--ink);
  border-radius: 12px;
  position: relative;
  overflow: hidden;
  margin: 24px 0;
}

.blockquote--dark::before {
  content: '"';
  font-family: var(--font-heading);
  font-size: 120px;
  font-weight: 800;
  color: var(--blue);
  opacity: 0.15;
  position: absolute;
  top: -20px;
  left: 16px;
  line-height: 1;
  pointer-events: none;
}

.blockquote--dark p {
  font-weight: 700;
  font-size: 20px;
  color: var(--white);
  line-height: 1.45;
  max-width: none;
  margin-bottom: 14px;
  position: relative;
  z-index: 1;
  letter-spacing: -0.3px;
}

.blockquote--dark cite {
  font-family: var(--font-hand);
  font-size: 17px;
  color: rgba(255,255,255,0.65);
  font-style: normal;
  position: relative;
  z-index: 1;
}
```

---

## Post Cards

```css
.post-card {
  padding: 24px 28px;
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  transition: border-color 0.15s, box-shadow 0.15s;
  text-decoration: none;
}

.post-card:hover {
  border-color: var(--blue-mid);
  box-shadow: 0 4px 20px rgba(59, 130, 246, 0.08);
}

.post-card__tag {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--blue-dark);
  background: var(--blue-light);
  padding: 4px 10px;
  border-radius: 100px;
  margin-bottom: 12px;
  width: fit-content;
}

.post-card__title {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 18px;
  color: var(--ink);
  letter-spacing: -0.3px;
  line-height: 1.3;
  margin-bottom: 8px;
  flex: 1;
}

.post-card__excerpt {
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  margin-bottom: 16px;
}

.post-card__footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid var(--border);
  font-size: 12px;
  color: var(--muted);
}

.post-card__read-link {
  color: var(--blue-dark);
  font-weight: 700;
}
```

---

## Tags

```css
.tag {
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 100px;
  display: inline-block;
}

.tag--default {
  background: var(--off-white);
  color: var(--body);
  border: 1px solid var(--border);
}

.tag--blue {
  background: var(--blue-light);
  color: var(--blue-dark);
  border: 1px solid var(--blue-mid);
}

.tag--dark {
  background: var(--ink);
  color: var(--white);
}
```

---

## Inline Highlights

```css
/* Background highlight */
.highlight-bg {
  background: var(--blue-mid);
  padding: 2px 6px;
  border-radius: 4px;
}

/* Underline highlight */
.highlight-line {
  border-bottom: 3px solid var(--blue);
  padding-bottom: 2px;
  color: var(--blue-dark);
}
```

---

## Section Bands

```css
/* White section — default */
.section {
  padding: var(--sp-4xl) 0;
  background: var(--white);
}

/* Off-white band — use for about, featured, alternating sections */
.section--off-white {
  padding: var(--sp-3xl) 0;
  background: var(--off-white);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

/* Dark section — newsletter CTA, big quotes */
.section--dark {
  padding: var(--sp-4xl) 0;
  background: var(--ink);
}

/* Page wrapper */
.page-wrapper {
  max-width: var(--max-page);
  margin: 0 auto;
  padding: 0 var(--sp-2xl);
}
```

---

## Newsletter (dark full-width)

```css
.newsletter {
  background: var(--ink);
  padding: var(--sp-4xl) 0;
  border-top: 1px solid var(--border);
}

.newsletter__inner {
  max-width: var(--max-page);
  margin: 0 auto;
  padding: 0 var(--sp-2xl);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--sp-3xl);
  align-items: center;
}

.newsletter__pre {
  font-family: var(--font-hand);
  font-size: 20px;
  font-weight: 600;
  color: var(--blue);
  display: block;
  margin-bottom: 8px;
}

.newsletter__title {
  font-weight: 800;
  font-size: 28px;
  color: var(--white);
  letter-spacing: -0.8px;
  line-height: 1.15;
  margin-bottom: 10px;
}

.newsletter__body {
  font-size: 16px;
  color: var(--white);
  line-height: 1.65;
}

.newsletter__input {
  width: 100%;
  padding: 13px 18px;
  background: rgba(255, 255, 255, 0.07);
  border: 2px solid rgba(255, 255, 255, 0.15);
  color: var(--white);
  font-family: var(--font-body);
  font-size: 14px;
  border-radius: 8px;
  outline: none;
  margin-bottom: 10px;
  display: block;
}

.newsletter__input:focus { border-color: var(--blue); }
.newsletter__input::placeholder { color: rgba(255, 255, 255, 0.4); }

.newsletter__note {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
  margin-top: 8px;
}
```

---

## Accent Rule (decorative divider)

```css
.accent-rule {
  width: 40px;
  height: 3px;
  background: var(--blue);
  border-radius: 2px;
  margin: 20px 0 28px;
}
```

---

## Reading List (numbered posts)

```css
.reading-list { display: flex; flex-direction: column; }

.reading-list__item {
  display: grid;
  grid-template-columns: 60px 1fr auto;
  gap: 20px;
  align-items: start;
  padding: 24px 0;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
  text-decoration: none;
}

.reading-list__item:first-child { padding-top: 0; }

.reading-list__number {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 30px;
  color: var(--border);
  letter-spacing: -1.5px;
  line-height: 1;
  transition: color 0.15s;
}

.reading-list__item:hover .reading-list__number { color: var(--blue-mid); }

.reading-list__category {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--blue-dark);
  margin-bottom: 4px;
}

.reading-list__title {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 18px;
  color: var(--ink);
  letter-spacing: -0.3px;
  line-height: 1.3;
}

.reading-list__item:hover .reading-list__title { color: var(--blue-dark); }

.reading-list__excerpt {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.6;
  margin-top: 4px;
}

.reading-list__meta {
  font-size: 12px;
  color: var(--muted);
  text-align: right;
  white-space: nowrap;
}
```

---

## Footer

```css
.footer {
  padding: 32px var(--sp-2xl);
  border-top: 1px solid var(--border);
  background: var(--white);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer__links {
  display: flex;
  gap: 22px;
  list-style: none;
}

.footer__links a {
  font-size: 14px;
  color: var(--muted);
  text-decoration: none;
}

.footer__links a:hover { color: var(--ink); }

.footer__copy {
  font-size: 13px;
  color: var(--muted);
}
```
