# Design skills, DESIGN.md contracts, vibe-design workspaces, anti-slop (design-agent-skills)

## design-agent-skills — scope

Installable design/taste/motion skill packs (Impeccable, Emil, Taste, interfaces.dev, MengTo, unlazy, /vision, /bro, no-ai-slop), DESIGN.md spec/extractors/collections, vibe-design and AI site builders (OpenDesign, Aura, Neuform, AIDesigner MCP, Orca design mode), UI prompt libraries for websites (SceneAI, typeui, 590+ prompts), anti-slop prose skills.

Exclusion: Image prompt galleries → image-prompt-galleries. Component libraries → landing-ui-motion. Generic agent harness → agent-harness-loops.

Priority `now`. Owner aliases: DESIGN.md, taste skill, anti-slop.
Expected primary range [38, 55]. This roster has **50** primary and **31** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## design-agent-skills — what the owner is trying to decide

Decide which design/taste/DESIGN.md skills actually change agent output (Impeccable, Taste, MengTo, no-ai-slop) versus prompt galleries and component kits.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## design-agent-skills — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=35, technique=13, example=12, claim-source=5, reference=24.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (31):
- [Emil Kowalski agent skills pack for animation and UI craft](../../items/github-emilkowalski-skills/card.md) — tool, technique — GitHub skill pack from Emil Kowalski encoding animation and UI craft for coding agents
- [Google Labs DESIGN.md spec with lint and diff CLI](../../items/github-google-labs-code-design-md/card.md) — tool, reference — Google Labs repo defining DESIGN.md: YAML token front matter plus markdown rationale so coding agents persist a lintable design system,…
- [interfaces.dev better-* agent skills for UI, type, color, and a11y review](../../items/github-jakubkrehel-skills/card.md) — tool, reference — MIT skill pack from Interfaces magazine: better-ui, better-typography, better-colors, better-accessibility, and better-layout review…
- [Leonxlnx Taste Skill: portable anti-slop agent skills for UI layout and motion](../../items/github-leonxlnx-taste-skill/card.md) — tool, technique — MIT-licensed agent-skills repo that upgrades AI-built interfaces on layout, typography, motion, and spacing, plus image-generation…
- [MengTo Skills: capture-to-prompt agent skills for web design and Three.js](../../items/github-mengto-skills/card.md) — tool, technique — MIT repo (~5.7k stars) of SKILL.md packs for Codex, Claude, and Cursor: video→HTML super prompts, HTML→interaction prompts, stitched…
- [OpenDesign: local-first open-source agent design workspace](../../items/github-nexu-io-open-design/card.md) — tool, example — Open-source desktop app (macOS/Windows) where coding agents drive design: prototypes, dashboards, decks, images, video, and HyperFrames…
- [Impeccable: agent design skill with PRODUCT.md, detectors, and 23 slash commands](../../items/github-pbakaus-impeccable/card.md) — tool, technique — GitHub repo (~65k stars) shipping one design skill, 23 slash commands, live browser iteration, and 61 deterministic anti-slop detector rules
- [AIDesigner remote MCP for in-repo HTML/Tailwind UI design](../../items/web-aidesigner-mcp/card.md) — tool, technique — Remote MCP server with 21 tools that generates, refines, and clones production HTML/Tailwind UI inside Cursor, Claude Code, Codex, and…
- [DESIGNMD: Hyperbrowser-powered DESIGN.md extractor for any URL](../../items/web-design-md-hyperbrowser/card.md) — tool — design-md.hyperbrowser.ai is a web extractor that reads a live site via Hyperbrowser and emits a Google-format DESIGN.md; the API key is…
- [getdesign.md: catalog of 550+ DESIGN.md files for coding agents](../../items/web-getdesign-md/card.md) — tool, reference — getdesign.md hosts 550+ DESIGN.md analyses of well-known sites (Apple, Stripe, Linear, etc.) following Google's spec, plus private…
- [Neuform: prompt-to-HTML landing builder exporting remixable DESIGN.md](../../items/web-neuform-ai/card.md) — tool, example — Neuform.ai turns prompts into AI HTML landing pages and remixable community templates while exporting DESIGN.md so later agent edits…
- [OpenDesign product site — local vibe-design workspace for 21+ agents](../../items/web-open-design-ai/card.md) — tool, example — Marketing site for OpenDesign, an Apache-2.0 local-first vibe design workspace that routes 21+ coding agents through composable skills…
- [SceneAI — copy-paste UI section prompt library with save counts](../../items/web-sceneai-art/card.md) — tool, reference — SceneAI hosts ready-made AI prompts for web heroes and landing pages—Neurolink, Exosia, Airlines, Shipmint, and similar sections—with…
- [Sokosumi free DESIGN.md generator from any website URL](../../items/web-sokosumi-design-md/card.md) — tool — Sokosumi free tool at sokosumi.com/tools/design-md opens a remote browser on any URL, reads computed styles, and writes a Google…
- [Refero Styles gallery: 2000+ downloadable DESIGN.md files for agents](../../items/web-styles-refero-design/card.md) — tool, reference — Beta gallery of 2,000+ AI-readable design systems scraped from product sites
- [Peter Yang /human-review skill: local visual editor for HTML and Markdown](../../items/x-2085006701984698712/card.md) — tool, technique — Peter Yang launches /human-review, a free skill that opens HTML and Markdown in a local visual editor for inline text edits, image…
- [/bro skill endorsement for humanizing AI copy and UI voice](../../items/x-2086845465140842638/card.md) — tool, example — Tom Johnson endorses the /bro agent skill (luchasarie/bro-skill) with a before/after example for restyling generated copy and UI toward…
- [pdfcn: shadcn-compatible open-source PDF component kit](../../items/x-2087656088124719304/card.md) — tool — pdfcn from @shadcnlabs is an OSS, shadcn/ui-compatible PDF document kit with 10+ themes and copy-paste blocks for invoices and reports,…
- [Orca design mode — on-page annotate and send to any AI agent](../../items/x-2087708050002239702/card.md) — tool, example — Orca design mode lets users draw and annotate directly on a live site, then package that spatial feedback for any AI coding agent
- [Impeccable 4.1 release — critique, native review, live mode fixes](../../items/x-2088254428730085690/card.md) — tool, reference — Paul Bakaus announces Impeccable 4.1 with 43 PRs: chat critique reliability, calmer design hooks, native iOS/Android reviews, Windows…
- [/vision skill writes VISION.md to gate agent feature work](../../items/x-2089189790881382676/card.md) — tool, technique — Kun Chen's /vision agent skill inspects repo context, proposes borderline feature ideas, and drafts a VISION.md file used to triage…
- [Emil Kowalski /animate-expo skill for React Native motion](../../items/x-2090031918523842766/card.md) — tool — Emil Kowalski releases /animate-expo, porting animations.dev knowledge to React Native and Expo—covering gestures, sheets, haptics, and…
- [Endorsement of Leonxlnx unlazy agent skill for design output](../../items/x-2091125349308399923/card.md) — tool, claim-source — 0x3b33 endorses the Leonxlnx/unlazy GitHub agent skill, saying its quality is not obvious until you try it — same repo referenced in an…
- [michaelmicasso /have-some-range skill for varied color palettes](../../items/x-2091865940581638285/card.md) — tool, example — Michael Micasso announces the /have-some-range slash-command skill via a demo video showing four distinct pixel-art UI themes in red,…
- [Refero styles.refero.design: 2000+ DESIGN.md files for coding agents](../../items/x-2091934379648110784/card.md) — tool, reference — ImranUxi promotes styles.refero.design as a library of 2000+ DESIGN.md files extracted from real product sites with colors, type,…
- [avoid-ai-writing CLI audits and rewrites AI prose patterns](../../items/x-2092656414351118647/card.md) — tool — GitHub tool avoid-ai-writing scans text for AI writing patterns and rewrites flagged passages in place—positioned as an anti-slop prose…
- [Ruben Hassid anti-AI-slop Claude skills pack at claude-skills.free](../../items/x-2093654908322951447/card.md) — tool, technique — Ruben Hassid lists 12 common AI writing tells and promotes eleven free Claude skills (/writer, /editor, /ban-the-AI-words, etc.)…
- [Refero DESIGN.md library — 2000+ product design languages for agents](../../items/x-2093766772029559077/card.md) — tool, reference — X post promoting styles.refero.design: over 2000 DESIGN.md files encoding colors, typography, spacing, and component rules from products…
- [motionsites.ai library of 590+ anti-slop website animation prompts](../../items/x-2094009989220430084/card.md) — tool, reference — viktoroddy promotes motionsites.ai with 590+ animation website prompts filterable by tone, copy-paste into Claude/Cursor/v0, interactive…
- [Taste Skill: open-source design-taste pack for coding agents (Spanish promo)](../../items/x-2094069236524061059/card.md) — tool, technique — Spanish-language promo for Leonxlnx/taste-skill: an open-source agent skill that forces layout, hierarchy, spacing, typography, and…
- [AIDesigner MCP clones site HTML and CSS into Claude Code projects](../../items/x-2094467179320119498/card.md) — tool, example — Spanish promo of a Claude Code demo using AIDesigner MCP to analyze page HTML/CSS and clone or inspire layouts from live URLs such as…

