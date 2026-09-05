# Agent harnesses, autoresearch loops, orchestration, agent ops (agent-harness-loops)

## agent-harness-loops — scope

Autoresearch and self-improving loops, harness design (Pi, Hermes, Headlong, loop-library, managed deep agents), orchestration cookbooks, multi-agent papers, permission stances, session/tool migration, agent observability (sideshow, Blume), curated repo lists, training pages, prompt-wording results.

Exclusion: Memory/knowledge systems → agent-memory-knowledge. MCP servers and agent browsers → mcp-and-agent-browsers.

Priority `standard`. Owner aliases: autoresearch, harness, agent ops.
Expected primary range [24, 36]. This roster has **35** primary and **12** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## agent-harness-loops — what the owner is trying to decide

Decide which harness/loop write-ups (Pi, Hermes, Headlong, autoresearch) describe a runnable control plane versus essay-only architecture.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## agent-harness-loops — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=11, technique=17, example=5, claim-source=8, reference=20.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (9):
- [Blume Sidecar desktop monitor for coding-agent config drift](../../items/web-blume-codes/card.md) — tool — Blume Sidecar is a local desktop app that watches Codex, Claude Code, and Cursor, tracking rules, skills, hooks, and hidden config files
- [loop-library: open catalog of field-tested agent loops at loopany.ai](../../items/x-2086790895538700379/card.md) — tool, reference — Jason Zhou introduces loop-library, an open-source catalog at loopany.ai/templates of named agent loops claimed to have shipped in…
- [Cloudflare OS repo — Workers-based agent workspace](../../items/x-2087178722420171020/card.md) — tool, reference — Bare X pointer to cloudflare/cloudflare-os, Cloudflare's agent workspace on Workers for documents, app builds, and company-context agents
- [pi-shepherdr: 271-token Pi orchestrator for Herdr multi-agent panes](../../items/x-2087232392209531166/card.md) — tool, technique — howaboua pi-shepherdr lets one master Pi agent list, start, watch, send to, and unwatch worker Pi agents in Herdr panes via a 271-token…
- [pi-clarify npm extension rewrites prompts before Pi coding agent](../../items/x-2087304957011911157/card.md) — tool — dodo-reach publishes pi-clarify on npm (`pi install npm:pi-clarify`), an extension that rewrites underspecified user prompts before Pi…
- [Howaboua Pi realtime voice changelog and extension announcement API](../../items/x-2087714580491370655/card.md) — tool, technique — Sixteen-hour voice-driven Pi release adds reportRealtimeVoicePrompt for extensions, togglable spoken acknowledgements and reasoning…
- [fortysevenfx weekend Sideshow.sh setup for visual agent-work inspection](../../items/x-2091622497393225801/card.md) — tool, example — Developer reports setting up bentlegen Sideshow.sh to visually understand and interact with agent work, calling it a step toward not…
- [session-migrate CLI converts coding-agent sessions across harnesses](../../items/x-2091970263088816272/card.md) — tool — Luca Huang announces session-migrate, a CLI that converts an in-progress coding-agent session from one harness to another — Claude Code,…
- [Headlong — open microharness for always-on persistent agents](../../items/x-2091990178638496195/card.md) — tool, technique — Headlong is an open-source Bash microharness (<10K LOC) where agents generate continuous inner thoughts, accept Slack/Telegram messages…

First role `technique` (7):
- [Hyperspace v3: generic Karpathy autoresearch swarms, Research DAG, and Warps](../../items/x-2032671842230501729/card.md) — technique, claim-source — Varun Mathur announces Hyperspace v3.0.10: plain-English goals spawn P2P Autoswarms, a cross-domain Research DAG compounds findings, and…
- [Kun Chen YOLO-agent ops: disposable Nix machine plus gated secrets](../../items/x-2082316720086405524/card.md) — technique, claim-source — Kun Chen explains running coding agents with all permission checks off by treating the laptop as a disposable employee device,…
- [Pocock /improve-codebase-architecture skill after blind vibe-coding](../../items/x-2086838432102228008/card.md) — technique, claim-source — Matt Pocock reports vibe-coding an app without inspecting internals, hitting failures, then recovering with the…
- [Pi AGENTS.md grill workflow with four taste skills and /handoff at 100k](../../items/x-2087263510090874911/card.md) — technique — Personal Pi workflow loads ponytail, grilling, wayfinder, and ask-matt via AGENTS.md, forces a long interrogation pass, then uses a…
- [Karpathy-cited REASONING block system prompt for step-by-step answers](../../items/x-2091118605392019658/card.md) — technique, reference — Thread shares a paste-once system prompt citing Karpathy: models imitate average answers unless forced to reason step-by-step, with…
- [Greg Mushen production agent stack: Hermes, skills, CLIs, telemetry](../../items/x-2093437790969385283/card.md) — technique, reference — Architecture note separating Hermes judgment layer, slim procedural skills, deterministic CLIs, and closed-loop telemetry for token…
- [fini multi-agent blast-radius checklist: one login, six bots, 24k actions](../../items/x-2094110975045554191/card.md) — technique, claim-source — fini warns six named sidebar bots can share one browser profile: 23,999 actions in twenty minutes across mail, drive, CRM, and billing…

