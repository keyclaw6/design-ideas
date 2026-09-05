# MiniMax H3 audio repair: low-res video, high-step audio regen, latent shrink

`x-2095427702325231977` · x · thread · ja · [source](https://x.com/aiaicreate/status/2095427702325231977) · [raw](../../../raw/items/x-2095427702325231977/)
**Author:** — (@aiaicreate) · **Published:** — · **Captured:** 2026-09-04T07:01:54Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [ai-video-generation](../../subjects/ai-video-generation/brief.md) · **Also:** — · **Roles:** technique, claim-source · **Platforms:** comfyui

**Summary.** Japanese post describes fixing MiniMax H3 video audio degradation by downscaling video, regenerating audio at high steps, compositing back, and shrinking latents to shorten generation while preventing drift.
**Question it answers.** How do ComfyUI users fast-fix MiniMax H3 video audio degradation without full rerenders?

**Claims.**
- `x-2095427702325231977#c1` (recipe, stated) Workflow downscales video, regenerates only audio at high steps, then composites with the original picture. — evidence: "映像を低解像度にして音声のみを高ステップで再生成し、元動画と合成する仕組み" [post]
- `x-2095427702325231977#c2` (recipe, stated) Shrinking latents is praised for cutting generation time while preventing A/V drift. — evidence: "Latentを縮小する工夫が賢いと好評" [post]
- `x-2095427702325231977#c3` (availability, demonstrated) Quoted t.co resolves to reddit.com/r/StableDiffusion/comments/1w5zh4z/bad_audio_fixed_with_fast_regen_audio/. www and old.reddit both HTTP 403. Amplify video on the root tweet is 10.354 s at 854×472. Downscale/step integers still missing. — evidence: "Quoted 2095427723858751958 text is the Reddit URL. urllib www + old.reddit → HTTP 403 Blocked. fxtwitter root video duration 10.354 width 854 height 472." [note]
**Numbers.** H3 audio-repair demo duration: 10.354 seconds (note)
**Recipe.** —
**Techniques.** [faceless-video-pipeline](../../techniques/faceless-video-pipeline.md), [agent-video-editing](../../techniques/agent-video-editing.md)
**Tools.** [minimax-h3](../../tools/minimax-h3.md)
**Links.** https://www.reddit.com/r/StableDiffusion/comments/1w5zh4z/bad_audio_fixed_with_fast_regen_audio/
**Related items.** —
**Media.** —
**Thread.** captured_partial · reported 5 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
