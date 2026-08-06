# NicAlpi v3 Components — Reference

Every reusable piece of the site, with its class or include and a usage
snippet. All of them render live at `/styleguide/`. CSS lives in
`_assets/main.css` (compile with `yarn css`); Liquid components live in
`_includes/` and `_includes/fn/`.

Everything is token-driven — components work in light and dark with no
variants.

---

## Layout shells

### Site frame
Applied by `_layouts/default.html`. 1280px `--panel` sheet on the `--canvas`
surround, side borders above 1280px.

```html
<div class="site-frame">…</div>
```

### Sidebar page
The inner-page shell: 248px sidebar + main column. Below 900px the sidebar
becomes the contents drawer automatically.

```liquid
<div class="with-sidebar" id="main-content">
  {% include sidebar.html context="post" %}
  <div class="flex flex-col min-w-0">
    {% include mobile-bar.html back_url="/blog/" back_label="writing" %}
    <div class="crumbs hidden md:flex">…</div>
    <article class="px-5 md:px-10 … max-w-article">…</article>
    <div class="mt-auto">{% include footer.html %}</div>
  </div>
</div>
```

`sidebar.html` contexts: `notes` (field-notes index), `note` (brief/progress),
`post`, `writing`, `about`, `drawer` (full-width pages: drawer only). Pass
`body=content` from `note` and `post` layouts — that powers the "on this
page" heading list (split on rendered `<h2>`s). The include resolves
experiments and progress notes from the `field_notes` collection by itself.

Section order inside the sidebar is fixed: context nav ("on this page",
experiment tree) → field notes → **writing, pinned to the bottom with
`mt-auto`** → meta links (about / work with me / rss) → theme toggle.

### Top nav (full-width pages)
```liquid
{% include nav-top.html %}
{% include sidebar.html context="drawer" %}   <!-- powers the mobile drawer -->
```

### Mobile bar
Sticky header on inner pages. `{% include mobile-bar.html back_url="/" back_label="home" label="field notes" %}`

### Breadcrumbs
```html
<div class="crumbs hidden md:flex">
  <span><a href="/">home</a> / <a href="/field-notes/">field notes</a> / exp-01</span>
  <span class="text-accent">● running · since Aug</span>
</div>
```

---

## Primitives

### Links (Aug 2026)
Inline text links are accent-coloured with a **hairline underline in
`--accent-line` at rest** (the pre-hover "this is a link" cue), strengthening
to `--accent` on hover. `.no-underline` opts out at rest; buttons, chips,
sidebar links and cards are excluded from the hover underline in CSS.

Row/card links use the **block-link pattern** — only the title responds; an
accent `→` after the title fades and bounces in on hover (space reserved, no
reflow; disabled under reduced motion):
```html
<a href="…" class="link-block no-underline text-ink …">
  <span class="link-title …">Post or experiment title</span>
  <span class="…">description, meta — never underlined</span>
</a>
```
`.link-title` also works inside `.fn-card`; `.xcard` titles underline on
hover without the arrow (their kickers already carry arrows).

### Buttons
```html
<a class="btn" href="…">Get the next field note →</a>
<a class="btn btn-ghost" href="…">Start reading</a>
<a class="btn btn-sm" href="…">subscribe</a>
```

### Chips / status pills
```html
<span class="chip chip-solid">running</span>
<span class="chip">closed</span>
```

### Kickers
```html
<span class="kicker">what I've learned</span>
<span class="kicker kicker-accent">field notes — the public cto lab</span>
```

### Markdown marks
Headings in layouts carry an explicit faint mark; `.prose` h2/h3 get theirs
from CSS `::before`.
```html
<h1><span class="md-mark"># </span>Page title</h1>
<h2><span class="on-accent-mark">## </span>On accent-soft surfaces</h2>
```

### Status dots
`<span class="dot-running">●</span>` / `<span class="dot-closed">○</span>`

