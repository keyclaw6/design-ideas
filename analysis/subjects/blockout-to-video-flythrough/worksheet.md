# Judgment worksheet: blockout → video flythrough (blockout-to-video-flythrough)

Owner question: a *repeatable camera stage*, not the newest video model. 23 primaries; the internal BESS note is the north star.

## blockout-to-video-flythrough — short stack to try

Three camera stages appear. Pick one stage, then one conditioner.

1. **Blender as the stage (BESS).** Research note [note-blender-minimax-h3-video-generation](../../items/note-blender-minimax-h3-video-generation/card.md): blender-mcp blockout + camera, depth/EXR, then MiniMax H3 / Seedance. Live demos: cafe flythrough Seedance 2.0/2.5 ([x-2087565352372723955](../../items/x-2087565352372723955/card.md) — must-read), Higgsfield MCP gray-box ([x-2093663876692754713](../../items/x-2093663876692754713/card.md), [x-2093377271771865267](../../items/x-2093377271771865267/card.md)), ComfyUI Blender motion + H3 env ([x-2092679517588574690](../../items/x-2092679517588574690/card.md)).
2. **Unreal as the stage.** Claude + Unreal MCP CineCamera / Level Sequence ([x-2092008677834387672](../../items/x-2092008677834387672/card.md) — must-read). Use when the blockout is already an engine scene.
3. **Browser previs when Blender is the cost.** CozyClay + MCP ([x-2091577179914338583](../../items/x-2091577179914338583/card.md), timeline handles [x-2091722166685610284](../../items/x-2091722166685610284/card.md)). Mint Studio / Intangible / MiniMax 3D Director Stage are hosted camera boxes ([x-2093051654937423887](../../items/x-2093051654937423887/card.md), [x-2093380307735232543](../../items/x-2093380307735232543/card.md), [x-2093053568748319181](../../items/x-2093053568748319181/card.md)). Magnific 3D Motion exports a path as a Seedance reference ([x-2091913781236683162](../../items/x-2091913781236683162/card.md)).

Conditioners seen: Seedance 2.0/2.5 motion or first/last-ish reference, MiniMax H3 + depth, Higgsfield in-Blender reblock.

Block the scene before spending credits ([x-2093374092795846745](../../items/x-2093374092795846745/card.md)). CozyClay exists because a miss cost $17/30s.

## blockout-to-video-flythrough — axis scores

| item | camera authored in 3D | reference conditioning | MCP/agent rebuild | repeatable shots | target model |
|---|---|---|---|---|---|
| BESS note | high (Blender camera) | high (depth / EXR / H3) | high (blender-mcp) | designed for it | MiniMax H3, Seedance, Veo family |
| cafe Seedance flythrough | high (.blend camera) | high (3D camera → Seedance) | mid (Claude Opus 5 once) | unknown (one demo) | Seedance 2.0/2.5 |
| Higgsfield MCP gray-box | high | high (path as motion ref) | high (Claude Desktop + MCP) | mid (four-step writeup) | Seedance 2.5 |
| ComfyUI + H3 | high | high (blockout motion + still) | mid (graph, not MCP) | mid | MiniMax H3 |
| Unreal MCP CineCamera | high (Level Sequence) | unknown (engine shot, not always a video model) | high | mid (one demo) | Unreal render or later model |
| CozyClay | mid (browser previs) | low (previs only) | high (MCP) | high (iterate before pay) | whatever you send next |
| Mint / Intangible | Intangible live: compose cameras + **MCP Beta**; Mint live URL is **mint.gg** (assets + MCP, not a path exporter) | unknown | Intangible MCP Beta; Mint MCP is asset pipeline | unknown | their renderer |
| MiniMax 3D Director | high | mid (H3 still drifts) | low | mid | H3 |
| Magnific 3D Motion | high | high (export → Seedance 2.5) | low | mid | Seedance 2.5 |
| kitchen / alchemist MCP builds | high (Blender world) | n/a (they stop at the scene) | high | unknown | none — these are worlds, not spots |

## blockout-to-video-flythrough — claims that need a receipt

