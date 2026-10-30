# Saurasakti Inventory Management: Plan

Status: **Demo stage** (2026-10-30). The demo is for the owner to try. If the owner approves, we build the real system in the phases below.

## 1. The problem

A solar dealer does not sell one fixed item. Each customer gets a **system** put together from many parts:
panels, an inverter, a mounting structure, DC/AC cable (sold by the metre), MC4 connectors, ACDB/DCDB, earthing, a lightning arrester, conduit, batteries and so on.
The mix changes for each customer: a different brand of panel, a bigger inverter, extra cable, a battery added.

Tally handles accounts well, but it does not handle this well:

| Pain today | Why Tally struggles |
|---|---|
| "Can we do a 5 kW job this week?" needs a manual count of 12 parts | Tally has no idea that 10 panels + 1 inverter + … = one 5 kW system |
| The same panels get promised to two customers | Tally has no "reserved for customer" stock, only closing stock |
| Cable is bought in 100 m coils and cut at site; leftover comes back | Part-quantities and returns from site are hard to track |
| Purchasing is guesswork | Nothing links open quotations to what needs to be bought |
| Selling one "system" but stock moves for 12 items | Data entry for every item, every sale |

## 2. The idea (what the demo shows)

Five simple ideas:

1. **Parts (stock):** every item with quantity in godown, **reserved**, and **free** (godown minus reserved).
2. **System kits (bill of materials):** saved recipes, e.g. "3 kW On-grid = 6 panels + 1 inverter + 3 structure sets + 30 m DC cable …". The app shows **how many complete systems can be built right now** and which part is the bottleneck.
3. **Orders built from kits:** pick a kit, then swap the brand, change quantities or add parts for this customer. The stock check happens live as you edit.
4. **Order life cycle:** Quotation → **Stock reserved** → **Dispatched** (stock leaves godown) → Installed. Leftover from site can be returned into stock.
5. **Purchase list worked out automatically:** from open quotations plus minimum stock levels, rounded to supplier pack sizes (100 m coils, packs of 10).

Tally stays the accounting system. This app exports closing stock and dispatched item lines in a format that can go into Tally.

## 3. Demo (built)

- Location: `site/` (the Vercel-ready website, see `site/README.md`), `demo/index.html` (editable source) and `demo/standalone.html` (a single file that opens by double-click).
- No server and no login. Sample data is stored in the browser (localStorage). "Reset sample data" restores the original data.
- Sample data: 21 real-world parts (Waaree/Adani/Vikram panels, Growatt/Luminous inverters, Exide batteries, Polycab-style cable…), 4 kits, 6 orders across Bhubaneswar, Cuttack, Puri, Khordha.

Screens: Home · Stock · System kits · Orders · Purchase · Insights (incl. Tally export) · New order.

**v2 (2026-10-30):** macOS-style look to suit a MacBook (frosted sidebar, SF system font, light and dark mode) and an analytics layer:
- KPI cards with trends: stock value, sales (30 days), open pipeline, parts needing attention.
- Automatic insights: orders blocked by a shortage, parts that will run out within 3 weeks, money tied up in slow stock, sales change, best seller, most profitable kit.
- Charts with hover details and a "view as table" option: sales and margin by 30-day period, stock value over time, stock health.
- Insights page: order pipeline, stock value by category, days of stock left per part, margin per kit, slow-moving stock, Tally export, stock register.
- Stock page has a "Lasts" column: how many days current free stock will last at the usual usage.
- **Live notifications (v5):** a bell in the toolbar with an unread badge and a Notification Center panel (All or Unread, grouped by day, click to jump to the item). Alerts are raised by themselves when a part drops below its minimum or runs out, and when orders and stock change. A simulated stream of activity from other staff shows how it behaves live. Settings choose what to be notified about, banners, a sound and desktop notifications. In the real system these would also go out by WhatsApp or SMS.
- **Ready to host (v5):** CSV downloads for the stock list, purchase list and Tally export, a printable quotation, and a first-visit guide. Every button was clicked automatically on every screen and inside every dialog, with no errors.
- **macOS interface (v4):** built to follow Apple's design conventions. Frosted sidebar with grouped sections (Inventory, Sales, Analytics), a translucent toolbar that stays at the top while scrolling, Mac-style push buttons, pop-up menus and segmented controls, dialogs that drop in as sheets, confirmations as Notification Center banners, thin overlay scrollbars, and full light and dark mode. On a phone it becomes an iOS-style tab bar.
- **Finding parts (v3):** every part has a brand. The Stock page has one search box that understands several words ("waaree 575", "inverter 5 kw"), with the matches highlighted, plus Category, Brand (pick several) and Availability filters. Each filter shows how many parts it would give, filters that give none are greyed out, and active filters show as removable tags with "Clear all". It can be sorted by urgency or days left. Press `/` to jump to search and Esc to clear it. On a phone the filters fold behind a "Filters" button.
- Adding parts to an order or a kit opens a searchable picker (same search and filters). Enter adds the top result, so a part can be added without touching the mouse.
- In the order screen, swapping a part lists the other brands of the same type, with free stock shown next to each.
- Sample trend history for the five earlier periods is dummy data. In the real system it comes from actual orders and stock movements.

