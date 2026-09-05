# NVIDIA ArtiFixer: diffusion repair for sparse 3D Gaussian reconstructions

`github-nv-tlabs-ArtiFixer` · github · repo · en · [source](https://github.com/nv-tlabs/ArtiFixer) · [raw](../../../raw/items/github-nv-tlabs-ArtiFixer/)
**Author:** NVIDIA SIL (@nv-tlabs) · **Published:** — · **Captured:** 2026-09-02T17:45:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [gaussian-splatting](../../subjects/gaussian-splatting/brief.md) · **Also:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Roles:** tool, technique · **Platforms:** other

**Summary.** Official NVIDIA SIL repo for ArtiFixer (SIGGRAPH 2026): auto-regressive diffusion models that enhance and extend 3DGRUT-based reconstructions. Ships training, eval, and data-processing code plus Hugging Face checkpoints for repairing holes in splat captures.
**Question it answers.** How do I repair sparse or incomplete 3D Gaussian splat reconstructions after capture?

**Claims.**
- `github-nv-tlabs-ArtiFixer#c1` (capability, stated) ArtiFixer uses auto-regressive diffusion to enhance and extend 3D reconstructions built on 3DGRUT. — evidence: "Enhancing and extending 3D reconstruction with auto-regressive diffusion models (SIGGRAPH 2026)" [linked-page]
- `github-nv-tlabs-ArtiFixer#c2` (availability, stated) Hugging Face hosts artifixer-14b.pt (~16.9B) and artifixer-1.3b.pt (~1.68B) checkpoints. — evidence: "Hugging Face checkpoints — `artifixer-14b.pt` (16.9B) and `artifixer-1.3b.pt` (1.68B)" [linked-page]
- `github-nv-tlabs-ArtiFixer#c3` (benchmark, demonstrated) leftover27 unused arXiv 2603.00492 abs 44,589 B names ArtiFixer (de Lutio et al.; SIGGRAPH 2026; v2 5 May 2026) and claims 1–3 dB PSNR over 3DGS baselines, with PDF artifixer.pdf listed at 91,742 KB. research.nvidia.com/labs/sil/projects/artifixer/ 18,793 B names ArtiFixer / ArtiFixer3D / ArtiFixer3D+ on MipNeRF 360, DL3DV, and Nerfbusters. huggingface.co/api/models/nvidia/ArtiFixer 850,636 B and 65 likes. leftover27 does not download the 91,742 KB PDF or rerun those PSNR tables. — evidence: "leftover27 artifixer-abs 44589 B; artifixer-nvidia 18793 B; hf-artifixer 65 likes. 1–3 dB PSNR." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** repo (https://github.com/nv-tlabs/ArtiFixer), paper (https://arxiv.org/abs/2603.00492), product (https://research.nvidia.com/labs/sil/projects/artifixer/), https://huggingface.co/nvidia/ArtiFixer, https://arxiv.org/abs/2603.00492, https://research.nvidia.com/labs/sil/projects/artifixer/, https://huggingface.co/api/models/nvidia/ArtiFixer
**Related items.** [web-arcana-splat2mesh](../web-arcana-splat2mesh/card.md), [github-oso95-scroll-world](../github-oso95-scroll-world/card.md), [github-scottstts-threejs-awesome-graphics-agent-skills](../github-scottstts-threejs-awesome-graphics-agent-skills/card.md), [web-fal-ai](../web-fal-ai/card.md), [web-utsubo](../web-utsubo/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
