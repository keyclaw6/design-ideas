## What they are actually doing

Aggregator recap (@0x0SojalSec), not an NVIDIA account. The linked model is real: **ArtiFixer** (NVIDIA Spatial Intelligence Lab). Tweet stats mix paper claims (1–3 dB PSNR over SOTA; “3dB” is the top of that range) with product-speak (“70x faster”, “1 to 4 steps”, optional text prompt).

**ArtiFixer** — few-step causal auto-regressive video model that enhances/extends sparse 3D reconstructions (3DGS / **3DGRUT**).

- Paper: de Lutio, Fischer, Chang, Zhang, Wu, Ren, Shen, Tothova, Gojcic, Turki. SIGGRAPH 2026. arXiv:2603.00492 (cs.CV, v2 2026-05-05). PDF: project `assets/paper.pdf`.
- Code: `https://github.com/nv-tlabs/ArtiFixer` (Apache-2.0, 635★ / 56 forks at capture). Clone with 3DGRUT submodule.
- Weights: `https://huggingface.co/nvidia/ArtiFixer` — `artifixer-14b.pt` (Wan2.1-T2V-14B-Diffusers, ~16.9B) and `artifixer-1.3b.pt` (Wan2.1 1.3B, ~1.68B), plus stage-1 bidirectional teachers `artifixer-s1-*.pt`. Research/dev only.
- Pipeline: Phase I finetunes a bidirectional video diffusion teacher with **opacity-aware noise mixing** (RGB latent mixed with noise via rendered opacity; camera control + optional text). Phase II **Self-Forcing-style DMD** distills a causal AR model that rolls out hundreds of frames in one pass.
- Variants: **ArtiFixer** (direct novel views), **ArtiFixer3D** (distill generated frames back into 3DGRUT), **ArtiFixer3D+** (AR post-process on ArtiFixer3D, as in Difix3D+).

## Fit for BESS / 3D marketing

Fixes holes and blur in sparse plant/site scans by synthesizing missing camera paths, then optionally baking that into the splat. Closer to “repair the flythrough capture” than mesh real-to-sim (Lucida).

## Open questions

- Whether 14B inference is practical off NVIDIA’s eval recipe (HF quotes 8.36 FPS at 4 steps on one GPU).
- License/use of Wan2.1 base weights vs ArtiFixer checkpoints.
- Tweet “70x faster” vs which baseline (not restated on the HF card in this capture).
