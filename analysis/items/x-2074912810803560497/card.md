# Codex auto-research loop: 212× faster QR kernel on GPU Mode

`x-2074912810803560497` · x · article · en · [source](https://x.com/dejavucoder/status/2074912810803560497) · [raw](../../../raw/items/x-2074912810803560497/)
**Author:** Sankalp (@dejavucoder) · **Published:** — · **Captured:** 2026-09-04T06:50:57Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** example, claim-source · **Platforms:** codex

**Summary.** X post announcing a blog write-up where Codex ran an auto-kernel search on GPU Mode's qr_v2 QR decomposition problem and claims a 212× speedup over baseline through propose-run-keep-winner loops.
**Question it answers.** What does a measured Codex autoresearch loop on a fixed GPU kernel benchmark look like?

**Claims.**
- `x-2074912810803560497#c1` (result, stated) Author claims Codex auto-kerneling on GPU Mode's qr_v2 problem achieved 212× faster kernel performance over baseline. — evidence: "how I achieved a 212x faster kernel over baseline with codex in GPU Mode's qr_v2 problem" [post]
- `x-2074912810803560497#c2` (counter-claim, demonstrated) Live GPU Mode API leaderboard/773 (ended) ranks sankalp1999 26th at 3916.103 µs (submission_id 796445, submission_homura.py, 420 LOC, 86 submissions) — not the blog's contest-time 12th / 1,805 µs. #1 nikhilbarhate99 is 704.865 µs (id 795226). — evidence: "GET https://www.gpumode.com/api/leaderboard/773 200 / 50,694 B. B200 rankings[25]: user_name sankalp1999 rank 26 score 0.003916102791313636 submission_id 796445. HTML /leaderboard/773 is a 1.6 KB SPA stub." [note]
- `x-2074912810803560497#c3` (availability, demonstrated) Official API names the contest qr (Python, B200, deadline 2026-06-30, time_left ended) with 85 ranked users. Author reply t.co/hBpJvk3YZV 301s to a photo, not submit_logs/. Public submit_logs/ is still missing; the Harbor id is 796445 from the JSON API. — evidence: "API data.name=qr, gpu_types=[B200], n_rankings=85. t.co/hBpJvk3YZV Location=.../photo/1. See analysis/_work/captures/gpumode-773-api.json." [note]
- `x-2074912810803560497#c4` (result, demonstrated) sankalp.bearblog.dev/autoresearch/ re-fetched 200 / 158,069 B (prior pass 403). First-party: 12th of 183; 232× from ~419,000 µs torch.geqrf baseline to 1,805 µs. submit_logs/ is a local workspace folder (“logs provided by the evaluator for each submission”; AGENTS.md: keep logs under submit_logs/). Not a public GitHub tree. popcorn CLI is named as the GPU Mode submit path. Do not collapse tweet 212× / blog 232× / live board 26th 3916.103 µs. — evidence: "analysis/_work/captures/sankalp-autoresearch-2026-09-05.json. Quote: I placed 12th out of 183 participants, ending up with a 232x speedup. The 232x number above comes from comparing the rough 419,000 µs baseline to the final 1,805 µs tracked result." [note]
**Numbers.** kernel speedup vs baseline: 212 × (post); live board rank (sankalp1999): 26 of 85 (linked-page); live board geomean: 3916.103 µs (linked-page); GPU Mode submission_id: 796445  (linked-page)
**Recipe.** —
**Techniques.** [autoresearch-loop](../../techniques/autoresearch-loop.md), [autoresearch-loop](../../techniques/autoresearch-loop.md)
**Tools.** [codex](../../tools/codex.md)
**Links.** —
**Related items.** [x-2080856252687745093](../x-2080856252687745093/card.md), [x-2032671842230501729](../x-2032671842230501729/card.md)
**Media.** —
**Thread.** captured_partial · reported 22 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2080856252687745093](../x-2080856252687745093/card.md), [web-chatgpt-training](../web-chatgpt-training/card.md)
