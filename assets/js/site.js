/* NicAlpi v3 — theme toggle + newsletter form.
   The initial theme is applied by an inline script in head.html
   before first paint; this file only handles interaction. */
(function () {
  'use strict';

  var root = document.documentElement;

  /* ---------- theme ---------- */

  function currentTheme() {
    return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    try { localStorage.setItem('theme', theme); } catch (e) { /* private mode */ }

    document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
      btn.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
      var label = btn.querySelector('[data-theme-label]');
      if (label) label.textContent = theme;
    });

    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) {
      meta.setAttribute('content', getComputedStyle(root).getPropertyValue('--panel').trim());
    }
  }

  function toggleTheme() {
    applyTheme(currentTheme() === 'dark' ? 'light' : 'dark');
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-theme-toggle]')) toggleTheme();
  });

  // ⌥T (Alt+T) anywhere toggles the theme — advertised in the top bar tooltip.
  document.addEventListener('keydown', function (e) {
    if (e.altKey && !e.ctrlKey && !e.metaKey && e.code === 'KeyT') {
      e.preventDefault();
      toggleTheme();
    }
  });

  // Sync labels/aria on load with the theme head.html already applied.
  applyTheme(currentTheme());

  /* ---------- newsletter (Kit) ----------
     Intercepts the plain POST so the reader stays on the page and sees an
     inline confirmation. If fetch fails for any reason, falls back to the
     native submit, which lands on Kit's hosted confirmation page. */

  document.querySelectorAll('[data-newsletter-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var note = form.querySelector('[data-newsletter-note]');
      var button = form.querySelector('button[type="submit"]');
      var input = form.querySelector('input[type="email"]');
      button.disabled = true;
      button.textContent = 'subscribing…';

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      })
        .then(function (res) { return res.json(); })
        .then(function (data) {
          if (data && data.status === 'success') {
            input.disabled = true;
            button.textContent = 'subscribed ✓';
            if (note) note.textContent = 'Success — now check your email to confirm your subscription.';
          } else {
            var msg = data && data.errors && data.errors.messages && data.errors.messages.length
              ? data.errors.messages[data.errors.messages.length - 1]
              : 'That didn’t go through — please try again.';
            button.disabled = false;
            button.textContent = 'subscribe';
            if (note) note.textContent = msg;
          }
        })
        .catch(function () {
          // Network hiccup: fall back to the plain POST (Kit's hosted page).
          // form.submit() bypasses submit listeners, so this cannot loop.
          form.submit();
        });
    });
  });
})();
