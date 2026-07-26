#!/usr/bin/env python3
"""Generate the site's OG/social images from the v3 templates.

Reads front matter from _posts/ and _field_notes/, fills the generator
templates in assets/social-templates/ (og-post.html, og-page.html,
og-field-note.html) and screenshots them at 1200×630 (2× scale) into
assets/images/og/<slug>.jpg.

Setup (once):
    pip3 install playwright        # or: brew install playwright
    # uses your installed Google Chrome; falls back to Playwright chromium

Usage:
    python3 scripts/generate-og.py            # everything
    python3 scripts/generate-og.py intention exp-01   # only these slugs
"""

import html
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "assets" / "social-templates"
OUT = ROOT / "assets" / "images" / "og"
WIDTH, HEIGHT, SCALE, JPEG_QUALITY = 1200, 630, 2, 88

# ---------------------------------------------------------------- front matter

def parse_front_matter(path):
    """Minimal YAML-subset parser: scalars, lists of scalars, lists of dicts.
    Covers everything the posts and field notes use."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    data, current_list, current_item, list_indent = {}, None, None, 0

    def unquote(v):
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        return v

    for raw in m.group(1).split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()

        if indent == 0 and re.match(r"^[\w-]+:", line):
            key, _, rest = line.partition(":")
            rest = rest.strip()
            if rest:
                data[key] = unquote(rest)
                current_list = None
            else:
                data[key] = []
                current_list, current_item = data[key], None
        elif current_list is not None and line.startswith("- "):
            entry = line[2:].strip()
            list_indent = indent
            if re.match(r"^[\w-]+:", entry):  # list of dicts
                k, _, v = entry.partition(":")
                current_item = {k.strip(): unquote(v)}
                current_list.append(current_item)
            else:
                current_item = None
                current_list.append(unquote(entry))
        elif current_list is not None and current_item is not None and indent > list_indent:
            k, _, v = line.partition(":")
            current_item[k.strip()] = unquote(v)
    return data


def esc(value):
    return html.escape(str(value), quote=False)

# ------------------------------------------------------------------- templates

def fill(template_name, slots):
    src = (TEMPLATES / template_name).read_text(encoding="utf-8")
    for key, value in slots.items():
        src = src.replace("{{%s}}" % key, value)
    return src


def stat_pair(label, before, now):
    return (
        '<div style="display:flex; flex-direction:column; gap:4px;">'
        f'<span style="font-size:15px; color:var(--muted);">{esc(label)}</span>'
        '<span style="font-size:32px; font-weight:700; letter-spacing:-0.02em;">'
        f'{esc(before)} <span class="faint">→</span> <span class="accent">{esc(now)}</span></span></div>'
    )


def stat_plain(label, value, accent=False):
    colour = "var(--accent)" if accent else "var(--ink)"
    return (
        '<div style="display:flex; flex-direction:column; gap:4px;">'
        f'<span style="font-size:15px; color:var(--muted);">{esc(label)}</span>'
        f'<span style="font-size:30px; font-weight:700; letter-spacing:-0.02em; color:{colour};">{esc(value)}</span></div>'
    )

# ------------------------------------------------------------------------ jobs

def post_jobs():
    for path in sorted(ROOT.glob("_posts/*.md")):
        fm = parse_front_matter(path)
        og = fm.get("og_image", "")
        slug = Path(og).stem if og else path.stem[11:]
        yield slug, fill("og-post.html", {
            "CATEGORY": esc(fm.get("category", "writing")).lower(),
            "READING": esc(fm.get("reading_time", "5")),
            "TITLE": esc(fm["title"]),
            "DEK": esc(fm.get("subtitle") or fm.get("description", "")),
        })


def field_note_jobs():
    # experiment briefs
    for path in sorted(ROOT.glob("_field_notes/exp-*.md")):
        fm = parse_front_matter(path)
        home_metrics = [m for m in fm.get("metrics", []) if isinstance(m, dict) and m.get("home") == "true"]
        if home_metrics:
            stats = "".join(stat_pair(m.get("home_label", m["label"]), m["before"], m["now"]) for m in home_metrics[:3])
        else:
            stats = "".join(stat_plain(f.get("label", ""), f.get("value", ""), f.get("accent") == "true")
                            for f in fm.get("facts", [])[:3])
        verdict = fm.get("verdict")
        foot = f"Verdict: {verdict}." if verdict else f"Next: {fm.get('next_label', 'in the newsletter first')}."
        yield fm["exp_id"], fill("og-field-note.html", {
            "STRIP_LEFT": esc(f"field note · {fm['exp_id']} · {fm.get('theme_tag', '')}"),
            "STRIP_RIGHT": esc(fm.get("status_label", fm.get("status", ""))),
            "TITLE": esc(fm["title"]),
            "DEK": esc(fm.get("summary") or fm.get("lead", "")),
            "STATS_LABEL": "the verdict" if verdict else "so far",
            "STATS": stats,
            "FOOT_NOTE": esc(foot),
        })

    # progress notes
    for path in sorted(ROOT.glob("_field_notes/*/*.md")):
        fm = parse_front_matter(path)
        if fm.get("kind") != "progress":
            continue
        slug = Path(fm.get("permalink", path.stem).rstrip("/")).name
        metrics = [m for m in fm.get("metrics", []) if isinstance(m, dict)]
        stats = "".join(stat_pair(m["label"], m["before"], m["now"]) for m in metrics[:3])
        yield slug, fill("og-field-note.html", {
            "STRIP_LEFT": esc(f"progress note · {fm.get('experiment', '')}"),
            "STRIP_RIGHT": esc(fm.get("status_label", "")),
            "TITLE": esc(fm["title"]),
            "DEK": esc(fm.get("lead", "")),
            "STATS_LABEL": "so far",
            "STATS": stats,
            "FOOT_NOTE": esc(f"Next: {fm.get('next_label', '—')}."),
        })


PAGES = [
    ("homepage", "field notes from a working cto", "AI made output cheap. Good judgement is now the advantage.",
     "Practical experiments on AI, attention, management and delivery — published with what worked, what failed, and what changes next.", "cto · bristol"),
    ("blog", "writing", "What the job actually looks like.",
     "Team management, agency life, AI honestly, and the reality of doing this without performing about it.", "writing"),
    ("about", "about", "A bit more about me…",
     "French developer in Bristol. Built and sold a Rails consultancy, now CTO at Amba. HYROX at 5:30am, hard 4pm stop.", "about"),
    ("contact", "work with me", "Let's talk.",
     "Fractional CTO and advisory support — a second brain on engineering leadership and AI adoption.", "work with me"),
    ("field-notes", "field notes — the public cto lab", "Change one thing. Measure it. Publish the result.",
     "Experiments with a baseline, a protocol, guardrails, and a verdict published either way — including the failures.", "field notes"),
]


def page_jobs():
    for slug, kicker, title, dek, top_right in PAGES:
        yield slug, fill("og-page.html", {
            "KICKER": esc(kicker),
            "TITLE": esc(title),
            "DEK": esc(dek),
            "TOP_RIGHT": esc(top_right),
        })

# ------------------------------------------------------------------------ main

def main():
    only = set(sys.argv[1:])
    jobs = [(slug, html_src) for gen in (post_jobs, field_note_jobs, page_jobs)
            for slug, html_src in gen() if not only or slug in only]
    if not jobs:
        sys.exit(f"No jobs matched {sorted(only)}")

    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="chrome")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=SCALE)
        for slug, html_src in jobs:
            tmp = TEMPLATES / f".tmp-{slug}.html"
            tmp.write_text(html_src, encoding="utf-8")
            try:
                page.goto(tmp.as_uri(), wait_until="networkidle")
                page.evaluate("() => document.fonts.ready")
                out = OUT / f"{slug}.jpg"
                page.screenshot(path=str(out), type="jpeg", quality=JPEG_QUALITY,
                                clip={"x": 0, "y": 0, "width": WIDTH, "height": HEIGHT})
                print(f"✓ {out.relative_to(ROOT)}")
            finally:
                tmp.unlink(missing_ok=True)
        browser.close()


if __name__ == "__main__":
    main()
