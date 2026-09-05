# Blender/Unreal blockout + agent camera → video model (blockout-to-video-flythrough)

## blockout-to-video-flythrough — scope

The BESS marketing pipeline: LLM/MCP-driven Blender or Unreal scene build, camera path authoring, depth/reference renders, first/last-frame or motion-reference conditioning into Seedance / MiniMax H3 / Veo / Kling / Runway; browser 3D camera stages (Mint Studio, MiniMax 3D Director, Higgsfield in Blender, CozyClay previs); camera-technique references.

Exclusion: Video generation without a 3D camera stage → ai-video-generation. Web 3D scroll heroes → web-3d-scenes.

Priority `now`. Owner aliases: BESS flythrough, blockout to video, camera path.
Expected primary range [18, 30]. This roster has **23** primary and **7** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## blockout-to-video-flythrough — what the owner is trying to decide

Decide the BESS-style pipeline: LLM/MCP blockout in Blender or Unreal, a locked camera path, then Seedance / MiniMax H3 / Veo conditioning. The question is which camera-stage + reference method is repeatable, not which video model is newest.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## blockout-to-video-flythrough — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=7, technique=18, example=14, claim-source=0, reference=5.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (6):
- [CozyClay open-source previs before pricey AI video generation](../../items/x-2091577179914338583/card.md) — tool, technique — Yun_HDY describes paying $17 per 30s AI video miss and open-sourcing CozyClay (NomaDamas/CozyClay) to block out scenes before sending…
- [CozyClay timeline slow-mo handles for in-editor camera timing](../../items/x-2091722166685610284/card.md) — tool, technique — Yun_HDY shows CozyClay adding slow-motion as draggable timeline handles so punch timing lands slower in-browser, linking the open-source…
- [CozyClay open-source previs tool with MCP for fast shot iteration](../../items/x-2092009056164872620/card.md) — tool, technique — Japanese review of CozyClay, an open-source previs app with MCP that is easier than Blender for blocking shots; author reports…
- [Higgsfield in Blender: prompt blockout, animate camera, reblock shots](../../items/x-2092255768770920506/card.md) — tool, technique — Higgsfield announces an in-Blender workflow to prompt a scene blockout, describe and animate camera moves, hand-tweak geometry, and…
- [Mint Studio browser 3D camera control for video generation](../../items/x-2093051654937423887/card.md) — tool, example — Product announcement for Mint Studio, a browser tool offering full 3D camera control for AI video generation without requiring Blender…
- [Intangible.ai — browser 3D camera control to AI-rendered video without Blender](../../items/x-2093380307735232543/card.md) — tool, example — Intangible.ai promotes an in-browser pipeline from interactive 3D camera control to AI-rendered video, positioning it as Blender-free…

First role `technique` (9):
- [Blender blockout camera path fed to Seedance 2.0/2.5 for cafe flythrough](../../items/x-2087565352372723955/card.md) — technique, example — Demo of Claude Opus 5 building a crude cafe blockout in Blender, keying the real camera in the .blend file, then using that 3D camera…
- [Magnific 3D Motion exports camera paths as Seedance 2.5 references](../../items/x-2091913781236683162/card.md) — technique, example — Demo thread for Magnific 3D Motion: generate a navigable 3D space, author camera motion around it, export the motion as a reference, and…
- [Claude via Unreal MCP spawns CineCamera and keyframes a full cinematic shot](../../items/x-2092008677834387672/card.md) — technique, example — Demo where Claude controls Unreal through MCP to spawn a CineCamera, create a Level Sequence with camera cuts, keyframe a slow dolly…
- [Intangible AI camera parenting for multi-angle scene consistency](../../items/x-2092657951618249080/card.md) — technique, tool — Intangible AI claims easier consistency across scenes by placing cameras, animating them, and parenting to moving objects instead of…
- [ComfyUI workflow: Blender blockout motion with MiniMax H3 environment](../../items/x-2092679517588574690/card.md) — technique, example — ComfyUI demonstrates a Blender blockout supplying camera motion and composition while a reference image guides environment, subject, and…
- [MiniMax 3D Director Stage: block scenes before H3 generation](../../items/x-2093053568748319181/card.md) — technique, example — Practitioner notes on MiniMax Design's 3D Director Stage: block figures, walls, and camera paths in 3D before generating, but H3 still…
- [Block Blender scenes before spending AI video generation credits](../../items/x-2093374092795846745/card.md) — technique, reference — Creator advises blocking scenes in Blender before burning AI video credits, pointing to a 19-minute tutorial
- [Blender camera lock plus Seedance 2.5 skin via Higgsfield plugin](../../items/x-2093377271771865267/card.md) — technique, example — Abyssal workflow builds a low-poly car scene in Blender with Higgsfield plugin, locks the camera path, then Seedance 2.5 skins the…
- [Blender blockout via Higgsfield MCP as Seedance 2.5 camera motion reference](../../items/x-2093663876692754713/card.md) — technique, example — Four-step BESS-style workflow: connect Claude Desktop to Blender through Higgsfield MCP, generate a gray-box blockout, tweak camera path…

