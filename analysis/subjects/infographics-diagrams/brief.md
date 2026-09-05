# Infographics, diagrams-as-content, charts (infographics-diagrams)

## infographics-diagrams — scope

Diagram/infographic skills and frameworks (AntV, diagram-design, archify, pretty-mermaid, system-atlas), chart ILs (Flint), chart component kits (Mono Charts), fast dataviz, codebase visual maps, social carousels, layer-diagram-as-argument.

Exclusion: A diagram that only illustrates an SEO claim → serp-ai-visibility primary, this secondary.

Priority `standard`. Owner aliases: infographics, diagrams, charts.
Expected primary range [12, 18]. This roster has **14** primary and **3** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## infographics-diagrams — what the owner is trying to decide

Decide which diagram/infographic skills (AntV, diagram-design, Flint, mermaid) produce publishable assets versus slides that only illustrate another subject.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## infographics-diagrams — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=9, technique=7, example=5, claim-source=2, reference=4.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (8):
- [AntV Infographic: AI-tuned SVG infographic framework with agent skills](../../items/github-antvis-infographic/card.md) — tool, reference — AntV Infographic (@antv/infographic) is an open-source framework for generating and editing SVG infographics from compact template…
- [Diagram Design: 39 editorial HTML+SVG diagram types for agents](../../items/github-cathrynlavery-diagram-design/card.md) — tool, technique — GitHub skill pack shipping 39 editorial diagram types as self-contained HTML and SVG for Claude Code, Codex, Factory Droid, and Pi
- [Microsoft Flint chart IL: compact specs compile to Vega, ECharts, Plotly](../../items/web-flint-chart/card.md) — tool, technique — Microsoft Flint is a visualization intermediate language where agents write compact chart specs that compile to Vega-Lite, ECharts,…
- [Pretty-Mermaid Skills: Mermaid to SVG or ASCII without a browser DOM](../../items/x-2087329201451855933/card.md) — tool, technique — Agent skill pack that renders Mermaid diagram source to polished SVG or ASCII art with zero DOM dependencies, so Cursor/Codex sessions…
- [Mono Charts: CLI-installable animated React chart components (Amicro)](../../items/x-2088599468698751328/card.md) — tool, example — Announcement of Mono Charts under the Amicro open-source UI collection: minimal animated React chart components installable with a…
- [iCraft Editor for 3D network architecture diagrams (gantFDT/icraft)](../../items/x-2089570022490263586/card.md) — tool, reference — Pointer to gantFDT/icraft iCraft Editor for 3D network and architecture diagrams with immersive visual effects—positioned between 2D…
- [Dashboard Stack carousel studio — Instagram and LinkedIn slide generator](../../items/x-2091767461058105402/card.md) — tool, example — Launch post for studio.dashboardstack.sh: a carousel builder for Instagram and LinkedIn slides, with an open-source repo promised soon…
- [archify trending repo — agent skill for animated architecture diagrams](../../items/x-2093309791120543846/card.md) — tool — Trending-repo highlight for archify, an agent skill that renders verifiable architecture, workflow, sequence, data-flow, and lifecycle…

First role `technique` (3):
- [FleetingBits: Claude-generated explorable codebase diagrams with inspectable data dots](../../items/x-2088016749849682120/card.md) — technique, example — FleetingBits describes having Claude render codebases as interactive visual diagrams so he can discuss architecture with the agent;…
- [Harness canvas worker draws architecture diagrams in chat](../../items/x-2088590355440476343/card.md) — technique, example — @mfpiccolo had the coding harness build a canvas worker so agents draw architecture diagrams directly in chat and via a…
- [system-atlas skill builds explorable isometric maps from one data file](../../items/x-2091559663833924082/card.md) — technique, tool — system-atlas is an agent skill that renders an explorable isometric map of a codebase, agent, or pipeline from one data file with…

First role `example` (1):
- [PRYNE math-brand visuals generated in minutes with AI](../../items/x-2092890365930131920/card.md) — example, claim-source — LexnLin shows four PRYNE math-education brand visuals — purple 3D symbol heroes and pastel operator blocks — claiming they were made in…

