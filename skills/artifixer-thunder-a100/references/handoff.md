# Handoff for a successor agent

Prepared 2026-09-07 in design-ideas on branch `cursor/bess-splat-mesh-plan-aa42`. The preparing chat is meant to be **terminated** after this skill lands. Do not wait for that chat. Do not treat hung cloud chat `bc-dd0309db-64cd-4c55-8c89-6ee190f2aa42` as recoverable.

## What you are being asked to do

After the human has a **paid Thunder Compute** account: mint an API token in the browser, rent **one A100 80GB** (16 vCPU, 400 GB disk), run ArtiFixer 14B + 3DGRUT on BESS phone stills, dump RGB-D, download, **delete** the instance, mesh locally with Open3D TSDF.

Quality-first: five or six really good Gaussian splats **and** corresponding meshes. Ignore splat file size and train time. Old $10 cap / 1.3B / 10k cheap cut are **dead**.

Read [../SKILL.md](../SKILL.md) and treat it as **unproven**. Update it as you go.

## What is already on disk (this machine)

| Path | Role |
|------|------|
| `skills/artifixer-thunder-a100/` | This skill (source of truth) |
| `~/.cache/splat-mesh-maxqual/` | Runtime root (keys, `.env`, tarball, logs). Symlink `/tmp/splat-mesh-maxqual` may exist. |
| `~/.cache/splat-mesh-maxqual/upload/scenes.tar.gz` | ~223M packed 1600px stills — **do not commit** |
| `~/.cache/bess-splat-plan/scene-zip5/colmap/` | C4 COLMAP 181/185 |
| `~/Downloads/splat-objects/` | Source JPEGs (do not mix folders) |
| `~/.tnr/bin/tnr` | Thunder CLI |
| `~/.cache/bess-gpu-rent/` | **Old RunPod playbook — do not execute** |

If `scenes.tar.gz` is missing, `pack_scenes.sh` rebuilds it from splat-objects + C4 COLMAP.

## Auth state when this was written

Thunder console in Cursor browser was **signed out**. User had **not** confirmed the account exists. Default `DRY_RUN=1`. Do not rent until they have paid **and** you are actually executing.

## Cost (estimate, unproven)

A100 sticker ~$1.09/hr + extra vCPUs $0.48 + extra disk $0.09 ≈ **$1.66/hr**. Five long scenes ~67–124 GPU-h → **~$110–205**. Tell the user before `DRY_RUN=0` if that still matches their intent.

## Mesh decision (already adjudicated)

CUDA for train + PLY/RGB-D dumps. Local Open3D TSDF + later Blender UV. ArtiFixer3D writes Gaussians (ckpt + PLY + USDZ particles), **not** triangles. `dump_rgbd.py` is supposed to emit OpenCV RDF camera-to-world dumps; TSDF inverts pose. **Unproven on a live box.**