First role `example` (4):
- [Codex driving Blender rigid-body demo at a desk setup](../../items/x-2065843739340509693/card.md) — example, technique — Short X demo showing Codex operating Blender via Python (bpy rigid-body keyframes) to animate a 3D cube over AR tracking markers on a…
- [Higgsfield + Claude Opus 5 builds animated low-poly Blender world in-prompt](../../items/x-2091497597743612379/card.md) — example, technique — Demo thread: Higgsfield plugin with Claude Opus 5 builds a full low-poly forest scene inside Blender from prompts—terrain, lake,…
- [GLM-5.3-Flash agent builds navigable Blender dream kitchen world](../../items/x-2093047548550525165/card.md) — example, technique — Lou claims GLM-5.3-Flash built a navigable dream-kitchen 3D world inside Blender and stresses the result is not a generated video
- [Claude Code alchemist shop pipeline across Blender MCP and 3D AI Studio](../../items/x-2093064017468145963/card.md) — example, technique — Thread describing a multi-MCP Claude Code pipeline: 3D AI Studio concept image, Blender MCP room build, reuse of 56 on-disk props plus…

First role `reference` (4):
- [BESS flythrough research — Blender MCP camera path to MiniMax H3 and depth conditioning](../../items/note-blender-minimax-h3-video-generation/card.md) — reference, technique — Internal research note mapping a photoreal BESS cabinet flythrough: LLM-driven Blender blockout and camera via blender-mcp, Cycles/EXR…
- [Blender Ponyo fan-film timelapse as camera layout reference](../../items/x-2093256024635666465/card.md) — reference, example — Japanese curator post linking a Ponyo and Sosuke Blender fan-movie timelapse on YouTube and a note.com write-up — useful as a manual…
- [Three bookmarked filmmaker refs: Eyecannndy, Sesohq moodboards, Tapir upscaler](../../items/x-2093986548404428942/card.md) — reference — Short X list recommending eyecannndy.com for camera techniques, Sesohq moodboards, and Tapir Convert's free 2× video upscaler as…
- [npaka note on when to drive Blender via CLI versus MCP](../../items/x-2095288402606514424/card.md) — reference — Japanese npaka note linked from X explaining how to operate Blender with AI, comparing CLI scripting versus MCP approaches for…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Blender blockout camera path fed to Seedance 2.0/2.5 for cafe flythrough](../../items/x-2087565352372723955/card.md)
- [Claude via Unreal MCP spawns CineCamera and keyframes a full cinematic shot](../../items/x-2092008677834387672/card.md)

Secondary membership (7), not in the primary count:
- [oso95 scroll-world: agent skill for scroll-scrubbed isometric flythrough landings](../../items/github-oso95-scroll-world/card.md) — primary `web-3d-scenes`
- [Three.js graphics agent skills: camera rigs, PBR, WebGPU validation](../../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md) — primary `web-3d-scenes`
- [Atlas 3D AI: one-sentence prompt to Blender staging and Unreal ride-through](../../items/x-2088299905324396589/card.md) — primary `image-to-3d-world`
- [After Effects rough comps as MiniMax H3 reference for AI video](../../items/x-2092040265234260091/card.md) — primary `code-motion-graphics`
- [MiniMax Agent H3 plugins for dynamic images and white-model rendering](../../items/x-2092702228947902622/card.md) — primary `ai-video-generation`
- [Spatial Studio: splat capture then in-browser camera animation and 4K export](../../items/x-2094377838774472944/card.md) — primary `gaussian-splatting`
- [Paper storyboards to Claude keyframes and Arcads MCP for AI Gucci ad](../../items/x-2095156045303701766/card.md) — primary `ai-video-generation`

## blockout-to-video-flythrough — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [blender-blockout-camera](../../techniques/blender-blockout-camera.md) — Agent or MCP builds a Blender/Unreal blockout and authors a camera path before any video model.
- [seedance-motion-reference](../../techniques/seedance-motion-reference.md) — Condition Seedance (or kin) with depth, first/last frame, or a motion plate from the 3D stage.
- [agent-video-editing](../../techniques/agent-video-editing.md) — Agent-driven cut, face-swap, and API routing with a local preview before spend.
- [worldgen-to-video](../../techniques/worldgen-to-video.md) — World/mesh generation handed to a video model for a flythrough instead of a real-time engine render.

