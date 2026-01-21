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
        sage: {
          DEFAULT: '#8FAE8B',
          text: '#4E7A4A',
          dark: '#3D6339',
          light: '#D4E4D2'
        },
        coral: {
          DEFAULT: '#E8998D',
          text: '#A8584F',
          dark: '#8B4840',
          light: '#F4DCD8'
        },
        sky: {
          DEFAULT: '#89B9C4',
          text: '#357A8A',
          dark: '#28606E',
          light: '#D0E5EA'
        },
        cream: '#F8F6F3',
        'off-white': '#FDFCFB',
        charcoal: '#2D3436',
        sand: '#D4C5B5',
        border: '#E5E7EB',
        'text-heading': '#2D3436',
        'text-body': '#4B5563',
        'text-muted': '#5C6370',
        'text-annotation': '#4F5662',
        focus: '#2563EB',
      },
      fontFamily: {
        heading: ['DM Sans', 'system-ui', 'sans-serif'],
        body: ['DM Sans', 'system-ui', 'sans-serif'],
        annotation: ['Caveat', 'cursive'],
        mono: ['JetBrains Mono', 'monospace'],
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