First role `technique` (4):
- [Opale UI essay: encoding personal design taste into agent skills](../../items/web-opale-ui-taste/card.md) — technique, reference — Opale UI blog essay arguing developers should encode their own likes and dislikes into SKILL.md files and persona prompts instead of…
- [Google dev-docs voice prompt to strip LLM slop from technical prose](../../items/x-2087346803268260043/card.md) — technique, claim-source — Aaron Villalpando shares a one-line style constraint—Google developer-docs dead prose, no aphorisms—that rewrites marketing-flourish…
- [Google Developer Docs style guide as agent writing skill](../../items/x-2089457435459404093/card.md) — technique, reference — Nate Jones recommends wrapping Google's Developer Docs Style Guide as an agent skill to replace Claude-lish prose, claiming it beats an…
- [Fable 5.1 scroll-scrubbed coffee hero prompt for LAOUNGE brand](../../items/x-2095482056180638142/card.md) — technique, example — Prompt drop for Fable 5.1 building a LAOUNGE coffee brand scroll-scrubbed hero where background video seeks with scroll and a giant…

First role `example` (2):
- [Aura.build hosted AI landing builder with HTML/Figma export](../../items/web-aura-build/card.md) — example, reference — Commercial SPA AI website builder that generates landing pages from prompts and exports to HTML and Figma; capture is meta-only because…
- [Claude Fable 5.1 praised for one-shot website generation quality](../../items/x-2095549461737111905/card.md) — example, claim-source — Designer @viktoroddy argues Claude Fable 5.1 produces the best one-shot website outputs among AI models tested, with minimal iteration,…

