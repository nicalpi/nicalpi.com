# .promo-memory

Working state for the social promotion workflow (`/promo-plan` → `/promo-draft`
→ `/promo-asset` → `/promo-status`). Committed on purpose, same as
`.writings-memory/`.

```
memory.md           social voice + what works, read by promo-drafter
research/           platform research (LinkedIn formats, Twitter specs, strategy)
<slug>/
  plan.md           /promo-plan — calendar with angles and briefs (status: plan)
  drafts/           /promo-draft — one file per social piece
    day-00-li.md
    day-00-tw.md
    day-01-tw-thread.md
    day-02-li-carousel.md
    …
  assets/           /promo-asset — quote cards, carousels, insight images
    quote-day04.html
    quote-day04-square.png
    carousel-day02.html
    carousel-day02.pdf
    …
```

`/promo-status` shows the calendar as a checklist. Nic marks pieces as posted;
when every piece is posted, `status: done`. The `<slug>/` folder stays until
Nic cleans it up (unlike `.writings-memory/<slug>/` which is deleted on
publish).

Front-matter on `plan.md`:

```yaml
---
slug: <slug>
post: _posts/<date>-<slug>.md
status: plan | drafting | approved | done
created: YYYY-MM-DD
---
```
