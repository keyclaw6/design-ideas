# AI video models, tools, and launch-video craft (ai-video-generation)

## ai-video-generation — scope

Model announcements with usable detail (MiniMax H3 / H3 Max, Seedance), audio fixes, story/consistency tools (OpenStory, Calliope), agent video editing (video-use), launch-video breakdowns, faceless/TikTok pipelines, product-render-via-video-model.

Exclusion: Code-rendered motion → code-motion-graphics. Anything with a Blender/Unreal camera stage → blockout-to-video-flythrough.

Priority `standard`. Owner aliases: video generation, Seedance, Kling, Veo.
Expected primary range [14, 24]. This roster has **20** primary and **14** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## ai-video-generation — what the owner is trying to decide

Decide which video-model items carry usable controls (audio-only regen, character lock, story tools) versus launch hype. Anything with a 3D camera stage belongs in blockout-to-video-flythrough.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## ai-video-generation — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=7, technique=8, example=11, claim-source=6, reference=3.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (7):
- [fal.ai unified generative media API and GPU platform](../../items/web-fal-ai/card.md) — tool, reference — Developer platform offering 1,000+ image, video, audio, and 3D model APIs plus serverless and dedicated GPU compute, with homepage…
- [OpenStory AI — script-to-video with cross-scene style consistency](../../items/x-2091713204418490406/card.md) — tool — Chinese-language intro to OpenStory, an open-source platform that turns a script into styled video by analyzing scenes and keeping…
- [MiniMax H3 Max on Magnific: 5s 480p clip in under 5 seconds](../../items/x-2091957150793023651/card.md) — tool, claim-source — Magnific announces MiniMax H3 Max generates a five-second 480p clip in under five seconds, offering unlimited generations for three…
- [MiniMax Agent H3 plugins for dynamic images and white-model rendering](../../items/x-2092702228947902622/card.md) — tool, example — MiniMax Agent shipped H3-based plugins for dynamic images and white-model (clay) rendering
- [video-use plus Codex for agent-driven video editing](../../items/x-2092980272819999227/card.md) — tool, example — Recommendation of browser-use/video-use paired with Codex for agent-driven video editing, pointing to the open-source video-use repo as…
- [Calliope: idea-to-finished 2D faceless YouTube video pipeline](../../items/x-2093481253043380418/card.md) — tool, technique — Calliope product demo claiming one idea flows through script, characters, 2D animation, and voiceover into a finished faceless YouTube…
- [Video Use: open-source Claude Code agent video editor (browser-use)](../../items/x-2094061655990702150/card.md) — tool — Spanish-language post highlights Video Use, an open-source browser-use project that auto-edits raw footage in a folder—cutting clips,…

First role `technique` (5):
- [ChatGPT ideation, Fable 5 build, Higgsfield animate design workflow](../../items/x-2093236801079279978/card.md) — technique, example — Designer elayadesigns shares a four-step workflow: ideate in ChatGPT, build scenes in Fable 5, animate with Higgsfield, then iterate
- [GPT Image 2 face-swap stills plus Seedance 2.5 for realistic character video](../../items/x-2094819241916801165/card.md) — technique, example — Thread recipe for realistic AI character video: swap faces into reference stills with GPT Image 2, lock identity across scenes, then…
- [Paper storyboards to Claude keyframes and Arcads MCP for AI Gucci ad](../../items/x-2095156045303701766/card.md) — technique, example — rom1trs describes hiring an artist for a Gucci-style AI ad: paper storyboards, Claude-generated keyframes and character sheets, Arcads…
- [MiniMax H3 audio repair: low-res video, high-step audio regen, latent shrink](../../items/x-2095427702325231977/card.md) — technique, claim-source — Japanese post describes fixing MiniMax H3 video audio degradation by downscaling video, regenerating audio at high steps, compositing…
- [MiniMax H3 as local product-CG renderer before API spend](../../items/x-2095483352375837020/card.md) — technique — Japanese practitioner testing MiniMax H3 as a product-CG renderer, noting local processing lets them lock creative direction before…

