# NicAlpi v4 Components — Reference

Every reusable piece of the site, with its class or include and a usage
snippet. All of them render live at `/styleguide/`. CSS lives in
`_assets/main.css` (compile with `yarn css`); Liquid components live in
`_includes/` and `_includes/fn/`. Visual spec for each: `DESIGN.md`.

Everything is token-driven — components work in light and dark with no
variants.

---

## Frame

`_layouts/default.html` wraps every page: `nav-top.html` → `<main
class="sheet">` (1024px, 880px inner) → `footer.html`. Pages only provide
what goes inside the sheet. Sections inside the sheet are
`<section class="sheet-section">` (40px padding, hairline above, first one
flush).

```liquid
{% include nav-top.html %}
<main id="main-content" class="sheet">{{ content }}</main>
{% include footer.html %}
```

### Top bar — `nav-top.html`
Borderless, sticky, 64px (56px on phones). Wordmark `nicalpi` + `.topbar-ext`
`.md`; `.topbar-nav` holds three nav chips (fog on hover / `aria-current`)
and the `theme-pill`. Four items fit a phone width, so there is no drawer.

### Footer — `footer.html`
One line above a hairline: © left, `writing · about · linkedin · twitter/x ·
rss` right, `.eof` last.

---

## Primitives

### Links
Inline text links are `--accent` with a hairline underline in
`--accent-line` at rest, full accent on hover. `.no-underline` opts out.
Block links (`.link-block` + `.link-title`) are used by directory rows; in
v4 the row title simply turns `--accent` on hover (the arrow is suppressed
inside `.dir-row`).

### Buttons
```html
<a class="btn" href="…">Start reading →</a>             <!-- ink pill, 40px -->
<a class="btn btn-ghost" href="…">Get new posts by email</a>  <!-- transparent, fog on hover -->
<a class="btn btn-outline" href="…">Start reading</a>   <!-- hairline edge -->
<a class="btn btn-sm" href="…">subscribe</a>             <!-- 34px -->
```

### Chips (filters) and tags
```html
<button class="chip chip-solid" aria-pressed="true">all</button>  <!-- ink fill -->
<button class="chip">ai</button>                                  <!-- 30px, hairline -->
```
`.chip-row` lays them out (used on `/blog/` with the topic filter script).

### Kickers
```html
<span class="kicker">worked with</span>
<span class="kicker kicker-accent">running · since Aug</span>
```

### Markdown marks
Headings in layouts carry an explicit mark; `.prose` h2–h4 get theirs from
CSS `::before`. Both use `--mark`.
```html
<h1 class="page-title"><span class="md-mark"># </span>Writing</h1>
<h2 class="section-title"><span class="md-mark">## </span>Writing</h2>
```

### Section head
```html
<div class="section-head">
  <h2 class="section-title"><span class="md-mark">## </span>Writing</h2>
  <span class="section-cmd">ls -t _posts/ · {{ site.posts.size }} files</span>
</div>
```

### Theme toggle
`theme-pill` in the top bar; needs `data-theme-toggle`, a child
`[data-theme-label]` gets "light"/"dark". ⌥T also toggles.

---

## Devices

### Front-matter block — `.fm`
```html
<div class="fm" aria-label="…">
  <span class="fm-fence">---</span>
  <span><span class="fm-k">name:</span> <span class="fm-v">Nic Alpi</span></span>
  <span><span class="fm-k">contact:</span> <a href="mailto:…" class="fm-v fm-accent no-underline">hi@nicalpi.com</a></span>
  <span class="fm-fence">---</span>
</div>
```
`.fm-post` is the post variant: unfilled, 13px, 28px below, metadata only
(category, date, reading_time) under a `.post-path` line. `_layouts/post.html`
then renders the title once as `h1.article-title` and the `subtitle` as
`p.article-dek` (serif 20px `--muted`). Don't add title/subtitle back into
the block. The whole post header holds the centred `--measure` column.

