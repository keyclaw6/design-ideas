# Handoff: cards-17

**Worker:** cards-17  
**Batch:** 17  
**Written at:** 2026-09-04

## IDs owned (19)

github-nv-tlabs-ArtiFixer, web-cerebras-knowledge-base, web-lottiefiles, web-vengence-ui, x-2086801779358875912, x-2087329201451855933, x-2087962842985058365, x-2088599468698751328, x-2089618415493218381, x-2090930324817498246, x-2091621183422943726, x-2091943679317463153, x-2092702228947902622, x-2093153416214114558, x-2093663876692754713, x-2094069236524061059, x-2094740953554932149, x-2095081419202560010, x-2095375790875840593

## IDs done (19)

All 19 above — `card.json` written and `validate_cards.py` exit 0.

## Blocked / failed

None.

## Disposition summary

| disposition | count | ids |
|-------------|-------|-----|
| analyze | 19 | all |

Legacy `extra.filtered` was true on x-2090930324817498246 and x-2091621183422943726; both re-judged **analyze** (local-inference-models benchmark claims; ai-cad-hardware CadX demo).

## Readiness

| readiness | ids |
|-----------|-----|
| ready | 16 |
| ready-with-gaps | x-2090930324817498246 (linked-page-unfetched — no repo URL in post), x-2094740953554932149 (thread-partial), x-2095081419202560010 (thread-partial) |

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "id": "x-2090930324817498246",
    "from": "uncategorized",
    "to": "local-inference-models",
    "why": "Post cites DeepSeek-V4-Flash 284B throughput and llama.cpp/Ollama comparisons; matches local-inference-models inclusion despite legacy filtered flag and missing repo link."
  },
  {
    "id": "x-2091621183422943726",
    "from": "uncategorized",
    "to": "ai-cad-hardware",
    "why": "CadX Studio one-shot consumer product CAD demo at cadxstudio.in; legacy filter noted keyboard-pcb mismatch but subject covers text-to-CAD tools."
  }
]
```

## Notes for threads worker

- x-2094740953554932149, x-2095081419202560010: partial reply capture; gaps marked thread-partial.
- Several X media paths end in `.jpg` but on-disk files are MP4; cards type them as `video`.
