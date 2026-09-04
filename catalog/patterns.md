# Patterns

Cross-cutting techniques and recurring pipelines discovered during harvest.

## SEO & AI search visibility

- **Directory backlinks for DR** — curated launch directories (TinyShelf, TinyLaunch) cited as dofollow/DR plays; pairs with topical authority posts (`x-2094328961522397530`, `web-tinyshelf`, `web-tinylaunch-directories`).
- **Free tools over blog posts** — one-page, browser-only utilities indexed in GSC + Bing; soft CTA to paid product (`x-2094770895021572502`).
- **Citation outreach / AEO** — get mentioned on pages AI models already cite for buying questions; CrowdReply MCP tracks visibility across ChatGPT/Grok/Perplexity (`x-2094553318031024285`, `web-crowdreply`).
- **Agent-run SEO audits** — local-first crawl + GSC + IndexNow via CLI/MCP skills (`github-iannuttall-seo`, `github-LessieAI-people-search-bench`).
- **Topical maps vs keyword chasing** — cluster content around jobs-to-be-done (`x-2095130625976176754`).

## MCP & agent orchestration

- **Design-in-editor MCP** — remote servers clone/enhance URLs into repo-aware UI (`web-aidesigner-mcp`, `x-2094467179320119498`).
- **Sales/outbound MCP stacks** — Grok Bot + MCP for prospecting, sequencing, visibility (`github-romangojiberryAI-gojiberryai-sales-os`, `x-2095081419202560010`).
- **Warehouse-connected marketing agents** — MCP over customer data for ad/SEO automation (`web-graphed`, `github-superdesigndev-treg`).
- **Headless browser for agents** — Rust/Workers browsers give each agent isolated sessions (`github-h4ckf0r0day-obscura`, `web-cloudflare-kitesurf`).

## DESIGN.md & design skills

- **DESIGN.md as agent contract** — brand tokens, component rules, lint/diff in CI (`github-google-labs-code-design-md`, `web-getdesign-md`, `web-sokosumi-design-md`).
- **Curated skill packs** — motion, taste, UI polish as installable agent skills (`github-emilkowalski-skills`, `github-leonxlnx-taste-skill`, `github-pbakaus-impeccable`).
- **Vibe-design workspaces** — conversational studio exports HTML/motion from DESIGN.md briefs (`github-nexu-io-open-design`, `web-open-design-ai`).

## Landing page & UI motion pipelines

- **Scroll-driven 3D hero** — agent skills + paid asset gen for flythrough landings (`github-oso95-scroll-world`, `github-nateherkai-scroll-craft`).
- **Layered parallax from image gen** — multi-layer alpha PNGs with scroll speed tiers; Codex or Claude + fal.ai (`x-2094524951025914278`, `web-blume-codes`, `web-fal-ai`).
- **Live product embed on marketing site** — shared Turborepo UI package so landing demo is the real app shell (`x-2094524951025914278`).
- **Daily-seeded decorative assets** — DiceBear custom styles for date-varying easter eggs (`web-dicebear`).

## 3D / video / BESS flythrough

- **Blender blockout → video model** — camera path in Blender via MCP, reference frames to Seedance/Veo/Kling/MiniMax H3 (`note-blender-minimax-h3-video-generation`, `web-fal-ai`, `web-meigen-ai`).
- **Gaussian splat repair & extension** — diffusion post-process on sparse reconstructions (`github-nv-tlabs-ArtiFixer`, `x-2094929928865341832`, `web-arcana-splat2mesh`).
- **PLY → mesh export** — desktop tools for 3DGS cleanup before web/Three.js (`web-arcana-splat2mesh`, `x-2094826117056414132`, `x-2094648474377839018`).
- **Depth-conditioned interior flythrough** — Blender Z-pass depth video as motion reference (Wan VACE / LTX 3DREAL) when tight interior geometry matters (`note-blender-minimax-h3-video-generation`).
- **Scroll-scrubbed industrial hero** — isometric diorama tied to page scroll (`github-oso95-scroll-world`, `web-utsubo`).
- **Indoor video → editable 3D** — real-to-sim assets from indoor footage (`x-2094961942058418268`).

## HTML-as-video / prompt-to-clip

- **HTML/CSS → MP4** — author the shot as a page, render via HyperFrames (`github-nexu-io-html-video`, `github-nexu-io-open-design`).
- **Prompt gallery → hosted model** — Seedance / GPT Image / Nano Banana prompts on fal or MeiGen MCP (`web-meigen-ai`, `web-fal-ai`, `github-wuyoscar-gpt-image2-skill`).
- **Chat-native motion then export** — motion-anything recipes to Lottie/MP4 when the job is a loop, not a 3D path (`github-nexu-io-motion-anything`; see also ui-motion).

## Capture-to-world (photo/video → 3D)

- **One still → Atlas world → three.js** — World Labs Atlas fills gaps; spark.js presents an orbitable scene (`x-2094864872853119216`).
- **Repair then fly** — ArtiFixer on broken/blurry 3DGS, then a camera path or mesh export (`github-nv-tlabs-ArtiFixer`, `web-arcana-splat2mesh`).
- **Indoor capture → posed assets** — Lucida-style video to individual 3D objects (`x-2094961942058418268`).

## Infographics & diagram-as-content

- **Editorial diagram skill** — HTML+SVG types, not Mermaid (`github-cathrynlavery-diagram-design`).
- **Infographic framework** — AntV SVG scenes + agent skills (`github-antvis-infographic`).
- **Chart IL via MCP** — Flint spec compiles to Vega/ECharts/Plotly (`web-flint-chart`).
- **Layer diagram as the argument** — one picture carries SEO or data-stack structure (`x-2094771557864292784`, `web-iandmacomber-post-ai-data-stack`, `x-2094558408259272998`).

## Data & context for agents

- **Context engineering as ETL** — knowledge bases built like data pipelines, not prompt stuffing (`web-davidgasquez-context-engineering`, `web-cerebras-knowledge-base`).
- **Self-service analytics via semantic layer** — Claude + foundations/skills for ~95% automated queries (`web-anthropic-claude-self-service-data`).