First role `claim-source` (1):
- [Hamilton Ulmer endorses DuckDB-speed SQL-native dataviz](../../items/x-2087205167662088363/card.md) — claim-source, reference — Hamilton Ulmer reacts that DuckDB-speed data visualization works extremely well, nearly free, with no JavaScript required—pointing…

First role `reference` (1):
- [Emil Kowalski markdown graphs with one vibrant accent color](../../items/x-2089372767934115883/card.md) — reference, technique — One-line taste constraint from Emil Kowalski: prefer markdown-native graphs with a single vibrant accent color instead of rainbow…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [AntV Infographic: AI-tuned SVG infographic framework with agent skills](../../items/github-antvis-infographic/card.md)
- [Diagram Design: 39 editorial HTML+SVG diagram types for agents](../../items/github-cathrynlavery-diagram-design/card.md)

Secondary membership (3), not in the primary count:
- [Ian Macomber essay on post-AI data stack and company reality](../../items/web-iandmacomber-post-ai-data-stack/card.md) — primary `agent-memory-knowledge`
- [Driscoll essay on AI-native company intelligence layer with Ramp/Cerebras refs](../../items/x-2094558408259272998/card.md) — primary `agent-memory-knowledge`
- [Five layers of SEO in 2026 framework (Known.agency)](../../items/x-2094771557864292784/card.md) — primary `serp-ai-visibility`

## infographics-diagrams — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [svg-infographic-rendering](../../techniques/svg-infographic-rendering.md) — Diagrams and infographics as SVG/mermaid/brand-matched layers.
- [chart-theme-presets](../../techniques/chart-theme-presets.md) — Chart intermediate languages and theme packs (Flint and kin).
- [agent-harness-ops](../../techniques/agent-harness-ops.md) — Harness, control plane, folder-as-agent, and multi-agent ops that a later judge can rerun.

## infographics-diagrams — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [antv-infographic](../../tools/antv-infographic.md)
- [diagram-design](../../tools/diagram-design.md)
- [flint-chart-mcp](../../tools/flint-chart-mcp.md)
- [system-atlas](../../tools/system-atlas.md)
- [dashboard-stack](../../tools/dashboard-stack.md)
- [archify](../../tools/archify.md)

## infographics-diagrams — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-antvis-infographic#c1` | Infographic ships ~200 built-in templates and AI-tuned syntax that agents emit as compact template strings rendered t… | stated | [AntV Infographic: AI-tuned SVG infogr…](../../items/github-antvis-infographic/card.md) |
| `github-cathrynlavery-diagram-design#c1` | The repo defines 39 diagram types including architecture, sequence, Sankey, Wardley, and user-journey layouts. | stated | [Diagram Design: 39 editorial HTML+SVG…](../../items/github-cathrynlavery-diagram-design/card.md) |
| `github-cathrynlavery-diagram-design#c2` | Diagrams ship as self-contained HTML and SVG with minimal light, dark, and editorial variants. | stated | [Diagram Design: 39 editorial HTML+SVG…](../../items/github-cathrynlavery-diagram-design/card.md) |
| `github-cathrynlavery-diagram-design#c3` | Install uses the diagram-design plugin marketplace commands. | stated | [Diagram Design: 39 editorial HTML+SVG…](../../items/github-cathrynlavery-diagram-design/card.md) |
| `web-flint-chart#c1` | Flint derives scales, axes, and spacing from a semantic spec plus data and optional theme. | stated | [Microsoft Flint chart IL: compact spe…](../../items/web-flint-chart/card.md) |
| `x-2087205167662088363#c1` | Author claims a dataviz path delivers DuckDB speed, near-zero cost, and no JavaScript requirement. | stated | [Hamilton Ulmer endorses DuckDB-speed …](../../items/x-2087205167662088363/card.md) |
| `x-2087329201451855933#c1` | Pretty-Mermaid Skills renders Mermaid diagrams as SVG or ASCII with zero DOM dependencies. | stated | [Pretty-Mermaid Skills: Mermaid to SVG…](../../items/x-2087329201451855933/card.md) |
| `x-2088016749849682120#c1` | Claude can render a codebase as a visual diagram with moving data snippets the author can inspect while discussing th… | demonstrated | [FleetingBits: Claude-generated explor…](../../items/x-2088016749849682120/card.md) |
| `x-2088590355440476343#c1` | Author built a harness canvas worker so the agent draws diagrams in chat rather than pasting screenshots. | stated | [Harness canvas worker draws architect…](../../items/x-2088590355440476343/card.md) |
| `x-2088599468698751328#c1` | Mono Charts is a collection of minimal, animated chart components for React, open source under Amicro. | stated | [Mono Charts: CLI-installable animated…](../../items/x-2088599468698751328/card.md) |
| `x-2088599468698751328#c2` | Charts install with a single CLI command. | stated | [Mono Charts: CLI-installable animated…](../../items/x-2088599468698751328/card.md) |
| `x-2089372767934115883#c1` | Emil Kowalski recommends markdown graphs that use one vibrant accent color. | stated | [Emil Kowalski markdown graphs with on…](../../items/x-2089372767934115883/card.md) |
| `x-2089570022490263586#c1` | iCraft Editor targets 3D network architecture diagrams with immersive visual effects. | stated | [iCraft Editor for 3D network architec…](../../items/x-2089570022490263586/card.md) |
| `x-2091559663833924082#c1` | The atlas uses progressive disclosure chapters that reveal a few boxes at a time instead of dumping the whole system. | stated | [system-atlas skill builds explorable …](../../items/x-2091559663833924082/card.md) |
| `x-2091767461058105402#c1` | Dashboard Stack studio is live for creating Instagram and LinkedIn carousels. | stated | [Dashboard Stack carousel studio — Ins…](../../items/x-2091767461058105402/card.md) |

