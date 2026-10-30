"""Builds site/index.html (the Vercel-ready page) from demo/index.html."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'demo' / 'index.html').read_text()
style = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
body = src[src.index('</style>') + len('</style>'):].strip()
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Saurasakti Stock Manager</title>
<meta name="description" content="Parts-level inventory for a solar dealer: system kits, orders with stock reservation, purchase list, live alerts and Tally export. Interactive demo with sample data.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#f5f5f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1e1e1e" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="Saurasakti Stock Manager">
<meta property="og:description" content="Interactive demo of the inventory system for Saurasakti Solar.">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
:root {{ color-scheme: light; }}
body {{ margin: 0; }}
[hidden] {{ display: none !important; }}
img {{ max-width: 100%; }}
{style}
</style>
</head>
<body>
<noscript>This demo needs JavaScript. Please enable it and reload.</noscript>
{body}
</body>
</html>
'''
(root / 'site').mkdir(exist_ok=True)
(root / 'site' / 'index.html').write_text(page)
print('site/index.html', len(page), 'bytes')
