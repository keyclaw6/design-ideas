# UI Motion

Topic slug: `ui-motion`. Scroll-driven heroes, parallax, Lottie/motion templates, CSS/JS motion, and marketing-page motion pipelines. Overlaps `design` (same landings) and `agent-skills` (installable motion skills). In-browser 3D motion that is actually a WebGL scene belongs in [`three-js`](three-js.md); camera paths and video models belong in [`camera-control`](camera-control.md) / [`video-generation`](video-generation.md).

Items here are recipes for **time on a page**: scroll as timeline (scroll-craft’s page grammars + Playwright verify), chat-native motion engines (motion-anything recipes → CSS/React/Lottie/MP4), and asset platforms (LottieFiles, animos) when you need a file not a component. Skill packs (Emil, Taste, Impeccable `/animate`) sit alongside component libraries (Originkit, Vengeance UI, Cult UI, GetLayers animated sections) that agents can drop in.

Query this lane for “scroll-animated landing,” “parallax from generated layers,” “Lottie in the hero,” or “agent that won’t write dead CSS animation.” Start with a grammar or recipe, then a verify pass — do not ask a model to invent easing from scratch. Presence is not a recommendation.

## Pipelines

- **Scroll as timeline** — pick one page grammar, require a signature move, screenshot-walk the scroll (`github-nateherkai-scroll-craft`; Fable 5.1 thread `x-2094978216146452971`).
- **Layered parallax from image gen** — multi-layer alpha stills with speed tiers; Codex/Claude + image model (`x-2094524951025914278`, `web-fal-ai` on the video-generation lane).
- **Live product on the marketing page** — same UI package as the app so “screenshots” are the real shell (`x-2094524951025914278`).
- **Chat-native motion** — natural language → recipes/workbench → export JSON/CSS/React/Lottie/MP4 (`github-nexu-io-motion-anything`, OpenDesign HyperFrames).
- **Template/export** — drop media into animos or a Lottie; skip AE when the job is a short showcase loop (`web-animos-editor`, `web-lottiefiles`).
- **Prompted cinematic sections** — copy a GetLayers/SceneAI animated block instead of describing motion in prose (`web-getlayers-ai`).

## Tools

- [scroll-craft](../../raw/items/github-nateherkai-scroll-craft/) — `github-nateherkai-scroll-craft` — Claude plugin: 8 page grammars, fingerprint gate, Playwright scroll verify.
- [motion-anything](../../raw/items/github-nexu-io-motion-anything/) — `github-nexu-io-motion-anything` — 403 recipes, live workbench, Lottie/MP4 export; OpenDesign family.
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design` — HyperFrames / HTML-video motion inside the vibe-design studio.
- [LottieFiles](../../raw/items/web-lottiefiles/) — `web-lottiefiles` — dotLottie library, Motion Copilot, runtimes/CDN.
- [animos](../../raw/items/web-animos-editor/) — `web-animos-editor` — 25 browser templates → MP4/WebM for design showcases.
- [Originkit](../../raw/items/web-originkit-dev/) — `web-originkit-dev` — free animated components + MCP import.
- [Vengeance UI](../../raw/items/web-vengence-ui/) — `web-vengence-ui` — shadcn registry: hover/glow, scroll-driven cards, scene fields.
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai` — animated Sections / WebGL gradients as copy-paste prompts.
- [Agent Skills (MengTo)](../../raw/items/github-mengto-skills/) — `github-mengto-skills` — GSAP/Three.js/web-design capture → prompt workflows.

## Techniques

