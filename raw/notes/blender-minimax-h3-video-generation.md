# LLM + Blender → AI Video: Photoreal BESS Flythrough

## Deep Research Report — updated for MiniMax H3

**Date:** Aug 15, 2026 · **Research:** 59 sub-agent sessions (plan → capability deep-dives → camera-adherence lane → MCP/Blender bridge → GitHub lanes → X/Reddit/YouTube/HN mining → synthesis) · **Format:** images in `bess-ai-flythrough-report/images/`, all links in §11.

**Your goal:** a photoreal marketing video of your battery energy storage cabinet — an LLM builds the scene and guides the camera in Blender, then a video-generation model produces the footage: flying tight inside the internals, exploded views, cell/battery close-ups.

---

## 1. Executive summary (what this report answers)

1. **Your exact pipeline is already a community standard in 2026.** The dominant recipe: *Blender blockout + LLM-authored camera path (via `blender-mcp`) → render reference video + first/last frames → feed to a video model (Seedance 2.0 / Veo 3.1 / Kling 3.0 / MiniMax H3) as "motion reference" / start+end frames → photoreal output.* There are curated catalogs of ~25 real case studies and 70+ production ComfyUI workflows doing exactly this.

2. **Photoreal — yes. Fully autonomous — no.** Video models inherit realism and roughly follow your camera move, but they never pin an exact per-frame path and they will garble fine brand markings. The professional answer is a **hybrid**: your Blender render is the master (exact geometry + camera), the AI model adds photorealism and polish, and text/nameplates are composited back in post.

3. **"Flying tight inside the internals" has one reliable route:** condition the model with a **depth video from Blender's Z pass** (Wan 2.2 VACE / LTX-2.3 3DREAL). Commercial models hallucinate tight-interior geometry if given only prompts.

4. **The model you meant — MiniMax H3 — is now your best-value hero-motion option** via its hosted API: it pins Blender's first+last frames precisely (FL2VA), follows plain-language camera direction, renders text better than any rival, ships native synced audio, at ~$7.80/min at 2K. **But the open-weight version is legally off-limits for a US/EU company** (Community License excludes US/EU/UK/KR, including the *outputs*).

5. **Nobody has made an AI BESS-cabinet flythrough yet.** That niche is traditional CGI studios today (BayWa r.e., Terrasun, Photon Vault). The closest AI precedent is Sarvesh Chitnis's photoreal BESS **site renders** (stills + strict JSON preservation prompts). You would be first in your specific niche.

6. **Budget:** ~$200–800 for a polished 30–60s video using APIs; <$100 self-hosted (Wan/LTX on a 24–48GB GPU).

---

## 2. The feasibility verdict

| Question                                                     | Verdict                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Can an LLM build the scene + guide the camera in Blender?    | **Yes** — `blender-mcp` (25k★) or the official Blender Lab MCP server; `create_camera`, `add_keyframe`, `render_from_camera` tools. Community-verified camera flythroughs. |
| Can a video model produce photoreal output from my 3D renders? | **Yes** — realism is the models' strength; feed a photoreal start frame + first/last anchors + camera prompt. |
| Can it preserve MY exact product design?                     | **Mostly** — subject binding is "recognizable, not pixel-locked." Kling (7 refs + element binding) and MiniMax Ref2VA (≤9 images, roles) are best; fine logos need post-compositing. |
| Can it follow MY exact camera path?                          | **Only with conditioning.** Start+end frames: approximate (5–10% endpoint drift). Depth-video conditioning (Wan VACE): near-exact per frame. |
| Can it fly INSIDE the cabinet tightly?                       | **Risky for commercial models; reliable with depth conditioning** — or just render the interior in Cycles and let AI add polish. |
| Free tiers?                                                  | Hailuo free tier: usable for tests but **not commercially** (watermark, non-commercial ToS). Kling free 66 cr/day (watermarked). No real free tier on Veo/Seedance/Omni. |

---

## 3. What people have actually created (the state of the art)

### The canonical pipeline (seen across the 2026 cohort)
**Generate/design a start image → block out the shot in Blender + animate the camera → feed both to Seedance 2.0 (or Veo 3.1 / Kling / H3) as a motion reference / first+last frames → photoreal clip.**

![MiniMax H3 banner](bess-ai-flythrough-report/images/h3_minimax-h3.png)
*MiniMax H3 banner (source: huggingface.co/MiniMaxAI/MiniMax-H3)*

