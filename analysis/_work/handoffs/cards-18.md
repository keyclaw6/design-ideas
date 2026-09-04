# Handoff: cards-18

**Worker:** cards-18  
**Batch:** batch-18.txt  
**Written at:** 2026-09-04

## IDs owned (19)

github-oso95-scroll-world, web-chatgpt-training, web-meigen-ai, x-2032330665081839791, x-2086838432102228008, x-2087346803268260043, x-2088016749849682120, x-2088600811307979218, x-2089701163117494735, x-2091118605392019658, x-2091622497393225801, x-2091951051343593929, x-2092790491741823402, x-2093160779960774982, x-2093669411685110141, x-2094110975045554191, x-2094742312433684496, x-2095085408208196006, x-2095427702325231977

## IDs done (19)

All 19 above — `card.json` written and `validate_cards.py` exit 0.

## Skipped

None (no pre-existing `card.json` in batch).

## Blocked / failed

None.

## Disposition summary

| disposition | count | ids |
|-------------|-------|-----|
| analyze | 15 | github-oso95-scroll-world, web-chatgpt-training, web-meigen-ai, x-2032330665081839791, x-2086838432102228008, x-2087346803268260043, x-2088016749849682120, x-2091118605392019658, x-2091622497393225801, x-2093160779960774982, x-2093669411685110141, x-2094110975045554191, x-2094742312433684496, x-2095085408208196006, x-2095427702325231977 |
| shelf | 4 | x-2088600811307979218, x-2089701163117494735, x-2091951051343593929, x-2092790491741823402 |

Legacy `extra.filtered` was true on x-2088600811307979218, x-2089701163117494735, x-2091951051343593929, x-2092790491741823402, and x-2093160779960774982. Shelved the first four after re-judge; **x-2093160779960774982** re-judged **analyze** (REAP-pruned MLX quant with HumanEval and VRAM numbers).

## Readiness

| readiness | ids |
|-----------|-----|
| ready | github-oso95-scroll-world, web-chatgpt-training, web-meigen-ai |
| ready-with-gaps | x-2032330665081839791, x-2086838432102228008, x-2087346803268260043, x-2088016749849682120, x-2091118605392019658, x-2091622497393225801, x-2093160779960774982, x-2093669411685110141, x-2094110975045554191, x-2094742312433684496, x-2095085408208196006, x-2095427702325231977 |
| shelved | x-2088600811307979218, x-2089701163117494735, x-2091951051343593929, x-2092790491741823402 |

Gap notes: `thread-partial` on X items with pre-existing `thread.json`; `linked-page-unfetched` on x-2093669411685110141 (designengineer.tools), x-2095427702325231977 (ComfyUI link in replies not captured).

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "id": "x-2093160779960774982",
    "from": "uncategorized",
    "to": "local-inference-models",
    "why": "HamsterResearch REAP-pruned Qwen MLX 4-bit with 39GB VRAM and HumanEval numbers; legacy filtered flag ignored per runnable local quant detail."
  },
  {
    "id": "x-2092790491741823402",
    "from": "local-inference-models",
    "to": "shelf/noise/availability-announcement",
    "why": "Merge Gateway discount post with per-token pricing only; subject exclusion_rule treats pure gateway promos as shelf noise."
  }
]
```

## Notes for threads worker

- x-2094742312433684496: partial reply capture in comments.md (Filip counter-claim, author rebuttal).
- x-2093160779960774982: `media/media_0.jpg` is an MP4 container; typed as `video`.
- x-2094110975045554191: attached `media_0.mp4` dashboard recording.
