# Judgment worksheet: infographics & diagrams (infographics-diagrams)

Owner aliases: infographics, diagrams, charts. A diagram that only illustrates an SEO claim stays secondary; judge the claim on [serp-ai-visibility](../serp-ai-visibility/worksheet.md).

## infographics-diagrams — short stack to try

1. **SVG / HTML the agent can edit.** Must-read AntV Infographic ([github-antvis-infographic](../../items/github-antvis-infographic/card.md)). Must-read Diagram Design 39 editorial types ([github-cathrynlavery-diagram-design](../../items/github-cathrynlavery-diagram-design/card.md)). Pretty-Mermaid → SVG/ASCII with no DOM ([x-2087329201451855933](../../items/x-2087329201451855933/card.md)).
2. **Charts as an intermediate language.** Microsoft Flint → Vega / ECharts / Plotly ([web-flint-chart](../../items/web-flint-chart/card.md)). Mono Charts if you want animated React primitives ([x-2088599468698751328](../../items/x-2088599468698751328/card.md)). DuckDB-speed SQL-native viz is an endorsement, not a kit ([x-2087205167662088363](../../items/x-2087205167662088363/card.md)).
3. **Architecture as a map, not a slide.** archify ([x-2093309791120543846](../../items/x-2093309791120543846/card.md)). system-atlas isometric from one data file ([x-2091559663833924082](../../items/x-2091559663833924082/card.md)). FleetingBits explorable codebase diagrams ([x-2088016749849682120](../../items/x-2088016749849682120/card.md)). Harness canvas worker ([x-2088590355440476343](../../items/x-2088590355440476343/card.md)).
4. **Social / 3D extras.** Dashboard Stack carousel studio ([x-2091767461058105402](../../items/x-2091767461058105402/card.md)). iCraft 3D network diagrams ([x-2089570022490263586](../../items/x-2089570022490263586/card.md)). Emil’s one-accent markdown graphs ([x-2089372767934115883](../../items/x-2089372767934115883/card.md)) is a taste constraint.

## infographics-diagrams — axis scores

| item | output format | brand/theme control | skill vs kit | data binding vs static | social/carousel sizes |
|---|---|---|---|---|---|
| AntV Infographic | SVG (SSR fixture hardcoded hex, not CSS vars) | template themes | **5** skills; **137** named templates vs README ~200 bundle | template-driven | unknown |
| Diagram Design | HTML+SVG (`:root` tokens + hex in SVG) | editorial types | skill (**39** `type-*.md`; extra example stems exist) | static illustration | mid (editorial) |
| Pretty-Mermaid | SVG or ASCII | mermaid theme | skill | mermaid source | n/a |
| Flint | JS: VL / ECharts / Chart.js / Plotly / Excel. Hosted MCP render enum: VL / ECharts / Chart.js | **11** theme preset files; ThemeSpec → Vega-Lite | IL + hosted MCP **6** tools (v0.5.1) | high (same spec compiled VL+ECharts here) | n/a |
| Mono Charts | React components | Amicro look | kit | data props implied | unknown |
| archify | animated architecture | unknown | skill | “verifiable” claimed | n/a |
| system-atlas | isometric map (`atlas.html`) + generated `SYSTEM.md` | one `data.mjs` | skill (`npx skills add inkboard/system-atlas`; MIT **392★**) | bound to that file | n/a |
| FleetingBits | explorable diagram | unknown | technique | inspectable dots claimed | n/a |
| canvas worker | in-chat canvas | unknown | harness add-on | unknown | n/a |
| iCraft | 3D network (GitHub **1,535★ / 128** forks; icraft.design live) | product look | editor (Free/Pro/Enterprise named) | static-ish | n/a |
| Dashboard Stack | IG/LI slides | studio presets (Wide pan + reveal, Blank, Cover, Slices) | hosted + **Use via MCP**; OSS still unlinked | static slides | high (1600×1200 4:3) |
| PRYNE stills | raster heroes | brand purple | example | static | mid |
| Emil accent graphs | markdown | one accent | taste rule | mermaid-ish | n/a |
| DuckDB viz endorsement | SQL-native | none | reference | high | n/a |

## infographics-diagrams — claims that need a receipt

- Diagram Design “39 types” — **39** `type-*.md` files counted ([diagram-design](../../tools/diagram-design.md)). Extra example stems are not extra types.
- AntV “~200” — README bundles templates + items + layouts. Named `registerTemplate` ids sum **137** ([antv-infographic](../../tools/antv-infographic.md)).
- Flint compiles to Vega, ECharts, *and* Plotly — local `assembleVegaLite` + `assembleECharts` ran on the getting-started spec. Plotly/Excel assemblers not exercised. Hosted `render_chart` enum omits Plotly. See [flint-chart-mcp](../../tools/flint-chart-mcp.md).
- archify “verifiable” diagrams — need what is verified (nodes vs runtime).
- Dashboard Stack “OSS repo soon” — studio is live (`studio.dashboardstack.sh` **103,784 B**, MCP mentioned); repo still unlinked ([dashboard-stack](../../tools/dashboard-stack.md)).
- PRYNE “minutes” — same stills already used as a prompt-gallery example; do not double-count as a diagram system. leftover12: `pryne.com` is **616 B** wasm-pack; `lexnlin.com` NXDOMAIN ([x-2092890365930131920#c2](../../items/x-2092890365930131920/card.md)).
- Emil one-accent graphs — leftover12 inspired-by t.co is **oxide.computer** (**164,446 B**), a hardware company, not a mermaid skill ([x-2089372767934115883#c2](../../items/x-2089372767934115883/card.md)).
- DuckDB-speed viz — leftover12 `duckdb.org` **409,105 B** is the SQL DBMS; DSR / 10M sparklines / no-JS product are not on the homepage ([x-2087205167662088363#c2](../../items/x-2087205167662088363/card.md)).

## infographics-diagrams — do not treat as load-bearing

- Known.agency SEO layer diagram (secondary) — SERP argument.
- Macomber / Driscoll essays (secondary) — company-brain prose.
- iCraft as a web-3d-scenes substitute — it is a diagram editor.

## infographics-diagrams — next capture work

1. AntV SSR fixture + Diagram Design architecture HTML token notes are on the tool pages. Remaining: a *fresh* agent-emitted SVG (not the repo fixture) if someone reruns the skill.
2. Flint `assemblePlotly` (1 scatter trace) and hosted `render_chart` vegalite **SVG 17,393 B / PNG 23,944 B** are on [flint-chart-mcp](../../tools/flint-chart-mcp.md). `render_chart` still has no Plotly/Excel backend.
3. Carousel studio is live (screenshot → pan → numbered frames; MCP named). 2026-09-05 OSS hunt still empty (card `#c4`): `dashboardstack.sh` is a different Nuxt/Next framework; org repos `[]`; dennis 26 public repos have no studio name. Remaining: the promised OSS repo.
4. system-atlas is first-party on [system-atlas](../../tools/system-atlas.md): MIT **392★**; `data.mjs` → `atlas.html` + `SYSTEM.md`; chapters ≤3 new structures ([x-2091559663833924082#c3](../../items/x-2091559663833924082/card.md)).
5. leftover13 canvas-worker reply is HQFlow (`hqflow.vercel.app` **15,455 B**; `WinterArc21/HQFlow` MIT **21★**) — a neighbor OSS workflow map, not the in-chat canvas worker ([x-2088590355440476343#c3](../../items/x-2088590355440476343/card.md)).
