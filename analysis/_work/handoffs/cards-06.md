# Handoff: cards-06

**Worker:** cards-06  
**Batch:** 06  
**Written at:** 2026-09-04

## IDs owned (20)

github-google-labs-code-design-md, github-youmind-openlab-nano-banana-pro-prompts, web-designmd-supply, web-recent-design, x-2082316720086405524, x-2087205167662088363, x-2087714580491370655, x-2088260067204137135, x-2089165107364278341, x-2090098441200517416, x-2091479075697430784, x-2091748299975880994, x-2092137646730727617, x-2093018082293813509, x-2093377271771865267, x-2093767075131220005, x-2094424967345496191, x-2094864872853119216, x-2095192939169234945, x-2095521587785081193

## IDs done (20)

All 20 above — `card.json` written and `validate_cards.py` exit 0.

## Blocked / failed

None (generation or validation).

## Disposition summary

| disposition | count | ids |
|-------------|-------|-----|
| analyze | 18 | all except x-2092137646730727617, x-2095192939169234945 |
| shelf | 2 | x-2092137646730727617 (noise/empty-capture), x-2095192939169234945 (out-of-scope GTM article) |

Legacy `extra.filtered` was true on x-2092137646730727617 and x-2095192939169234945; both re-judged **shelf** (empty reaction tweet; outbound launch-distribution article outside taxonomy).

## Readiness

| readiness | ids |
|-----------|-----|
| ready | 14 |
| ready-with-gaps | web-designmd-supply (linked-page-unfetched), x-2087205167662088363 (thread-partial), x-2094424967345496191 (linked-page-unfetched), x-2095521587785081193 (media-undescribed, linked-page-unfetched) |
| shelved | x-2092137646730727617, x-2095192939169234945 |

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "id": "x-2095192939169234945",
    "from": "uncategorized",
    "to": "outbound-gtm-agents",
    "why": "Category note identifies social launch-distribution GTM article; shelved as out-of-scope for this library but belongs in outbound-gtm-agents if ever in scope."
  },
  {
    "id": "x-2091748299975880994",
    "from": "three-js topic tag",
    "to": "web-3d-scenes",
    "why": "Post explicitly uses WebGPU not Three.js; primary web-3d-scenes with image-to-3d-world secondary for Blender-sourced geometry."
  }
]
```

## Notes for threads worker

- x-2087205167662088363: parent tweet/tool not captured; thin quote reaction only.
- x-2094424967345496191, x-2095521587785081193: X article / breakdown body not fetched.
- web-designmd.supply: Vercel 429 checkpoint; recapture when accessible.