### Theme controls
`theme-pill` (nav), `theme-row` (sidebar), `icon-btn` (mobile). All need
`data-theme-toggle`; a child `[data-theme-label]` gets "light"/"dark".

### Progress bar
```html
<div class="progress-track" role="progressbar" aria-valuenow="23" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-fill" style="width:23%;"></div>
</div>
```

---

## Field-note components (`_includes/fn/`)

Usable inside markdown bodies — Jekyll renders Liquid before kramdown.
Data lives in front matter; see `_field_notes/README.md` for the schema.

### Meta block — `fn/meta-block.html`
The "front matter strip" between ink rules. Layouts build it automatically
for briefs and progress notes; use the include for custom rows.
```liquid
{% include fn/meta-block.html rows=page.meta_rows %}
<!-- row: { label, value, status: true → accent } -->
```

### Metrics table — `fn/metrics.html`
before / now / target. Stacks into `before → now` rows under 640px.
```liquid
{% include fn/metrics.html rows=page.metrics caption="Small sample." %}
<!-- row: { label, before, now, target, home: true, home_label } -->
```
Rows flagged `home: true` also feed the flagship card on the homepage.

### Checklist — `fn/checklist.html`
```liquid
{% include fn/checklist.html items=page.guardrails %}
<!-- item: { text, done: bool, note: "muted suffix" } -->
```

### Field log — `fn/field-log.html`
```liquid
{% include fn/field-log.html entries=page.field_log %}
<!-- entry: { date, strong: "lead sentence", text, planned: bool } -->
```

### Experiment card — `fn/exp-card.html`
Index card with status strip, title, summary, progress bar and facts column.
```liquid
{% include fn/exp-card.html e=experiment_doc %}
```

### Cross-link card — `fn/xcard.html`
Prev/next and field-note cross-promotion.
```liquid
{% include fn/xcard.html url="…" kicker="← previous · leadership" title="…" %}
{% include fn/xcard.html url="…" kicker="field note · exp-01" title="…" accent=true %}
```

### Follow CTA — `fn/follow-cta.html`
```liquid
{% include fn/follow-cta.html text="…" button="follow this experiment →" %}
```

### Queued box
Renders queued experiments from `_data/field_notes.yml`; guard it so it
disappears when the queue is empty.
```liquid
{% if site.data.field_notes.queued.size > 0 %}
<div class="queued-box">
  <span class="kicker">queued</span>
  <div class="checklist">
    {% for q in site.data.field_notes.queued %}<span class="check">{{ q.id }} — {{ q.text }}</span>{% endfor %}
  </div>
</div>
{% endif %}
```

---

## Bands & sections

### Newsletter — `newsletter.html`
```liquid
{% include newsletter.html %}
{% include newsletter.html title="…" text="…" kicker="…" id="newsletter" %}
```
Wired to Kit form 5638226 (plain POST of `email_address`, works without
JS). `site.js` intercepts `[data-newsletter-form]` for an inline success
message ("subscribed ✓" + check-your-email note in `[data-newsletter-note]`,
`aria-live`); on network failure it falls back to the plain POST and Kit's
hosted confirmation page.

### Footer — `footer.html`
Slim © + links row; used at the bottom of every main column.

### Accent band
The "lab" treatment: `bg-accent-soft border-t border-b border-accent-line`,
cells separated with `gap-px bg-accent-line` grids.

### Raise band
Quieter alternate band: `bg-raise border-t border-line` (beliefs, logos).

---

## Prose

`.prose` styles rendered markdown: faint `##` marks on h2–h4, accent
blockquotes, `--raise` code blocks, bordered images with `figcaption`,
GFM task lists rendered as `- [ ]` text marks, tables in the metrics style.
`.lead` for the opening paragraph.

## Lightbox

`lightbox.html` + images inside post bodies. Unchanged behaviour; backdrop is
theme-independent black.