### Curated case-study repositories — start here
- **Awesome-Blender-Seedance-Workflow-Usecases** — ~25 real X case studies of the Blender→Seedance camera-previs pipeline (see under `Evolink-AI` and a fork under `ismael-joffroy-chandoutis`; the exact owner path has been inconsistent between mirrors — verify before cloning).
- **comfyui-cinema-pipeline** (ismael-joffroy-chandoutis) — 70+ production workflows: Blender VSE → ControlNet → Wan 2.2, MCP, local/cloud hybrid.
- **comfyui-blender-temporal** — Blender EXR depth/normal passes → per-frame ControlNet conditioning ("the secret sauce" for temporal consistency).
- **EvoLink cookbook** "Blender to Video" (evolink.ai/cookbook/blender-to-video).

### Direct proofs of the "3D previz → AI video" pattern
- **X:** @reidhannaford "Camera Blocking with Midjourney Start Frame" — *Seedance tracks the Blender move closely*; @noman23761 gray-box blockout as motion reference; @DiabloNemesis viewport preview → realistic first frame → Seedance; @Viggle_PINOC FBX clay + Claude-keyframed camera → Seedance; @akiyoshisan Codex + BlenderMCP → MP4 reference → Seedance.
- **LinkedIn:** Kari Piirainen — *Claude + Blender MCP directs a Seedance flythrough* (Jul 2026); Arminas Valunas — *gray-shaded Blender scene → Seedance 2.0, same car/driver/camera path* (Jul 2026) — the closest public analog to your product case.
- **Reddit:** r/comfyui "Blender Layout → AI Render | 1:1 Camera Tracking"; r/StableDiffusion "Blender Depth to Final Video with LTX-2.3 IC-LoRA" and "3D to photoreal, open source IC-LoRA for LTX 2.3" (most-upvoted render→photoreal recipes); r/aivideo "Shining product integration" (759▲).
- **YouTube:** Dan Kieft "Seedance + Blender Unlocks Advanced AI Filmmaking"; Yaroflasher "Seedance 2.0 Video Reference Tutorial" (80K views); Max Novak "I connected Claude AI to Blender 3D (MCP)" (318K views); Thomas Lundström "3 Steps to Perfect AI Product Animations with Kling 3.0"; Matt Wolfe "I Tried Every New Veo 3.1 Trick".
- **NVIDIA official:** "Blender 3D scene → 4K video in ComfyUI" (start/end frames → LTX-2.3 FLF → RTX VSR).

### Product flythroughs / exploded views / interiors
- Mike Futia: **one product photo → exploded end-frame → Veo 3 animates → auto-assembly** (Dec 2025).
- Eugenio Zabell: **iPhone internal fly-through exploded ad — Nano Banana Pro + Kling, <2 min** (Mar 2026) — the most reusable template for your cabinet.
- Karthikeyan R (Kling 2.5 exploded shot via keyframe interpolation); Tanay Ahir (stopwatch exploded view).
- r/VEO3 "I made this product demo within 1 hour" (Jun 2026).
- **Interior caveat:** practitioners agree — *do the structure in 3D, let AI add polish.* Pure text-to-video "fly inside a machine" invents wrong internals.

### BESS / battery-specific (your gap to fill)
No AI-generated BESS-cabinet flythrough exists yet. Closest precedents:
- **Sarvesh Chitnis** (UK) — AI-assisted photoreal **BESS site visuals** for Pacific Green: 3Ds Max/Blender → Twinmotion + Google Earth → Nano Banana Pro upscale with strict JSON prompts ("preserve geometry 1:1, no added elements"). Stills + camera GIFs, not motion video. **sarvesh.co.uk/battery-energy-parks**
- **BayWa r.e. BESS explainer** (The Imagineers) — Unreal; precise **cross-sections of the cabinet interior** (modules, sprinklers, cooling). theimagineers.com/en/news/baywa-r.e.-visualization
- IMMIX **Terrasun** + **Photon Vault** (pure CGI); **Cobra Designs BESS container** (ships a `blender_cycles` PBR model — an exact-interior Blender scene you can buy cheaply). cobradesigns.net · cgtrader.com

---

## 4. Model comparison matrix (updated: MiniMax H3 included)

