# Judgment worksheet: local / edge inference (local-inference-models)

Later lane. Owner aliases: local LLM, GGUF, FreeToken. Gateway “now live” posts with no numbers were shelved as noise.

## local-inference-models — short stack to try

1. **Weights + a quant recipe you can download.** Unsloth Qwen3.8-27B Dynamic GGUF ~17GB RAM ([x-2088281537427235320](../../items/x-2088281537427235320/card.md)). Dynamic V3 + 8GB 1-bit path and “+10% vs others” ([x-2090103470015828184](../../items/x-2090103470015828184/card.md)).
2. **MoE offload / streaming on one box.** Must-read FreeToken PCIe/CPU split + prefill checkpoints ([x-2091150763418620133](../../items/x-2091150763418620133/card.md)). Qwen expert-on-disk 37GB / 40 tok/s ([x-2093429897188299113](../../items/x-2093429897188299113/card.md)). HamsterResearch REAP-288 MLX 4-bit, 180B-class on 39GB ([x-2093160779960774982](../../items/x-2093160779960774982/card.md)).
3. **On-device demos (treat as research).** Edge8-35B on iPhone 44 tok/s ([x-2087562269807030754](../../items/x-2087562269807030754/card.md)). Bonsai-1.7B 90 tok/s CPU on Android ([x-2087962842985058365](../../items/x-2087962842985058365/card.md)).
4. **Hosted numbers, not local.** RunInfra BF16 DeepSeek V4 Flash 278 tok/s at $0.13/$0.27 per M ([x-2088594942482374759](../../items/x-2088594942482374759/card.md)). AMD Token Factory daily credits ([x-2087240056037908509](../../items/x-2087240056037908509/card.md)). Unnamed Berkeley/MIT engine vs llama.cpp ([x-2090930324817498246](../../items/x-2090930324817498246/card.md)).

## local-inference-models — axis scores

| item | weights downloadable | quant recipe | VRAM / token numbers | license allows local | hosting-discount excluded? |
|---|---|---|---|---|---|
| Unsloth Qwen3.8-27B GGUF | claimed HF | Dynamic GGUF / NVFP4 | ~17GB RAM stated | Unsloth + Qwen (check cards) | yes — local path |
| Unsloth Dynamic V3 | claimed | V3 + 1-bit 8GB path | +10% Div-300/KLD stated | same | yes |
| FreeToken | engine; model BYO | MoE cache split | PCIe vs CPU profile | OSS claimed | yes |
| Qwen expert-on-disk | implied same family | 60% experts on disk | 37GB / 40 tok/s stated | check Qwen | yes |
| HamsterResearch REAP-288 | claimed MLX | 4-bit, 512→288 experts | 39GB / 180B-class stated | unknown | yes |
| Edge8-35B | announcement | sparse MoE + SSD stream | 44 tok/s iPhone stated | unknown | yes (device) |
| Bonsai-1.7B | announcement | CPU decode | 64→90 tok/s Android | unknown | yes (device) |
| RunInfra BF16 | hosted | none (full BF16) | 278 tok/s; $0.13/$0.27 | n/a (hosted) | no — this *is* a host |
| AMD Token Factory | hosted credits | n/a | ~$10/day stated | n/a | no — discount post with a number |
| Berkeley/MIT engine tweet | unnamed | vs llama.cpp/Ollama | 25? tok/s on 284B stated | unknown | treat as promo until named |

## local-inference-models — claims that need a receipt

- FreeToken split and prefill checkpoints — README + paper body ([freetoken](../../tools/freetoken.md)). Apache-2.0. Paper: 39.3 tok/s on 8 GB 4060 / 35B; TTFT <44 s vs baselines >150 s; 5090 77–83 tok/s (35B) and 22–25 tok/s (284B). Local clone: **499** `.py` files; `torch>=2.11,<2.12`; README now **290B+** (older NOTES 284B). Still no local `profile` here.
- Unsloth “+10% on Div-300 and KLD” — provider blog; save the table.
- 17GB / 8GB / 37GB / 39GB envelopes — restated; time tokens/s on a named GPU/CPU.
- Edge8 44 tok/s and Bonsai 90 tok/s — device demos, no traces.
- RunInfra 278 tok/s and AMD ~$10/day — host quotes; re-check the public pricing page.
- Unnamed Berkeley/MIT engine — do not install from a teaser.

## local-inference-models — do not treat as load-bearing

- AMD daily credits as a “local stack.”
- Any gateway-only availability tweet already on the noise shelf.
- Ranking language about engines vs llama.cpp until the repo is named.

## local-inference-models — next capture work

1. Paper tok/s/TTFT + clone file count are on the tool NOTES. Remaining: one `profile` on a real GPU (none here).
2. Unsloth `Qwen3.8-27B-GGUF` is **apache-2.0**; Q4_0 file **16.06 GB**; UD-IQ1_S **6.19 GB**. Filenames + sizes on [unsloth](../../tools/unsloth.md). Remaining: a local load timing those envelopes.
3. Leave Edge8 / Bonsai as device research until weights are linked.
