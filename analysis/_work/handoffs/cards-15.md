# cards-15

**Worker:** cards-15  
**Batch:** 15 (`analysis/_work/reports/batch-15.txt`)  
**Written:** 2026-09-04T18:15:00Z

## IDs owned (19)

```
github-nexu-io-motion-anything
web-brave-submit-url
web-iandmacomber-post-ai-data-stack
web-typeui-sh
x-2086715093707063445
x-2087280401475600698
x-2087905319255257296
x-2088590355440476343
x-2089570022490263586
x-2090839282831270173
x-2091577179914338583
x-2091927587471712274
x-2092658333337469133
x-2093118868092748246
x-2093624705030959554
x-2094009989220430084
x-2094684433546985907
x-2095060844547592437
x-2095352925597884465
```

## IDs done (19)

All 19 ids above have `analysis/items/<id>/card.json` validated with `python3 scripts/analysis/validate_cards.py analysis/items/<id>` (exit 0).

| disposition | count | ids |
|-------------|------:|-----|
| analyze | 16 | all except the three shelved below |
| shelf | 3 | `x-2087280401475600698`, `x-2092658333337469133`, `x-2093118868092748246` |

## Blocked / failed

None.

## Readiness

| readiness | count | notes |
|-----------|------:|-------|
| ready | 4 | github/web items without thread gaps |
| ready-with-gaps | 12 | thread-partial, linked-page-unfetched, or translation-needed |
| shelved | 3 | noise shelf items |

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "id": "x-2087280401475600698",
    "from": "uncategorized",
    "to": "shelf/noise",
    "why": "Legacy extra.filtered=true; re-judged promo-no-artifact — Polymarket copy-trading ad with no agent or design artifact."
  },
  {
    "id": "x-2092658333337469133",
    "from": "uncategorized",
    "to": "shelf/noise",
    "why": "Legacy extra.filtered=true; NVIDIA Studio #StudioShare engagement bait without pipeline detail."
  },
  {
    "id": "x-2093118868092748246",
    "from": "uncategorized",
    "to": "shelf/noise",
    "why": "Legacy extra.filtered=true; Calliope YouTube growth teaser with follow-for-recreate CTA and no linked artifact."
  },
  {
    "id": "x-2095060844547592437",
    "from": "design",
    "to": "outbound-gtm-agents",
    "why": "Legacy topic design; primary subject outbound-gtm-agents because the artifact is LinkedIn lead-magnet distribution, not UI craft."
  }
]
```

## Notes

- Several X `media/media_0.jpg` files are MP4 payloads on disk; cards type them as `video`.
- `web-typeui-sh` and `x-2089570022490263586` flagged `linked-page-unfetched` (Vercel 429 / repo not harvested).
- `x-2086715093707063445` flagged `translation-needed` (Chinese post body).
- `x-2094684433546985907` DM-gated LIST sheet not in capture; fifteen directory names are in the note-tweet body.
