# Local / edge inference, open-weight model releases (local-inference-models)

## local-inference-models — scope

Open-weight model releases with runnable detail (Qwen GGUFs, Unsloth, Bonsai, Edge8), inference engines (FreeToken, MLX tricks), cheap hosted endpoints with numbers (RunInfra, AMD Token Factory), VRAM math. Pure now-live-on-gateway or discount posts are noise/availability-announcement.

Exclusion: Gateway promo with no runnable detail → shelf noise.

Priority `later`. Owner aliases: local LLM, GGUF, FreeToken.
Expected primary range [8, 13]. This roster has **10** primary and **0** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## local-inference-models — what the owner is trying to decide

Later lane. Decide which open-weight / GGUF / MLX / MoE-offload notes have runnable numbers. Pure “now live on gateway X” posts were shelved as noise.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## local-inference-models — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=5, technique=2, example=1, claim-source=7, reference=3.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (5):
- [Unsloth Qwen3.8-27B Dynamic GGUF runs locally on about 17GB RAM](../../items/x-2088281537427235320/card.md) — tool, reference — Unsloth announces Qwen3.8-27B local inference via Dynamic GGUF quantizations targeting about 17GB RAM, plus NVFP4 quants on NVIDIA hardware
- [RunInfra hosts full BF16 DeepSeek V4 Flash at 278 tok/s](../../items/x-2088594942482374759/card.md) — tool — RunInfra announces full-precision BF16 DeepSeek V4 Flash inference at about 278 tokens per second with $0.13 per million input and $0.27…
- [Unsloth Dynamic V3 Qwen3.8-27B GGUFs — 10% accuracy gain, 8GB 1-bit path](../../items/x-2090103470015828184/card.md) — tool, reference — Unsloth releases Qwen3.8-27B Dynamic V3 GGUF quants claiming over 10% better accuracy on Div-300 and KLD versus other providers, plus…
- [FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints](../../items/x-2091150763418620133/card.md) — tool, claim-source — Long-form thread on Berkeley FlashML FreeToken: profiles PCIe vs CPU bandwidth per machine to split MoE expert cache misses, serves…
- [HamsterResearch Qwen3.8-Flash REAP-288 MLX 4-bit runs 180B-class on 39GB](../../items/x-2093160779960774982/card.md) — tool, claim-source — Eyal Toledano announces HamsterResearch Qwen3.8-Flash-Next-REAP-288-MLX-4bit: MLX-native 4-bit quant pruned from 512 to 288 experts via…

First role `technique` (1):
- [Qwen expert-on-disk streaming runs full model in 37GB at 40 tok/s](../../items/x-2093429897188299113/card.md) — technique, claim-source — Follow-up on Qwen3.8-Flash-Next storing sixty percent of MoE experts on disk with on-demand streaming; author reports full-expert eval…

First role `claim-source` (4):
- [AMD Token Factory daily free inference credits roundup](../../items/x-2087240056037908509/card.md) — claim-source, reference — Promo post listing AMD Token Factory free daily credits for DeepSeek V4 Flash, Qwen3.6 35B, MiniCPM5, and MiniCPM-V46 plus a SuperGrok…
- [Edge8-35B sparse MoE running on-device on an iPhone](../../items/x-2087562269807030754/card.md) — claim-source, example — Announcement of Edge8-35B, a 35B ultra-sparse MoE with dynamic expert planner and SSD-streaming runtime, demoed on one iPhone at 44…
- [Bonsai-1.7B hits 90 tok/s CPU decode on Android without NPU or GPU](../../items/x-2087962842985058365/card.md) — claim-source, technique — Glenn Sonna reports PrismML Bonsai-1.7B decode rising from 64 to 90 tokens per second on the same Android device using CPU only—no NPU…
- [Unnamed Berkeley/MIT inference engine benchmarks vs llama.cpp and Ollama](../../items/x-2090930324817498246/card.md) — claim-source — Promotional thread claiming UC Berkeley and MIT researchers open-sourced a new inference engine running DeepSeek-V4-Flash 284B at 25…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints](../../items/x-2091150763418620133/card.md)

## local-inference-models — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [moe-expert-offload](../../techniques/moe-expert-offload.md) — Stream or prune MoE experts to disk so large models run on one GPU.
- [dynamic-quantization](../../techniques/dynamic-quantization.md) — GGUF/MLX dynamic quant so a local model fits a given VRAM envelope.
- [agent-harness-ops](../../techniques/agent-harness-ops.md) — Harness, control plane, folder-as-agent, and multi-agent ops that a later judge can rerun.

## local-inference-models — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [edge8-35b](../../tools/edge8-35b.md)
- [unsloth](../../tools/unsloth.md)
- [qwen3-8-27b](../../tools/qwen3-8-27b.md)
- [runinfra](../../tools/runinfra.md)
- [llama-cpp](../../tools/llama-cpp.md)
- [freetoken](../../tools/freetoken.md)

