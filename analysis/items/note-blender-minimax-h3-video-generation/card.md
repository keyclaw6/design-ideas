# BESS flythrough research — Blender MCP camera path to MiniMax H3 and depth conditioning

`note-blender-minimax-h3-video-generation` · note · note · en · [source](raw/notes/blender-minimax-h3-video-generation.md) · [raw](../../../raw/notes/)
**Author:** — (@—) · **Published:** 2026-08-15T00:00:00Z · **Captured:** 2026-09-04T17:00:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [blockout-to-video-flythrough](../../subjects/blockout-to-video-flythrough/brief.md) · **Also:** [ai-video-generation](../../subjects/ai-video-generation/brief.md) · **Roles:** reference, technique · **Platforms:** blender, fal, comfyui

**Summary.** Internal research note mapping a photoreal BESS cabinet flythrough: LLM-driven Blender blockout and camera via blender-mcp, Cycles/EXR renders, then first/last-frame or depth-video conditioning into MiniMax H3, Kling, Veo, or Wan VACE with licensing and budget guidance.
**Question it answers.** How do you pipeline Blender agent camera work into MiniMax H3 and depth-conditioned video models for a product flythrough?

**Claims.**
- `note-blender-minimax-h3-video-generation#c1` (recipe, stated) The dominant 2026 recipe is Blender blockout plus LLM camera path, then feed reference video or first/last frames to a video model for photoreal output. — evidence: "Blender blockout + LLM-authored camera path (via `blender-mcp`) → render reference video + first/last frames → feed to a video model" [note]
- `note-blender-minimax-h3-video-generation#c2` (pricing, stated) MiniMax H3 hosted API pins Blender first and last frames via FL2VA at roughly $0.13/s for 2K while open weights exclude US/EU/UK/KR outputs. — evidence: "**$0.08/s (768p), $0.13/s (2K)** ≈ **$7.80/min at 2K**; US/EU region selectable" [note]
- `note-blender-minimax-h3-video-generation#c3` (recipe, stated) Tight interior camera moves need depth-video conditioning such as Wan 2.2 VACE rather than prompt-only commercial models. — evidence: "condition the model with a **depth video from Blender's Z pass** (Wan 2.2 VACE / LTX-2.3 3DREAL)" [note]
- `note-blender-minimax-h3-video-generation#c4` (availability, demonstrated) leftover28 unused MiniMax Create Video Generation Task docs 442,375 B titles the H3 video-generation POST and names MiniMax-H3 as a new-generation open general-purpose multimodal video model. leftover28 unused HF api/models/MiniMaxAI/MiniMax-H3 20,848 B: 4,913 likes, 5,118,457 downloads, pipeline image-text-to-video, license other / minimax-h3-community-license-agreement. leftover28 does not submit a create-task call or run a Blender blockout through H3. — evidence: "leftover28 minimax-docs 442375 B; hf-minimax-h3 4913 likes / 5118457 downloads." [note]
- `note-blender-minimax-h3-video-generation#c5` (availability, demonstrated) leftover30 unused platform.minimax.io create-video docs host string is leftover28 #c4 (442,375 B + HF 4,913 / 5,118,457). No new integers. — evidence: "leftover30-2026-09-05.json skip minimax create-video already leftover28." [note]
**Numbers.** polished 30-60s API budget: 200-800 USD (note)
**Recipe.** —
**Techniques.** [blender-blockout-camera](../../techniques/blender-blockout-camera.md), [seedance-motion-reference](../../techniques/seedance-motion-reference.md), [seedance-motion-reference](../../techniques/seedance-motion-reference.md)
**Tools.** [minimax-h3](../../tools/minimax-h3.md), [wan-vace](../../tools/wan-vace.md), [kling](../../tools/kling.md), [veo](../../tools/veo.md), [blender-mcp](../../tools/blender-mcp.md)
**Links.** repo (https://github.com/ahujasid/blender-mcp), product (https://platform.minimax.io/docs/api-reference/video-generation-v2-create), https://huggingface.co/MiniMaxAI/MiniMax-H3, https://platform.minimax.io/docs/api-reference/video-generation-v2-create
**Related items.** [x-2091497597743612379](../x-2091497597743612379/card.md), [x-2093380307735232543](../x-2093380307735232543/card.md), [x-2093064017468145963](../x-2093064017468145963/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: [x-2093374092795846745](../x-2093374092795846745/card.md), [x-2093064017468145963](../x-2093064017468145963/card.md)