## blockout-to-video-flythrough — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [minimax-h3](../../tools/minimax-h3.md)
- [wan-vace](../../tools/wan-vace.md)
- [kling](../../tools/kling.md)
- [veo](../../tools/veo.md)
- [blender-mcp](../../tools/blender-mcp.md)
- [codex](../../tools/codex.md)
- [blender](../../tools/blender.md)
- [seedance](../../tools/seedance.md)
- [higgsfield](../../tools/higgsfield.md)
- [meshy](../../tools/meshy.md)
- [cozyclay](../../tools/cozyclay.md)
- [magnific-3d-motion](../../tools/magnific-3d-motion.md)
- [unreal-engine](../../tools/unreal-engine.md)
- [higgsfield-mcp](../../tools/higgsfield-mcp.md)
- [comfyui](../../tools/comfyui.md)
- [glm-5-3-flash](../../tools/glm-5-3-flash.md)
- [mint-studio](../../tools/mint-studio.md)
- [minimax-3d-director](../../tools/minimax-3d-director.md)
- [intangible-ai](../../tools/intangible-ai.md)

## blockout-to-video-flythrough — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `note-blender-minimax-h3-video-generation#c1` | The dominant 2026 recipe is Blender blockout plus LLM camera path, then feed reference video or first/last frames to … | stated | [BESS flythrough research — Blender MC…](../../items/note-blender-minimax-h3-video-generation/card.md) |
| `note-blender-minimax-h3-video-generation#c3` | Tight interior camera moves need depth-video conditioning such as Wan 2.2 VACE rather than prompt-only commercial mod… | stated | [BESS flythrough research — Blender MC…](../../items/note-blender-minimax-h3-video-generation/card.md) |
| `x-2065843739340509693#c1` | The attached clip shows Blender Python driving rigid-body animation in a live viewport. | demonstrated | [Codex driving Blender rigid-body demo…](../../items/x-2065843739340509693/card.md) |
| `x-2087565352372723955#c1` | Author keys an animated camera inside Blender on blockout geometry and feeds that move to Seedance 2.0/2.5 for starti… | stated | [Blender blockout camera path fed to S…](../../items/x-2087565352372723955/card.md) |
| `x-2087565352372723955#c2` | Quoted Blender MCP X article 2083925419800002560 is 44 blocks / 3,924 chars (cube→red-sphere live check). | demonstrated | [Blender blockout camera path fed to S…](../../items/x-2087565352372723955/card.md) |
| `x-2091497597743612379#c1` | Claude Opus 5 through the Higgsfield plugin generates terrain, lake, mountains, trees, paths, lighting, and camera in… | stated | [Higgsfield + Claude Opus 5 builds ani…](../../items/x-2091497597743612379/card.md) |
| `x-2091497597743612379#c2` | A follow-on prompt uses Meshy 6 to generate a rigged low-poly adventurer and animate walking in the same Blender scene. | stated | [Higgsfield + Claude Opus 5 builds ani…](../../items/x-2091497597743612379/card.md) |
| `x-2091577179914338583#c2` | CozyClay is an open-source previs tool to build the scene before turning it into video. | stated | [CozyClay open-source previs before pr…](../../items/x-2091577179914338583/card.md) |
| `x-2091722166685610284#c1` | CozyClay exposes slow-motion as stretchable timeline handles that slow impact timing in the same editor. | demonstrated | [CozyClay timeline slow-mo handles for…](../../items/x-2091722166685610284/card.md) |
| `x-2091913781236683162#c1` | Magnific 3D Motion lets you generate a 3D space and control camera motion around it. | stated | [Magnific 3D Motion exports camera pat…](../../items/x-2091913781236683162/card.md) |
| `x-2091913781236683162#c2` | Exported 3D motion from Magnific can be used as a reference for Seedance 2.5 to recreate movement in a new scene. | stated | [Magnific 3D Motion exports camera pat…](../../items/x-2091913781236683162/card.md) |
| `x-2092008677834387672#c1` | Claude via Unreal MCP spawns CineCamera, creates a Level Sequence with camera cuts, keyframes a slow dolly, and runs … | stated | [Claude via Unreal MCP spawns CineCame…](../../items/x-2092008677834387672/card.md) |
| `x-2092009056164872620#c1` | CozyClay has MCP and is much easier to use than Blender despite lower extensibility. | stated | [CozyClay open-source previs tool with…](../../items/x-2092009056164872620/card.md) |
| `x-2092009056164872620#c2` | Reframing an existing scene takes about 30 seconds. | stated | [CozyClay open-source previs tool with…](../../items/x-2092009056164872620/card.md) |
| `x-2092255768770920506#c1` | Workflow covers prompt blockout, camera move animation, manual adjustment, and fast reblocking. | stated | [Higgsfield in Blender: prompt blockou…](../../items/x-2092255768770920506/card.md) |
| `x-2092255768770920506#c2` | Feature ships via Higgsfield MCP or Supercomputer. | stated | [Higgsfield in Blender: prompt blockou…](../../items/x-2092255768770920506/card.md) |

