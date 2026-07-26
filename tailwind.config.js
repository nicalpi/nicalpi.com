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
      // NicAlpi v3 "Field Notes" tokens.
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
        'on-accent': 'var(--on-accent)',
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      maxWidth: {
        frame: '1280px',
        article: '820px',
      },
      borderRadius: {
        brand: '4px',
        panel: '6px',
      },
    },
  },
  plugins: [],
}