### Suggested 5-minute demo script for the owner
1. **Home:** "What can I build right now?" shows how many complete systems of each kit are in the godown, and which part is holding each one back.
2. **New order:** type a customer name, pick "3 kW On-grid", swap Waaree for Vikram panels, add a battery. Point at the live red/green stock check and the margin.
3. Save and reserve. Go to **Stock** and show that the panels now show as "Reserved", so nobody can promise them twice.
4. **Orders:** Dispatch, then "Return leftover" (4 m cable comes back).
5. **Purchase:** "This is what you need to buy, and why." Then **Mark received**.
6. **Reports:** stock value by category, and the copy-for-Tally export.

## 4. Real system: proposed scope

### Phase 1: Core (MVP), about 3–4 weeks
- Login with roles: Owner, Store keeper, Sales.
- Parts master, kits (BOM), orders with reserve, dispatch and return; purchase receipts (GRN), stock adjustments with reason.
- Purchase list, low-stock alerts.
- Excel/CSV import of current Tally stock items to start (no retyping).
- Tally export (CSV first; Tally XML import as a later option).
- Works on phone for the godown (big buttons, simple screens).

### Phase 2: Control, about 3 weeks
- **Serial numbers** for panels, inverters and batteries, recorded at dispatch, for warranty claims and DISCOM/PM Surya Ghar paperwork.
- Multiple godowns / site stock (material lying at site).
- Supplier master, purchase orders, supplier price history.
- Quotation PDF with company letterhead; WhatsApp share.
- Photo of delivery challan / installation.

### Phase 3: Extras
- Odia language option for store staff.
- Direct Tally sync (Tally Prime XML/ODBC) instead of copy-paste.
- Subsidy / net-metering application tracker per order.
- Dashboard of margin per system type, salesperson, month.

## 5. Suggested technology (for the real build)

Match what already runs on our server so it is easy to host and maintain:
- Frontend: React (Vite), mobile-first.
- Backend: Python FastAPI (or Node), PostgreSQL. Stock movements are an append-only ledger. Current stock is computed from it, so every number can be traced.
- Hosting: Docker on the existing VPS behind Nginx + HTTPS, daily database backup.

Core tables: `parts`, `kits`, `kit_items`, `orders`, `order_items`, `stock_moves` (in / out / return / adjust, with reference), `suppliers`, `purchases`, `serials`, `users`.

## 6. Questions for the owner

1. How many godowns / store locations? Does material sit at sites for days?
2. Which items need serial numbers (panels? inverters? batteries?)?
3. Who will use it day to day: owner only, or store staff and sales too?
4. Which Tally version (Tally Prime?), and is item-level stock kept in Tally today?
5. Typical kits sold, and the brands in use?
6. Is GST billing done in Tally (keep it there) or should this app create invoices?
7. Phone or computer in the godown?
