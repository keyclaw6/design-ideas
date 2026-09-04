# cards-01

**Worker:** cards-01  
**Batch:** 01 (`analysis/_work/reports/batch-01.txt`)  
**Written:** 2026-09-04T18:10:00Z

## IDs owned (20)

```
github-LessieAI-people-search-bench
github-romangojiberryAI-gojiberryai-sales-os
web-crowdreply
web-obscura-sh
x-2065843739340509693
x-2087026930323247306
x-2087562269807030754
x-2088155107544191339
x-2088695568474546387
x-2089770081459056765
x-2091157554919280688
x-2091688420695564296
x-2091990178638496195
x-2092979866836648104
x-2093256024635666465
x-2093681908227936745
x-2094164487381414344
x-2094771557864292784
x-2095130625976176754
x-2095451624139567162
```

## IDs done (20)

All 20 ids above have `analysis/items/<id>/card.json` validated with `python3 scripts/analysis/validate_cards.py analysis/items/<id>` (exit 0).

| disposition | count | ids |
|-------------|------:|-----|
| analyze | 19 | all except `x-2088695568474546387` |
| shelf | 1 | `x-2088695568474546387` (noise / availability-announcement) |

## Blocked / failed

None.

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "from": "x-2089770081459056765",
    "to": "blockout-to-video-flythrough",
    "why": "Seedance hero + Cursor skills matches BESS landing split; kept primary ai-video-generation because motion is the named artifact."
  },
  {
    "from": "x-2093256024635666465",
    "to": "image-to-3d-world",
    "why": "Manual Blender fan-film timelapse is craft reference, not an agent blockout pipeline; blockout-to-video-flythrough kept for camera-path adjacency."
  }
]
```

## Notes

- `media/media_0.jpg` on `x-2065843739340509693`, `x-2087562269807030754`, and `x-2088155107544191339` are MP4 payloads with a `.jpg` extension; cards type them as `video`.
- `x-2091688420695564296` references video in post but no media file was harvested — `media-undescribed` gap flagged.
- `x-2095451624139567162` prompt body lives behind marketplace link; paired with `x-2095368133070700884` in judge_hints.
