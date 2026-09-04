# Thread — HamsterResearch Qwen3.8-Flash REAP-288 MLX 4-bit runs 180B-class on 39GB (x-2093160779960774982)

**Status:** captured_partial · **Author thread:** none · **Replies reported:** 29 · **Captured:** 1 · **Relevant:** 1 · **Unfetched:** 28 · **Truncated:** False
**Fetch log:** x-web-dom→ok (2026-09-04T17:54:20Z); fxtwitter-api→ok (2026-09-04T17:54:20Z)
**Raw payloads:** `raw/items/x-2093160779960774982/thread-raw/x-web-dom-20260904T175326Z.html`

**Author continuation (0 posts).**
**Quoted.**
> **@EyalToledano** · 2093160782733124024
> The folks at @Alibaba_Qwen recently released Qwen3.8-Flash-Next, a 180B-class sparse MoE with 48 layers, 512 routed experts each and top-10 routing (for 6B active params).

Like most MoE models there's a distribution for how much work each expert tends to do overall. I charted https://t.co/0ukOvJ4enf

> **@EyalToledano** · 2093160785966948458
> I measured an eleven-point pruning ladder and 288 is where quality-per-GB peaks among usable builds. 

Aggregate metrics (KL divergence against the stock model) suggest pruning deeper, but sampled rare-token reliability collapses below 288

At 256 experts, the model produces an https://t.co/JvYFKa8Wd6

> **@EyalToledano** · 2093160787996999774
> Huggingface Links

Model
https://t.co/kxeAbtS6Mh

MTP drafter
https://t.co/lKJEKcujWr

> **@EyalToledano** · 2093160789603385820
> + 2 variants:

Qwen3.8-Flash-Next-REAP-288-MLX-8bit
- 8 bit, 90.9% HumanEval, 70 GB resident
- q8 27% smaller than the q4 stock model
https://t.co/KzGrK5bhe8 

Qwen3.8-Flash-Next-REAP-384-MLX-8bit
- 4 bit with 384 experts, 92.1% HumanEval, 51 GB resident
https://t.co/1d3vB2m2qo

> **@EyalToledano** · 2093160791658660082
> This model could go fast. REALLY FAST. 

MLX inference today (mlx_lm, mlx_vlm and other friends) is constrained by components it depends on. That's why I'm writing a pure MLX inference engine - to get the most out of our machines.

It opens up techniques and possibilities (i.e.

**Relevant replies (1 of 1 captured).**
> **@EyalToledano** · 2093290575449526712 · depth 1 · answered-question
> @EyalToledano @HamsterResearch @huggingface Thanks for the reap_kept_experts.json. Working on adding SSD expert streaming to oMLX and was wanting a useful base for expert pinning, and this is it.

**Dropped as noise:** 0 replies (praise, emoji, bots, unrelated promo).
