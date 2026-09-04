# cards-14 handoff

**Worker:** cards-14  
**Batch:** 14 (`analysis/_work/reports/batch-14.txt`)  
**Written:** 2026-09-04

## ids owned (19)

github-nexu-io-html-video, web-blume-codes, web-graphed, web-treg-people-search, x-2086599657925329347, x-2087272209429766596, x-2087898602890744089, x-2088345102540587356, x-2089457435459404093, x-2090837707069014224, x-2091571624390881664, x-2091924963288580539, x-2092657951618249080, x-2093081833911058772, x-2093583622691283018, x-2093990583576486268, x-2094648474377839018, x-2095055297949610427, x-2095336950890983773

## ids done (19)

All 19 ids above — `card.json` written and `validate_cards.py` exit 0.

## blocked / failed

None.

## disposition summary

| disposition | count |
|-------------|------:|
| analyze     | 19 |
| shelf       | 0 |

## readiness summary

| readiness        | count |
|------------------|------:|
| ready            | 5 |
| ready-with-gaps  | 14 |
| blocked          | 0 |
| shelved          | 0 |

**Explicit gaps:** x-2086599657925329347 (`media-undescribed` — course video omitted from git), x-2093583622691283018 (`translation-needed`), x-2094648474377839018 (`translation-needed`), x-2095055297949610427 (`thread-partial`), x-2095336950890983773 (`translation-needed`).

**Implicit thread gaps:** 12 other X items have `analysis/items/<id>/thread.json` with `captured_partial` from threads-script, so readiness is `ready-with-gaps` even when `gaps` is empty.

## primary_subject counts

| subject | count |
|---------|------:|
| agent-harness-loops | 2 |
| ai-cad-hardware | 1 |
| ai-video-generation | 1 |
| blockout-to-video-flythrough | 1 |
| code-motion-graphics | 2 |
| design-agent-skills | 2 |
| gaussian-splatting | 2 |
| mcp-and-agent-browsers | 1 |
| outbound-gtm-agents | 2 |
| serp-ai-visibility | 3 |
| web-3d-scenes | 2 |

## alias proposals

```json
[]
```

## reclass proposals

```json
[
  {
    "id": "x-2094648474377839018",
    "from": "gaussian-splatting",
    "to": "shelf:duplicate",
    "why": "JP launch tweet for product already captured as web-arcana-splat2mesh; keep only if the quoted 70s demo video is required — otherwise merge angle into the web item."
  },
  {
    "id": "x-2090837707069014224",
    "from": "serp-ai-visibility",
    "to": "mcp-and-agent-browsers",
    "why": "UA negotiation table is primarily agent-browser policy intel; SERP subject kept primary because publishers gate AI crawlers for citation/AEO work."
  }
]
```

## notes

- `x-2087272209429766596` and `x-2091571624390881664` ship MP4 captures mislabeled as `.jpg`; cards mark `type: video`.
- `x-2093583622691283018` is Spanish-only promo with no linked syllabus URL in capture.
- No `thread.json` or `card.md` written per worker rules.