First role `claim-source` (1):
- [Field test: /unlazy skill with Opus 5 plus ponytail combo](../../items/x-2088742864310481025/card.md) — claim-source, tool — LexnLin reports the Leonxlnx/unlazy Cursor skill works well with Opus 5, especially paired with the ponytail write-less-code skill to…

First role `reference` (12):
- [Checklist Design: page-type QA checklists with Figma plugin and agent skill](../../items/web-checklist-design/card.md) — reference, tool — George Hatzis checklist.design offers searchable design checklists for websites, web apps, mobile, design-system components, and flows —…
- [designmd.me — blocked DESIGN.md ecosystem URL stub](../../items/web-designmd-me/card.md) — reference — designmd.me is listed in the DESIGN.md tools thread but capture failed behind a Vercel Security Checkpoint HTTP 429
- [designmd.supply DESIGN.md marketplace (capture blocked)](../../items/web-designmd-supply/card.md) — reference — Suspected DESIGN.md supply marketplace at designmd.supply, named alongside other token extractors; HTTP capture blocked by Vercel…
- [typeui.sh DESIGN.md-adjacent domain (capture blocked)](../../items/web-typeui-sh/card.md) — reference — typeui.sh domain listed in tranmautritam's DESIGN.md ecosystem tweet as likely typography/UI tooling for agents; HTTP and jina captures…
- [Chinese field report: four design skills kept after trials](../../items/x-2086715093707063445/card.md) — reference, claim-source — Chinese-language practitioner shortlist after trialing popular design skills: keep Impeccable, emilkowalski/skills, transitions.dev, and…
- [Agentic UI Showcase gallery of agent-built product interfaces](../../items/x-2086801779358875912/card.md) — reference, example — Launch post for Agentic UI Showcase at agenticui.net/showcase: a curated gallery of product interfaces built with Agentic UI
- [Matt Pocock ten-minute tour of all 25 skills in mattpocock/skills](../../items/x-2088290952704151671/card.md) — reference, example — Matt Pocock recorded a roughly ten-minute overview explaining every skill in his mattpocock/skills repo—25 skills marked…
- [Community ranked top 10 anti-slop writing skills on skills.sh](../../items/x-2090834948332655011/card.md) — reference — Curated X thread ranking ten installable anti-slop skills—stop-slop, no-ai-slop, humanizer variants, unslop, deslop, and…
- [Name That UI: visual dictionary of component names and prompts](../../items/x-2091689598883934666/card.md) — reference, tool — Toolfolio promotes Name That UI, a visual dictionary that names common UI patterns with example prompts so builders can ask for…
- [21-minute GPT-5.6 Sol cinematic web page tutorial (Spanish)](../../items/x-2093583622691283018/card.md) — reference — Spanish-language promo for a 21-minute tutorial on building professional cinematic web pages with GPT-5.6 Sol, step by step
- [designengineer.tools curated index for design-engineer tooling](../../items/x-2093669411685110141/card.md) — reference, tool — Taher Max shares designengineer.tools, a curated collection of tools and resources for design engineers covering designing, prototyping,…
- [Tran Mau Tri Tam roundup of nine DESIGN.md sources for coding agents](../../items/x-2095078647652917329/card.md) — reference — Designer Tran Mau Tri Tam lists nine DESIGN.md generator or catalog sites—Refero, designmd.me, open-design.ai, designmd.supply,…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Emil Kowalski agent skills pack for animation and UI craft](../../items/github-emilkowalski-skills/card.md)
- [Opale UI essay: encoding personal design taste into agent skills](../../items/web-opale-ui-taste/card.md)
- [Impeccable 4.1 release — critique, native review, live mode fixes](../../items/x-2088254428730085690/card.md)
- [Refero DESIGN.md library — 2000+ product design languages for agents](../../items/x-2093766772029559077/card.md)

