# Cult Ui

**Slug:** `cult-ui` · **Kind:** product · **URL:** https://www.cult-ui.com/ · **Canonical item:** [web-cult-ui](../items/web-cult-ui/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [landing-ui-motion](../subjects/landing-ui-motion/brief.md)
**Referenced by (1):**
- [Cult UI: shadcn components plus 92+ AI SDK agent patterns](../items/web-cult-ui/card.md) — tool, example — landing-ui-motion

<!-- NOTES:START -->
**2026-09-04 capture — OSS docs vs live neighbors.**
Clone `https://github.com/nolly-studio/cult-ui.git` (6106 stars, MIT). **77** `content/docs/components/*.mdx` including `ai-instructions.mdx`. Homepage `cult-ui.com` fetch hit Vercel 429. “92+ AI SDK patterns” looks Cult Pro, not the OSS docs count.

**Vengeance** (no tool file — park here as neighbor): live `https://www.vengeanceui.com/` (not vengence-ui.com) **46 components / 9 families**; `npx shadcn@latest add @vengeanceui/[component]`. Registry `https://www.vengeanceui.com/r/registry.json` is a **132-item** list (includes accordion etc. — may be more than marketing 46). Repo `Ashutoshx7/VengeanceUI`.

**Originkit** (no tool file): homepage RSC dump **468 unique** `originkit.dev/components/<slug>-gallery` slugs. Card “363+” is marketing; 363 in the dump was a font hash, not a count. MCP `https://mcp.originkit.dev` JSON hello. Public `/registry.json` 404. Beta quota on integrations page: components 10/day 25/week, sections 5/day 10/week, templates 3/day 7/week.

**2026-09-04 capture — pricing pages (Cult Pro / Originkit / Vengeance).**

Cult Pro `https://pro.cult-ui.com/pricing` HTTP 200, 328,495 B, title `cult ui/pro`. Visible offer: **one-time payment, lifetime access, $129** (struck **$179**), badge **Summer Sale — Save $50**. FAQ from the RSC payload (not the collapsed accordion DOM): Pro is Templates + Full Stack Patterns + Blocks (TypeScript / Next.js). **Annual** = updates for **1 year**; **Lifetime** = updates for the lifetime of the product; license activates on the purchase email; login `pro.cult-ui.com`. **aisdkagents.com is a completely separate product** — Cult Pro is SaaS blocks/templates/animated marketing; AI SDK Agents is Vercel AI SDK Full Stack Patterns only. OSS homepage `cult-ui.com` still Vercel **429**.

Originkit `https://www.originkit.dev/pricing` HTTP 200, title `Pricing · Originkit`. Plan objects in the RSC dump (version 2):

| slug | yearly (compare-at) | monthly | daily copies C/S/T | weekly C/S/T | notes |
|---|---|---|---|---|---|
| Free | **$0/year** | — | **3 / 2 / 1** | **5 / 5 / 2** | Limited; `purchasable: false` |
| Pro | **$79/year** (`compareAtUsd` **108**, label Founding offer) | **$8** | **10 / 5 / 3** | **25 / 20 / 6** | email.updates + filters.recommended |
| Studio | **$179/year** (`compareAtUsd` **228**, Founding offer) | **$19** | **25 / 10 / 5** | **60 / 30 / 10** | same features as Pro |

Visible page prints `$0/year` / `$79/year` / `$179/year` with sr-only “was, now”. `offerEndsAt` on the monthly rows is `2026-09-01T23:59:59+00:00`; the 2026-09-04 fetch still showed the founding yearly prices. Do not collapse these daily caps with the integrations-page beta quota (10/5/3 daily, 25/10/7 weekly). Fetched HTML has no CSS `@media` (client-rendered).

Vengeance: `https://vengeanceui.com/pricing` and `/pro` **404**. `/about`, `/templates`, `/docs` 200. GitHub README is **MIT**, Vercel OSS program; no paid-plan dollar on the README. Homepage `$` tokens are demo numerals, not a price table. Same-copy hero/pricing bake-off still missing a Vengeance paid column — treat Vengeance as MIT registry, Cult as paid Pro + 429 OSS home, Originkit as metered yearly copies.

**2026-09-04 capture — live hero strings (not a same-copy bake-off).** Fetched HTML, not a headed breakpoint log. Cult OSS `cult-ui.com` still **429** (Vercel Security Checkpoint; `@media (width<=600px)` only on that challenge page). Cult Pro home: title “Shadcn Blocks, Full Stack Patterns & Templates | Cult UI Pro”; h1s **“Shadcn blocks for marketing.”** / **“Ship your ideas.Even if you don't code.”**; fetched CSS `@media` is `prefers-color-scheme:dark` only. Originkit home: title **“Originkit — Free Animated component library for modern websites”**; **no h1/h2** in the SSR HTML; **0** `@media` in the HTML. Vengeance home: h1s **“Next-Gen UI Interactions”** / **“Ship landing pages at lightspeed”**; h2 “Hover effects, animated tooltips, and scroll-driven layouts…”; HTML-inline `@media` is `prefers-color-scheme:dark` only. `$` tokens on Vengeance/Originkit homes are demo numerals.

**2026-09-04 capture — CSS-bundle breakpoints (not a same-copy bake-off).** `originkit.com` returned **503** “no available server”; use `originkit.dev`. Originkit CSS `https://www.originkit.dev/_next/static/css/bc22663ac2289487.css` **201,892** B, **21** `@media` blocks / **11** unique queries: `max-width:1023px` (pad-header safe-area), `min-width` **640 / 768 / 1024 / 1280 / 1536 / 1920**, plus `prefers-reduced-motion` and `not all and (min-width:…)` Tailwind max-* inverses. Vengeance `https://www.vengeanceui.com/_next/static/chunks/0usnzzgtjcl0a.css` **507,862** B, **35** blocks / **11** unique: `min-width` **640 / 768 / 1200 / 1440 / 1600**, `hover:hover` (10), `forced-colors:active` (6), `prefers-reduced-motion`, and `not all and (min-width: 640/768/1000)`. These are layout utilities in the shipped CSS, not color-scheme-only. Remaining: a controlled same-copy hero built from one kit vs the others. Cult OSS CSS bundle still blocked (429).
<!-- NOTES:END -->