First role `example` (3):
- [Autoquant: Karpathy autoresearch swarm applied to multi-factor quant backtests](../../items/x-2032330665081839791/card.md) — example, technique — Varun Mathur describes Autoquant v2.6.9: 135 agents mutate four-layer trading pipelines (macro, sector, alpha, risk officer) via…
- [Codex auto-research loop: 212× faster QR kernel on GPU Mode](../../items/x-2074912810803560497/card.md) — example, claim-source — X post announcing a blog write-up where Codex ran an auto-kernel search on GPU Mode's qr_v2 QR decomposition problem and claims a 212×…
- [rauchg runs is-agentic scorer in a loop until 100/100 on is-agentic.com](../../items/x-2090858571613470919/card.md) — example, technique — Guillermo Rauch describes looping the is-agentic evaluator against is-agentic.com until scoring 100/100, using the rubric to close…

First role `claim-source` (1):
- [Ouroboros agent evolves tools and prompts via reviewed commits](../../items/x-2087151807965401320/card.md) — claim-source, reference — HuggingPapers announces Ouroboros, a self-improving coding agent that evolves its own tools, prompts, and architecture through reviewed…

First role `reference` (15):
- [Sindresorhus awesome: canonical meta-index of curated GitHub lists](../../items/github-sindresorhus-awesome/card.md) — reference — The canonical awesome-list meta-index maintained by Sindresorhus, linking hundreds of topic-specific curated GitHub resource lists
- [OpenAI ChatGPT Training: Work/Codex labs and plugins-vs-skills walkthroughs](../../items/web-chatgpt-training/card.md) — reference, technique — Official learn.chatgpt.com/training hub with hands-on Work and Codex labs plus six walkthroughs covering plugins vs skills, scheduled…
- [Aman Chadha autoresearch and Meta-Harness engineering primer](../../items/x-2080856252687745093/card.md) — reference, technique — X thread promoting autoresearch.aman.ai, a primer on autonomous research loops and Meta-Harness optimization
- [Anthropic Dynamic Workflows cookbook — Claude spawns 1,000 subagents](../../items/x-2087026930323247306/card.md) — reference, technique — Pointer to Anthropic's Claude Agent SDK Dynamic Workflows notebook where Claude writes its own orchestration script and can fan out to…
- [Control Plane Pattern X article: replace brittle multi-agent handoff chains](../../items/x-2087254502210490739/card.md) — reference, technique — X article (not a Stanford paper) arguing multi-agent analytics pipelines rot context at each handoff and proposing a Control Plane…
- [Survey maps reliable evaluation for self-evolving agents (L0–L4)](../../items/x-2087444616832594022/card.md) — reference, claim-source — Tencent Hunyuan announces a survey and 549-work catalog on reliable self-evolving agents, defining an L0–L4 taxonomy and a ladder…
- [Shubhamsaboo awesome-llm-apps catalog (~132k stars)](../../items/x-2088116807869854126/card.md) — reference — Tweet pointing at Shubhamsaboo/awesome-llm-apps, a large curated list of end-to-end LLM application examples spanning RAG, agents, and…
- [Permalink to Matt Pocock grilling SKILL.md for pre-build interrogation](../../items/x-2088260067204137135/card.md) — reference, claim-source — Reply pointing to the canonical Matt Pocock grilling skill file that interrogates constraints and success criteria before an agent…
- [LangChain managed deep agent folder architecture (MDA)](../../items/x-2088345102540587356/card.md) — reference, technique — Caspar shares LangChain's managed deep agent diagram: an agent is a folder with instructions, skills, memory, tools, MCP connectors,…
- [codex-plusplus community Codex CLI tweak pack (repo pointer)](../../items/x-2088634091671531923/card.md) — reference, tool — Short reply asking which codex-plusplus tweak produced a behavior, linking b-nnett/codex-plusplus — a community patch pack for OpenAI…
- [Anthropic agent cost optimization cookbook pointer ($0.29 to 90% less)](../../items/x-2089165107364278341/card.md) — reference — Daniel San highlights Anthropic's cost_optimization.ipynb cookbook where a real agent task drops from about $0.29 to ninety percent less…
- [Spanish roundup of six trending GitHub AI agent repos](../../items/x-2091157554919280688/card.md) — reference — Spanish-language list post highlighting six GitHub agent projects — Graft cost savings, Agency Agents subagent roster, codebase-memory…
- [Rivet agentOS technical manual exported as 825-page PDF book](../../items/x-2091686636698657080/card.md) — reference, example — Rivet founder Nathan Flurry shares a PDF export of Rivet's hand-written docs as an 825-page technical manual covering actors, agentOS,…
- [David Ondrej Agentic Engineering Setup X article link](../../items/x-2094424967345496191/card.md) — reference — David Ondrej shares an X article on Agentic Engineering Setup covering bb, cmux, Herdr, skills, worktrees, and cloud VPS configuration;…
- [OpenAI ChatGPT Training hub for Work, Codex, plugins, and skills](../../items/x-2095133695480873023/card.md) — reference, tool — Codex APAC lead promotes learn.chatgpt.com/training: guided hands-on tracks for ChatGPT Work and Codex plus walkthroughs on plugins,…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Codex auto-research loop: 212× faster QR kernel on GPU Mode](../../items/x-2074912810803560497/card.md)
- [Aman Chadha autoresearch and Meta-Harness engineering primer](../../items/x-2080856252687745093/card.md)

