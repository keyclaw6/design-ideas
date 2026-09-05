# Codex

**Slug:** `codex` · **Kind:** product · **URL:** https://x.com/EHuanglu/status/2065843739340509693 · **Canonical item:** [x-2065843739340509693](../items/x-2065843739340509693/card.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md), [ai-video-generation](../subjects/ai-video-generation/brief.md), [blockout-to-video-flythrough](../subjects/blockout-to-video-flythrough/brief.md), [design-agent-skills](../subjects/design-agent-skills/brief.md), [landing-ui-motion](../subjects/landing-ui-motion/brief.md)
**Referenced by (4):**
- [Codex driving Blender rigid-body demo at a desk setup](../items/x-2065843739340509693/card.md) — example, technique — blockout-to-video-flythrough
- [Codex auto-research loop: 212× faster QR kernel on GPU Mode](../items/x-2074912810803560497/card.md) — example, claim-source — agent-harness-loops
- [video-use plus Codex for agent-driven video editing](../items/x-2092980272819999227/card.md) — tool, example — ai-video-generation
- [Blume.codes landing page build breakdown (X article)](../items/x-2094524951025914278/card.md) — technique, example — landing-ui-motion

<!-- NOTES:START -->
212× tweet vs blog (fetched 2026-09-04 https://sankalp.bearblog.dev/autoresearch/):

The **blog title and body say 232×**, not 212×. GPU Mode × Core Automation contest: batched compact-Householder QR (`qr_v2`). Blog (contest write-up): placed **12th of 183**; baseline `torch.geqrf` ~419,000 µs; author’s tracked **1,805 µs** → 232×; lineage 108,803 → 1,805 µs; **>1500 submissions / 14 days**. Treat the card’s “212×” as a stale tweet number.

**popcorn CLI** (first-party, `gpu-mode/popcorn-cli`): `curl -fsSL https://raw.githubusercontent.com/gpu-mode/popcorn-cli/main/install.sh | bash` then `popcorn register discord`. Starter `https://raw.githubusercontent.com/gpu-mode/reference-kernels/main/problems/linalg/qr_v2/submission.py`. Test: `popcorn submit --leaderboard qr_v2 --gpu B200 --mode test submission.py`. Leaderboard: `popcorn submit --leaderboard qr_v2 --gpu B200 --mode leaderboard submission.py`. NCU via `--profile-brev`.

**Live board 2026-09-04** https://www.gpumode.com/leaderboard/773 (ended 2026-06-29): geomean µs, B200. #1 nikhilbarhate99 **704.865 µs**. **sankalp1999 is 26th at 3916.103 µs** (`submission_homura.py`, 420 LOC) — not 12th / 1805 µs. Quote the blog as a contest-time snapshot; quote the board for the public ranking. Seven shapes include batched 512² (640 batch) through 4096².

**2026-09-04 capture — popcorn `submit_logs/` still missing.** `sankalp1999` GitHub user 200, **82** public repos, twitter `dejavucoder`. No public repo name/description matches popcorn / qr / gpu / submit / kernel / homura / autoresearch. Five public gists (timer, bearblog CSS, BigInt, pylearnings, perceptron) — none are submit logs. GitHub code search `submit_logs user:sankalp1999` **401** (needs auth). `gpu-mode/popcorn-cli` README has `popcorn submit --output results.json` and `popcorn submissions list` — no public `submit_logs/` tree. Re-fetch of the live board HTML is now a **1.6 KB SPA stub** (no integers); keep the earlier 26th / 3916.103 µs quote. Blog `sankalp.bearblog.dev/autoresearch/` returned **403** this pass (was fetchable earlier).

**2026-09-04 capture — GPU Mode JSON API restores the board.** `GET https://www.gpumode.com/api/leaderboard/773` **200 / 50,694 B** (`analysis/_work/captures/gpumode-773-api.json`). `data.name` is **`qr`** (not `qr_v2`), `lang` Python, `gpu_types` `["B200"]`, `deadline` 2026-06-30, `time_left` ended, **85** B200 rows. sankalp1999: rank **26**, score **0.003916102791313636** (3916.103 µs), `submission_id` **796445**, `file_name` `submission_homura.py`, 420 LOC, 86 submissions, `submission_time` 2026-06-14T23:59:36Z. #1 nikhilbarhate99 **704.865 µs** id **795226**. Other `/api/submission/796445` paths return the 1.6 KB HTML shell. Author reply `t.co/hBpJvk3YZV` **301 → photo/1**, not `submit_logs/`. Harbor id is now the API `submission_id`; the author’s public log tree is still missing.

**2026-09-05 capture — blog 200 again; `submit_logs/` is local.** `https://sankalp.bearblog.dev/autoresearch/` **200 / 158,069 B** (prior pass **403**). Body: **12th of 183**; **232×** from ~**419,000 µs** `torch.geqrf` to **1,805 µs**; lineage 108,803 → 1,805. `submit_logs/` is a **local workspace folder** (“logs provided by the evaluator for each submission”; AGENTS.md: keep logs under `submit_logs/`). popcorn CLI is the named submit path. Do not treat this as a public GitHub dump. Receipt `sankalp-autoresearch-2026-09-05.json`.

**2026-09-05 leftover19.** `gpu-mode/popcorn-cli` MIT **178★**. README **12,541 B** still names `popcorn submit --leaderboard qr_v2 --profile-brev` and the `qr_v2` starter. `gpu-mode/reference-kernels` **303★** NOASSERTION. No public `submit_logs/`. Receipt `leftover19-2026-09-05.json`.
<!-- NOTES:END -->
