# Styles Refero Design

**Slug:** `styles-refero-design` · **Kind:** product · **URL:** https://x.com/ImranUxi/status/2091934379648110784 · **Canonical item:** [x-2091934379648110784](../items/x-2091934379648110784/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md)
**Referenced by (2):**
- [Refero styles.refero.design: 2000+ DESIGN.md files for coding agents](../items/x-2091934379648110784/card.md) — tool, reference — design-agent-skills
- [Refero DESIGN.md library — 2000+ product design languages for agents](../items/x-2093766772029559077/card.md) — tool, reference — design-agent-skills

<!-- NOTES:START -->
Fetched 2026-09-04 https://styles.refero.design/

Beta gallery copy: **“Browse 2,000+ AI-readable design systems.”** Refero MCP advertised for agent search. Visible tiles include Caldera, ORYZO, Apple, Stripe, Linear, Notion, etc. Count not independently enumerated (no public file list). MCP not connected in this pass.

**2026-09-04 capture — paged `/api/styles`.**
`GET https://styles.refero.design/api/styles?page=N` returned 20 items/page through page 64, then 10 on page 65. **1,289 unique style ids** / **1,241 unique `siteName`s**. Homepage first paint is the first 20. Marketing **2,000+** is still above this public API. These are gallery records (screenshot + tokens), not a downloadable DESIGN.md file tree.

**2026-09-04 capture — Linear `fullResult.designSystem`.** `GET https://styles.refero.design/api/styles/90ce5883-bb24-4466-93f7-801cd617b0d1` HTTP 200, **81,180** bytes. `style.fullResult.designSystem` keys: dos (7), donts (7), theme `dark`, colors (16, e.g. Void `#08090a`, Acid Lime CTA `#e4f222`), layout, imagery, similar (Vercel / Cursor / Raycast / Framer), spacing, surfaces (4), northStar “midnight precision instrument”, typeScale (8), components (12), typography (Inter Variable, weights cap **590**; Berkeley Mono for IDs), description, customSections (`Agent Prompt Guide`, `Type Scale Detail`), elevationPhilosophy. `meta.extractedAt` 2026-07-03; viewport 1440×900; elementCount 2469. This is **JSON tokens + a prompt guide**, not a downloadable DESIGN.md tree.

**2026-09-04 capture — Notion + Stripe same API.** Same `fullResult.designSystem` shape, still no `.md` file. Notion (`2bf4c61f-…`, notion.so) 68,148 bytes: theme `light`, northStar “warm paper notebook under afternoon sun”, 17 colors (Notion Blue `#0075de`, Paper Warmth `#f6f5f4`), 14 components, typeScale 10, families NotionInter + Lyon Text, customSections Agent Prompt Guide + Decorative Marks System; extractedAt 2026-07-03; elementCount 657. Stripe (`48e5de76-…`) 70,976 bytes: theme `light`, northStar “indigo-ink ledger on frosted glass”, 14 colors (Indigo Ink `#533afd`), 12 components, typeScale 9, family sohne-var 300/400, Agent Prompt Guide only; extractedAt 2026-07-03; elementCount 1599.

**2026-09-04 capture — Sokosumi YAML vs this JSON (same three brands).** Sokosumi published DESIGN.md uses 47 color keys and a Google-style frontmatter. Overlap: Linear surface/Void `#08090a`; Notion primary `#0075de`; Stripe primary `#533afd`. Divergence: Sokosumi Linear `primary` `#e5e5e6` vs this record’s Acid Lime CTA `#e4f222`. Do not treat the two extractors as the same token sheet. Hyperbrowser still 401.
<!-- NOTES:END -->
