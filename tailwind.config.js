module.exports = {
  content: [
    './_drafts/**/*.html',
    './_includes/**/*.html',
    './_layouts/**/*.html',
    './_field_notes/**/*.md',
    './_posts/*.md',
    './*.md',
    './*.html',
    './assets/js/*.js',
  ],
  theme: {
    extend: {
      // NicAlpi v4 "Graphite notebook" tokens (Sep 2026).
      // Values live as CSS variables in assets/main.css (:root = light,
      // [data-theme="dark"] = dark) so every utility is theme-aware.
      colors: {
        canvas: 'var(--canvas)',
        panel: 'var(--panel)',
        side: 'var(--side)',
        raise: 'var(--raise)',
        ink: 'var(--ink)',
        body: 'var(--body)',
        muted: 'var(--muted)',
        faint: 'var(--faint)',
        line: {
          DEFAULT: 'var(--line)',
          2: 'var(--line2)',
        },
        accent: {
          DEFAULT: 'var(--accent)',
          soft: 'var(--accent-soft)',
          line: 'var(--accent-line)',
        },
        mark: 'var(--mark)',
        'on-accent': 'var(--on-accent)',
        'on-ink': 'var(--on-ink)',
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
        serif: ['Source Serif 4', 'Georgia', 'Times New Roman', 'serif'],
      },
      maxWidth: {
        sheet: '760px',
        article: '820px',
      },
      borderRadius: {
        brand: '12px',   // v4 Graphite notebook: content cards and images
        panel: '16px',
      },
    },
  },
  plugins: [],
}