| Model                        | Ref frames                     | First/last frame              | Camera control                                           | Res / Dur                                | Product fidelity                                | Text / logos                     | Cost                         | Free tier   | Commercial                                |
| ---------------------------- | ------------------------------ | ----------------------------- | -------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------- | -------------------------------- | ---------------------------- | ----------- | ----------------------------------------- |
| **MiniMax H3** (API)         | ≤9 img + ≤3 vid (Ref2VA)       | **Yes (FL2VA, both anchors)** | Natural-language cinematography; static needs "refusals" | 2K (hosted) / 768p weights, 4–15s, 24fps | Strong with role-tagged refs; no exact geometry | **Best-in-class for typed text** | **$0.08/s 768p, $0.13/s 2K** | No          | **API yes** (weights exclude US/EU/UK/KR) |
| **Gemini Omni Flash**        | 7–10 imgs                      | First only, **no last**       | Text + chat edits                                        | 720p, 3–10s                              | Approximate                                     | Unreliable                       | ~$0.10/s                     | No          | Paid OK                                   |
| **MiniMax Hailuo 2.3**       | 1 (S2V-01)                     | FL2V-02 API only              | 15 text commands                                         | 720p–1080p, 6s                           | Drifts past 4–6s                                | Weak                             | $0.27–0.53/clip              | ~100 cr/day | Paid only                                 |
| **Veo 3.1**                  | 3 imgs                         | **Yes** (8s; frame ≈ guide)   | Best text precision; presets                             | 720p–4K, 4–8s +extend                    | Strong                                          | Weak text                        | Std $0.40/s                  | No          | Paid OK                                   |
| **Kling 3.0**                | 7 (4 w/ video)                 | **Native start+end**          | Text moves; excl. w/ frames                              | **4K**, ≤15s, 60fps                      | Best first-frame/element binding                | **Best among rivals**            | Std $6.99/mo                 | 66 cr/day   | Paid OK                                   |
| **Seedance 2.5**             | ≤30 img +10 vid                | **Yes** first+last            | Motion-ref video; camera-preserving edits                | ≤1080p, ≤30s, 24fps                      | Top I2V leaderboard                             | Garbled signs                    | ~$0.10–0.35/s                | No          | Paid OK                                   |
| **Wan 2.2 + LTX-2.3** (open) | VACE depth seq; 3DREAL IC-LoRA | **Yes**, native FLF2V         | **Exact via depth/trajectory**                           | 720p–4K                                  | Exact camera/geometry                           | Not preserved in edits           | Open (~$0.27/121f on fal)    | Self-host   | Apache-2.0                                |
| **Runway Gen-4.5/Aleph 2.0** | 3 refs / 5 anchored            | Anchored frames               | Director-Mode slider                                     | 720p gen / Aleph 1080p                   | Strict binding                                  | "Pixel-exact" (skeptical)        | Premium                      | Limited     | Paid OK                                   |

*Sora 2 excluded — product closed Apr 2026, API sunsetting Sept 2026.*

### BESS-fit score (fidelity 30% · camera 25% · photorealism 20% · cost/free 15% · text/logos 10%)

| Rank | Model                       | Score   | One-line why                                                 |
| ---- | --------------------------- | ------- | ------------------------------------------------------------ |
| 1    | **Wan 2.2 + LTX-2.3 combo** | **9.1** | Only stack with *exact* camera + geometry control (depth-sequence VACE, render-to-real); Apache-2.0, unlimited iteration |
| 2    | **Kling 3.0**               | 8.5     | Best practical balance: 7 refs hold your cabinet, native start+end, crispest rival text, free daily credits |
| 3    | **MiniMax H3 (hosted API)** | **8.4** | Best-value hero-motion upgrade: pins both frames, plain-language camera, native audio, ~$7.80/min 2K — API is license-clean for US/EU |
| 4    | **Veo 3.1**                 | 8.0     | Best pure photorealism + camera-language precision; use first+last frame as endpoints |
| 5    | **Seedance 2.5**            | 7.9     | Best I2V leaderboard + motion-reference; signs garbled       |
| 6    | **Runway Aleph 2.0**        | 7.8     | Strict binding + anchored frames; premium, 720p gen ceiling  |
| 7    | **Gemini Omni Flash**       | 6.3     | Great for iteration/edits; no last-frame, experimental       |
| 8    | **MiniMax Hailuo 2.3**      | 6.3     | Cheap but drift + no brand lock + free tier non-commercial   |

*Leaderboard anchors (Artificial Analysis, Aug 2026): T2V — Omni Flash 1241, H3 1238, Seedance 2.0 1222, Kling 3.0 1109, Veo 3.1 1091. I2V — Seedance 1198, H3 1192, Omni Flash 1191. Video Editing — H3 #1 ~1130. VBench-2.0 Camera Motion: Kling 61.7% vs Sora 27.2%. WRBench D1 trajectory precision: Wan-Fun cam ≈0.76–0.84.*

