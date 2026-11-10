# MCP

Topic slug: `mcp`. Adjacent: [agent-skills](agent-skills.md), [seo-agents](seo-agents.md), [design](design.md).

This lane is Model Context Protocol servers and tool routing: directories, gateways, remote endpoints, and stacks that expose SEO, sales, warehouse, browser, or design tools to an agent. `SKILL.md` install instructions live on [agent-skills](agent-skills.md); here the question is which server to attach.

Items cluster as catalogs/gateways (awesome-mcp-servers, treg as OpenRouter-for-tools), domain MCPs (Ian Nuttall SEO, CrowdReply AEO, Gojiberry outbound, Graphed warehouse marketing, AIDesigner in-editor UI, Hyperbrowser DESIGN.md extract, Flint charts), and X threads that show those MCPs wired into Grok Bot or Claude Code. Overlap with [seo-agents](seo-agents.md) is expected — same products, this file is the wire-up.

Query here for “what MCP do I add” or “how did someone route tools through one token.” For citation/AEO tactics, also open [seo-agents](seo-agents.md). For DESIGN.md as a file format, open [design](design.md). Follow `related_items`; presence is not a ranking.

## Pipelines

- One gateway token → catalog search by job → metered call; BYO keys unmetered (treg)
- Clone live URL HTML/CSS → tokens/components written into the repo (AIDesigner)
- Grok Bot + hosted sales MCP → prospect / score / sequence (Gojiberry Sales OS)
- Warehouse MCP → query modeled marketing data from Cursor (Graphed; Anthropic analytics pattern)
- Local SEO CLI as MCP using your crawl + GSC + IndexNow (iannuttall/seo)

## Tools

- [awesome-mcp-servers](../../raw/items/github-punkpeye-awesome-mcp-servers/) — canonical server list plus Glama directory.
- [treg — OpenRouter for agent tools](../../raw/items/github-superdesigndev-treg/) — one token, ~2.9k endpoints; SEO/people/ads APIs metered per call.
- [SEO Skill](../../raw/items/github-iannuttall-seo/) — local crawl + GSC/GA4 CLI; `seo mcp install`.
- [AIDesigner MCP](../../raw/items/web-aidesigner-mcp/) — generate / refine / clone UI inside the editor (21 tools).
- [CrowdReply](../../raw/items/web-crowdreply/) — AI-search visibility + citation outreach; remote MCP (~18 tools).
- [gojiberryai-sales-os](../../raw/items/github-romangojiberryAI-gojiberryai-sales-os/) — 13-agent outbound team on hosted Gojiberry MCP.
- [Graphed](../../raw/items/web-graphed/) — warehouse-connected marketing agents; MCP over modeled data.
- [DESIGNMD — Hyperbrowser](../../raw/items/web-design-md-hyperbrowser/) — extract DESIGN.md from any URL via browser API.
- [Originkit](../../raw/items/web-originkit-dev/) — animated component library with MCP import.

## Techniques

