# Handoff: cards-12

**Worker:** cards-12  
**Batch:** 12 (`analysis/_work/reports/batch-12.txt`)  
**Written:** 2026-09-04

## IDs owned (19)

```
github-mengto-skills
web-arxiv-2603-27476
web-getdesign-md
web-tinyshelf
x-2086533896993112572
x-2087254502210490739
x-2087873421094896122
x-2088299905324396589
x-2089377925086982281
x-2090787985721856437
x-2091564966797029541
x-2091913781236683162
x-2092644473868050684
x-2093053568748319181
x-2093481253043380418
x-2093964632562253866
x-2094553318031024285
x-2094978216146452971
x-2095231184531828762
```

## IDs done (19/19)

All 19 `card.json` files written and validated (`python3 scripts/analysis/validate_cards.py analysis/items/<id>` → exit 0).

| Disposition | Count | IDs |
|-----------|-------|-----|
| analyze | 14 | github-mengto-skills, web-arxiv-2603-27476, web-getdesign-md, web-tinyshelf, x-2087254502210490739, x-2088299905324396589, x-2091913781236683162, x-2092644473868050684, x-2093053568748319181, x-2093481253043380418, x-2093964632562253866, x-2094553318031024285, x-2094978216146452971, x-2095231184531828762 |
| shelf | 5 | x-2086533896993112572, x-2087873421094896122, x-2089377925086982281, x-2090787985721856437, x-2091564966797029541 |

## Blocked / failed

None.

## Alias proposals

```json
[
  {
    "from": "x-2093964632562253866",
    "to": "web-brave-submit-url",
    "why": "Tweet is a three-step recap of the Brave submit-url page already captured as web-brave-submit-url; no independent artifact beyond the screenshot."
  }
]
```

## Reclass proposals

```json
[
  {
    "id": "x-2091564966797029541",
    "current": "shelf/out-of-scope",
    "proposed": "keep shelved",
    "why": "Seed in ai-cad-hardware but capture is FreeCAD internal toponaming PR, not text-to-CAD or marketing workflow; re-judged out-of-scope."
  },
  {
    "id": "x-2087254502210490739",
    "current": "analyze/agent-harness-loops",
    "proposed": "keep",
    "why": "Paper URL still missing from post; flagged linked-page-unfetched. Fits harness-loops over memory-knowledge despite KG mention."
  }
]
```

## Notes

- `media/media_0.jpg` on x-2088299905324396589 and x-2093053568748319181 are MP4 payloads misnamed as `.jpg`; cards record `type: video`.
- X items with `thread.json` marked `captured_partial` → readiness `ready-with-gaps` + gap `thread-partial`.
- Did not write `card.md` or `thread.json`.