First role `example` (5):
- [Seedance 2.5 animation with Cursor Composer and AI design skills](../../items/x-2089770081459056765/card.md) — example, technique — Pipeline example pairing Higgsfield Seedance 2.5 for animated hero motion with Cursor Composer 2.5 plus the elayadesign ai-design-skills…
- [MiniMax H3 free tier enables parallel video generation experiments](../../items/x-2091519705911795761/card.md) — example — Japanese post noting MiniMax H3 is free enough to run many parallel video generation trials, with the author offering a tutorial article…
- [7.5M-view Base44 launch video breakdown thread](../../items/x-2093681908227936745/card.md) — example, claim-source — Fakhar threads a breakdown of a Base44 launch video that exceeded 7.5M views, with a 52-second attached clip showing…
- [Six-model stack claims 160k daily TikTok views via LightReel](../../items/x-2095202138854977756/card.md) — example, technique — Poster claims connecting six models through @lightreelai and Doublespeed runs unsupervised TikTok accounts hitting about 160k views per…
- [Titouan Gillet 4.6M-view Intelligence Co launch video breakdown](../../items/x-2095521587785081193/card.md) — example, claim-source — Titouan Gillet cites a founder-posted launch video that generated over 4.6 million views for Intelligence Co and promises a full…

First role `claim-source` (1):
- [AI coding models can render imperfect handcrafted-style motion videos](../../items/x-2091622751756751211/card.md) — claim-source, example — kickingkeys argues AI coding models can produce beautifully imperfect videos — positioning code-rendered motion as an alternative to…

First role `reference` (2):
- [MiniMax H3 unlimited generations on Runway host](../../items/x-2090098441200517416/card.md) — reference — Official MiniMax post announces H3 video model is unlimited on Runway, enabling high-volume iteration on camera-path and site-plate…
- [MiniMax H3 Max video model on Magnific tuned by fal](../../items/x-2091924963288580539/card.md) — reference, claim-source — Magnific announces H3 Max, a post-trained MiniMax H3 variant tuned by fal for stronger prompt adherence and visual quality, now…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [GPT Image 2 face-swap stills plus Seedance 2.5 for realistic character video](../../items/x-2094819241916801165/card.md)

Secondary membership (14), not in the primary count:
- [BESS flythrough research — Blender MCP camera path to MiniMax H3 and depth conditioning](../../items/note-blender-minimax-h3-video-generation/card.md) — primary `blockout-to-video-flythrough`
- [Blender blockout camera path fed to Seedance 2.0/2.5 for cafe flythrough](../../items/x-2087565352372723955/card.md) — primary `blockout-to-video-flythrough`
- [MiniMax M3 logo-to-brand-film motion workflow claim](../../items/x-2091441060153278565/card.md) — primary `code-motion-graphics`
- [CozyClay open-source previs before pricey AI video generation](../../items/x-2091577179914338583/card.md) — primary `blockout-to-video-flythrough`
- [Claude via Unreal MCP spawns CineCamera and keyframes a full cinematic shot](../../items/x-2092008677834387672/card.md) — primary `blockout-to-video-flythrough`
- [After Effects rough comps as MiniMax H3 reference for AI video](../../items/x-2092040265234260091/card.md) — primary `code-motion-graphics`
- [ComfyUI workflow: Blender blockout motion with MiniMax H3 environment](../../items/x-2092679517588574690/card.md) — primary `blockout-to-video-flythrough`
- [MiniMax 3D Director Stage: block scenes before H3 generation](../../items/x-2093053568748319181/card.md) — primary `blockout-to-video-flythrough`
- [Glif skill generates script-to-motion-graphics videos (Vox style)](../../items/x-2093081833911058772/card.md) — primary `code-motion-graphics`
- [Intangible.ai — browser 3D camera control to AI-rendered video without Blender](../../items/x-2093380307735232543/card.md) — primary `blockout-to-video-flythrough`
- [Blender blockout via Higgsfield MCP as Seedance 2.5 camera motion reference](../../items/x-2093663876692754713/card.md) — primary `blockout-to-video-flythrough`
- [Three bookmarked filmmaker refs: Eyecannndy, Sesohq moodboards, Tapir upscaler](../../items/x-2093986548404428942/card.md) — primary `blockout-to-video-flythrough`
- [Scroll-scrubbed 300-frame landing via Gemini video and Framer Motion](../../items/x-2094984529853530345/card.md) — primary `landing-ui-motion`
- [Hyper3D WorldGen builds editable physics worlds from one photo](../../items/x-2095437841958314100/card.md) — primary `image-to-3d-world`

