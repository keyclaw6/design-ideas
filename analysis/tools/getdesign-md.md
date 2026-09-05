# Getdesign Md

**Slug:** `getdesign-md` · **Kind:** product · **URL:** https://getdesign.md · **Canonical item:** [web-getdesign-md](../items/web-getdesign-md/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md)
**Referenced by (1):**
- [getdesign.md: catalog of 550+ DESIGN.md files for coding agents](../items/web-getdesign-md/card.md) — tool, reference — design-agent-skills

<!-- NOTES:START -->
Fetched 2026-09-04 https://getdesign.md

Homepage still advertises **550+** DESIGN.md analyses and “Follows Google’s official DESIGN.md spec.” Catalog is request/gated (sign-in, Catalog Pass). Did not download a file to diff against the Google Labs YAML+markdown spec.

**2026-09-04 capture — sitemap vs homepage vs marketing.**
`https://getdesign.md/sitemap.xml`: **764** `<loc>`s. Unique brand slugs: **566** `/design-md/{slug}` + **76** `/{slug}/design-md` homepage rows; union **627**. Homepage HTML lists those **76** `/…/design-md` rows (Catalog Pass). Sibling repo `VoltAgent/awesome-design-md` tree: **147** folders under `design-md/`. Marketing **550+** is below the sitemap union; do not treat 76, 147, 550+, or 627 as the same number.

**2026-09-04 neighbor — designmd.app (no tool file).** `https://designmd.app/` HTTP 200, **75,265** B, title **“DESIGN.md — 562 Design System Files for AI Coding Agents”**. Visible copy: “Open library · 562 documented files”, “562 DESIGN.md ready to use”, h1 **DESIGN MD (DESIGN.md)**. Mentions Claude Code / Cursor / Kiro / Windsurf / Cline. This is **not** getdesign.md and **not** the blocked designmd.me / designmd.supply hosts. Do not collapse **562** with getdesign marketing 550+ or sitemap union 627.

**2026-09-04 neighbor — designengineer.tools (no tool file).** `GET https://designengineer.tools/` **200 / 138,283 B**. Title **Design Engineer Tools**. Meta curated by James Warner. **20** H2 sections (Inspiration … Emoji). **128** unique external hrefs this pass — do not collapse with a prior **129** count. Bookmark index, not a DESIGN.md pack. Receipt `designengineer-tools-2026-09-04.json`.

**2026-09-04 designmd.app sitemap + library title.** `GET /sitemap.xml` is a one-child index; `sitemap-0.xml` has **198** unique `<loc>`s: **74** `/library/<slug>` style pages, **35** `/brands/<slug>` (plus 10 `/brands/category/…`), **51** blog, **12** guides. `/library` HTTP 200, **1,455,593** B, title **“DESIGN.md Library — 561 Design Systems for AI Agents”**. Do not collapse homepage **562**, library-title **561**, sitemap **198**, or library slugs **74**. No `/api/files` dump (404). Author link on the home page: `gitlab.com/fabriciotelles/vibe-styles`.

**2026-09-05 roundup re-fetch (Tran Mau nine).** getdesign.md **200 / 193,240 B** still markets **550+**. neuform.ai **6,499 B** SPA. aura.build **7,737 B** SPA. sokosumi.com/tools/design-md **109,208 B**. open-design.ai **339,680 B**. designmd.me / designmd.supply / typeui.sh still **429** — do not hammer. Receipt `analysis/_work/captures/mustread-2026-09-05.json`.

**2026-09-05 leftover18.** Same 429 re-count on the stub cards: designmd.me **32,188 B** / designmd.supply **32,184 B** (Vercel Security Checkpoint). Neighbor designmd.app this receipt **75,632 B** / **562** files. Do not hammer. Do not collapse 562 with 550+ / 627.

**2026-09-05 leftover19.** designmd.app home **75,265 B / 562**; `/library` **1,455,593 B / 561**. Byte drift vs leftover18 **75,632** — do not collapse. 429 hosts untouched.

**2026-09-05 leftover22.** Unused neighbor `google-labs-code/design.md` Apache-2.0 **27,737★**. Spec repo, not the designmd.supply marketplace (still 429). Receipt `leftover22-2026-09-05.json`.

**2026-09-05 leftover24.** Unused `design-md.hyperbrowser.ai` **5,659 B** is a “Booting DESIGNMD” SPA — not a catalog count. Receipt `leftover24-2026-09-05.json`.

**2026-09-05 leftover27.** Unused Stitch spec `https://stitch.withgoogle.com/docs/design-md/specification` **25,497 B** titles *Stitch - Design with AI*. Visible extract empty (client-rendered SPA). No spec headings / schema / version integers. Receipt `leftover27-2026-09-05.json`.
<!-- NOTES:END -->