Secondary membership (12), not in the primary count:
- [Opus 5 recursive loop builds interactive textureless 3D vehicle](../../items/x-2086537093120164177/card.md) — primary `web-3d-scenes`
- [EP Hermes agent prompt for four-layer personal second-brain OS](../../items/x-2086920236079681607/card.md) — primary `agent-memory-knowledge`
- [Sentrux Rust binary scores codebase architecture for agent sessions](../../items/x-2087239769877295158/card.md) — primary `agent-memory-knowledge`
- [Rakazo: Apache-2.0 open-source Grok Bot on pi harness](../../items/x-2087898602890744089/card.md) — primary `mcp-and-agent-browsers`
- [FleetingBits: Claude-generated explorable codebase diagrams with inspectable data dots](../../items/x-2088016749849682120/card.md) — primary `infographics-diagrams`
- [Matt Pocock ten-minute tour of all 25 skills in mattpocock/skills](../../items/x-2088290952704151671/card.md) — primary `design-agent-skills`
- [Harness canvas worker draws architecture diagrams in chat](../../items/x-2088590355440476343/card.md) — primary `infographics-diagrams`
- [/vision skill writes VISION.md to gate agent feature work](../../items/x-2089189790881382676/card.md) — primary `design-agent-skills`
- [FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints](../../items/x-2091150763418620133/card.md) — primary `local-inference-models`
- [Self-maintaining second brain: RAW, WIKI, CLAUDE.md, five automations](../../items/x-2093677274641969390/card.md) — primary `agent-memory-knowledge`
- [Video Use: open-source Claude Code agent video editor (browser-use)](../../items/x-2094061655990702150/card.md) — primary `ai-video-generation`
- [Six-model stack claims 160k daily TikTok views via LightReel](../../items/x-2095202138854977756/card.md) — primary `ai-video-generation`

## agent-harness-loops — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [autoresearch-loop](../../techniques/autoresearch-loop.md) — Self-improving research swarms with an eval, not a single long chat.
- [agent-harness-ops](../../techniques/agent-harness-ops.md) — Harness, control plane, folder-as-agent, and multi-agent ops that a later judge can rerun.
- [session-hardening](../../techniques/session-hardening.md) — Secrets, session migration, blast-radius, and worker isolation for long-running agents.

## agent-harness-loops — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [blume-sidecar](../../tools/blume-sidecar.md)
- [hyperspace](../../tools/hyperspace.md)
- [codex](../../tools/codex.md)
- [nix-darwin](../../tools/nix-darwin.md)
- [automicvault](../../tools/automicvault.md)
- [loop-library](../../tools/loop-library.md)
- [claude-agent-sdk](../../tools/claude-agent-sdk.md)
- [pi-shepherdr](../../tools/pi-shepherdr.md)
- [herdr](../../tools/herdr.md)
- [pi-clarify](../../tools/pi-clarify.md)
- [pi-codex-conversion](../../tools/pi-codex-conversion.md)
- [pi-gippity-control](../../tools/pi-gippity-control.md)
- [codex-plusplus](../../tools/codex-plusplus.md)
- [is-agentic](../../tools/is-agentic.md)
- [graft](../../tools/graft.md)
- [agency-agents](../../tools/agency-agents.md)
- [codebase-memory-mcp](../../tools/codebase-memory-mcp.md)
- [openmontage](../../tools/openmontage.md)
- [agent-reach](../../tools/agent-reach.md)
- [orca](../../tools/orca.md)
- [sideshow-sh](../../tools/sideshow-sh.md)
- [rivet](../../tools/rivet.md)
- [session-migrate](../../tools/session-migrate.md)
- [headlong](../../tools/headlong.md)
- [hermes](../../tools/hermes.md)
- [chatgpt-training](../../tools/chatgpt-training.md)

