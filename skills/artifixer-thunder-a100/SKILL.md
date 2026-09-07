---
name: artifixer-thunder-a100
description: Rent a Thunder Compute A100 80GB, run ArtiFixer 14B + 3DGRUT on BESS phone stills, dump RGB-D, delete the instance, mesh locally. Use after the user has paid on Thunder, or when repeating this splat-to-mesh GPU run. Pipeline is unproven — update this skill as you go.
license: MIT
metadata:
  author: design-ideas
  unproven: "true"
  last_verified: never
  provider: thunder-compute
  gpu: a100-80gb
---

# ArtiFixer on Thunder A100 (unproven)

**Everything in this skill is unproven on a live Thunder box.** Parsers, SSH user, Qwen VRAM, 14B construct, RGB-D dump, and local TSDF have been dry-run or reasoned from docs — not confirmed end-to-end. The first live run **must** treat this file as a draft: when something fails or a better command is found, **edit this skill immediately** (SKILL.md + `references/learnings.md` + scripts). Goal: one living skill in [agent-skills.io](https://agentskills.io/specification) format that a later agent can follow without this chat.

Do not invent a second skill. Patch this one.

## When to use

- User has (or will have) a **paid Thunder Compute** account and wants BESS Gaussian splats + meshes.
- Successor agent in another harness is taking over GPU rent / ArtiFixer / download / delete.
- Repeating the same pipeline later.

**Not for:** RunPod, Vast.ai bidding, H100-by-default, Brush/Spirula CPU salvage, mixing C5+C6, Woshixing `20250806_*`, C8 alcove fans.

## Read first

| File | Why |
|------|-----|
| [references/learnings.md](references/learnings.md) | Facts from live runs (empty until first GPU hour) |
| [references/handoff.md](references/handoff.md) | Why this exists; objects; kill-gates; cost |
| [references/decision.md](references/decision.md) | A100 SKU, 14B stack, no auto-H100 |
| [references/human.md](references/human.md) | Human job: account + card only |
| [references/browser.md](references/browser.md) | Agent: mint token in browser, never paste into chat |

Scripts: `skills/artifixer-thunder-a100/scripts/playbook/`. Runtime artifacts (token, PEM, tarball, instance id) stay in `$HOME/.cache/splat-mesh-maxqual/` — **never git those**.

## Unproven — update as you go

After **every** first-of-kind event, commit an update to this skill in the same branch (or a follow-up commit):

1. Append a dated bullet to `references/learnings.md` (command, actual JSON shape, error, fix).
2. If the procedure changed, rewrite the matching section in this SKILL.md.
3. If a script was wrong, fix the script **and** mention it in learnings.
4. Set frontmatter `metadata.last_verified` to the ISO date of the last successful live step (or `partial: <step>`).
5. Keep SKILL.md **under 500 lines**. Park dumps in `references/`.

Priority unknowns (fill these first):

- Real `tnr create --json` / `tnr status --json` shapes vs `parse_tnr_*.py`
- SSH user (`ubuntu` vs `root`) and whether create-response PEM works
- Qwen3-VL-30B-A3B caption VRAM vs 80 GB after 3DGRUT
- Wan-14B construct RAM on 128 GB vs 96 GB
- Whether `dump_rgbd.py` emits `*.color.png` + `*.depth.npy` + `*.pose.txt` + `K.txt`
- Whether local Open3D TSDF actually meshes those dumps
- A100 OOM path: `--num_views` 6 → 4 → 2
- Thunder billing: auto-pay, delete vs stop, snapshot trap

## Hard locks (do not weaken unless the user says so)

- Provider: **Thunder Compute**. No RunPod. Vast is not this skill.
- GPU: **A100 80GB**. Do **not** auto-rent H100. If A100 is stock-out, stop and ask.
- SKU: `tnr create --gpu a100 --num-gpus 1 --vcpus 16 --template base --disk 400` (~$1.66/hr with extra vCPU + disk). Fallback **12 vCPU / 96 GB**. Never 8 vCPU (64 GB kills 14B).
- Quality: pin ArtiFixer `a392c4dfe17459ef9952407accdb9fcdcdddba98`; checkpoint **`artifixer-14b.pt`** + `Wan-AI/Wan2.1-T2V-14B-Diffusers`; captions via `--phases caption` (Qwen is **hardcoded** in ArtiFixer — `--text_encoder_model_id` is Wan UMT5, not Qwen); 3DGRUT **30000**; ArtiFixer3D **30000** + 3D+.
- Images: **1600px** longest edge. Issue **#13**: never 100% of frames as selected; hold out every 3rd non-macro.
- FA3 **off** on Ampere. Uninstall flash-attn; SDPA only.
- No nested Docker. Disk **400 GB**. Do **not** snapshot (Thunder snapshots bill monthly).
- **Delete** the instance when done (`tnr delete -y`), do not leave it stopped.
- Default **`DRY_RUN=1`**. Set `DRY_RUN=0` only when executing for real after token + paid account.
- Mesh: CUDA trains + dumps; **local** Open3D TSDF. No Splat2Mesh. No Inria 2DGS/SuGaR/GOF for shipped meshes.

## Human vs agent

Human: create Thunder account + payment card (billing UI min credit **$10**). Ping that it exists.

Agent: mint API token, `tnr login --token`, create A100, SCP, install, C4 kill-gate, remaining scenes, download, **delete**, local TSDF. Do not ask the human to paste tokens or click Create.

Kill switch: `touch "$HOME/.cache/splat-mesh-maxqual/KILL"`

## Setup after they have paid

1. Confirm console is signed in (not “Signed Out”; Billing enabled). Login: https://console.thundercompute.com/login
2. Follow [references/browser.md](references/browser.md): create token `splat-mesh-maxqual` at `/settings/tokens`.
3. Install CLI if needed: `curl -fsSL https://raw.githubusercontent.com/Thunder-Compute/thunder-cli/main/scripts/install.sh | bash` — `tnr` lives at `~/.tnr/bin/tnr` (seen at 2.0.71; re-check version and record it in learnings).
4. `tnr login --token '<token>'` then write to `~/.cache/splat-mesh-maxqual/.env` (`chmod 600`): `TNR_API_TOKEN=...`. **Never** paste the token into chat.
5. Dry-run from repo root:

```bash
export PATH="$HOME/.tnr/bin:$PATH"
DRY_RUN=1 bash skills/artifixer-thunder-a100/scripts/playbook/go.sh
```

6. Live (only with paid account + token + user intent to rent):

```bash
DRY_RUN=0 bash skills/artifixer-thunder-a100/scripts/playbook/go.sh
```

`tnr` uses global `--json` and `-y`. `tnr connect` is PTY-only — use `ssh` + `tnr scp`. `tnr scp` wants a **numeric identifier ≤20 chars**, not UUID.

## Pipeline order (GPU)

1. Pack stills (`pack_scenes.sh`) — skip if `~/.cache/splat-mesh-maxqual/upload/scenes.tar.gz` already exists unless `FORCE_PACK=1`.
2. Create A100 16 vCPU (fallback 12). Parse `identifier`, `uuid`, `key` → `instance.pem` + `instance.env` under the cache root.
3. Wait RUNNING; SSH (ubuntu then root; instance PEM then playbook key).
4. SCP remote scripts + `scenes.tar.gz`.
5. `03_install.sh` + `04_weights.sh`.
6. **C4 kill-gate first:** `05_prepare.sh c4-cabinet` (phases `prepare,reconstruct,render,scale` — **no caption**). Then `c4_gate.py`: `recon_results/` PNGs (≥8), `ckpt_30000.pt`, selected ≠ 100% of frames. If 30k recon is still needle soup / gate fail → **abort all splat**, download whatever exists, delete.
7. Caption / infer / ArtiFixer3D / export C4.
8. Other scenes: exhaustive COLMAP (`colmap_scene.sh`; C7 min 70%, others 30%). Same ArtiFixer loop if they pass.
9. `dump_rgbd.py` inside `09_export.sh` (unproven).
10. Download → `tnr delete -y` → `12_mesh_local.sh` (Open3D TSDF).

Unload / empty CUDA cache after Qwen caption before 14B infer.

OOM: `--num_views` **6 → 4 → 2**. Do not start at 1.3B. Do not train C8. Do not merge C5 and C6. Drop `20260610_140213.jpg` from C6. C2 includes chassis closeups.

## Objects

Stills: `~/Downloads/splat-objects/` (hardlinks of unique Samsung JPEGs). Do not mix folders.

| ID | Folder | Plan |
|----|--------|------|
| C4 | `04-assembled-open-cabinet` | Kill-gate first. COLMAP already at `~/.cache/bess-splat-plan/scene-zip5/colmap/sparse/0/` (181/185). Fire-COM macros out (`wide.json`). |
| C5 | `05-envicool-lcu-closed` | Own scene |
| C6 | `06-envicool-lcu-open` | Own scene; never merge with C5 |
| C1 | `01-pcs-inverter-open` | Train |
| C2 | `02-bcu-b30-chassis` | Train if COLMAP ≥30% |
| C7 | `07-zg-mod-52-face` | Sixth splat only if COLMAP ≥70% + sharp |
| C8 | `08-alcove-fans` | Skip |

C4 Brush/Spirula already failed (needle soup). ArtiFixer is a CUDA hail-mary, not a guaranteed fix.

## CLI / API facts (pre-live, verify)

- Create JSON: `identifier` (int), `uuid`, `key` (private PEM). Status JSON may be a **map** id→item, not a list.
- REST delete: `https://api.thundercompute.com:8443/v1/instances/{uuid}/delete` (scripts use `tnr delete`).
- Remote workdir in scripts: `/home/ubuntu/workspace`. If SSH user is `root`, fix scripts and this paragraph.
- Caption: no writing dummy text onto `caption.h5` on failure.

## After the run

1. Results expected under `~/Downloads/splat-mesh-maxqual/`.
2. Confirm instance is **deleted** (not stopped).
3. Update this skill from `references/learnings.md`.
4. Catalog note: `raw/notes/artifixer-gpu-run.md` — keep it pointing here.

## Graphify

This repo uses graphify. After editing `catalog/`, `raw/`, or this skill’s scripts: `graphify update .`
