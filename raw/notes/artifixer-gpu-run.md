# ArtiFixer GPU run — Thunder Compute, max quality

**Date:** 2026-09-07  
**Status:** skill checked in; **not rented**. Console was signed out when prepared.  
**Skill (source of truth):** [`skills/artifixer-thunder-a100/SKILL.md`](../../skills/artifixer-thunder-a100/SKILL.md)  
**Runtime cache:** `~/.cache/splat-mesh-maxqual/` (token, PEM, tarball — not git)

Human job is **only** Thunder account + payment card (billing UI minimum credit is **$10**). Agent owns API token, SSH key from `tnr create`, **A100 16 vCPU / 128 GB RAM** (~$1.66/hr), 14B + Qwen + ArtiFixer3D, RGB-D dump, local TSDF, delete.

Do not use RunPod. Do not auto-rent H100. Default `DRY_RUN=1`.

The GPU pipeline is **unproven**. The agent that actually rents must update the skill as they go (`references/learnings.md` + SKILL.md).
