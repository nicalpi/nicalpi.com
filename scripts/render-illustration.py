#!/usr/bin/env python3
"""Render one HTML file to a JPG/PNG at 2× — inline post illustrations and promo cards.

Same Playwright + system Chrome route as generate-og.py. Needs a Python with
playwright installed (on this machine: /opt/homebrew/bin/python3.13).

Usage:
    python3.13 scripts/render-illustration.py assets/images/<slug>/<name>.html
        → assets/images/<slug>/<name>.jpg at 1200×630
    python3.13 scripts/render-illustration.py <file.html> --size 1080x1080
    python3.13 scripts/render-illustration.py assets/social-templates/quote-square.html \
        --size 1080x1080 --theme dark --out assets/images/social/<slug>/quote-dark.png
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent


def parse(argv):
    src, size, theme, out = None, (1200, 630), None, None
    it = iter(argv)
    for a in it:
        if a == "--size":
            w, h = next(it).lower().split("x")
            size = (int(w), int(h))
        elif a == "--theme":
            theme = next(it)
        elif a == "--out":
            out = Path(next(it))
        elif a.startswith("--"):
            sys.exit(f"unknown flag {a}")
        else:
            src = Path(a)
    if not src or not src.exists():
        sys.exit(__doc__)
    if out is None:
        out = src.with_suffix(".jpg")
    return src.resolve(), size, theme, out


def main():
    src, (w, h), theme, out = parse(sys.argv[1:])
    out.parent.mkdir(parents=True, exist_ok=True)
    url = src.as_uri() + (f"?theme={theme}" if theme else "")
    fmt = "png" if out.suffix.lower() == ".png" else "jpeg"
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="chrome")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        page.goto(url, wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        kwargs = {"quality": 90} if fmt == "jpeg" else {}
        page.screenshot(path=str(out), type=fmt, clip={"x": 0, "y": 0, "width": w, "height": h}, **kwargs)
        browser.close()
    try:
        print(f"✓ {out.resolve().relative_to(ROOT)}")
    except ValueError:
        print(f"✓ {out}")


if __name__ == "__main__":
    main()
