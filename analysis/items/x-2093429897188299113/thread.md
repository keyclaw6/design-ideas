# Thread — Qwen expert-on-disk streaming runs full model in 37GB at 40 tok/s (x-2093429897188299113)

**Status:** captured_partial · **Author thread:** none · **Replies reported:** 38 · **Captured:** 2 · **Relevant:** 2 · **Unfetched:** 36 · **Truncated:** False
**Fetch log:** x-web-dom→ok (2026-09-04T17:54:20Z); fxtwitter-api→ok (2026-09-04T17:54:20Z)
**Raw payloads:** `raw/items/x-2093429897188299113/thread-raw/x-web-dom-20260904T175327Z.html`

**Author continuation (0 posts).**
**Quoted.**
> **@HamsterResearch** · 2093986486089584779
> "which quant should I download?" is a question you may never have to answer again

the team @HamsterResearch has figured out how to kill it with pMLX. download once at full precision (bf16) and the engine re-fits it to your machine on the fly, based on the job you give it

tell https://t.co/nMOmYBKEMx

**Relevant replies (2 of 2 captured).**
> **@EyalToledano** · 2093987103306641890 · depth 1 · link
> @HamsterResearch https://t.co/ud5cHirR69

> **@EyalToledano** · 2093451189337924073 · depth 1 · answered-question
> @EyalToledano @HamsterResearch I had exactly this idea earlier today and came up with a prototype - using Hamster's REAP'd expert selection as a pinned source of truth and then letting analytics inform which experts to hold in the cache and which to evict. oMLX fork with this &amp; some optimisations I discovered

**Dropped as noise:** 0 replies (praise, emoji, bots, unrelated promo).