Full set: claims.jsonl (59 rows)

## blockout-to-video-flythrough — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- camera authored in 3D vs prompt-only
- reference conditioning (depth, first/last frame, motion)
- MCP/agent can rebuild the scene
- repeatability across shots
- target model family (Seedance, MiniMax H3, Veo, Kling)

## blockout-to-video-flythrough — thread coverage

X items in primary roster: 22. captured_full=2, captured_partial=13, empty=6, failed=1.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2065843739340509693](../../items/x-2065843739340509693/thread.md) | captured_partial | 119 | 3 | 1 |
| [x-2087565352372723955](../../items/x-2087565352372723955/thread.md) | empty | 0 | 0 | 0 |
| [x-2091497597743612379](../../items/x-2091497597743612379/thread.md) | empty | 0 | 0 | 0 |
| [x-2091577179914338583](../../items/x-2091577179914338583/thread.md) | captured_partial | 17 | 1 | 0 |
| [x-2091722166685610284](../../items/x-2091722166685610284/thread.md) | captured_partial | 3 | 1 | 0 |
| [x-2091913781236683162](../../items/x-2091913781236683162/thread.md) | captured_partial | 6 | 3 | 1 |
| [x-2092008677834387672](../../items/x-2092008677834387672/thread.md) | captured_full | 2 | 2 | 1 |
| [x-2092009056164872620](../../items/x-2092009056164872620/thread.md) | captured_partial | 4 | 1 | 0 |
| [x-2092255768770920506](../../items/x-2092255768770920506/thread.md) | captured_partial | 158 | 1 | 0 |
| [x-2092657951618249080](../../items/x-2092657951618249080/thread.md) | captured_partial | 5 | 3 | 2 |
| [x-2092679517588574690](../../items/x-2092679517588574690/thread.md) | captured_partial | 21 | 1 | 0 |
| [x-2093047548550525165](../../items/x-2093047548550525165/thread.md) | captured_partial | 315 | 3 | 3 |
| [x-2093051654937423887](../../items/x-2093051654937423887/thread.md) | failed | 2 | 0 | 0 |
| [x-2093053568748319181](../../items/x-2093053568748319181/thread.md) | empty | 0 | 0 | 0 |
| [x-2093064017468145963](../../items/x-2093064017468145963/thread.md) | empty | 0 | 0 | 0 |
| [x-2093256024635666465](../../items/x-2093256024635666465/thread.md) | captured_full | 1 | 1 | 0 |
| [x-2093374092795846745](../../items/x-2093374092795846745/thread.md) | captured_partial | 71 | 1 | 1 |
| [x-2093377271771865267](../../items/x-2093377271771865267/thread.md) | empty | 0 | 0 | 0 |
| [x-2093380307735232543](../../items/x-2093380307735232543/thread.md) | captured_partial | 4 | 3 | 2 |
| [x-2093663876692754713](../../items/x-2093663876692754713/thread.md) | captured_partial | 11 | 1 | 0 |
| [x-2093986548404428942](../../items/x-2093986548404428942/thread.md) | captured_partial | 18 | 1 | 0 |
| [x-2095288402606514424](../../items/x-2095288402606514424/thread.md) | empty | 0 | 0 | 0 |

## blockout-to-video-flythrough — gaps and open questions

Primary readiness: ready=8, ready-with-gaps=15. Gap tags: thread-partial=5, linked-page-unfetched=4, media-undescribed=1, thread-failed=1, translation-needed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- MiniMax H3 vs Seedance: which accepts Blender camera + depth most reliably?
- Can an MCP rebuild the same shot without a human nudging the viewport?

If this subject drops below 6 primary items after a future reclass, merge it into `ai-video-generation` and delete the folder.

## blockout-to-video-flythrough — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [ai-video-generation](../ai-video-generation/brief.md)
- [image-to-3d-world](../image-to-3d-world/brief.md)
- [web-3d-scenes](../web-3d-scenes/brief.md)