---

## 5. MiniMax H3 — the model you actually meant (deep dive)

> The open-weight model you referenced is **MiniMax H3** (a.k.a. Hailuo 3.0), released July 31 2026, open weights Aug 3, 2026 — not "MIMO v2.5." Here is exactly how it changes your plan.

### What it is
A 33B multimodal video system with two interchangeable modes in one model:
- **FL2VA** — text-to-video AND image-anchored video: give it **0, 1, or 2 images** (first frame, last frame, or **both**). Two-image mode *resolves precisely onto your Blender first+last frames* — community testers confirm the clip "lands exactly" on the closing frame.
- **Ref2VA** — reference-to-video: up to **9 images + 3 video clips + 3 audio clips**, each assignable a role ("Image 2 = the cabinet, exact design"). Use this as your **brand-consistency pass** across a multi-shot set.
- Modes are mutually exclusive per request. Native **stereo audio** generated in the same pass (32kHz), 4–15s, 24fps, 21:9→9:16.

### Camera control
- Natural-language cinematography — *push-in, pull, arc, truck, track, tilt, pedestal, static, POV, shake* — better than the bracket syntax of Hailuo 2.3.
- **The catch:** static/locked shots need "camera refusals" — list the moves it must *not* make ("frame never moves, no push-in, no dolly") — otherwise it drifts, reframes, or cuts (r/comfyui 1vg3j6m, r/StableDiffusion 1vl07cw).

### Product & text fidelity
- **Ref2VA holds object identity if you name it** ("Image 2 = the bag, exact design and gold chain"); products are less forgiving than faces — use a clean, plain-background packshot of your cabinet and state shape/colourway/labels explicitly.
- **Text is its standout strength:** spelled-out strings come back correctly spelled and kerned through push-ins at 2K — best of any video model tested. *But* text can mutate in editing passes, so your real nameplates still get composited in post.

### Specs, speed, cost
| Item                 | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Resolution           | 768p short-edge (open weights) · **2K (hosted, via H3-Regenerate-2K)** |
| Hardware (self-host) | ~24GB VRAM (pruned/NVFP4); RTX 4090: 5s clip ≈ 90s–7min, 15s clip ≈ 23–30min; GGUF available |
| Hosted API           | **$0.08/s (768p), $0.13/s (2K), +$0.05/s for 2K regen** ≈ **$7.80/min at 2K**; US/EU region selectable |

### The licensing catch (critical for you)
- The **Community License excludes self-hosting in the US, EU, UK, South Korea — and the exclusion extends to the finished videos** (§V.4 covers the outputs). $20M/yr revenue cap elsewhere; UI attribution required; no distillation; Hong Kong jurisdiction.
- **The hosted API is globally available and license-clean** for a US/EU business (no territory or revenue ceiling).
- **Net for you:** use H3 through **MiniMax's hosted API** for hero shots; the 768p self-host route is off the table for a US company — and that makes **Wan 2.2 / LTX-2.3 the safer lawful self-hosted stack** for repeatable local rendering.

![H3 architecture overview](bess-ai-flythrough-report/images/h3_overview.png)
*H3 FL2VA / Ref2VA system (source: huggingface.co/MiniMaxAI/MiniMax-H3)*

![H3 full architecture](bess-ai-flythrough-report/images/h3_full-arch.png)
*H3 architecture detail (source: huggingface.co/MiniMaxAI/MiniMax-H3)*

### Verdict for your BESS flythrough
H3 (hosted) is a **quality-and-cost upgrade for the hero-motion step, not a rewrite of your pipeline.** It pins your Blender first+last frames, follows camera direction faithfully, gives native audio, and undercuts Veo/Kling. It is still a generative model — it cannot guarantee millimeter-accurate internals, so **Wan 2.2 VACE / LTX-2.3 3DREAL stays as the tight-interior fallback**, and nameplates stay in post.

Key links: huggingface.co/MiniMaxAI/MiniMax-H3 · github.com/MiniMax-AI/MiniMax-H3 · platform.minimax.io/docs/api-reference/video-generation-v2-create · github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt · artificialanalysis.ai/video · reddit.com/r/StableDiffusion/comments/1vl07cw · reddit.com/r/comfyui/comments/1vg3j6m · reddit.com/r/comfyui/comments/1vm8j2c · huggingface.co/MiniMaxAI/MiniMax-H3/discussions/65

---

## 6. The two models you originally named

