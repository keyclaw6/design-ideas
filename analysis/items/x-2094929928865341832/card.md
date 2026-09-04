# NVIDIA ArtiFixer tweet: video diffusion repairs sparse 3D scans

`x-2094929928865341832` · x · announcement · en · [source](https://x.com/0x0SojalSec/status/2094929928865341832) · [raw](../../../raw/items/x-2094929928865341832/)
**Author:** Md Ismail Šojal (@0x0SojalSec) · **Published:** 2026-09-01T23:26:31Z · **Captured:** 2026-09-02T17:38:09Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [gaussian-splatting](../../subjects/gaussian-splatting/brief.md) · **Also:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Roles:** reference, claim-source · **Platforms:** other

**Summary.** Aggregator recap of NVIDIA open-source ArtiFixer: video diffusion synthesizes missing camera angles on broken 3D scans then reconstructs the scene; claims seventy-times speed, one-to-four steps, and about three dB over SOTA with Hugging Face weights linked.
**Question it answers.** What does NVIDIA ArtiFixer do for broken or sparse 3D Gaussian reconstructions?

**Claims.**
- `x-2094929928865341832#c1` (capability, stated) ArtiFixer uses video diffusion to generate camera angles never captured and reconstructs the scene from generated frames. — evidence: "It uses video diffusion to generate the camera angles you never captured, then reconstructs the scene from the generated frames." [post]
- `x-2094929928865341832#c2` (benchmark, unverified) The tweet claims ArtiFixer finishes in one to four steps and beats SOTA by about three dB. — evidence: "- 70x faster, Finishes in 1 to 4 steps
- Beats SOTA by 3dB" [post]
**Numbers.** inference steps cited: 1-4 steps (post); PSNR improvement cited: 3 dB (post)
**Recipe.** —
**Techniques.** [splat-pipeline](../../techniques/splat-pipeline.md)
**Tools.** [artifixer](../../tools/artifixer.md)
**Links.** repo (https://github.com/nv-tlabs/ArtiFixer), paper (https://arxiv.org/abs/2603.00492), product (https://huggingface.co/nvidia/ArtiFixer), https://research.nvidia.com/labs/sil/projects/artifixer/
**Related items.** [github-nv-tlabs-ArtiFixer](../github-nv-tlabs-ArtiFixer/card.md), [x-2094648474377839018](../x-2094648474377839018/card.md), [x-2094826117056414132](../x-2094826117056414132/card.md)
**Media.**
`media/video.mp4` (video, carries_technique=true) — Sixteen second comparison video showing ArtiFixer3D+ producing a sharp bicycle-and-bench scene versus blurry 3DGUT, GenFusion, and GSFixer outputs.
`media/thumb.jpg` (image, carries_technique=true) — Static four-panel grid comparing 3DGUT, GenFusion, GSFixer noise against a sharp ArtiFixer3D+ bicycle beside a park bench.
**Thread.** captured_full · reported 2 · captured 2 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: ['github-nv-tlabs-ArtiFixer'] · compare with: [github-nv-tlabs-ArtiFixer](../github-nv-tlabs-ArtiFixer/card.md), [x-2094648474377839018](../x-2094648474377839018/card.md)
