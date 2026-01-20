# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- `bundle install` - Install Ruby dependencies
- `bundle exec jekyll serve` - Start local development server with auto-regeneration (http://localhost:4000)
- `bundle exec jekyll build` - Build static site to `_site/` directory

## Project Structure

This is a Jekyll 4.4 static site using the Minima theme.

- `_posts/` - Blog posts in Markdown (format: `YYYY-MM-DD-title.markdown`)
- `_config.yml` - Site configuration (requires server restart when changed)
- `index.markdown` - Homepage
- `about.markdown` - About page
- `_site/` - Generated output (gitignored)

## Content Guidelines

### Creating Posts

Posts must follow the naming convention `YYYY-MM-DD-title.markdown` and include front matter:

```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: category1 category2
---
```

### Customizing Theme

Override Minima theme defaults by creating matching files in the project root. See https://jekyllrb.com/docs/themes/#overriding-theme-defaults

## Skills

### `/calm-cto-brand`

Complete design system for "The Calm CTO" brand. Use for any visual content or web pages.

**Capabilities:**
- WCAG AA accessible colour palette (Sage `#5F8A5A`, Coral `#C4716A`, Sky `#4A8FA0`)
- DM Sans typography with Caveat for annotations, JetBrains Mono for code
- Tailwind CSS configuration for web development
- CSS design tokens (`assets/design-tokens.css`)
- Visual templates for image generation (`references/visual-templates.md`)
- Web component patterns (`references/web-components.md`)
- HTML to JPEG/PNG export script (`scripts/export_image.py`)

**Visual Templates:** Process Flow, Quote Card, Concept Grid, Comparison, Stats Card, Timeline, List Card, Social Post, Bold Statement

**Export Images:**
```bash
python3 .claude/skills/calm-cto-brand/scripts/export_image.py input.html output.jpg
```