Secondary membership (31), not in the primary count:
- [AntV Infographic: AI-tuned SVG infographic framework with agent skills](../../items/github-antvis-infographic/card.md) — primary `infographics-diagrams`
- [Diagram Design: 39 editorial HTML+SVG diagram types for agents](../../items/github-cathrynlavery-diagram-design/card.md) — primary `infographics-diagrams`
- [scroll-craft: Claude Code skill for scroll-driven landing QA](../../items/github-nateherkai-scroll-craft/card.md) — primary `landing-ui-motion`
- [nexu-io/html-video: agent-driven HTML/CSS to local MP4](../../items/github-nexu-io-html-video/card.md) — primary `code-motion-graphics`
- [motion-anything: chat-native motion engine with 403 recipes and Lottie/MP4 export](../../items/github-nexu-io-motion-anything/card.md) — primary `code-motion-graphics`
- [GPT Image 2 prompt gallery, agent skill, and CLI](../../items/github-wuyoscar-gpt-image2-skill/card.md) — primary `image-prompt-galleries`
- [YouMind Nano Banana Pro prompt recommender skill (10k+ prompts)](../../items/github-youmind-openlab-nano-banana-pro-prompts/card.md) — primary `image-prompt-galleries`
- [Cult UI: shadcn components plus 92+ AI SDK agent patterns](../../items/web-cult-ui/card.md) — primary `landing-ui-motion`
- [GetLayers AI prompt library for cinematic WebGL heroes and MCP assembly](../../items/web-getlayers-ai/card.md) — primary `web-3d-scenes`
- [MeiGen: cross-model prompt gallery with MCP for GPT Image, Seedance, Nano Banana](../../items/web-meigen-ai/card.md) — primary `image-prompt-galleries`
- [RoundtableSpace free 1-hour Claude interactive 3D web course](../../items/x-2086599657925329347/card.md) — primary `web-3d-scenes`
- [Pocock /improve-codebase-architecture skill after blind vibe-coding](../../items/x-2086838432102228008/card.md) — primary `agent-harness-loops`
- [Pi AGENTS.md grill workflow with four taste skills and /handoff at 100k](../../items/x-2087263510090874911/card.md) — primary `agent-harness-loops`
- [Pretty-Mermaid Skills: Mermaid to SVG or ASCII without a browser DOM](../../items/x-2087329201451855933/card.md) — primary `infographics-diagrams`
- [ReactBits Pro: restyle motion primitives instead of inventing from scratch](../../items/x-2087812720762425743/card.md) — primary `landing-ui-motion`
- [OpenSCAD homelab rack via Cursor plan mode and grill-me skill](../../items/x-2088252062454751483/card.md) — primary `ai-cad-hardware`
- [Meng To tutorial pointer — Three.js landing pages with Claude Code and Opus 5](../../items/x-2088265078919282836/card.md) — primary `web-3d-scenes`
- [AICSS.dev — agent-chat UI components for thinking, tools, and streaming](../../items/x-2089182103153897532/card.md) — primary `landing-ui-motion`
- [Curated list of animated UI kits plus Agentation for agent UI markup](../../items/x-2089263766428950683/card.md) — primary `landing-ui-motion`
- [Emil Kowalski markdown graphs with one vibrant accent color](../../items/x-2089372767934115883/card.md) — primary `infographics-diagrams`
- … 11 more in items.jsonl