- [How Anthropic enables self-service data analytics with Claude](../../raw/items/web-anthropic-claude-self-service-data/) — map questions to a semantic layer; MCP/skills over the warehouse, not dumped schemas.
- [AI-native company #3: centralized intelligence layer](../../raw/items/x-2094558408259272998/) — one intelligence layer agents share vs per-harness context.
- [treg people-search GTM](../../raw/items/x-2094740953554932149/) — metered people-search as a GTM motion (~$0.0089/lead claim).
- [Flint: A Visualization Language for the AI Era](../../raw/items/web-flint-chart/) — chart IL that compiles to Vega/ECharts/Plotly; MCP for agents.
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — cinematic HTML layer templates assembled via MCP.

## Examples

- [MCP that clones any site's HTML/CSS for Claude Code (AIDesigner)](../../raw/items/x-2094467179320119498/) — demo: clone Linear/Browserbase-class pages in-repo.
- [Open-sourced outbound team — 13 AI sales agents](../../raw/items/x-2095081419202560010/) — Grok Bot + Gojiberry MCP role graph (strategy → prospect → sequence).
- [GrokBot booked a demo via GojiberryAI MCP](../../raw/items/x-2094326291906310180/) — claimed 97 prospects / 24h through the same stack.
- [Grok Bot as Chief of AI Visibility + CrowdReply MCP](../../raw/items/x-2094553318031024285/) — AEO loop: Grok Bot + CrowdReply tools.
- [treg — Claude for People Search](../../raw/items/web-treg-people-search/) — people-search product surface on the treg gateway.

## All items

<!-- AUTO:ITEMS -->
- [Obscura — headless browser for AI agents](../../raw/items/github-h4ckf0r0day-obscura/) — `github-h4ckf0r0day-obscura`
- [SEO Skill](../../raw/items/github-iannuttall-seo/) — `github-iannuttall-seo`
- [awesome-mcp-servers](../../raw/items/github-punkpeye-awesome-mcp-servers/) — `github-punkpeye-awesome-mcp-servers`
- [gojiberryai-sales-os](../../raw/items/github-romangojiberryAI-gojiberryai-sales-os/) — `github-romangojiberryAI-gojiberryai-sales-os`
- [treg — OpenRouter for agent tools](../../raw/items/github-superdesigndev-treg/) — `github-superdesigndev-treg`
- [LLM + Blender → AI Video: Photoreal BESS Flythrough](../../raw/notes/blender-minimax-h3-video-generation.md) — `note-blender-minimax-h3-video-generation`
- [🚀 New release of Android Remote Control MCP is out — the MCP server that runs on your phone and gives your AI agent the ability to use any app you want!](../../raw/items/reddit-1uy83bk/) — `reddit-1uy83bk`
- [We built an MCP server for CAD](../../raw/items/reddit-1w37d9y/) — `reddit-1w37d9y`
- [Qwen Open Sources zg Local Search Tool for Code and Docs](../../raw/items/reddit-1w5dab4/) — `reddit-1w5dab4`
- [Anthropic hackathon winner just open-sourced his entire Claude Code setup 🔥](../../raw/items/reddit-1wgu40p/) — `reddit-1wgu40p`
- [I built a way for Hermes to use any website as an API WITHOUT browser automation](../../raw/items/reddit-1wp4i6k/) — `reddit-1wp4i6k`
- [Breakscale: Build a system, load it until it breaks, and watch why (1.3k stars)](../../raw/items/reddit-1x49yi0/) — `reddit-1x49yi0`
- [AIDesigner MCP — AI UI design in the editor](../../raw/items/web-aidesigner-mcp/) — `web-aidesigner-mcp`
- [How Anthropic enables self-service data analytics with Claude](../../raw/items/web-anthropic-claude-self-service-data/) — `web-anthropic-claude-self-service-data`
- [Blume Sidecar — monitor and improve coding agents](../../raw/items/web-blume-codes/) — `web-blume-codes`
- [Kitesurf — agent-first browser on Cloudflare Workers](../../raw/items/web-cloudflare-kitesurf/) — `web-cloudflare-kitesurf`
- [CrowdReply — AI search visibility platform](../../raw/items/web-crowdreply/) — `web-crowdreply`
- [DESIGNMD — Hyperbrowser DESIGN.md Extractor](../../raw/items/web-design-md-hyperbrowser/) — `web-design-md-hyperbrowser`
- [Flint: A Visualization Language for the AI Era](../../raw/items/web-flint-chart/) — `web-flint-chart`
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai`
- [Graphed — Deploy AI Agents for Marketing](../../raw/items/web-graphed/) — `web-graphed`
- [Obscura — Give every agent its own browser](../../raw/items/web-obscura-sh/) — `web-obscura-sh`
- [Originkit](../../raw/items/web-originkit-dev/) — `web-originkit-dev`
- [treg — Claude for People Search](../../raw/items/web-treg-people-search/) — `web-treg-people-search`
- [That's the full stack. One package. One port. `npm i @copilotkit/aimock` Docs: http://aimock.copilotkit.dev GitHub: http](../../raw/items/x-2087151521121419648/) — `x-2087151521121419648`
- [KERNEL browsers now support custom proxies with CA bundles. pass your CA bundle in when you create the proxy and it will](../../raw/items/x-2087555254757757116/) — `x-2087555254757757116`
- [Orca has a design mode: draw and annotate right on your site, then send that feedback to any AI agent. Drop the site you](../../raw/items/x-2087708050002239702/) — `x-2087708050002239702`
- [another day where OSS win i stopped paying AHREF plan and switched to http://openseo.so The more i paid AHREF the less i](../../raw/items/x-2087827123331383751/) — `x-2087827123331383751`
- [Introducing Rakazo, an open-source Grok Bot alternative! - Use any LLM (pi harness) - Use any sandbox provider. Or Docke](../../raw/items/x-2087898602890744089/) — `x-2087898602890744089`
- [The scary part about AI in CAD is not that it can draw a part. It is that it can now understand a messy engineering proj](../../raw/items/x-2088296314484162719/) — `x-2088296314484162719`
- [anatomy of a managed deep agent. https://langch.in/mda](../../raw/items/x-2088345102540587356/) — `x-2088345102540587356`
- [Connects enterprise knowledge across your organization to build AI agents, RAG applications, and search on a single gove](../../raw/items/x-2088623462109593792/) — `x-2088623462109593792`
- [6 repos de AI Agents que estan explotando en github 1. Graft — https://github.com/NanoNets/Graft Hace que claude code se](../../raw/items/x-2091157554919280688/) — `x-2091157554919280688`
- [CLAUDE DIRECTS A FULL CINEMATIC SHOT IN UNREAL One prompt. Claude takes control through Unreal MCP > Spawns CineCamera >](../../raw/items/x-2092008677834387672/) — `x-2092008677834387672`
- [CozyClayっていうオープンソースのプレビス制作ソフトつかってみました。Blenderに比べると拡張性は低いんだけど、MCPあるし格段に使いやすい 一回シーンをつくっちゃったら構図変更するのも30秒くらい。これで何回もやり直して、そこか](../../raw/items/x-2092009056164872620/) — `x-2092009056164872620`
- [Introducing Higgsfield in Blender. > Prompt the scene and build the blockout > Describe the camera move and get it anima](../../raw/items/x-2092255768770920506/) — `x-2092255768770920506`
- [CLAUDE BUILDS AN ALCHEMIST SHOP ACROSS TWO MCP SERVERS This is not one tool doing everything. Claude Code runs the whole](../../raw/items/x-2093064017468145963/) — `x-2093064017468145963`
- [This is what happens when you stop testing AI CAD on sensible objects. Built inside Autodesk Fusion through MCP, the ass](../../raw/items/x-2093305736717545869/) — `x-2093305736717545869`
- [Stop wasting hundreds of AI credits trying to get precise camera movement in Seedance 2.5 🚫 Instead of relying purely on](../../raw/items/x-2093663876692754713/) — `x-2093663876692754713`
- [I created the world's best library of AI prompts for websites that don’t look like AI slop. 👇 • 590+ Al Animation Websit](../../raw/items/x-2094009989220430084/) — `x-2094009989220430084`
- [GrokBot booked a demo via GojiberryAI MCP (97 prospects / 24h)](../../raw/items/x-2094326291906310180/) — `x-2094326291906310180`
- [MCP that clones any site's HTML/CSS for Claude Code (AIDesigner)](../../raw/items/x-2094467179320119498/) — `x-2094467179320119498`
- [Grok Bot as Chief of AI Visibility + CrowdReply MCP](../../raw/items/x-2094553318031024285/) — `x-2094553318031024285`
- [AI-native company #3: centralized intelligence layer](../../raw/items/x-2094558408259272998/) — `x-2094558408259272998`
- [treg people-search GTM — $0.0089/lead, quotes Jason Zhou](../../raw/items/x-2094740953554932149/) — `x-2094740953554932149`
- [Meet investors in waves — venture fundraising FRM](../../raw/items/x-2094820035344621901/) — `x-2094820035344621901`
- [Open-sourced outbound team — GojiberryAI Sales OS for Grok Bot](../../raw/items/x-2094892848042725416/) — `x-2094892848042725416`
- [Ian Nuttall asking if anyone uses his SEO skill/CLI for real work](../../raw/items/x-2095055297949610427/) — `x-2095055297949610427`
- [Open-sourced outbound team — 13 AI sales agents in Grok Bot + GojiberryAI MCP](../../raw/items/x-2095081419202560010/) — `x-2095081419202560010`
- [AI was supposed to replace artists. So I hired one to make an AI Gucci ad. He drew every shot on paper first. Then Claud](../../raw/items/x-2095156045303701766/) — `x-2095156045303701766`
- [Blender MCPでFable 5.1を使い、右のエクイレクタングラー方式の都市パノラマ画像をリソースとして都市を構築させたところ、一発でこの情報量のモデルが完成。 これを手作業で作れと言われたら、3人日はかかるかな……。 テストでこの](../../raw/items/x-2095159781883597031/) — `x-2095159781883597031`
- [Claude Fable 5.1 is a beast at agentic CAD! At Max effort it's the most capable model we've tested so far. Here, inside ](../../raw/items/x-2095193896687177873/) — `x-2095193896687177873`
- [AIでBlenderを操作する方法 - CLIとMCPの使い分け｜npaka @npaka123 https://note.com/npaka/n/n7f7531e7b9ed?sub_rt=share_sb](../../raw/items/x-2095288402606514424/) — `x-2095288402606514424`
- [A two-person AI startup crossed $1 million in annualized revenue two months after launch. The founder just walked](../../raw/items/x-2096224107121516997/) — `x-2096224107121516997`
- [3 KiCad MCP servers bringing AI into PCB design  1. KiCad MCP Server by Seeed Studio Analyze schematics & PCBs, trace](../../raw/items/x-2096269926302613765/) — `x-2096269926302613765`
- [Some promising early results of my enhanced Blender MCP compared to the standard Blender MCP. It was able to generate](../../raw/items/x-2097072609351405641/) — `x-2097072609351405641`
- [MCP & Skills: https://appllama.io https://github.com/Appllama/appllama-skills Prompt: /goal Using Appllama MCP & App](../../raw/items/x-2098140208264851676/) — `x-2098140208264851676`
- [Try it out https://monid.ai/blog/saperly](../../raw/items/x-2098314696457875816/) — `x-2098314696457875816`
- [We FINALLY shipped an MCP so your AI Agent can rent 100s of iPhones 🚀 not "another AI wrapper" not "a dashboard you](../../raw/items/x-2099301416468652506/) — `x-2099301416468652506`
- [We open sourced BrowserSkill, a bridge between your agent and your actual browser. most tools give the agent a blank](../../raw/items/x-2100143086429217278/) — `x-2100143086429217278`
- [100% agree. Here is KiChad, KiCad + Astra.](../../raw/items/x-2100240455917297896/) — `x-2100240455917297896`
- [We just killed Monid ourselves. Monid is now open source. The OpenRouter for agent tools. Your agents can now: >](../../raw/items/x-2100330818958975088/) — `x-2100330818958975088`
- [If I Had to Build My Hermes Setup From Zero Today, I’d Start Here](../../raw/items/x-2101884812189684015/) — `x-2101884812189684015`
- [지금 전 세계 개발자 커뮤니티가 발칵 뒤집힌 이유.](../../raw/items/x-2102286564521111687/) — `x-2102286564521111687`
- [AstraにBlenderで昭和の日本家屋をモデリングしてもらった。ただし、CodexじゃなくてChatで。セキュアMCPTunnelって機能でWebのChatGPTから僕の手元のPCのBlenderをMCPで操作できます。チャットのProでワンショット42分間作業してくれました。Pro200ドルプランなら1週間あたり200回Proとチャット出来ます。つまり](../../raw/items/x-2103729495618281838/) — `x-2103729495618281838`
- [CLAUDE CODE CAN NOW TURN HIGGSFIELD INTO A ONE-PERSON AI VIDEO STUDIO.](../../raw/items/x-2106636580735619118/) — `x-2106636580735619118`
- [is it legal?](../../raw/items/x-2109716261160538324/) — `x-2109716261160538324`
- [MCP gives AI agents superpowers.](../../raw/items/x-2109897254849101986/) — `x-2109897254849101986`
- [We officially release smlibpy open source. A python API for the smlib nurbs kernel (inspired by cad-query, build123d & classcad). A wasm compile for javascript/ts (1.8mb dl/brotli ](../../raw/items/x-2110022758729937313/) — `x-2110022758729937313`
<!-- /AUTO:ITEMS -->
