# Design

Topic slug: `design`. DESIGN.md as an agent contract, vibe-design workspaces, landing builders, UI kits, taste/checklists, and infographics treated as design artifacts. Many items also carry `ui-motion`, `agent-skills`, or `three-js` — use those lanes when the question is specifically motion, skill install, or WebGL.

This slice is the visual-language layer for coding agents. One cluster is **DESIGN.md**: Google Labs’ spec (YAML tokens + rationale prose), catalogs of extracted systems, generators, and MCP that clone a URL into repo-aware UI. Another is **anti-slop skill packs** (Impeccable, Taste, Emil Kowalski, interfaces.dev) that encode layout, type, motion, and refuse-lists so agents stop shipping Inter + purple gradients. A third is **builders and kits** that consume those contracts: OpenDesign, Aura, Neuform, Cult UI, SceneAI prompts, GetLayers cinematic layers.

Query here for brand tokens, landing-page direction, checklist QA, or “make it not look like AI.” For scroll timelines and Lottie pipelines go to [`ui-motion`](ui-motion.md). For in-browser 3D scenes go to [`three-js`](three-js.md). For installable skill plumbing go to [`agent-skills`](agent-skills.md). Presence in this file is not a recommendation.

## Pipelines

- **DESIGN.md as contract** — tokens + rationale in-repo; lint/diff; agent reads it before generating UI (`github-google-labs-code-design-md`, `web-getdesign-md`, `web-sokosumi-design-md`).
- **Extract then lock** — scrape a live site into DESIGN.md (Hyperbrowser, Refero, getdesign.md catalogs) or clone HTML/CSS via AIDesigner MCP, then treat the file as source of truth (`web-design-md-hyperbrowser`, `web-aidesigner-mcp`, `x-2095078647652917329`).
- **Skill-pack polish** — init PRODUCT.md / DESIGN.md, then `/critique` `/polish` `/animate` or Taste/Emil skills instead of restyling from scratch (`github-pbakaus-impeccable`, `github-leonxlnx-taste-skill`, `github-emilkowalski-skills`).
- **Vibe-design workspace** — conversational studio (OpenDesign) or prompt-to-HTML builders (Aura, Neuform) that export files + reusable DESIGN.md (`github-nexu-io-open-design`, `web-open-design-ai`, `web-neuform-ai`).
- **Prompt-as-layer** — copy a self-contained HTML prompt (GetLayers, SceneAI) rather than describing a hero from scratch (`web-getlayers-ai`, `web-sceneai-art`).

## Tools

