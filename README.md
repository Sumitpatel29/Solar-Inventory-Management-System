# Solar Inventory Management System

Parts-level inventory for a solar panel dealer (Saurasakti). A solar system is built from many parts (panels, inverter, structure, cable, protection gear) that change for each customer, which is hard to track in Tally. This project is an interactive demo of the system, with sample data.

**What the demo does:** system kits and "what can I build right now", orders that reserve stock, dispatch, return leftover and install, a purchase list worked out automatically, stock search with brand, category and availability filters, charts and insights, live notifications, CSV export for Tally, and printable quotations. It uses a macOS-style interface with light and dark mode and works on phones.

## Contents
| Path | What it is |
|---|---|
| `site/` | The website to deploy (one static page, no build step) |
| `demo/index.html` | Editable source of the page |
| `demo/standalone.html` | Same page as a single file you can open by double-click |
| `build_site.py` | Rebuilds `site/index.html` from `demo/index.html` |
| `PLAN.md` | Problem, approach, phased plan for the real system, questions for the owner |

## Deploy on Vercel
1. Import this repository at vercel.com.
2. Set **Root Directory** to `site`, **Framework Preset** to **Other**, and leave the build command and output directory empty.
3. Deploy.

Or from a terminal: `cd site && npx vercel --prod`.

## Run locally
Open `demo/standalone.html` in a browser, or run `python3 -m http.server --directory site 8000` and visit http://localhost:8000.

## Editing
Edit `demo/index.html`, then run `python3 build_site.py` to refresh `site/index.html`.

## Notes
- Data lives in each visitor's browser (localStorage). "Reset sample data" restores the originals.
- Sample numbers, the trend history and the "live activity from other staff" are made up for the demo.
