# Handoff: cards-08

**Worker:** cards-08  
**Batch:** 08 (`analysis/_work/reports/batch-08.txt`)  
**Written:** 2026-09-04T18:05:00Z

## IDs owned (20)

```
github-iannuttall-seo
web-aidesigner-mcp
web-fal-ai
web-seowins-io
x-2084613319558635940
x-2087224641849045110
x-2087733334617063503
x-2088277946918142211
x-2089189790881382676
x-2090165248196252003
x-2091519705911795761
x-2091835143522840732
x-2092242135504552118
x-2093024468209733756
x-2093397098544648516
x-2093776000781869278
x-2094450512938856802
x-2094893065202803014
x-2095202138854977756
x-2095549461737111905
```

## IDs done (20/20)

All 20 `analysis/items/<id>/card.json` files written and validated (`python3 scripts/analysis/validate_cards.py analysis/items/<id>` → exit 0).

| Disposition | Count | IDs |
|-------------|------:|-----|
| analyze | 14 | github-iannuttall-seo, web-aidesigner-mcp, web-fal-ai, web-seowins-io, x-2088277946918142211, x-2089189790881382676, x-2091519705911795761, x-2092242135504552118, x-2093024468209733756, x-2093397098544648516, x-2094450512938856802, x-2094893065202803014, x-2095202138854977756, x-2095549461737111905 |
| shelf | 6 | x-2084613319558635940, x-2087224641849045110, x-2087733334617063503, x-2090165248196252003, x-2091835143522840732, x-2093776000781869278 |

## Blocked / failed

None. All items completed.

**Gaps noted on analyze cards:**

| ID | readiness | gaps |
|----|-----------|------|
| x-2088277946918142211 | ready-with-gaps | media-undescribed (video/prompt not in raw media/) |
| x-2091519705911795761 | ready-with-gaps | translation-needed (JP post) |
| x-2094893065202803014 | ready-with-gaps | thread-partial (~25 replies login-walled) |
| x-2095202138854977756 | ready-with-gaps | linked-page-unfetched (OSS link promised, not in capture) |
| x-2095549461737111905 | ready-with-gaps | thread-partial (existing thread.json: 1/27 replies) |

**Media note:** `x-2092242135504552118` and `x-2093024468209733756` store MP4 payloads with `.jpg` extensions; cards type them as `video`.

## Alias proposals

```json
{"from": "Claude Fable 5.1", "to": "claude-code", "why": "Post names 'Claude Fable 5.1' as a website generator; likely Claude Code/Fable branding—confirm official product name before registry."}
```

## Reclass proposals

```json
{"id": "x-2094893065202803014", "from": "shelf (legacy extra.filtered)", "to": "analyze / outbound-gtm-agents", "why": "Re-judged: IQ meme contains substantive cold-email technique content despite legacy filter flag."}
```

```json
{"id": "x-2093776000781869278", "from": "analyze candidate", "to": "shelf / out-of-scope", "why": "Real GTM flywheel infographic but no taxonomy subject covers full-stack B2B GTM consulting playbooks."}
```

```json
{"id": "x-2092242135504552118", "from": "three-js (legacy topic)", "to": "image-to-3d-world", "why": "Post describes single-image-to-mesh topology, not a WebGL scene; seed item under image-to-3d-world."}
```

## Notes

- Did **not** write `card.md` or `thread.json` (pre-existing `thread.json` for x-2095549461737111905 left untouched).
- Legacy `extra.filtered` re-judged per CARD_WORKER; not copied blindly into disposition.