- [DESIGN.md](../../raw/items/github-google-labs-code-design-md/) — `github-google-labs-code-design-md` — format spec, `npx @google/design.md lint` / `diff`.
- [getdesign.md](../../raw/items/web-getdesign-md/) — `web-getdesign-md` — 550+ site analyses as paste-ready DESIGN.md.
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design` — local-first vibe-design app; site twin `web-open-design-ai`.
- [AIDesigner MCP](../../raw/items/web-aidesigner-mcp/) — `web-aidesigner-mcp` — clone / enhance / inspire a URL inside the editor (thread: `x-2094467179320119498`).
- [Checklist Design](../../raw/items/web-checklist-design/) — `web-checklist-design` — page/flow/system checklists as web, Figma, and agent skill.
- [Cult UI](../../raw/items/web-cult-ui/) — `web-cult-ui` — copy-paste Tailwind/shadcn components plus AI-SDK agent patterns.
- [Neuform](../../raw/items/web-neuform-ai/) — `web-neuform-ai` — prompt → HTML landing + remixable DESIGN.md.
- [Aura](../../raw/items/web-aura-build/) — `web-aura-build` — prompt landing builder, HTML/Figma export.
- [DiceBear](../../raw/items/web-dicebear/) — `web-dicebear` — deterministic avatars/API; used for daily-seeded decorative assets.
- [AntV Infographic](../../raw/items/github-antvis-infographic/) — `github-antvis-infographic` — chart-as-design; also tagged `infographics`.

## Techniques

- [Impeccable](../../raw/items/github-pbakaus-impeccable/) — `github-pbakaus-impeccable` — PRODUCT.md + DESIGN.md + 61 detectors; `/craft` `/critique` `/live`.
- [Taste Skill](../../raw/items/github-leonxlnx-taste-skill/) — `github-leonxlnx-taste-skill` — portable anti-slop skills (layout, type, motion, reference boards).
- [Skills For Designers and Engineers](../../raw/items/github-emilkowalski-skills/) — `github-emilkowalski-skills` — animation vocabulary, easing mistakes, `emil-design-eng`.
- [interfaces.dev Skills](../../raw/items/github-jakubkrehel-skills/) — `github-jakubkrehel-skills` — better-ui / type / color / a11y / layout review.
- [A Developer's Guide to Taste in the Age of AI](../../raw/items/web-opale-ui-taste/) — `web-opale-ui-taste` — encode hates/loves into skill files; do not download generic taste.
- [DESIGNMD — Hyperbrowser](../../raw/items/web-design-md-hyperbrowser/) — `web-design-md-hyperbrowser` — extract DESIGN.md from a live URL.
- [Best websites to get DESIGN.md](../../raw/items/x-2095078647652917329/) — `x-2095078647652917329` — roundup of catalogs/builders (Refero, designmd.me/supply, typeui.sh, …).
- [SceneAI](../../raw/items/web-sceneai-art/) — `web-sceneai-art` — copy-paste prompts for hero/landing sections.

## Examples

- [Utsubo](../../raw/items/web-utsubo/) — `web-utsubo` — studio-grade immersive scroll/3D brand site (also `three-js`, `bess-3d-flythrough`).
- [ORYZO AI](../../raw/items/web-oryzo-ai/) — `web-oryzo-ai` — Lusion craft applied to AI-landing satire; high-production 3D tropes.
- [Ballon Bleu de Cartier](../../raw/items/web-cartier-ballon-bleu/) — `web-cartier-ballon-bleu` — luxury PDP: fit, engraving, animated user guide.
- [Swiss grids / Neo Industrialism](../../raw/items/x-2095123902947090682/) — `x-2095123902947090682` — industrial HUD overlay mock (FROM ABOVE TO AHEAD).
- [How we built the blume.codes landing page](../../raw/items/x-2094524951025914278/) — `x-2094524951025914278` — parallax layers + live product embed + DiceBear vine (also `ui-motion`).
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai` — cinematic section/background/3D scene prompts.
- [FeralUI](../../raw/items/web-feralui-dev/) — `web-feralui-dev` — physically-inspired components (swing, crumple, hologram).
- [Recent — Design Inspiration](../../raw/items/web-recent-design/) — `web-recent-design` — motion/web masonry feed for references.

## All items