- Mint Studio “browser 3D camera for video” — thread failed. “Live now here!” `t.co/kfmFB5sFWU` → **mint.gg**. That site is a 3D-asset + MCP pipeline, not a documented camera-path exporter ([mint-studio](../../tools/mint-studio.md)).
- npaka CLI vs MCP note is live ([blender-blockout-camera](../../techniques/blender-blockout-camera.md)): CLI = `blender … --background --python`; MCP = running-Blender dialogue. Combine CLI → MCP → CLI.
- Cafe flythrough: confirm the `.blend` camera, not a prompt-only path, is what Seedance consumed (must-read). Official Seedance 2.0 page claims image/audio/video reference including camera movement ([seedance](../../tools/seedance.md)); the cafe `.blend` is still not in this bank. Quoted Blender MCP article **2083925419800002560** is now in-bank (**3,924** chars): cube→red-sphere live check + campsite/angel recipes ([blender-mcp](../../tools/blender-mcp.md)). That article is an operating loop, not the Seedance export. Root video **46.733 s** / 1920×1080. Card is now `ready` (thread `empty`).
- MiniMax 3D Director: author already says H3 still drifts after a blocked camera — treat that as a live limit, not a solved stage. Root video **51.478 s** / 1920×1080. Card is now `ready` (thread `empty`).
- CozyClay $17/30s miss — useful cost signal. **MCP verified** on this host: **25** tools (`load_motion` is the extra vs README 24), 420 `frame_shot` combos, `render_prompt` seedance_2, `.cclayproject` round-trip. AGPL-3.0 ([cozyclay](../../tools/cozyclay.md)).
- Unreal MCP shot — Level Sequence exists in the demo; whether it then hits Seedance/H3 is not in the card.
- GLM kitchen “not a generated video” — adjacent to freedom-modeling; do not file it as a finished spot.

## blockout-to-video-flythrough — do not treat as load-bearing

- Ponyo timelapse and Eyecannndy bookmarks — camera *taste*, not a pipeline.
- npaka CLI-vs-MCP note — operations (CLI batch vs MCP dialogue), not a camera-path recipe. Body now fetched.
- Codex rigid-body desk clip — Blender via Python, no video model.

## blockout-to-video-flythrough — next capture work

1. Keep the BESS note and the cafe Seedance card in sync; if the note’s EXR/depth recipe changed, update the note (you own that file). Cafe card is `ready`; remaining gap is the `.blend` file and a same-blockout Seedance vs 3D Director pass, not thread capture.
2. CozyClay `mcp` verify (25 tools, 420 `frame_shot` combos, `render_prompt` seedance_2, `.cclayproject` round-trip) is on [cozyclay](../../tools/cozyclay.md). Stock `verify:capture` timed out at 5 s. With SwiftShader flags + 30 s timeout it passed: **640×360** PNG, **230,400** non-black pixels, five on-camera views, cube occluder 0→7168. Banked `analysis/_work/captures/cozyclay-capture/artifact-640x360.png` (**93,730** B). Product page `cozyclay.org` **22,437 B** now on leftover [x-2092009056164872620#c3](../../items/x-2092009056164872620/card.md). Remaining: a GPU (non-SwiftShader) capture, and the same-blockout Seedance vs 3D Director pass.
3. One headed pass: Blender camera → Seedance vs MiniMax 3D Director → H3 on the *same* blockout, so drift is comparable.
4. Intangible homepage is live (**130,479 B**, MCP Beta, no Blender string). Mint “Live now” t.co → mint.gg. Remaining: a downloadable camera-path from either host.
5. Do not expand this lane with more model-launch tweets.
6. adilinthewild “19-minute” Blender-first tutorial is the X amplify video (**1187.497 s**, 3840×2160). Quoted prompts link is a Higgsfield blog **200 / 72,653 B** whose HTML does not repeat the 19-minute string ([higgsfield](../../tools/higgsfield.md)). Thread stays `captured_partial` (71/1).
7. npaka CLI-vs-MCP note card is now `ready` (thread `empty`; body already on [blender-blockout-camera](../../techniques/blender-blockout-camera.md)).
8. Higgsfield + Claude Opus 5 in-Blender world-build ([x-2091497597743612379](../../items/x-2091497597743612379/card.md)) is now `ready` (thread `empty`). Root video **49.6 s** / 1440×1080. Remaining: the `.blend` / Meshy project, not thread capture.