## design-agent-skills — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [design-md-contract](../../techniques/design-md-contract.md) — A DESIGN.md (or Vision.md) file that compiles taste into a checkable contract.
- [anti-slop-ui-skills](../../techniques/anti-slop-ui-skills.md) — Banned words, AI-tell lists, and token lint so the agent cannot emit generic UI copy or layout.
- [taste-skill-encoding](../../techniques/taste-skill-encoding.md) — Installable taste/Impeccable/MengTo skills that change defaults, not just prompts.
- [url-clone-ui](../../techniques/url-clone-ui.md) — Clone or extract a live URL into a design contract or component restyle.
- [prompt-to-html-landing](../../techniques/prompt-to-html-landing.md) — A named prompt or pattern that emits a full landing page in HTML/React.
- [remotion-code-video](../../techniques/remotion-code-video.md) — The timeline is code (Remotion, html-video, Motion Prompt), not a GUI project file.
- [screenshot-verify-loop](../../techniques/screenshot-verify-loop.md) — Render, screenshot, and score the page before the agent calls the work done.
- [shadcn-component-kit](../../techniques/shadcn-component-kit.md) — Install or copy shadcn-compatible components and keep naming stable for agents.
- [scroll-driven-3d](../../techniques/scroll-driven-3d.md) — A Three.js/WebGPU scene where scroll or pointer is the camera rig.
- [parallax-scroll-landing](../../techniques/parallax-scroll-landing.md) — 2D scroll-driven sections, blur reveals, and word-focus — not a 3D world.

## design-agent-skills — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [google-design-md-cli](../../tools/google-design-md-cli.md)
- [better-interface](../../tools/better-interface.md)
- [better-accessibility](../../tools/better-accessibility.md)
- [taste-skill](../../tools/taste-skill.md)
- [mengto-skills](../../tools/mengto-skills.md)
- [open-design](../../tools/open-design.md)
- [hyperframes](../../tools/hyperframes.md)
- [impeccable](../../tools/impeccable.md)
- [aidesigner-mcp](../../tools/aidesigner-mcp.md)
- [aidesigner-agent-skills](../../tools/aidesigner-agent-skills.md)
- [checklist-design](../../tools/checklist-design.md)
- [getdesign-md](../../tools/getdesign-md.md)
- [neuform](../../tools/neuform.md)
- [sokosumi-design-md](../../tools/sokosumi-design-md.md)
- [refero-mcp](../../tools/refero-mcp.md)
- [human-review](../../tools/human-review.md)
- [gsap-skills](../../tools/gsap-skills.md)
- [bro-skill](../../tools/bro-skill.md)
- [vision-skill](../../tools/vision-skill.md)
- [unlazy](../../tools/unlazy.md)
- [name-that-ui](../../tools/name-that-ui.md)
- [have-some-range](../../tools/have-some-range.md)
- [styles-refero-design](../../tools/styles-refero-design.md)
- [avoid-ai-writing](../../tools/avoid-ai-writing.md)
- [claude-skills-free](../../tools/claude-skills-free.md)
- [motionsites-ai](../../tools/motionsites-ai.md)
- [fable](../../tools/fable.md)

