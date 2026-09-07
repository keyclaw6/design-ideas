# Decision record — max-quality splat → mesh

Provider: **Thunder Compute** (not RunPod). GPU: **A100 80GB**, not H100.

SKU: `tnr create --gpu a100 --num-gpus 1 --vcpus 16 --template base --disk 400`
- 16 vCPUs × 8 GiB = **128 GB host RAM**. A100 default 8 vCPU is 64 GB and can kill 14B construct.
- Fallback: same A100 at **12 vCPU / 96 GB**. Do **not** auto-rent H100.
- Disk 400 GB (A100 x1 max 500).
- FA3: **off** (Ampere). SDPA only. `03_install.sh` uninstalls flash-attn.

Cost: GPU **$1.09/hr** + extra vCPUs $0.48 + extra disk $0.09 ≈ **$1.66/hr**. Five long scenes ~67–124 h → **~$110–205**.

SSH: parse `tnr create --json` → `identifier` (tnr scp/delete), `uuid` (REST), `key` (PEM).

Quality unchanged: ArtiFixer pin `a392c4dfe17459ef9952407accdb9fcdcdddba98`, `artifixer-14b.pt`, Wan 14B, Qwen captions (`--phases caption`), 3DGRUT 30k + ArtiFixer3D 30k + 3D+, 1600px, issue #13 holdout. OOM: `--num_views` 6 → 4 → 2.

Objects: C4 kill-gate first, then C5, C6, C1, C2 if COLMAP ≥30%, C7 iff ≥70% + sharp. Skip C8. Never merge C5/C6.

Mesh: CUDA RGB-D dump; local Open3D TSDF.

Human: account + card only. Agent: token, rent, run, download, delete.