## agent-harness-loops — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-sindresorhus-awesome#c1` | The README indexes hundreds of specialized awesome lists across platforms, languages, and tool categories. | stated | [Sindresorhus awesome: canonical meta-…](../../items/github-sindresorhus-awesome/card.md) |
| `github-sindresorhus-awesome#c2` | awesome.md defines what qualifies as an awesome curated list. | stated | [Sindresorhus awesome: canonical meta-…](../../items/github-sindresorhus-awesome/card.md) |
| `web-blume-codes#c1` | Sidecar monitors Codex, Claude Code, and Cursor hidden rules/skills/hooks locally. | stated | [Blume Sidecar desktop monitor for cod…](../../items/web-blume-codes/card.md) |
| `web-chatgpt-training#c1` | OpenAI defines plugins as new capabilities and skills as how you want them done. | stated | [OpenAI ChatGPT Training: Work/Codex l…](../../items/web-chatgpt-training/card.md) |
| `web-chatgpt-training#c2` | Training hub ships two hands-on labs (Work planning, Codex first code change) and six ordered walkthroughs. | stated | [OpenAI ChatGPT Training: Work/Codex l…](../../items/web-chatgpt-training/card.md) |
| `x-2032330665081839791#c1` | Autoquant runs ~135 agents with 30 mutations per round and Darwinian selection across a P2P gossip network. | stated | [Autoquant: Karpathy autoresearch swar…](../../items/x-2032330665081839791/card.md) |
| `x-2032330665081839791#c2` | Agents independently converged on dropping three factors and risk-parity sizing, claiming Sharpe 1.32 versus 1.04 bas… | contested | [Autoquant: Karpathy autoresearch swar…](../../items/x-2032330665081839791/card.md) |
| `x-2032671842230501729#c1` | Autoswarms let users describe a goal in English and the network spins up sandboxed mutate-evaluate WASM experiments o… | stated | [Hyperspace v3: generic Karpathy autor…](../../items/x-2032671842230501729/card.md) |
| `x-2032671842230501729#c2` | Research DAG links observations and experiments across ML, search, finance, and skills so AutoThinker proposes cross-… | stated | [Hyperspace v3: generic Karpathy autor…](../../items/x-2032671842230501729/card.md) |
| `x-2032671842230501729#c3` | Warps are declarative presets (power-mode, privacy-mode, GPU sentinel) stackable to change overnight agent behavior. | stated | [Hyperspace v3: generic Karpathy autor…](../../items/x-2032671842230501729/card.md) |
| `x-2074912810803560497#c1` | Author claims Codex auto-kerneling on GPU Mode's qr_v2 problem achieved 212× faster kernel performance over baseline. | stated | [Codex auto-research loop: 212× faster…](../../items/x-2074912810803560497/card.md) |
| `x-2074912810803560497#c2` | Live GPU Mode API ranks sankalp1999 26th at 3916.103 µs (submission_id 796445), not the blog's 12th / 1,805 µs. | demonstrated | [Codex auto-research loop: 212× faster…](../../items/x-2074912810803560497/card.md) |
| `x-2080856252687745093#c1` | Autoresearch turns manual experimentation into a continuous propose-run-evaluate-learn loop. | stated | [Aman Chadha autoresearch and Meta-Har…](../../items/x-2080856252687745093/card.md) |
| `x-2080856252687745093#c2` | Meta-Harness extends search to prompts, retrieval, memory, tools, state, parsers, and control flow. | stated | [Aman Chadha autoresearch and Meta-Har…](../../items/x-2080856252687745093/card.md) |
| `x-2080856252687745093#c7` | Arbor (arXiv:2606.11926) reports best held-out on six AO tasks, >2.5× gain vs Codex/Claude Code, 86.36% MLE-Bench Lite Any Medal. | demonstrated | [Aman Chadha autoresearch and Meta-Har…](../../items/x-2080856252687745093/card.md) |
| `x-2082316720086405524#c1` | Author disables all agent permission checks and skips auto-review, treating the machine as an employee laptop not a p… | stated | [Kun Chen YOLO-agent ops: disposable N…](../../items/x-2082316720086405524/card.md) |
| `x-2082316720086405524#c2` | Recovery path is nix-darwin plus home-manager dotfiles: wipe, clone, rebuild in minutes. | stated | [Kun Chen YOLO-agent ops: disposable N…](../../items/x-2082316720086405524/card.md) |