## design-agent-skills — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-emilkowalski-skills#c1` | Skills list typical agent mistakes like wrong easing and solid borders instead of shadows. | stated | [Emil Kowalski agent skills pack for a…](../../items/github-emilkowalski-skills/card.md) |
| `github-emilkowalski-skills#c2` | Install via npx skills@latest add emilkowalski/skills. | demonstrated | [Emil Kowalski agent skills pack for a…](../../items/github-emilkowalski-skills/card.md) |
| `github-google-labs-code-design-md#c1` | DESIGN.md combines YAML front matter tokens with markdown prose so agents get exact values and application rationale. | stated | [Google Labs DESIGN.md spec with lint …](../../items/github-google-labs-code-design-md/card.md) |
| `github-google-labs-code-design-md#c2` | CLI supports lint for WCAG contrast and token validation plus diff to compare design system versions. | stated | [Google Labs DESIGN.md spec with lint …](../../items/github-google-labs-code-design-md/card.md) |
| `github-jakubkrehel-skills#c1` | better-interface runs a combined review across the better-* specialist skills. | stated | [interfaces.dev better-* agent skills …](../../items/github-jakubkrehel-skills/card.md) |
| `github-jakubkrehel-skills#c2` | Install command is npx skills add jakubkrehel/skills. | stated | [interfaces.dev better-* agent skills …](../../items/github-jakubkrehel-skills/card.md) |
| `github-leonxlnx-taste-skill#c1` | The repo ships portable Agent Skills that improve layout, typography, motion, and spacing on AI-built interfaces. | stated | [Leonxlnx Taste Skill: portable anti-s…](../../items/github-leonxlnx-taste-skill/card.md) |
| `github-leonxlnx-taste-skill#c2` | Image-generation skills produce reference boards meant to hand off mood and direction to coding agents. | stated | [Leonxlnx Taste Skill: portable anti-s…](../../items/github-leonxlnx-taste-skill/card.md) |
| `github-mengto-skills#c1` | Video to Super Prompt turns a screen recording into a detailed HTML recreation prompt. | stated | [MengTo Skills: capture-to-prompt agen…](../../items/github-mengto-skills/card.md) |
| `github-mengto-skills#c2` | Stitched Full Page Capture grabs a whole landing page reference, not just the hero. | stated | [MengTo Skills: capture-to-prompt agen…](../../items/github-mengto-skills/card.md) |
| `github-nexu-io-open-design#c1` | Marketed as the open-source Claude Design alternative with a discover-brief-lock-critique-deliver agent loop. | stated | [OpenDesign: local-first open-source a…](../../items/github-nexu-io-open-design/card.md) |
| `github-nexu-io-open-design#c2` | Supports Claude Code, Codex, Cursor, DeepSeek Harness, and 26+ CLIs via BYOK with six artifact types and live iframe … | stated | [OpenDesign: local-first open-source a…](../../items/github-nexu-io-open-design/card.md) |
| `github-pbakaus-impeccable#c1` | Install via npx impeccable install then /impeccable init writes PRODUCT.md for audience and voice apart from DESIGN.m… | stated | [Impeccable: agent design skill with P…](../../items/github-pbakaus-impeccable/card.md) |
| `github-pbakaus-impeccable#c2` | 61 deterministic detector rules flag Inter-everywhere, purple-blue gradients, and card-in-card patterns without calli… | stated | [Impeccable: agent design skill with P…](../../items/github-pbakaus-impeccable/card.md) |
| `web-aidesigner-mcp#c1` | AIDesigner exposes 21 MCP tools for design generation, refinement, brand kits, and editor sessions. | stated | [AIDesigner remote MCP for in-repo HTM…](../../items/web-aidesigner-mcp/card.md) |

Full set: claims.jsonl (136 rows)