### 6.1 Gemini Omni Flash (`gemini-omni-flash-preview`) — Google
Announced May 19, 2026 at I/O. Multimodal input (text/image/video/audio) → video. **Strengths:** conversational — prompt tags `<FIRST_FRAME>` vs `<IMAGE_REF_N>`, stateful edits via `previous_interaction_id` ("now dolly closer", "change the angle"), up to 7–10 reference images, camera vocabulary is a documented strength. **Limits:** **no last-frame interpolation** (docs explicit — cannot pin the endpoint of a flythrough), subject binding is "recognizable, not pixel-locked," text/logos unreliable, output 720p/24fps, 3–10s, paid tier ~$0.10/s, and practitioners call it "experimental" (safety false-positives burning credits, drift past ~4–5 edit turns).
**Your use:** look development and "edit this shot" iteration; not the anchor for a precise flythrough.
→ ai.google.dev/gemini-api/docs/omni · deepmind.google/models/model-cards/gemini-omni-flash

### 6.2 MiniMax Hailuo — the free tier (reality check)
Free ~100 daily credits ≈ **2–5 gens/day**, 720p/768p, 6s, **always watermarked**, **consumer ToS = non-commercial use**, slow queue. Paid Standard ~$9.99–14.99/mo (watermark can persist on Standard in some regions; Pro is the practical floor). API (no free tier): ~$0.27–0.53/clip, `aigc_watermark` defaults false. Camera = 15 bracket commands, purely linguistic. Subject Reference (S2V-01) = one image, drifts past 4–6s. **Conclusion: fine for tests; pay or use the API for anything commercial.** → hailuoai.video · platform.minimaxi.com/docs/api-reference/video-generation-fl2v

---

## 7. The make-or-break question: can the camera follow YOUR path?

**Short answer: not exactly — except with conditioning.**

- **Start+end frame conditioning** (supported by H3 FL2VA, Kling, Veo 3.1, Wan FLF2V, Hailuo-02, Pika): the model interpolates between your two rendered endpoints. Practitioners accept a ~5–10% endpoint hit and chain short 3–5s clips. Large/interior moves degrade into fades or a "lens switch." Veo's last frame is a "guide, not a hard constraint"; H3 resolves tightly onto both anchors but may reach the end early and hold a frozen tail.
- **Exact per-frame lock requires control conditioning:** feed the model a **depth video from Blender's Z pass**.
  - **Wan 2.2 VACE** `control_video` (depth/pose/flow) — the highest-fidelity path.
  - **Wan Fun-Control** (canny/depth/MLSD), **comfyui-blender-temporal** (Blender EXR Z/normal → per-frame ControlNet), RunComfy "Blender-to-ComfyUI AI Renderer 2.0".
  - **CameraCtrl / MotionCtrl** consume per-frame 4×4 camera matrices (export `cam.world_matrix`). **Wan-Move / ATI** use pixel point-trajectories.
- **V2V preserves motion best:** Wan 2.2 V2V (denoise 0.2–0.5), LTX-2 as a temporal upscaler for Wan (denoise ≤0.15), deterministic upscalers (RTX VSR, SeedVR2, RIFE) lock pixels by construction.
- **Known failure modes:** geometry warp in tight interiors, camera jitter/micro-tremor, extra "parasitic" dollies, flicker over 6–10s, object substitution, **nameplate text always degrades** (ViTeX-Bench: all 8 leading editors flicker/misspell — composite your labels, never let the model redraw them).

---

## 8. The pipeline — how to actually do it (step by step)

> This is the working flow. Each step names the exact tool, the decision point, and the fallback.

### Stage A — Prepare the asset (one-time)
1. **Clean CAD → Blender:** decimate topology, apply scale, build PBR materials (dielectric, brushed metal, rubber seals).
2. **Name your collections** — `cell_stack`, `busbars`, `inverter`, `cooling` — so the LLM agent can address parts by name.
3. *(Optional)* Buy a ready `blender_cycles` BESS container model (cgtrader.com) to shortcut interior modeling.

### Stage B — LLM builds the scene + camera (the orchestration layer)
4. Install **`blender-mcp`** (github.com/ahujasid/blender-mcp) or the **official Blender Lab MCP server** (blender.org/lab/mcp-server) — both expose `create_camera`, `add_keyframe`, `set_render_settings(engine=CYCLES)`, `render_from_camera`, `execute_blender_code`.
5. Ask the LLM for a **shot list** — *fly-in, tight interior sweep, exploded view, cell macro* — each a keyframed **4–8s camera path, slow moves**.
6. **Human gate:** render EEVEE/low-res previews per keyframe; approve before expensive passes. (LLM camera scripts are good at layout, still need supervision.)

