module.exports = {
  content: [
    './_drafts/**/*.html',
    './_includes/**/*.html',
    './_layouts/**/*.html',
    './_posts/*.md',
    './*.md',
    './*.html',
  ],
  theme: {
    extend: {
      colors: {
        // NicAlpi brand palette
        'off-white': '#F5F4F1',
        ink: '#111111',
        muted: '#717171',
        border: '#E3E1DD',
        blue: {
          DEFAULT: '#3B82F6',
          dark: '#1A4FA8',
          light: '#EFF6FF',
          mid: '#BFDBFE',
        },
        // Semantic text aliases
        'text-heading': '#111111',
        'text-body': '#3A3A3A',
        'text-muted': '#717171',
        'text-annotation': '#1A4FA8',
      },
      fontFamily: {
        heading: ['DM Sans', 'system-ui', 'sans-serif'],
        body: ['DM Sans', 'system-ui', 'sans-serif'],
        annotation: ['Caveat', 'cursive'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      maxWidth: {
        article: '640px',
      },
      borderRadius: {
        'xl': '16px',
        'lg': '12px',
        'md': '8px',
      }
    }
  },
  plugins: [
    require('@tailwindcss/typography')
  ]
}
