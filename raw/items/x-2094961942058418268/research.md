## What they are actually doing

Tokuyama’s post is a Japanese recap of a LinkedIn share of **Lucida**, a ByteDance Seed research system. Not a shipping product. No public GitHub repo at `lucida-r2s/lucida` (404). Project page + arXiv only.

**Lucida** — parse / generate / place for composable real-to-sim

- Paper: Qin, Wang, Yang, Long, Zhang, Wang, Ye, Zhang, Li. *Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling*. arXiv:2608.30821 (cs.CV, v1 2026-08-31). ByteDance Seed + Peking + Zhejiang. https://lucida-r2s.github.io/
- **Parse:** keyframes → instance association → scene graph. Each node carries multi-view RGB, masks, partial point clouds, 3D boxes, referring text.
- **Generate:** VLM + Set-of-Mark → amodal (occlusion-free) object image → **Seed3D 2.0** image-to-3D (Gu et al., arXiv:2605.13862; https://seed.bytedance.com/en/seed3d_2_0). Separate editable meshes, not a fused splat.
- **Place:** **GizmoAct** — VLM treats a 3D editor gizmo as a GUI. Closed-loop render → one executable pose/scale edit → stop. 9-DoF. SFT + RL. Recovers from bad inits (Boxer, Any6D-style, SAM 3D).
- Reported: scene-level det mAP 0.592 vs Boxer 0.351 on R2S-Scene; ADD-SB@0.05 83.4% vs 57.8% on CA-1M; scene F-Score 0.924 vs SAM 3D 0.794 on R2S-Scene.

**Seed3D 2.0** (the lift model, Apr 2026): coarse-to-fine geometry, unified PBR, optional parts/URDF/Isaac Sim. Lucida uses it as the per-object generator, not as the full scene composer.

## Fit for BESS / 3D marketing

Indoor walkthrough video → object-level meshes you can rearrange is closer to a plant/site twin than a cinematic Gaussian splat flythrough. No public weights/code; paper + project page only.

## Open questions

- Code / weights release (none found).
- Whether Seed3D 2.0 is callable independently of Lucida (Volcano / Seed “Try Now”).