- [Skills For Designers and Engineers](../../raw/items/github-emilkowalski-skills/) — `github-emilkowalski-skills` — `animate`, `review-animations`, easing/shadow mistakes, animation vocabulary.
- [Taste Skill](../../raw/items/github-leonxlnx-taste-skill/) — `github-leonxlnx-taste-skill` — motion + spacing upgrades for boilerplate UIs.
- [Impeccable](../../raw/items/github-pbakaus-impeccable/) — `github-pbakaus-impeccable` — `/animate` `/bolder` `/quieter` on top of DESIGN.md.
- [Scroll-animated $5k site without writing CSS](../../raw/items/x-2094984529853530345/) — `x-2094984529853530345` — ChatGPT + Gemini + Claude Code chained for a 300-frame scroll.
- [Fable 5.1 + /scroll-craft](../../raw/items/x-2094978216146452971/) — `x-2094978216146452971` — references + named interaction + verify, not “make it professional.”
- [A Developer's Guide to Taste](../../raw/items/web-opale-ui-taste/) — `web-opale-ui-taste` — scroll-linked springs, WebGL orbs, magnetic cursor as encoded taste.

## Examples

- [How we built the blume.codes landing page](../../raw/items/x-2094524951025914278/) — `x-2094524951025914278` — hero parallax layers, scroll-drawn vine, theme picker, live Electron UI embed.
- [Ballon Bleu de Cartier](../../raw/items/web-cartier-ballon-bleu/) — `web-cartier-ballon-bleu` — animated product user guide on a luxury PDP.
- [FeralUI](../../raw/items/web-feralui-dev/) — `web-feralui-dev` — components that swing, grab, crumple, catch light.
- [The Complete Shelf](../../raw/items/github-mengto-complete-shelf/) — `github-mengto-complete-shelf` — single-file Three.js shelf as motion/state-machine reference (also `three-js`).
- [Cult UI](../../raw/items/web-cult-ui/) — `web-cult-ui` — marketing/agent blocks with live previews.
- [Recent — Design Inspiration](../../raw/items/web-recent-design/) — `web-recent-design` — video-heavy UI motion feed.
- [TinyShots](../../raw/items/web-tinyshots/) — `web-tinyshots` — screenshot polish (presentation motion adjacent).

## All items

<!-- AUTO:ITEMS -->
- [Skills For Designers and Engineers](../../raw/items/github-emilkowalski-skills/) — `github-emilkowalski-skills`
- [Taste Skill](../../raw/items/github-leonxlnx-taste-skill/) — `github-leonxlnx-taste-skill`
- [The Complete Shelf](../../raw/items/github-mengto-complete-shelf/) — `github-mengto-complete-shelf`
- [Agent Skills (MengTo)](../../raw/items/github-mengto-skills/) — `github-mengto-skills`
- [scroll-craft](../../raw/items/github-nateherkai-scroll-craft/) — `github-nateherkai-scroll-craft`
- [motion-anything](../../raw/items/github-nexu-io-motion-anything/) — `github-nexu-io-motion-anything`
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design`
- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world`
- [Impeccable](../../raw/items/github-pbakaus-impeccable/) — `github-pbakaus-impeccable`
- [animos — Motion templates for design showcases](../../raw/items/web-animos-editor/) — `web-animos-editor`
- [Ballon Bleu de Cartier watch CRWSBB0049](../../raw/items/web-cartier-ballon-bleu/) — `web-cartier-ballon-bleu`
- [Cult UI](../../raw/items/web-cult-ui/) — `web-cult-ui`
- [FeralUI](../../raw/items/web-feralui-dev/) — `web-feralui-dev`
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai`
- [LottieFiles](../../raw/items/web-lottiefiles/) — `web-lottiefiles`
- [A Developer's Guide to Taste in the Age of AI](../../raw/items/web-opale-ui-taste/) — `web-opale-ui-taste`
- [Originkit](../../raw/items/web-originkit-dev/) — `web-originkit-dev`
- [Recent — Design Inspiration](../../raw/items/web-recent-design/) — `web-recent-design`
- [TinyShots — macOS screenshot polish app](../../raw/items/web-tinyshots/) — `web-tinyshots`
- [Vengeance UI](../../raw/items/web-vengence-ui/) — `web-vengence-ui`
- [this is terrifying. Claude Opus 5 + Remotion can now generate videos. It can do motion design, demos and animations from](../../raw/items/x-2086030681772376399/) — `x-2086030681772376399`
- [在试用了大部分热门的设计 SKILL 之后，最终我只留下这 4 个： 1. Impeccable http://impeccable.style 2. Skills for Design Engineers http://github.co](../../raw/items/x-2086715093707063445/) — `x-2086715093707063445`
- [One component, 10 examples. https://pro.reactbits.dev components do 90% of the work: motion, structure, customization. T](../../raw/items/x-2087812720762425743/) — `x-2087812720762425743`
- [Homieeee... This feels like finding a shovel during a gold rush. 🌋 A stunning collection of UI components built specific](../../raw/items/x-2087832615797833807/) — `x-2087832615797833807`
- [claude dropped Motion Prompt, and the crazy part is this entire animation was made with code, not AI-generated images or](../../raw/items/x-2088155107544191339/) — `x-2088155107544191339`
- [Impeccable 4.1 is here: core: -critique results more reliably prints in chat before asking you questions - the design ho](../../raw/items/x-2088254428730085690/) — `x-2088254428730085690`
- [This is a really useful tutorial if you want to learn how to build more advanced Three.js landing pages with Claude Code](../../raw/items/x-2088265078919282836/) — `x-2088265078919282836`
- [Introducing Mono Charts. A collection of minimal, animated chart components for React. Now you can add beautiful, intera](../../raw/items/x-2088599468698751328/) — `x-2088599468698751328`
- [wtf this is sick https://www.aicss.dev/](../../raw/items/x-2089182103153897532/) — `x-2089182103153897532`
- [30｜带物理摆动感的作品集 Carousel 来自@YousufSoomroDev 一个用于作品集展示的 Carousel 组件。切换项目时，卡片不是沿着水平轨道简单滑入，而是带着明显的摆动和惯性从画面外进入，最终回到稳定位置。作者同时将这](../../raw/items/x-2089223944700326052/) — `x-2089223944700326052`
- [The best UI components ready to use, save this 👇 - http://originkit.dev free animated component library - http://orbs.ja](../../raw/items/x-2089263766428950683/) — `x-2089263766428950683`
- [Introducing /improve-threejs Turn vibe-slop Three.js prototypes into stunning apps It makes slow, visually buggy games r](../../raw/items/x-2089400082550620636/) — `x-2089400082550620636`
- [I open-sourced the Sylva three.js site and the skills behind it. I started with one reference and asked Opus 5 to recrea](../../raw/items/x-2089602918605619401/) — `x-2089602918605619401`
- [The craziest font website ever https://departuremono.com](../../raw/items/x-2089618415493218381/) — `x-2089618415493218381`
- [Whatttt this existed, why no one showed me this yet, https://23rd.dev](../../raw/items/x-2089740155179643231/) — `x-2089740155179643231`
- [Animated in Higgsfield Seedance 2.5 + Cursor Composer 2.5 AI Skill: https://github.com/elayadesign/ai-design-skills](../../raw/items/x-2089770081459056765/) — `x-2089770081459056765`
- [Grind Log #044 - 18 August 2026 - Solved LeetCode: 268, 1656, 3043. - Added 3 new components to https://great-ui.com : h](../../raw/items/x-2089775679600812150/) — `x-2089775679600812150`
- [New skill: /animate-expo All the animation knowledge, but for your native apps. React Native and Expo: gestures, sheets,](../../raw/items/x-2090031918523842766/) — `x-2090031918523842766`
- [AI just changed how we create creative logo videos. MiniMax M3 can turn a simple logo into a polished, premium brand fil](../../raw/items/x-2091441060153278565/) — `x-2091441060153278565`
- [We are working on the new animated gradients collection “Dither Animation” It will be live on http://grainient.supply th](../../raw/items/x-2091479075697430784/) — `x-2091479075697430784`
- [This blew up, so I added 60 more three.js components from experiments I made over the last two weeks. I'm still amazed b](../../raw/items/x-2091571624390881664/) — `x-2091571624390881664`
- [can you believe that every pixel here is fully editable? this was created with the Motion harness](../../raw/items/x-2091688420695564296/) — `x-2091688420695564296`
- [AfterEffect → Minimax H3 「AI動画をレンダリングマシンとして使う」 生成するとき… ・AEでラフな同コンテを作成 ・Chat GPTでマテリアルを作成 ・強化するプロンプトを作成 ・H3でAEラフとマテリアル画像を](../../raw/items/x-2092040265234260091/) — `x-2092040265234260091`
- [Built a @heyglif skill that generates incredible motion graphics videos end to end, in any style, based on your script o](../../raw/items/x-2093081833911058772/) — `x-2093081833911058772`
- [Trending repository of the day 📈 archify Agent skill for beautiful, verifiable architecture, workflow, sequence, data-fl](../../raw/items/x-2093309791120543846/) — `x-2093309791120543846`
- [I can't wait to finally launch this site](../../raw/items/x-2093364419044794836/) — `x-2093364419044794836`
- [Walk into Hogwarts... Built this landing for an AI-based Harry Potter Experience event. Built by Custom Skills + My Vide](../../raw/items/x-2093767075131220005/) — `x-2093767075131220005`
- [🚨 THIS IS INSANE A Claude Code skill just started REFUSING to build websites that look like everyone else’s. Sameness is](../../raw/items/x-2093900284896657841/) — `x-2093900284896657841`
- [You don't need a massive agency budget to build an ultra-premium, interactive finance website. Watch how to build this p](../../raw/items/x-2093915384944414827/) — `x-2093915384944414827`
- [I created the world's best library of AI prompts for websites that don’t look like AI slop. 👇 • 590+ Al Animation Websit](../../raw/items/x-2094009989220430084/) — `x-2094009989220430084`
- [🔴 Los DISEÑOS web que genera tu agente APESTAN Espaciado raro Tipografia generica Gradientes de siempre Ese look de IA q](../../raw/items/x-2094069236524061059/) — `x-2094069236524061059`
- [Today we're launching Claude for motion graphics 2.0. It does the sound now. One person is now a whole production team: ](../../raw/items/x-2094164487381414344/) — `x-2094164487381414344`
- [How we built the blume.codes landing page (X article)](../../raw/items/x-2094524951025914278/) — `x-2094524951025914278`
- [Fable 5.1 website outputs cheaper than Fable 5 — /scroll-craft in replies](../../raw/items/x-2094978216146452971/) — `x-2094978216146452971`
- [Scroll-animated $5k site without writing CSS — ChatGPT + Gemini + Claude Code](../../raw/items/x-2094984529853530345/) — `x-2094984529853530345`
- [Made this 3D keyboard animation with CoAnimator, Claude Fable 5.1 ⌨️ ✨ Best part ? You can edit and customize the whole ](../../raw/items/x-2095111032171876470/) — `x-2095111032171876470`
- [Generates cinematic product videos with Claude Code and Remotion using 152 shot recipe cards and motion styles. https://](../../raw/items/x-2095204640690147487/) — `x-2095204640690147487`
- [Hero section design. built by Custom Skills + My Video Tool + Cursor + Client design md file and Some Creativity](../../raw/items/x-2095207624396652956/) — `x-2095207624396652956`
- [Premium design isn’t just about looking good—it’s about making your brand feel valuable before a customer even interacts](../../raw/items/x-2095429087141515616/) — `x-2095429087141515616`
- [Claude Fable 5.1 has given me the best website outputs compared to any AI model One-shots - don't need to spend a lot.](../../raw/items/x-2095549461737111905/) — `x-2095549461737111905`
<!-- /AUTO:ITEMS -->