## ai-video-generation — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [agent-video-editing](../../techniques/agent-video-editing.md) — Agent-driven cut, face-swap, and API routing with a local preview before spend.
- [seedance-motion-reference](../../techniques/seedance-motion-reference.md) — Condition Seedance (or kin) with depth, first/last frame, or a motion plate from the 3D stage.
- [remotion-code-video](../../techniques/remotion-code-video.md) — The timeline is code (Remotion, html-video, Motion Prompt), not a GUI project file.
- [worldgen-to-video](../../techniques/worldgen-to-video.md) — World/mesh generation handed to a video model for a flythrough instead of a real-time engine render.
- [faceless-video-pipeline](../../techniques/faceless-video-pipeline.md) — YouTube/TikTok pipelines that regenerate audio or picture without an on-camera talent.

## ai-video-generation — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [fal-api](../../tools/fal-api.md)
- [seedance](../../tools/seedance.md)
- [elayadesign-ai-design-skills](../../tools/elayadesign-ai-design-skills.md)
- [minimax-h3](../../tools/minimax-h3.md)
- [openstory](../../tools/openstory.md)
- [minimax-h3-max](../../tools/minimax-h3-max.md)
- [magnific](../../tools/magnific.md)
- [video-use](../../tools/video-use.md)
- [codex](../../tools/codex.md)
- [fable-5](../../tools/fable-5.md)
- [higgsfield](../../tools/higgsfield.md)
- [calliope](../../tools/calliope.md)
- [gpt-image-2](../../tools/gpt-image-2.md)
- [lightreelai](../../tools/lightreelai.md)
- [doublespeed](../../tools/doublespeed.md)

## ai-video-generation — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `web-fal-ai#c1` | fal hosts 1,000+ production-ready generative media models behind one API. | stated | [fal.ai unified generative media API a…](../../items/web-fal-ai/card.md) |
| `web-fal-ai#c2` | Homepage highlights MiniMax H3 Max and Seedance 2.5 image-to-video endpoints. | stated | [fal.ai unified generative media API a…](../../items/web-fal-ai/card.md) |
| `x-2089770081459056765#c1` | Animation is produced in Higgsfield Seedance 2.5 while implementation uses Cursor Composer 2.5. | stated | [Seedance 2.5 animation with Cursor Co…](../../items/x-2089770081459056765/card.md) |
| `x-2090098441200517416#c1` | MiniMax H3 is available with unlimited generation quota on Runway according to the official account. | stated | [MiniMax H3 unlimited generations on R…](../../items/x-2090098441200517416/card.md) |
| `x-2091519705911795761#c1` | The author runs parallel MiniMax H3 video tests because the model is free. | stated | [MiniMax H3 free tier enables parallel…](../../items/x-2091519705911795761/card.md) |
| `x-2091519705911795761#c2` | The post identifies MiniMax H3 as the model in use. | stated | [MiniMax H3 free tier enables parallel…](../../items/x-2091519705911795761/card.md) |
| `x-2091622751756751211#c1` | AI coding models can create videos with a beautifully imperfect aesthetic. | stated | [AI coding models can render imperfect…](../../items/x-2091622751756751211/card.md) |
| `x-2091713204418490406#c1` | OpenStory converts a script into video while maintaining consistent characters, scenes, color, and lighting. | stated | [OpenStory AI — script-to-video with c…](../../items/x-2091713204418490406/card.md) |
| `x-2091713204418490406#c2` | It automatically analyzes a script and splits scenes before generation. | stated | [OpenStory AI — script-to-video with c…](../../items/x-2091713204418490406/card.md) |
| `x-2091924963288580539#c1` | H3 Max is a fal-tuned MiniMax H3 post-train focused on prompt adherence and visual quality. | stated | [MiniMax H3 Max video model on Magnifi…](../../items/x-2091924963288580539/card.md) |
| `x-2091957150793023651#c1` | MiniMax H3 Max generates a 5-second 480p clip in under 5 seconds on Magnific. | stated | [MiniMax H3 Max on Magnific: 5s 480p c…](../../items/x-2091957150793023651/card.md) |
| `x-2091957150793023651#c2` | Magnific offered unlimited H3 Max generations for three days at launch. | stated | [MiniMax H3 Max on Magnific: 5s 480p c…](../../items/x-2091957150793023651/card.md) |
| `x-2092702228947902622#c1` | MiniMax Agent released H3-based plugins for dynamic images and white-model rendering. | stated | [MiniMax Agent H3 plugins for dynamic …](../../items/x-2092702228947902622/card.md) |
| `x-2092980272819999227#c1` | Author reports video-use combined with Codex is highly effective for AI-driven video editing. | stated | [video-use plus Codex for agent-driven…](../../items/x-2092980272819999227/card.md) |
| `x-2093236801079279978#c1` | The workflow chains ChatGPT ideation, Fable 5 building, and Higgsfield animation with iterative refinement. | stated | [ChatGPT ideation, Fable 5 build, Higg…](../../items/x-2093236801079279978/card.md) |