<!-- AUTO:ITEMS -->
- [AntV Infographic](../../raw/items/github-antvis-infographic/) — `github-antvis-infographic`
- [Diagram Design](../../raw/items/github-cathrynlavery-diagram-design/) — `github-cathrynlavery-diagram-design`
- [QRFerry (qr-data-transfer)](../../raw/items/github-deedy-qr-data-transfer/) — `github-deedy-qr-data-transfer`
- [Skills For Designers and Engineers](../../raw/items/github-emilkowalski-skills/) — `github-emilkowalski-skills`
- [DESIGN.md](../../raw/items/github-google-labs-code-design-md/) — `github-google-labs-code-design-md`
- [interfaces.dev Skills](../../raw/items/github-jakubkrehel-skills/) — `github-jakubkrehel-skills`
- [Taste Skill](../../raw/items/github-leonxlnx-taste-skill/) — `github-leonxlnx-taste-skill`
- [The Complete Shelf](../../raw/items/github-mengto-complete-shelf/) — `github-mengto-complete-shelf`
- [Agent Skills (MengTo)](../../raw/items/github-mengto-skills/) — `github-mengto-skills`
- [scroll-craft](../../raw/items/github-nateherkai-scroll-craft/) — `github-nateherkai-scroll-craft`
- [motion-anything](../../raw/items/github-nexu-io-motion-anything/) — `github-nexu-io-motion-anything`
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design`
- [Impeccable](../../raw/items/github-pbakaus-impeccable/) — `github-pbakaus-impeccable`
- [awesome](../../raw/items/github-sindresorhus-awesome/) — `github-sindresorhus-awesome`
- [GPT Image 2 Prompt Gallery + Agentic Skill + CLI](../../raw/items/github-wuyoscar-gpt-image2-skill/) — `github-wuyoscar-gpt-image2-skill`
- [Nano Banana Pro Prompts Recommend Skill](../../raw/items/github-youmind-openlab-nano-banana-pro-prompts/) — `github-youmind-openlab-nano-banana-pro-prompts`
- [AIDesigner MCP — AI UI design in the editor](../../raw/items/web-aidesigner-mcp/) — `web-aidesigner-mcp`
- [animos — Motion templates for design showcases](../../raw/items/web-animos-editor/) — `web-animos-editor`
- [Aura — AI Website Builder](../../raw/items/web-aura-build/) — `web-aura-build`
- [Ballon Bleu de Cartier watch CRWSBB0049](../../raw/items/web-cartier-ballon-bleu/) — `web-cartier-ballon-bleu`
- [Checklist Design — Check every detail, ship better work](../../raw/items/web-checklist-design/) — `web-checklist-design`
- [Cult UI](../../raw/items/web-cult-ui/) — `web-cult-ui`
- [DESIGNMD — Hyperbrowser DESIGN.md Extractor](../../raw/items/web-design-md-hyperbrowser/) — `web-design-md-hyperbrowser`
- [designmd.me](../../raw/items/web-designmd-me/) — `web-designmd-me`
- [designmd.supply](../../raw/items/web-designmd-supply/) — `web-designmd-supply`
- [DiceBear — open source avatar library & API](../../raw/items/web-dicebear/) — `web-dicebear`
- [FeralUI](../../raw/items/web-feralui-dev/) — `web-feralui-dev`
- [Flowmapp — Website Planning Tool](../../raw/items/web-flowmapp/) — `web-flowmapp`
- [getdesign.md — DESIGN.md Collection for AI Coding Agents](../../raw/items/web-getdesign-md/) — `web-getdesign-md`
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai`
- [LottieFiles](../../raw/items/web-lottiefiles/) — `web-lottiefiles`
- [MeiGen — Free GPT Image 2, Nano Banana & Seedance Prompts](../../raw/items/web-meigen-ai/) — `web-meigen-ai`
- [Neuform — AI HTML Landing Page Builder](../../raw/items/web-neuform-ai/) — `web-neuform-ai`
- [A Developer's Guide to Taste in the Age of AI](../../raw/items/web-opale-ui-taste/) — `web-opale-ui-taste`
- [OpenDesign — Open Source Vibe Design Workspace](../../raw/items/web-open-design-ai/) — `web-open-design-ai`
- [Originkit](../../raw/items/web-originkit-dev/) — `web-originkit-dev`
- [ORYZO AI](../../raw/items/web-oryzo-ai/) — `web-oryzo-ai`
- [Recent — Design Inspiration](../../raw/items/web-recent-design/) — `web-recent-design`
- [SceneAI — UI Prompt Library](../../raw/items/web-sceneai-art/) — `web-sceneai-art`
- [Sokosumi — Free DESIGN.md Generator](../../raw/items/web-sokosumi-design-md/) — `web-sokosumi-design-md`
- [Refero Styles — DESIGN.md Examples for AI Agents](../../raw/items/web-styles-refero-design/) — `web-styles-refero-design`
- [TinyShots — macOS screenshot polish app](../../raw/items/web-tinyshots/) — `web-tinyshots`
- [typeui.sh](../../raw/items/web-typeui-sh/) — `web-typeui-sh`
- [Utsubo](../../raw/items/web-utsubo/) — `web-utsubo`
- [Vengeance UI](../../raw/items/web-vengence-ui/) — `web-vengence-ui`
- [I'm working on a one-click AI-generated texturing feature for 3D models. I render the model from four sides and project ](../../raw/items/x-2057113327508345047/) — `x-2057113327508345047`
- [My last open-source skill, /no-ai-slop, clearly hit a nerve with 4K GitHub stars. Today, I’m introducing /human-review, ](../../raw/items/x-2085006701984698712/) — `x-2085006701984698712`
- [Day 15 of the dream game build (yeah I know the real count is higher, but this is update #15) 🚀 I finally figured out ho](../../raw/items/x-2086537093120164177/) — `x-2086537093120164177`
- [Claude can now build 3D websites and most people still don't know how. This free 1-hour course covers interactive 3D exp](../../raw/items/x-2086599657925329347/) — `x-2086599657925329347`
- [在试用了大部分热门的设计 SKILL 之后，最终我只留下这 4 个： 1. Impeccable http://impeccable.style 2. Skills for Design Engineers http://github.co](../../raw/items/x-2086715093707063445/) — `x-2086715093707063445`
- [Introducing ... 🥁 "Agentic UI Showcase" https://agenticui.net/showcase A collection of best product interfaces made with](../../raw/items/x-2086801779358875912/) — `x-2086801779358875912`
- [/bro is my new favorite skill. before | after https://github.com/luchasarie/bro-skill](../../raw/items/x-2086845465140842638/) — `x-2086845465140842638`
- [My workflow now is basically this: 1. AGENTS.md auto loads up these 4 skills: ponytail grilling wayfinder ask-matt 2. I ](../../raw/items/x-2087263510090874911/) — `x-2087263510090874911`
- [Hardware design is having its Chat GPT moment. Typed one prompt. CadXStudio generated this full parametric bookshelf spe](../../raw/items/x-2087272209429766596/) — `x-2087272209429766596`
- [Pretty-Mermaid Skills renders Mermaid diagrams as beautiful SVGs or ASCII art with zero DOM dependencies. https://github](../../raw/items/x-2087329201451855933/) — `x-2087329201451855933`
- [Slop writing is mostly solved "Can you make it like google dev docs style. More dead prose. No aphorisms, no flourishes.](../../raw/items/x-2087346803268260043/) — `x-2087346803268260043`
- [Introducing pdfcn 📄 by @shadcnlabs > Built on Takumi by @kanewang_ and Forme > Zero config, one command setup. > @shadcn](../../raw/items/x-2087656088124719304/) — `x-2087656088124719304`
- [Orca has a design mode: draw and annotate right on your site, then send that feedback to any AI agent. Drop the site you](../../raw/items/x-2087708050002239702/) — `x-2087708050002239702`
- [One component, 10 examples. https://pro.reactbits.dev components do 90% of the work: motion, structure, customization. T](../../raw/items/x-2087812720762425743/) — `x-2087812720762425743`
- [Homieeee... This feels like finding a shovel during a gold rush. 🌋 A stunning collection of UI components built specific](../../raw/items/x-2087832615797833807/) — `x-2087832615797833807`
- [i've started having claude turn my codebases into visual diagrams so i can discuss the codebases with claude more easily](../../raw/items/x-2088016749849682120/) — `x-2088016749849682120`
- [claude dropped Motion Prompt, and the crazy part is this entire animation was made with code, not AI-generated images or](../../raw/items/x-2088155107544191339/) — `x-2088155107544191339`
- [Impeccable 4.1 is here: core: -critique results more reliably prints in chat before asking you questions - the design ho](../../raw/items/x-2088254428730085690/) — `x-2088254428730085690`
- [This is a really useful tutorial if you want to learn how to build more advanced Three.js landing pages with Claude Code](../../raw/items/x-2088265078919282836/) — `x-2088265078919282836`
- [I heavily use diagraming tools for architecting which means a lot of screenshotting and pasting. To make things simpler,](../../raw/items/x-2088590355440476343/) — `x-2088590355440476343`
- [Introducing Mono Charts. A collection of minimal, animated chart components for React. Now you can add beautiful, intera](../../raw/items/x-2088599468698751328/) — `x-2088599468698751328`
- [okay I tested /unlazy more with Opus 5 and I'm ngl it's really good Sol, Fable and I cooked lol try it here! https://git](../../raw/items/x-2088742864310481025/) — `x-2088742864310481025`
- [wtf this is sick https://www.aicss.dev/](../../raw/items/x-2089182103153897532/) — `x-2089182103153897532`
- [i didn't tell anyone about this repo but it kept getting stars 😂 so i guess it's time to share it introducing /vision. i](../../raw/items/x-2089189790881382676/) — `x-2089189790881382676`
- [30｜带物理摆动感的作品集 Carousel 来自@YousufSoomroDev 一个用于作品集展示的 Carousel 组件。切换项目时，卡片不是沿着水平轨道简单滑入，而是带着明显的摆动和惯性从画面外进入，最终回到稳定位置。作者同时将这](../../raw/items/x-2089223944700326052/) — `x-2089223944700326052`
- [The best UI components ready to use, save this 👇 - http://originkit.dev free animated component library - http://orbs.ja](../../raw/items/x-2089263766428950683/) — `x-2089263766428950683`
- [Currently I’m really into markdown graphs with one vibrant accent color](../../raw/items/x-2089372767934115883/) — `x-2089372767934115883`
- [PSA: If you are tired of Claude-lish or Chat-lish, tell your AI to read the Google Developer Docs Style Guide and build ](../../raw/items/x-2089457435459404093/) — `x-2089457435459404093`
- [iCraft Editor designs 3D network architecture diagrams with immersive visual effects. https://github.com/gantFDT/icraft](../../raw/items/x-2089570022490263586/) — `x-2089570022490263586`
- [The craziest font website ever https://departuremono.com](../../raw/items/x-2089618415493218381/) — `x-2089618415493218381`
- [Straight from the team: From prompt to a fully designed Screwdriver all in https://cadxstudio.in #TextToCAD #CAD](../../raw/items/x-2089717063921332378/) — `x-2089717063921332378`
- [Whatttt this existed, why no one showed me this yet, https://23rd.dev](../../raw/items/x-2089740155179643231/) — `x-2089740155179643231`
- [Animated in Higgsfield Seedance 2.5 + Cursor Composer 2.5 AI Skill: https://github.com/elayadesign/ai-design-skills](../../raw/items/x-2089770081459056765/) — `x-2089770081459056765`
- [Grind Log #044 - 18 August 2026 - Solved LeetCode: 268, 1656, 3043. - Added 3 new components to https://great-ui.com : h](../../raw/items/x-2089775679600812150/) — `x-2089775679600812150`
- [New skill: /animate-expo All the animation knowledge, but for your native apps. React Native and Expo: gestures, sheets,](../../raw/items/x-2090031918523842766/) — `x-2090031918523842766`
- [Another design direction for this AI SaaS. built by Custom Skills + My Video Tool + Claude + Some Creativity](../../raw/items/x-2090079734571098131/) — `x-2090079734571098131`
- [wow spline is so back if anything disrupts the big 3d softwares, it'll be spline](../../raw/items/x-2090526692427104508/) — `x-2090526692427104508`
- [Testing if AI can actually design a wheel hub on CadXStudio. Bolt circle. Drive spline. Brake disc mount. From prompt to](../../raw/items/x-2090535643353153833/) — `x-2090535643353153833`
- [Post got a lot of traction, so I made a rank with the anti-slop skills people need to install. 1. stop-slop - @hvpandya ](../../raw/items/x-2090834948332655011/) — `x-2090834948332655011`
- [You don't know how good this skill is until you try it https://github.com/Leonxlnx/unlazy](../../raw/items/x-2091125349308399923/) — `x-2091125349308399923`
- [We are working on the new animated gradients collection “Dither Animation” It will be live on http://grainient.supply th](../../raw/items/x-2091479075697430784/) — `x-2091479075697430784`
- [system-atlas: a skill that builds an explorable isometric map of your codebase / agent / pipeline from one data file arr](../../raw/items/x-2091559663833924082/) — `x-2091559663833924082`
- [on a quest to create the most beautiful non-vibe-coded-yet-it's-beige-themed website on the internet. 🤝](../../raw/items/x-2091560960066793483/) — `x-2091560960066793483`
- [You can just RL a coding model to paint with javascript btw](../../raw/items/x-2091570990048276897/) — `x-2091570990048276897`
- [Someday I'll return to entertaining "what's necessary?" in design. But right now, I'm only interested in "what's possibl](../../raw/items/x-2091616414063022208/) — `x-2091616414063022208`
- [Weekend project: setting up @bentlegen's http://sideshow.sh to visually understand & interact with my agents' work. This](../../raw/items/x-2091622497393225801/) — `x-2091622497393225801`
- [can you believe that every pixel here is fully editable? this was created with the Motion harness](../../raw/items/x-2091688420695564296/) — `x-2091688420695564296`
- [This site is perfect for Vibecoding It gives you the names of all the common UI + their prompts so you can tell AI to bu](../../raw/items/x-2091689598883934666/) — `x-2091689598883934666`
- [3d model within a website is just so crazy with Claude. I built this template where one 3D scene drives the whole page. ](../../raw/items/x-2091748299975880994/) — `x-2091748299975880994`
- [and it is live; Instagram + LinkedIn carousels open source repo soon available go farm some engagement on Instagram and ](../../raw/items/x-2091767461058105402/) — `x-2091767461058105402`
- [/have-some-range](../../raw/items/x-2091865940581638285/) — `x-2091865940581638285`
- [2,000+ DESIGN.md files from real product sites, colors, type, spacing, components, ready to paste into Cursor, Claude Co](../../raw/items/x-2091934379648110784/) — `x-2091934379648110784`
- [Trending repository of the day 📈 awesome-gpt-image-2 Prompt as Code | Industrial-grade prompt engine and template librar](../../raw/items/x-2092222199620833420/) — `x-2092222199620833420`
- [who made the https://www.doss.com/ website???? idk what an ERP is, but god those illustrations look nice](../../raw/items/x-2092624919653671200/) — `x-2092624919653671200`
- [Polly Pockets, but for gamers: ViscousRealm imagined tiny gaming rooms inside different controllers. Which animation is ](../../raw/items/x-2092644473868050684/) — `x-2092644473868050684`
- [@MiniMaxAgent just shipped H3-based plugins for dynamic images and white-model rendering! Been playing around with them ](../../raw/items/x-2092702228947902622/) — `x-2092702228947902622`
- [made all of these visuals for a random math brand in a few minutes with AI pretty insane that we live in this era](../../raw/items/x-2092890365930131920/) — `x-2092890365930131920`
- [okay yall asked for the prompt under this here's the exact template + a mini tutorial on how to use it for basically any](../../raw/items/x-2092979866836648104/) — `x-2092979866836648104`
- [Releasing my new template - Forja Template for AI agencies, agent studios, and automation companies Check the full websi](../../raw/items/x-2092996828752916622/) — `x-2092996828752916622`
- [You don't need to outbid everyone for attention if your product actually looks good. Here’s a design that proves it](../../raw/items/x-2093024468209733756/) — `x-2093024468209733756`
- [Trending repository of the day 📈 archify Agent skill for beautiful, verifiable architecture, workflow, sequence, data-fl](../../raw/items/x-2093309791120543846/) — `x-2093309791120543846`
- [I can't wait to finally launch this site](../../raw/items/x-2093364419044794836/) — `x-2093364419044794836`
- [BQR is an absolute GAME-CHANGER for hard surface modeling! 🔥Clean quad topology with native modifiers" after booleans? T](../../raw/items/x-2093421870951387625/) — `x-2093421870951387625`
- [Este tipo explica cómo crear páginas web profesionales con GPT-5.6 Sol. Un tutorial de 21 minutos donde explica paso a p](../../raw/items/x-2093583622691283018/) — `x-2093583622691283018`
- [Design Engineers, this one's for you. A curated collection of the best tools and resources for designing, prototyping, a](../../raw/items/x-2093669411685110141/) — `x-2093669411685110141`
- [This launch video got more than 7.5M views. full breakdown:](../../raw/items/x-2093681908227936745/) — `x-2093681908227936745`
- [Someone turned the design language of 2,000+ of the world’s best products into DESIGN.md files that Codex / Claude Code ](../../raw/items/x-2093766772029559077/) — `x-2093766772029559077`
- [Walk into Hogwarts... Built this landing for an AI-based Harry Potter Experience event. Built by Custom Skills + My Vide](../../raw/items/x-2093767075131220005/) — `x-2093767075131220005`
- [Just found https://unive.ai on todays top 3 of https://outbid.lol and I just wanted to give a shoutout to them as their ](../../raw/items/x-2093774183356379560/) — `x-2093774183356379560`
- [🚨 THIS IS INSANE A Claude Code skill just started REFUSING to build websites that look like everyone else’s. Sameness is](../../raw/items/x-2093900284896657841/) — `x-2093900284896657841`
- [You don't need a massive agency budget to build an ultra-premium, interactive finance website. Watch how to build this p](../../raw/items/x-2093915384944414827/) — `x-2093915384944414827`
- [I created the world's best library of AI prompts for websites that don’t look like AI slop. 👇 • 590+ Al Animation Websit](../../raw/items/x-2094009989220430084/) — `x-2094009989220430084`
- [🔴 Los DISEÑOS web que genera tu agente APESTAN Espaciado raro Tipografia generica Gradientes de siempre Ese look de IA q](../../raw/items/x-2094069236524061059/) — `x-2094069236524061059`
- [MCP that clones any site's HTML/CSS for Claude Code (AIDesigner)](../../raw/items/x-2094467179320119498/) — `x-2094467179320119498`
- [How we built the blume.codes landing page (X article)](../../raw/items/x-2094524951025914278/) — `x-2094524951025914278`
- [Atlas Fields Studios — EM fields around PCB designs, free](../../raw/items/x-2094840529997410525/) — `x-2094840529997410525`
- [Atlas + spark.js + three.js scene from one input image](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216`
- [Fable 5.1 website outputs cheaper than Fable 5 — /scroll-craft in replies](../../raw/items/x-2094978216146452971/) — `x-2094978216146452971`
- [Scroll-animated $5k site without writing CSS — ChatGPT + Gemini + Claude Code](../../raw/items/x-2094984529853530345/) — `x-2094984529853530345`
- [How to write LinkedIn lead magnets that get comments](../../raw/items/x-2095060844547592437/) — `x-2095060844547592437`
- [Best websites to get DESIGN.md](../../raw/items/x-2095078647652917329/) — `x-2095078647652917329`
- [Made with @ChatGPT check out https://Imageory.in for prompts](../../raw/items/x-2095085408208196006/) — `x-2095085408208196006`
- [Swiss grids / Neo Industrialism — FROM ABOVE TO AHEAD mock](../../raw/items/x-2095123902947090682/) — `x-2095123902947090682`
- [Hero section design. built by Custom Skills + My Video Tool + Cursor + Client design md file and Some Creativity](../../raw/items/x-2095207624396652956/) — `x-2095207624396652956`
- [❤️‍🔥GPT 5.6 Sol Prompt 👇](../../raw/items/x-2095368133070700884/) — `x-2095368133070700884`
- [Premium design isn’t just about looking good—it’s about making your brand feel valuable before a customer even interacts](../../raw/items/x-2095429087141515616/) — `x-2095429087141515616`
- [❤️‍🔥 GPT 5.6 Sol Prompt 👇](../../raw/items/x-2095451624139567162/) — `x-2095451624139567162`
- [Fabel 5.1 cooked it. Try the prompt yourself👇](../../raw/items/x-2095482056180638142/) — `x-2095482056180638142`
- [I2M 1.2 is Live! 🎉 ✅ Improved Metallics ✅ Improved Roughness ✅ Improved Albedo ✅ Improved Index of Refraction Other gene](../../raw/items/x-2095502642218664004/) — `x-2095502642218664004`
- [Claude Fable 5.1 has given me the best website outputs compared to any AI model One-shots - don't need to spend a lot.](../../raw/items/x-2095549461737111905/) — `x-2095549461737111905`
<!-- /AUTO:ITEMS -->