### Stage C — Render the master (your ground truth)
7. **Cycles, GPU, OptiX** — transparent film; enable **Z, Normal, Object-ID, Mist** passes; write them with a compositor **File Output** node to **EXR MultiLayer** (plain PNG can't carry raw Z/normal).
8. Render once, from headless CLI: `blender -b scene.blend -o //frames/##### -F PNG -a`. ~1.5–3 min/frame at 1080p/512 samples on RTX 5090-class → **1000 frames ≈ 25–50 GPU-hours** (use Flamenco to farm; temporal/compositor denoise to avoid flicker).
9. Export **first frame, last frame, and a grayscale depth video** for the models.

### Stage D — Generate (the video models)
10. **Hero shots (primary):** feed first+last frames to **MiniMax H3 (hosted API)** or **Veo 3.1**, with a camera prompt that includes *refusals* for locked shots ("frame never moves, no push-in, no dolly"). 3–5 re-rolls per shot.
11. **Adherence/price alternative:** **Kling 3.0** start+end-frame mode (native 4K/60fps, best-in-class labels).
12. **Tight interiors (fallback — exact geometry):** condition **Wan 2.2 VACE** with the depth video, or use **LTX-2.3 3DREAL IC-LoRA** ("render-to-real": your grey-blockout render is the *only* source of truth for geometry — camera survives because motion is densely conditioned; ~$0.27 per 121 frames @720p on fal).
13. **Brand-consistency across shots:** MiniMax **Ref2VA** with up to 9 role-tagged cabinet images.

### Stage E — Finish (the part that makes it sellable)
14. **Composite your real logos/nameplates/labels in post** (After Effects/Resolve) — *never* in the prompt.
15. **Grade with one shared LUT** + film grain + slight motion blur; cut 4–8s clips with dissolves into a 30–60s edit.
16. **Quality bar:** product identity 30% · camera adherence 25% · realism 25% · artifacts 20%.

### The pipeline at a glance
```
CAD → Blender ──(blender-mcp, LLM shot list + camera)──→ EEVEE previews (human gate)
      │
      └─► Cycles master render (EXR: Beauty + Z + Normal; PNG frames) ──► first frame + last frame + depth video
                    │
                    ├─► [Hero]  MiniMax H3 (FL2VA) / Veo 3.1  — camera-language prompt + refusals
                    ├─► [Price] Kling 3.0 — start+end frames
                    └─► [Exact]  Wan 2.2 VACE (depth) / LTX-2.3 3DREAL — geometry-locked fallback
                    │
                    └─► pick 3–5 takes → composite nameplates → grade (shared LUT) → 30–60s edit
```

![Render-to-real example: cargo ship (clay render → photoreal)](bess-ai-flythrough-report/images/3dreal_cargo.gif)
*LTX-2.3 3DREAL "render-to-real": grey-blockout render → photoreal, camera locked (source: huggingface.co/fal/LTX-2.3-3DREAL-LoRA)*

![Render-to-real example: harbor (clay render → photoreal)](bess-ai-flythrough-report/images/3dreal_harbor.gif)
*Same pipeline, harbor scene (source: huggingface.co/fal/LTX-2.3-3DREAL-LoRA)*

![Render-to-real example: iron canyon](bess-ai-flythrough-report/images/3dreal_iron_canyon.gif)
*3DREAL strong v2 example (source: huggingface.co/fal/LTX-2.3-3DREAL-LoRA)*

---

## 9. Test plan + budget

**Test plan (same unit, one camera path):** render first frame, last frame, depth video, 1s preview → generate one 6–8s flythrough per model — **MiniMax H3, Veo 3.1, Kling 3.0, Seedance 2.5, Wan 2.2 VACE, LTX-2.3 3DREAL, Hailuo** → grade each on identity / camera adherence / realism / artifacts → advance the top 2.

| Item                                | API cost estimate                                            |
| ----------------------------------- | ------------------------------------------------------------ |
| MiniMax H3                          | ~$0.48–0.78 per 6s clip (768p→2K); **~$7.80/min at 2K**      |
| Veo 3.1                             | ~$0.5–3.5/clip depending on tier                             |
| Kling 3.0                           | ~$0.10–0.20 / 5s                                             |
| Seedance 2.5                        | ~$0.20–0.40 / clip                                           |
| Wan/LTX (self-host)                 | GPU time only; fal ~$0.27/121f@720p                          |
| Test round (6 models × 3–5 rerolls) | **~$50–300**                                                 |
| Polished 30–60s final edit          | **$200–800 (API)** · **<$100 (open-source + cloud)**         |
| Local GPU                           | RTX 4090 (24GB, slow for video) or 48GB-class; else cloud ~$1–3/hr |

---

## 10. Honest risks & mitigations

1. **Tight-interior geometry hallucinated** → depth conditioning (Wan VACE) or render the interior in Cycles and let AI add polish only.
2. **Brand markings garble** → composite overlays in post; keep markings out of macros.
3. **"Plastic" look** → richer PBR materials + normal-pass conditioning; negative prompts (`3d render, cgi`).
4. **Drift on fast moves** → slow cameras, short 4–8s clips, dissolves.
5. **Camera jitter / "stationary ignored"** → first+last anchors + explicit refusals (H3/Kling) + re-roll budget.
6. **Text corruption** → never in prompts; overlay in comp.
7. **Inconsistent look across shots** → one shared LUT + fixed exposure per render.
8. **License traps** → Hailuo free tier is non-commercial; **H3 open weights exclude US/EU/UK/KR (outputs included)** — use the hosted API; verify Wan/LTX licenses (Apache-2.0 OK) before local commercial rendering.

---

## 11. Master link library

**Models & docs**
- ai.google.dev/gemini-api/docs/omni · deepmind.google/models/model-cards/gemini-omni-flash · blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni
- deepmind.google/models/veo · developers.googleblog.com/en/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api · docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames
- huggingface.co/MiniMaxAI/MiniMax-H3 · github.com/MiniMax-AI/MiniMax-H3 · platform.minimax.io/docs/api-reference/video-generation-v2-create · platform.minimax.io/docs/api-reference/video-generation-fl2v · platform.minimaxi.com/docs/api-reference/video-generation-s2v · minimax.io/news/minimax-hailuo-02-start-end-frames-feature-is-now-live
- kling.ai/quickstart/ai-video-start-end-frames · kling.ai/blog/kling-ai-camera-control-video-guide · kling.ai/quickstart/klingai-video-3-model-user-guide
- seed.bytedance.com/en/seedance2_0 · seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- runway.com/research/introducing-runway-gen-4 · runway.com/news/introducing-aleph-2-and-edit-studio
- github.com/Wan-Video/Wan2.2 · github.com/ali-vilab/VACE · github.com/Lightricks/LTX-Video · huggingface.co/Lightricks/LTX-2.3
- openai.com/index/sora-2 (retiring Sept 2026)

**Pricing / free tiers**
- ai.google.dev/gemini-api/docs/pricing · hailuoai.video/doc/payment-policy.html · hailuoai.video/doc/terms-of-service.html (non-commercial consumer ToS) · platform.minimax.io/docs/guides/pricing-video · fal.ai · blogs.novita.ai/minimax-hailuo-2-3-...

**Blender ↔ LLM bridge**
- github.com/ahujasid/blender-mcp · blender.org/lab/mcp-server · github.com/youichi-uda/blender-mcp-pro · github.com/dwgx/blender-copilot · github.com/naab007/blender_mcp · github.com/threedle/ll3m · github.com/ETH-DISCO/reason-3d · github.com/EngineeringAI-LAB/Look-Before-Move · github.com/fathmamehnoor/PreViz

**Blender → AI workflows (the gold)**
- github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases (+ fork ismael-joffroy-chandoutis) · evolink.ai/cookbook/blender-to-video
- github.com/ismael-joffroy-chandoutis/comfyui-cinema-pipeline · github.com/ismael-joffroy-chandoutis/comfyui-blender-temporal
- blog.fal.ai/from-clay-3d-render-to-a-real-action-short-a-3d-to-ai-pipeline-with-total-control/ · huggingface.co/fal/LTX-2.3-3DREAL-LoRA
- flick.art/blog/blender-ai-filmmaking · runcomfy.com/comfyui-workflows/blender-to-comfyui-ai-renderer-2-0-workflow-cinematic-video-output · blogs.nvidia.com/blog/rtx-ai-garage-flux-ltx-video-comfyui-gdc/ · mickmumpitz.ai/guides/ai-powered-3d-animation-rendering

**Camera / trajectory control**
- github.com/ali-vilab/Wan-Move · github.com/bytedance/ATI · huggingface.co/morphic/reshoot-anything · github.com/hehao13/CameraCtrl · github.com/TencentARC/MotionCtrl · github.com/Stability-AI/stable-virtual-camera · github.com/Alexankharin/camera-comfyUI

**Benchmarks**
- artificialanalysis.ai/video · huggingface.co/spaces/Vchitect/VBench_Leaderboard · jinplu.github.io/WRBench · vitex-bench.github.io · t2v-compbench.github.io · iworld-bench.com · github.com/eBay/ConsID-Gen

**Community (best of the mined threads/posts)**
- X: x.com/reidhannaford/status/2069074506849685773 · x.com/noman23761/status/2071534020014563328 · x.com/Viggle_PINOC/status/2070183934265012392 · x.com/akiyoshisan/status/2071081230108660199 · x.com/bilawalsidhu/status/2059419767417487718 · x.com/GoogleAI/status/1979270059727196539 (Veo 3.1) · x.com/PJaccetturo/status/1978482410145628256 (brand ad build) · x.com/lorenzo_pravata/status/2080257056418787346 (Kling 3.0 ad pipeline) · x.com/emollick/status/2057874739817808223 (Omni edits)
- Reddit: r/comfyui 1sz9cf4 (Blender→AI 1:1 camera) · r/StableDiffusion 1v2i4jz (Blender depth→LTX-2.3 3DREAL) · 1ugg4tb (3D→photoreal IC-LoRA) · 1rb4ms7 (LTX-2 upscaler for Wan) · 1vl07cw (H3 camera controls) · r/comfyui 1vg3j6m + 1vm8j2c (H3 static-camera failures, drift) · r/KLING 1uuuy20 (3D renders → cartoon mode caveat) · r/VEO3 1u63xr9 (product demo in 1h) · r/aivideo 1phlpza (photoreal product integration) · r/HailuoAiOfficial 1ldy740 (credits complaints)
- LinkedIn: Kari Piirainen (Claude+BlenderMCP→Seedance) · Arminas Valunas (gray-shade→Seedance) · Mike Futia (exploded-view→Veo 3) · Eugenio Zabell (iPhone internal flythrough)
- BESS: sarvesh.co.uk/battery-energy-parks · theimagineers.com/en/news/baywa-r.e.-visualization · immixproductions.com/projects/terrasun-battery-energy-storage-system-animation/ · cobradesigns.net/portfolio/battery-energy-storage-system-container-bess · cgtrader.com (BESS PBR with `blender_cycles`)

**Video tutorials (YouTube)**
- miIDu04N7_4 (Dan Kieft, Seedance+Blender) · ikPGQGoUjQ0 (Yaroflasher) · r7H60u0kHRA (Max Novak, Blender MCP) · bxzZXYpTS64 (Thomas Lundström, Kling product) · kYtCVXaB9Jw (Matt Wolfe, Veo 3.1) · tPOOm1YRMRc (GeekatPlay, Wan FLF) · T-uBgMC6dG4 (Wan FLF2V ComfyUI) · aw6N7M4fPuo (Kling start/end) · la0iBk8g8_g (H3 full test — sponsored, treat critically) · hYKFv-V4jcw (H3 vs LTX vs Wan side-by-side)

---

## 12. Methodology, caveats & the vision question

- **Method:** 59 sub-agent sessions in 8 batches + this H3 update round (4 focused agents). Every claim was tagged primary/practitioner/hype in working notes; where sub-agents disagreed, both views are recorded here.
- **Vision analysis (your MIMO v2.5 request):** I attempted to use a sub-agent for image analysis, but it returned **`VISION_UNAVAILABLE`** — the Read tool reported *"this model does not support image input"*, and my own model reports the same. So the permission change did not take effect on the sub-agent's model, and **no frame-by-frame visual analysis was possible**. Demo/artifact claims in this report rest on written evidence (reviews, model cards, forum reports), not on me viewing frames. If you want visual QC of candidate clips, that is a fast follow-up once the sub-agent model is actually multimodal — the report's §9 test plan is designed so each candidate clip can be graded with vision.
- **Flagged / unverifiable:** "Hands-On-Video" camera benchmark (does not exist — closest real ones: WRBench / iWorld-Bench); "Veo 3.1 has 16 camera presets" (official copy says "cinematic presets" — treat the number as unverified); several X URLs recovered via mirrors/roundups (marked in §3); the Awesome-Blender-Seedance repo's canonical owner is ambiguous (Evolink-AI vs fork — verify before cloning); NVIDIA "GenVid"/"vai" USD tools not found.
- **Prices shift monthly** — re-verify live vendor pages before committing budget.