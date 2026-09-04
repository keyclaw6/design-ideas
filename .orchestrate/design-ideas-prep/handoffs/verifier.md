# Verifier handoff — design-ideas analysis corpus

**Branch:** `main`  
**Verifier run:** 2026-09-04  
**Spec:** `docs/ANALYSIS_STRUCTURE.md` §9

## VERDICT: PASS

**Failing check numbers:** none

---

## Mechanical checks (1–39, 42–44)

Confirmed via `python3 scripts/analysis/verify.py`:

| Checks | Result |
|--------|--------|
| 1–39 | PASS |
| 42–43 | PASS |
| 44 | PASS (clean working tree at handoff commit) |

---

## Check 40 — analyze sample (manual)

**Score: 10/10 PASS** (≥9/10 required)

Sampling rule: sort analyze ids ascending, N = count, index `floor(k·N/10)` for k = 0..9.

| id | Verdict | Notes |
|----|---------|-------|
| `github-LessieAI-people-search-bench` | PASS | Summary describes MIT benchmark artifact. Both claim evidence quotes match `page.md` leaderboard and methodology (Tavily, κ=0.84). Analyst question on eval methodology is concrete. No media. |
| `web-cartier-ballon-bleu` | PASS | Summary names PDP features (fit, engraving, motion guide). Claim evidence (“125–190 mm”, animated user guide) in `page.md`. Question targets luxury PDP motion/personalization pattern. No media. |
| `web-tinylaunch-directories` | PASS | Summary states paid directory submission service with DR guarantees. Evidence “0–10 \| DR 15–20” and “~10 days” in `page.md`. Question asks what paid DR-lift service exists. No media. |
| `x-2087254502210490739` | PASS | Summary describes Stanford Control Plane paper thread, not hype alone. All three claim quotes verbatim in `post.md`. Question on multi-agent handoff failure is analyst-grade. No media. |
| `x-2088308976278790258` | PASS | Summary describes CadX hexacopter text-to-CAD demo. Claim evidence (“hexacopter…cadxstduio.in”) in `post.md`. Question asks what CadX output looks like on drone hardware. No media. |
| `x-2090839282831270173` | PASS | Summary names Splat.js in-browser training. Claim evidence matches `post.md`. Question on in-browser SfM+splat training is specific. Video thumb description consistent with post crediting PixelBilly/arrival_space (MP4 stored as media_0.jpg). |
| `x-2091970263088816272` | PASS | Summary names session-migrate CLI. Both claims quoted from `post.md` (harness list, GitHub URL). Question on cross-harness session migration is actionable. No media. |
| `x-2093179838249251011` | PASS | Summary describes upcoming Splat2Mesh local no-GPU tool. Japanese evidence quotes in `post.md`. Question on printable mesh conversion tool is analyst-grade. Video attachment described as splat-to-mesh demo (consistent with announcement + attached MP4). |
| `x-2094069236524061059` | PASS | Summary describes Leonxlnx/taste-skill repo and install path. Spanish evidence (layout/hierarchy/spacing/typography/motion, npx command) in `post.md`. Question on reducing visual slop via design skill is real. No media. |
| `x-2094984529853530345` | PASS | Summary chains ChatGPT/Gemini/Ezgif/Claude scroll-scrub workflow. Claim c1 (300 frames via Ezgif) and c2 (React/Vite/Tailwind/Framer Motion) evidenced in `comments.md` author thread. Question on scroll-scrub hero without hand CSS is analyst-grade. `thumb.jpg` matches description (Braix hero, glassmorphism brain widgets, scroll indicator). |

**Misses:** none

---

## Check 41 — shelf sample (manual)

**Score: 10/10 PASS** (≥9/10 required)

Sampling rule: `floor(k·N/10)` over `shelf.jsonl` line order.

| id | Verdict | Notes |
|----|---------|-------|
| `github-deedy-qr-data-transfer` | PASS | Reason names QRFerry QR fountain-code transfer repo (`page.md`). `out-of-scope` / `real-artifact-no-subject` fits §4.5. |
| `x-2084613319558635940` | PASS | Reason cites unnamed AI-agent explainer with no linked artifact (`post.md` has praise only). `noise` / `engagement-bait` fits. |
| `x-2087280401475600698` | PASS | Reason cites 650% ROI Polymarket whale copy promo (`post.md`). `noise` / `promo-no-artifact` fits. |
| `x-2087873421094896122` | PASS | Reason cites `cathrynlavery/diagram-design` star spike repost without new angle (`post.md`). `duplicate` / `same-artifact-no-new-angle` fits; `duplicate_of` targets analyzed card. |
| `x-2088830609615397333` | PASS | Reason cites `amicro.vercel.app` Mono Charts repost duplicating primary (`post.md`). `duplicate` / `same-artifact-no-new-angle` fits. |
| `x-2090787985721856437` | PASS | Reason cites 100M GLM-5.3 token weekend giveaway Aug 22–24 (`post.md`). `noise` / `availability-announcement` fits. |
| `x-2091560960066793483` | PASS | Reason cites beige website quest with no URL/repo (`post.md` one-liner). `noise` / `engagement-bait` fits. |
| `x-2091918691747189053` | PASS | Reason cites Marmoset Toolbag 5.03 SpaceMouse support (`post.md`). `out-of-scope` / `real-artifact-no-subject` fits. |
| `x-2092658333337469133` | PASS | Reason cites Blender showcase + `#StudioShare` CTA (`post.md`). `noise` / `engagement-bait` fits. |
| `x-2093690856637182435` | PASS | Reason quotes “$1,000,000 content system…bookmark this” hook with no playbook (`post.md`). `noise` / `engagement-bait` fits. |

**Misses:** none