## design-agent-skills — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- installable skill vs prompt dump
- DESIGN.md or equivalent contract present
- anti-slop rules are checkable
- visual verify loop (screenshot/browser)
- changes agent output on a real page

## design-agent-skills — thread coverage

X items in primary roster: 29. captured_full=0, captured_partial=28, empty=0, failed=1.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2085006701984698712](../../items/x-2085006701984698712/thread.md) | captured_partial | 73 | 3 | 3 |
| [x-2086715093707063445](../../items/x-2086715093707063445/thread.md) | captured_partial | 3 | 1 | 1 |
| [x-2086801779358875912](../../items/x-2086801779358875912/thread.md) | captured_partial | 33 | 3 | 2 |
| [x-2086845465140842638](../../items/x-2086845465140842638/thread.md) | captured_partial | 8 | 3 | 0 |
| [x-2087346803268260043](../../items/x-2087346803268260043/thread.md) | captured_partial | 21 | 3 | 1 |
| [x-2087656088124719304](../../items/x-2087656088124719304/thread.md) | captured_partial | 38 | 1 | 0 |
| [x-2087708050002239702](../../items/x-2087708050002239702/thread.md) | captured_partial | 6 | 3 | 1 |
| [x-2088254428730085690](../../items/x-2088254428730085690/thread.md) | captured_partial | 11 | 3 | 2 |
| [x-2088290952704151671](../../items/x-2088290952704151671/thread.md) | captured_partial | 85 | 1 | 1 |
| [x-2088742864310481025](../../items/x-2088742864310481025/thread.md) | captured_partial | 21 | 3 | 1 |
| [x-2089189790881382676](../../items/x-2089189790881382676/thread.md) | captured_partial | 37 | 3 | 2 |
| [x-2089457435459404093](../../items/x-2089457435459404093/thread.md) | captured_partial | 114 | 1 | 1 |
| [x-2090031918523842766](../../items/x-2090031918523842766/thread.md) | captured_partial | 53 | 1 | 1 |
| [x-2090834948332655011](../../items/x-2090834948332655011/thread.md) | captured_partial | 56 | 1 | 1 |
| [x-2091125349308399923](../../items/x-2091125349308399923/thread.md) | captured_partial | 4 | 3 | 2 |
| [x-2091689598883934666](../../items/x-2091689598883934666/thread.md) | captured_partial | 6 | 1 | 1 |
| [x-2091865940581638285](../../items/x-2091865940581638285/thread.md) | captured_partial | 10 | 3 | 0 |
| [x-2091934379648110784](../../items/x-2091934379648110784/thread.md) | captured_partial | 22 | 3 | 1 |
| [x-2092656414351118647](../../items/x-2092656414351118647/thread.md) | captured_partial | 5 | 3 | 2 |
| [x-2093583622691283018](../../items/x-2093583622691283018/thread.md) | captured_partial | 70 | 2 | 1 |
| [x-2093654908322951447](../../items/x-2093654908322951447/thread.md) | captured_partial | 73 | 3 | 2 |
| [x-2093669411685110141](../../items/x-2093669411685110141/thread.md) | failed | 1 | 0 | 0 |
| [x-2093766772029559077](../../items/x-2093766772029559077/thread.md) | captured_partial | 28 | 3 | 2 |
| [x-2094009989220430084](../../items/x-2094009989220430084/thread.md) | captured_partial | 19 | 2 | 2 |
| [x-2094069236524061059](../../items/x-2094069236524061059/thread.md) | captured_partial | 20 | 1 | 0 |
| … | 4 more X items | — | — | — |

## design-agent-skills — gaps and open questions

Primary readiness: ready=14, ready-with-gaps=36. Gap tags: linked-page-unfetched=8, thread-partial=8, translation-needed=2, thread-failed=2.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which DESIGN.md extractors survive a real client site, not a blog template?
- Do anti-slop lists change layout or only copy?

If this subject drops below 6 primary items after a future reclass, merge it into `landing-ui-motion` and delete the folder.

## design-agent-skills — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [landing-ui-motion](../landing-ui-motion/brief.md)
- [image-prompt-galleries](../image-prompt-galleries/brief.md)
- [agent-harness-loops](../agent-harness-loops/brief.md)