## local-inference-models — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `x-2087240056037908509#c1` | AMD Token Factory resets about ten dollars of free usage daily for listed models on developer.amd.com. | stated | [AMD Token Factory daily free inferenc…](../../items/x-2087240056037908509/card.md) |
| `x-2087240056037908509#c2` | DeepSeek V4 Flash, Qwen3.6 35B, MiniCPM5, and MiniCPM-V46 are named as zero-cost models on AMD Token Factory. | stated | [AMD Token Factory daily free inferenc…](../../items/x-2087240056037908509/card.md) |
| `x-2087562269807030754#c1` | Demo reports 44 tokens per second at about 1.06 GB peak memory on one iPhone without cloud. | stated | [Edge8-35B sparse MoE running on-devic…](../../items/x-2087562269807030754/card.md) |
| `x-2087562269807030754#c2` | The stack pairs a jointly trained dynamic expert planner with an SSD-streaming inference engine. | stated | [Edge8-35B sparse MoE running on-devic…](../../items/x-2087562269807030754/card.md) |
| `x-2087962842985058365#c1` | Bonsai-1.7B reached 90 tok/s decode on the same Android device, up from 64 tok/s, CPU only. | stated | [Bonsai-1.7B hits 90 tok/s CPU decode …](../../items/x-2087962842985058365/card.md) |
| `x-2087962842985058365#c2` | The reported speed is almost 3× faster than the llama.cpp reference on that setup. | stated | [Bonsai-1.7B hits 90 tok/s CPU decode …](../../items/x-2087962842985058365/card.md) |
| `x-2088281537427235320#c1` | Dynamic GGUF path targets about 17GB RAM for Qwen3.8-27B local runs. | stated | [Unsloth Qwen3.8-27B Dynamic GGUF runs…](../../items/x-2088281537427235320/card.md) |
| `x-2088281537427235320#c2` | Unsloth also uploaded NVFP4 quantizations for NVIDIA boxes. | stated | [Unsloth Qwen3.8-27B Dynamic GGUF runs…](../../items/x-2088281537427235320/card.md) |
| `x-2088594942482374759#c1` | RunInfra claims the fastest full-precision V4 Flash inference at 278.3 tok/s with sub-dollar-per-million-token pricing. | stated | [RunInfra hosts full BF16 DeepSeek V4 …](../../items/x-2088594942482374759/card.md) |
| `x-2090103470015828184#c1` | Dynamic V3 Qwen3.8-27B GGUFs claim over 10% higher accuracy than other quants on Div-300 and KLD benchmarks. | stated | [Unsloth Dynamic V3 Qwen3.8-27B GGUFs …](../../items/x-2090103470015828184/card.md) |
| `x-2090103470015828184#c2` | Unsloth also ships 1-bit quants retaining about 77% accuracy runnable on 8GB RAM. | stated | [Unsloth Dynamic V3 Qwen3.8-27B GGUFs …](../../items/x-2090103470015828184/card.md) |
| `x-2090930324817498246#c1` | The engine runs DeepSeek-V4-Flash 284B at 25 tok/s on an RTX 5090 system. | unverified | [Hesamation paraphrases FreeToken as a…](../../items/x-2090930324817498246/card.md) |
| `x-2090930324817498246#c2` | Reported 1.46× faster than llama.cpp on the same test; Ollama cannot serve that model. | unverified | [Hesamation paraphrases FreeToken as a…](../../items/x-2090930324817498246/card.md) |
| `x-2091150763418620133#c1` | FreeToken serves Qwen3.6-35B at 39.3 tokens per second on an 8GB GPU by exploiting MoE sparsity. | stated | [FreeToken MoE inference engine: PCIe/…](../../items/x-2091150763418620133/card.md) |
| `x-2091150763418620133#c2` | The engine profiles PCIe and CPU bandwidth once per machine and splits each step's expert misses proportionally betwe… | stated | [FreeToken MoE inference engine: PCIe/…](../../items/x-2091150763418620133/card.md) |

Full set: claims.jsonl (29 rows)

## local-inference-models — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- weights actually downloadable
- quant recipe (GGUF, MLX, MoE offload)
- VRAM / token numbers present
- license allows local use
- hosting discount posts excluded

## local-inference-models — thread coverage

X items in primary roster: 10. captured_full=0, captured_partial=10, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2087240056037908509](../../items/x-2087240056037908509/thread.md) | captured_partial | 35 | 3 | 0 |
| [x-2087562269807030754](../../items/x-2087562269807030754/thread.md) | captured_partial | 32 | 3 | 1 |
| [x-2087962842985058365](../../items/x-2087962842985058365/thread.md) | captured_partial | 15 | 1 | 1 |
| [x-2088281537427235320](../../items/x-2088281537427235320/thread.md) | captured_partial | 204 | 2 | 2 |
| [x-2088594942482374759](../../items/x-2088594942482374759/thread.md) | captured_partial | 72 | 2 | 1 |
| [x-2090103470015828184](../../items/x-2090103470015828184/thread.md) | captured_partial | 227 | 3 | 2 |
| [x-2090930324817498246](../../items/x-2090930324817498246/thread.md) | captured_partial | 32 | 3 | 2 |
| [x-2091150763418620133](../../items/x-2091150763418620133/thread.md) | captured_partial | 72 | 3 | 3 |
| [x-2093160779960774982](../../items/x-2093160779960774982/thread.md) | captured_partial | 29 | 1 | 1 |
| [x-2093429897188299113](../../items/x-2093429897188299113/thread.md) | captured_partial | 38 | 2 | 2 |

## local-inference-models — gaps and open questions

Primary readiness: ready=0, ready-with-gaps=10. Gap tags: thread-partial=2, linked-page-unfetched=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which GGUF/MLX recipes still match the published VRAM numbers on a 24 GB card?
- Are MoE offload tricks worth the I/O hit for design-agent local use?

If this subject drops below 6 primary items after a future reclass, merge it into `a neighbour` and delete the folder.

## local-inference-models — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [agent-harness-loops](../agent-harness-loops/brief.md)