On the home page the `.fm` follows the headline, lead and `.hero-actions`
inside `.hero-text`; the claim is read before the bio.

### Worked with — logo strip
```html
<section class="sheet-section worked-with" aria-label="Companies I've worked with">
  <span class="kicker">worked with</span>
  <div class="logo-row">
    <img src="…" alt="…" class="logo-img logo-wide">   <!-- 9:1 wordmark, 17px -->
    <img src="…" alt="…" class="logo-img logo-mid">    <!-- ~4:1, 24px -->
    <img src="…" alt="…" class="logo-img logo-block">  <!-- stacked ~4:3, 32px -->
  </div>
</section>
```
Sits directly after the hero (`.hero + .worked-with` drops the divider).
Pick the height class by the logo's shape so they read at equal weight;
grayscale (and inverted in dark) comes from the "Client logos" CSS.

### Directory listing — `post-row.html` + `dir-head.html`
```liquid
<div class="dir-list">
  {% include dir-head.html %}
  {% for post in site.posts %}{% include post-row.html post=post %}{% endfor %}
</div>
```
One row = `a.dir-row.link-block` with `.dir-date`, `.dir-cat` (plain
`--accent` word), `.dir-title.link-title` (Source Serif 600 17.5px — the
only serif in the row), `.dir-read`. Stacks on phones.

### Beliefs
```html
<section class="sheet-section beliefs-section">
  <div class="beliefs-intro">…section-title + section-lead…</div>
  <ul class="beliefs"><li><strong>Claim.</strong> Support.</li>…</ul>
</section>
```
Two columns above 800px, with the intro sticky under the top bar; each
item gets a `- [x]` mark from CSS.

### Newsletter — `newsletter.html`
```liquid
{% include newsletter.html %}
{% include newsletter.html title="…" text="…" kicker="…" id="newsletter" %}
```
Fog card, 20px, `> kicker`, pill input (`.news-input`) + `.btn`. Wired to
Kit form 5638226 (plain POST of `email_address`, works without JS);
`site.js` intercepts `[data-newsletter-form]` for the inline success note.

### Cross-link card — `fn/xcard.html`
```liquid
{% include fn/xcard.html url="…" kicker="← previous · leadership" title="…" %}
{% include fn/xcard.html url="…" kicker="field note · exp-01" title="…" accent=true %}
```
Post prev/next uses it inside `nav.article-next`.

### Page head (writing, about, contact, 404)
```html
<div class="page-head">
  <h1 class="page-title"><span class="md-mark"># </span>Writing</h1>
  <p class="page-lead">…</p>
  <div class="chip-row">…chips…</div>
</div>
```

### Contact
`.offer-grid` of `.offer` cards (12px) and the `.email-band` (accent-soft,
16px, no border).

---

## Prose

`.prose` styles rendered markdown: mono 600 headings with `##`/`###` marks
in `--mark` (h2 keeps a hairline below), italic blockquotes with a hanging
`>`, fog inline code (6px) and `pre` (12px), images with a hairline and 12px
corners, GFM task lists rendered as `- [ ]`/`- [x]` text marks, hairline
tables. `.lead` for an opening paragraph.

## Field-note components (`_includes/fn/`) — paused

Usable inside markdown bodies; data lives in front matter (schema in
`_field_notes/README.md`). `fn/meta-block.html` (hairline rules),
`fn/metrics.html` (before / now / target; stacks under 640px),
`fn/checklist.html` (`- [ ]`/`- [x]`), `fn/field-log.html`,
`fn/exp-card.html` (12px card, fog hover), `fn/follow-cta.html`,
`.queued-box` (dashed, 12px), `.progress-track/.progress-fill`. All token
driven; nothing to restyle when the lab returns.

## Lightbox

`lightbox.html` + images inside post bodies. Backdrop is theme-independent
black.

## Retired

`_retired/` holds `sidebar.html`, `mobile-bar.html`, `field-notes.html`
(v2/v3 shells). Not processed by Jekyll.
