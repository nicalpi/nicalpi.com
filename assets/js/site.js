/* NicAlpi v3 — theme toggle + mobile contents drawer.
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

  // ⌥T (Alt+T) anywhere toggles the theme — advertised in the sidebar.
  document.addEventListener('keydown', function (e) {
    if (e.altKey && !e.ctrlKey && !e.metaKey && e.code === 'KeyT') {
      e.preventDefault();
      toggleTheme();
    }
  });

  // Sync labels/aria on load with the theme head.html already applied.
  applyTheme(currentTheme());

  /* ---------- mobile contents drawer ---------- */

  var drawer = document.querySelector('.sidebar');
  var lastFocused = null;

  function drawerIsOpen() {
    return document.body.classList.contains('drawer-open');
  }

  function openDrawer() {
    if (!drawer) return;
    lastFocused = document.activeElement;
    document.body.classList.add('drawer-open');
    document.querySelectorAll('[data-drawer-toggle]').forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'true');
    });
    var close = drawer.querySelector('.sidebar-close');
    if (close) close.focus();
  }

  function closeDrawer() {
    document.body.classList.remove('drawer-open');
    document.querySelectorAll('[data-drawer-toggle]').forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'false');
    });
    if (lastFocused && document.contains(lastFocused)) lastFocused.focus();
    lastFocused = null;
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-drawer-toggle]')) {
      drawerIsOpen() ? closeDrawer() : openDrawer();
      return;
    }
    if (e.target.closest('[data-drawer-close]')) {
      closeDrawer();
      return;
    }
    // Following a link inside the drawer should close it.
    if (drawerIsOpen() && e.target.closest('.sidebar a')) closeDrawer();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawerIsOpen()) closeDrawer();
  });

  // Leaving the mobile breakpoint clears the open state.
  window.matchMedia('(min-width: 901px)').addEventListener('change', function (ev) {
    if (ev.matches && drawerIsOpen()) closeDrawer();
  });
})();
