# NicAlpi Social Cards — HTML Templates

Three card styles. All use plain wordmark (no coloured letters). Export at 2× scale for retina.

---

## Export Command

```bash
python3 scripts/export_image.py input.html output.jpg --width 1200 --height 630 --scale 2 --quality 95
```

For square (Instagram): `--width 1080 --height 1080`

---

## Style 1: Dark

Use for: bold takes, hot opinions, contrarian content.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700;800&family=Caveat:wght@600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px; height: 630px; overflow: hidden;
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #111111;
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 52px 60px;
    -webkit-font-smoothing: antialiased;
  }
  .top { display: flex; justify-content: space-between; align-items: center; }
  .wordmark { font-weight: 800; font-size: 18px; color: rgba(255,255,255,0.4); letter-spacing: -0.5px; }
  .domain { font-size: 12px; color: rgba(255,255,255,0.2); letter-spacing: 1px; text-transform: uppercase; }
  .title {
    font-weight: 800;
    font-size: 52px;
    color: #ffffff;
    line-height: 1.1;
    letter-spacing: -1.5px;
    max-width: 900px;
  }
  .title .accent { color: #3B82F6; }
  .bottom { display: flex; justify-content: space-between; align-items: flex-end; }
  .category { font-size: 12px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.35); }
  .read-time { font-size: 12px; color: rgba(255,255,255,0.25); }
</style>
</head>
<body>
  <div class="top">
    <div class="wordmark">NicAlpi</div>
    <div class="domain">nicalpi.com</div>
  </div>
  <div class="title">Why <span class="accent">navy seal advice</span><br>is useless for normal people</div>
  <div class="bottom">
    <div class="category">Team Management</div>
    <div class="read-time">6 min read</div>
  </div>
</body>
</html>
```

---

## Style 2: Light

Use for: how-to content, practical guides, explainers.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700;800&family=Caveat:wght@600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px; height: 630px; overflow: hidden;
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #FFFFFF;
    border-top: 8px solid #3B82F6;
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 52px 60px;
    -webkit-font-smoothing: antialiased;
  }
  .top { display: flex; justify-content: space-between; align-items: center; }
  .wordmark { font-weight: 800; font-size: 18px; color: #111111; letter-spacing: -0.5px; }
  .domain { font-size: 12px; color: #717171; letter-spacing: 1px; text-transform: uppercase; }
  .pre { font-family: 'Caveat', cursive; font-size: 22px; font-weight: 600; color: #1A4FA8; margin-bottom: 12px; }
  .title {
    font-weight: 800;
    font-size: 48px;
    color: #111111;
    line-height: 1.1;
    letter-spacing: -1.5px;
    max-width: 900px;
  }
  .bottom { display: flex; justify-content: space-between; align-items: flex-end; }
  .category {
    font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
    color: #1A4FA8; background: #EFF6FF; padding: 6px 14px; border-radius: 100px;
  }
  .read-time { font-size: 13px; color: #717171; }
</style>
</head>
<body>
  <div class="top">
    <div class="wordmark">NicAlpi</div>
    <div class="domain">nicalpi.com</div>
  </div>
  <div>
    <div class="pre">Practical guide</div>
    <div class="title">How to have a performance conversation<br>without it becoming a war</div>
  </div>
  <div class="bottom">
    <div class="category">Team Management</div>
    <div class="read-time">8 min read · Feb 24, 2026</div>
  </div>
</body>
</html>
```

---

## Style 3: Blue (Statement)

Use for: manifestos, personal takes, quote-style content.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700;800&family=Caveat:wght@600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px; height: 630px; overflow: hidden;
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #3B82F6;
    display: flex; flex-direction: column;
    justify-content: space-between;
    padding: 52px 60px;
    -webkit-font-smoothing: antialiased;
  }
  .wordmark { font-weight: 800; font-size: 18px; color: rgba(255,255,255,0.55); letter-spacing: -0.5px; }
  .statement {
    font-weight: 800;
    font-size: 64px;
    color: #ffffff;
    line-height: 1.05;
    letter-spacing: -2px;
    max-width: 900px;
  }
  .attribution {
    font-family: 'Caveat', cursive;
    font-size: 22px;
    font-weight: 600;
    color: rgba(255,255,255,0.65);
  }
</style>
</head>
<body>
  <div class="wordmark">NicAlpi</div>
  <div class="statement">Perfectionism isn't a<br>personality trait.<br>It's a fear habit.</div>
  <div class="attribution">Nic Alpi · nicalpi.com</div>
</body>
</html>
```

---

## Instagram Square (1080×1080)

Adjust font sizes: title ~44px, everything else proportionally. Use the same three styles but change body dimensions to `width: 1080px; height: 1080px`.
