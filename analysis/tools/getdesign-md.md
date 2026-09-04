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

**2026-09-04 designmd.app sitemap + library title.** `GET /sitemap.xml` is a one-child index; `sitemap-0.xml` has **198** unique `<loc>`s: **74** `/library/<slug>` style pages, **35** `/brands/<slug>` (plus 10 `/brands/category/…`), **51** blog, **12** guides. `/library` HTTP 200, **1,455,593** B, title **“DESIGN.md Library — 561 Design Systems for AI Agents”**. Do not collapse homepage **562**, library-title **561**, sitemap **198**, or library slugs **74**. No `/api/files` dump (404). Author link on the home page: `gitlab.com/fabriciotelles/vibe-styles`.
<!-- NOTES:END -->