Full set: claims.jsonl (28 rows)

## infographics-diagrams — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- output format (SVG, mermaid, chart IL)
- brand/theme control
- agent-skill vs component kit
- data binding vs static illustration
- fits social/carousel sizes

## infographics-diagrams — thread coverage

X items in primary roster: 11. captured_full=2, captured_partial=9, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2087205167662088363](../../items/x-2087205167662088363/thread.md) | captured_partial | 6 | 3 | 0 |
| [x-2087329201451855933](../../items/x-2087329201451855933/thread.md) | captured_full | 1 | 1 | 0 |
| [x-2088016749849682120](../../items/x-2088016749849682120/thread.md) | captured_partial | 196 | 3 | 3 |
| [x-2088590355440476343](../../items/x-2088590355440476343/thread.md) | captured_partial | 4 | 3 | 1 |
| [x-2088599468698751328](../../items/x-2088599468698751328/thread.md) | captured_partial | 47 | 1 | 1 |
| [x-2089372767934115883](../../items/x-2089372767934115883/thread.md) | captured_partial | 54 | 1 | 0 |
| [x-2089570022490263586](../../items/x-2089570022490263586/thread.md) | captured_full | 1 | 1 | 0 |
| [x-2091559663833924082](../../items/x-2091559663833924082/thread.md) | captured_partial | 30 | 1 | 1 |
| [x-2091767461058105402](../../items/x-2091767461058105402/thread.md) | captured_partial | 5 | 3 | 1 |
| [x-2092890365930131920](../../items/x-2092890365930131920/thread.md) | captured_partial | 8 | 3 | 1 |
| [x-2093309791120543846](../../items/x-2093309791120543846/thread.md) | captured_partial | 2 | 1 | 1 |

## infographics-diagrams — gaps and open questions

Primary readiness: ready=4, ready-with-gaps=10. Gap tags: thread-partial=2, linked-page-unfetched=2.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Can AntV / Flint emit on-brand SVG from a claim table without a designer pass?
- When is a diagram the artifact versus decoration on an SEO post?

If this subject drops below 6 primary items after a future reclass, merge it into `landing-ui-motion` and delete the folder.

## infographics-diagrams — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [landing-ui-motion](../landing-ui-motion/brief.md)
- [serp-ai-visibility](../serp-ai-visibility/brief.md)
- [design-agent-skills](../design-agent-skills/brief.md)

