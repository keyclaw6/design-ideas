# cards-20

**Worker:** cards-20  
**Batch:** 20 (`analysis/_work/reports/batch-20.txt`)  
**Written:** 2026-09-04T18:25:00Z

## IDs owned (19)

```
github-punkpeye-awesome-mcp-servers
web-cloudflare-kitesurf
web-nqz-ai-search-prompt-generator
x-2057113327508345047
x-2086920236079681607
x-2087555254757757116
x-2088116807869854126
x-2088634091671531923
x-2089740155179643231
x-2091150763418620133
x-2091686636698657080
x-2091970263088816272
x-2092918452423983363
x-2093236801079279978
x-2093677274641969390
x-2094162743985308047
x-2094770895021572502
x-2095123902947090682
x-2095437841958314100
```

## IDs done (19)

All 19 ids above have `analysis/items/<id>/card.json` validated with `python3 scripts/analysis/validate_cards.py analysis/items/<id>` (exit 0).

| disposition | count | ids |
|-------------|------:|-----|
| analyze | 19 | all ids in batch |

## Blocked / failed

None.

## Readiness

| readiness | count | notes |
|-----------|------:|-------|
| ready | 11 | github/web items and several X posts without thread gaps |
| ready-with-gaps | 8 | linked-page-unfetched or thread-partial |

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "id": "x-2091150763418620133",
    "from": "uncategorized",
    "to": "local-inference-models",
    "why": "Legacy extra.filtered=true with empty topics; re-judged analyze — detailed FreeToken MoE inference writeup with benchmarks and repo link."
  },
  {
    "id": "x-2094162743985308047",
    "from": "uncategorized",
    "to": "outbound-gtm-agents",
    "why": "Legacy extra.filtered=true; re-judged analyze — seed item for outbound GTM channel-order playbook with measurable claims and slide evidence."
  },
  {
    "id": "x-2057113327508345047",
    "from": "three-js/design",
    "to": "image-to-3d-world",
    "why": "Legacy topics three-js/design; primary image-to-3d-world because artifact is AI mesh texturing pipeline, secondary web-3d-scenes."
  },
  {
    "id": "x-2089740155179643231",
    "from": "design/ui-motion/three-js",
    "to": "landing-ui-motion",
    "why": "Legacy topics design/ui-motion/three-js; primary landing-ui-motion for shadcn registry, secondary web-3d-scenes for shader components."
  }
]
```

## Notes

- Several X `media/media_0.jpg` files are MP4 payloads on disk; cards type them as `video`.
- `web-cloudflare-kitesurf` capture truncated mid-PageRenderer; flagged `linked-page-unfetched`.
- `x-2094770895021572502` and `x-2095123902947090682` flagged `thread-partial` (login-walled replies).
- `x-2094162743985308047` references an article below the tweet body that was not harvested; flagged `linked-page-unfetched`.