Full set: claims.jsonl (38 rows)

## ai-video-generation — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- control surface beyond text prompt
- audio and lip-sync handling
- character or product consistency
- local preview before paid API
- usable duration and resolution numbers

## ai-video-generation — thread coverage

X items in primary roster: 19. captured_full=2, captured_partial=17, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2089770081459056765](../../items/x-2089770081459056765/thread.md) | captured_partial | 10 | 3 | 0 |
| [x-2090098441200517416](../../items/x-2090098441200517416/thread.md) | captured_partial | 16 | 3 | 1 |
| [x-2091519705911795761](../../items/x-2091519705911795761/thread.md) | captured_partial | 24 | 3 | 0 |
| [x-2091622751756751211](../../items/x-2091622751756751211/thread.md) | captured_partial | 45 | 3 | 1 |
| [x-2091713204418490406](../../items/x-2091713204418490406/thread.md) | captured_partial | 12 | 1 | 1 |
| [x-2091924963288580539](../../items/x-2091924963288580539/thread.md) | captured_full | 2 | 2 | 1 |
| [x-2091957150793023651](../../items/x-2091957150793023651/thread.md) | captured_partial | 18 | 3 | 1 |
| [x-2092702228947902622](../../items/x-2092702228947902622/thread.md) | captured_partial | 16 | 3 | 1 |
| [x-2092980272819999227](../../items/x-2092980272819999227/thread.md) | captured_partial | 15 | 3 | 2 |
| [x-2093236801079279978](../../items/x-2093236801079279978/thread.md) | captured_partial | 29 | 3 | 0 |
| [x-2093481253043380418](../../items/x-2093481253043380418/thread.md) | captured_full | 3 | 3 | 2 |
| [x-2093681908227936745](../../items/x-2093681908227936745/thread.md) | captured_partial | 18 | 1 | 0 |
| [x-2094061655990702150](../../items/x-2094061655990702150/thread.md) | captured_partial | 49 | 1 | 0 |
| [x-2094819241916801165](../../items/x-2094819241916801165/thread.md) | captured_partial | 57 | 1 | 1 |
| [x-2095156045303701766](../../items/x-2095156045303701766/thread.md) | captured_partial | 17 | 3 | 0 |
| [x-2095202138854977756](../../items/x-2095202138854977756/thread.md) | captured_partial | 11 | 1 | 0 |
| [x-2095427702325231977](../../items/x-2095427702325231977/thread.md) | captured_partial | 5 | 1 | 1 |
| [x-2095483352375837020](../../items/x-2095483352375837020/thread.md) | captured_partial | 4 | 1 | 0 |
| [x-2095521587785081193](../../items/x-2095521587785081193/thread.md) | captured_partial | 20 | 1 | 1 |

## ai-video-generation — gaps and open questions

Primary readiness: ready=2, ready-with-gaps=18. Gap tags: thread-partial=6, linked-page-unfetched=4, translation-needed=1, thread-failed=1, media-undescribed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which audio-only regen tools keep lipsync without re-rolling picture?
- Are story/consistency tools (Calliope, OpenStory) usable without their SaaS?

If this subject drops below 6 primary items after a future reclass, merge it into `blockout-to-video-flythrough` and delete the folder.

## ai-video-generation — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [blockout-to-video-flythrough](../blockout-to-video-flythrough/brief.md)
- [code-motion-graphics](../code-motion-graphics/brief.md)
- [image-prompt-galleries](../image-prompt-galleries/brief.md)