Full set: claims.jsonl (116 rows)

## agent-harness-loops — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- runnable loop vs architecture essay
- permission / blast-radius model
- eval or out-of-sample check
- session persistence and migration
- multi-agent vs single harness

## agent-harness-loops — thread coverage

X items in primary roster: 32. captured_full=2, captured_partial=27, empty=2, failed=1.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2032330665081839791](../../items/x-2032330665081839791/thread.md) | captured_partial | 79 | 1 | 1 |
| [x-2032671842230501729](../../items/x-2032671842230501729/thread.md) | captured_partial | 158 | 2 | 2 |
| [x-2074912810803560497](../../items/x-2074912810803560497/thread.md) | captured_partial | 22 | 1 | 1 |
| [x-2080856252687745093](../../items/x-2080856252687745093/thread.md) | captured_full | 4 | 4 | 3 |
| [x-2082316720086405524](../../items/x-2082316720086405524/thread.md) | captured_partial | 41 | 3 | 3 |
| [x-2086790895538700379](../../items/x-2086790895538700379/thread.md) | captured_partial | 8 | 1 | 0 |
| [x-2086838432102228008](../../items/x-2086838432102228008/thread.md) | captured_partial | 78 | 1 | 0 |
| [x-2087026930323247306](../../items/x-2087026930323247306/thread.md) | captured_partial | 15 | 3 | 1 |
| [x-2087151807965401320](../../items/x-2087151807965401320/thread.md) | failed | 2 | 0 | 0 |
| [x-2087178722420171020](../../items/x-2087178722420171020/thread.md) | empty | 0 | 0 | 0 |
| [x-2087232392209531166](../../items/x-2087232392209531166/thread.md) | captured_partial | 12 | 3 | 1 |
| [x-2087254502210490739](../../items/x-2087254502210490739/thread.md) | captured_partial | 30 | 3 | 0 |
| [x-2087263510090874911](../../items/x-2087263510090874911/thread.md) | captured_partial | 20 | 2 | 1 |
| [x-2087304957011911157](../../items/x-2087304957011911157/thread.md) | captured_partial | 21 | 1 | 1 |
| [x-2087444616832594022](../../items/x-2087444616832594022/thread.md) | captured_partial | 14 | 3 | 2 |
| [x-2087714580491370655](../../items/x-2087714580491370655/thread.md) | captured_partial | 10 | 3 | 1 |
| [x-2088116807869854126](../../items/x-2088116807869854126/thread.md) | empty | 0 | 0 | 0 |
| [x-2088260067204137135](../../items/x-2088260067204137135/thread.md) | captured_full | 1 | 2 | 2 |
| [x-2088345102540587356](../../items/x-2088345102540587356/thread.md) | captured_partial | 34 | 3 | 0 |
| [x-2088634091671531923](../../items/x-2088634091671531923/thread.md) | captured_partial | 4 | 3 | 1 |
| [x-2089165107364278341](../../items/x-2089165107364278341/thread.md) | captured_partial | 19 | 1 | 1 |
| [x-2090858571613470919](../../items/x-2090858571613470919/thread.md) | captured_partial | 142 | 3 | 3 |
| [x-2091118605392019658](../../items/x-2091118605392019658/thread.md) | captured_partial | 11 | 3 | 3 |
| [x-2091157554919280688](../../items/x-2091157554919280688/thread.md) | captured_partial | 64 | 3 | 3 |
| [x-2091622497393225801](../../items/x-2091622497393225801/thread.md) | captured_partial | 8 | 3 | 2 |
| … | 7 more X items | — | — | — |

## agent-harness-loops — gaps and open questions

Primary readiness: ready=7, ready-with-gaps=28. Gap tags: thread-partial=8, linked-page-unfetched=2, thread-failed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which loop has an eval that is not the author’s anecdote?
- What is the minimum permission stance that still lets a design agent click a browser?

If this subject drops below 6 primary items after a future reclass, merge it into `agent-memory-knowledge` and delete the folder.

## agent-harness-loops — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [agent-memory-knowledge](../agent-memory-knowledge/brief.md)
- [mcp-and-agent-browsers](../mcp-and-agent-browsers/brief.md)
- [design-agent-skills](../design-agent-skills/brief.md)

