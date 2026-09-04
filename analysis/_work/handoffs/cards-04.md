# cards-04 handoff

**Worker:** cards-04  
**Batch:** 04 (`analysis/_work/reports/batch-04.txt`)  
**Written:** 2026-09-04

## IDs owned (19)

```
github-deedy-qr-data-transfer
github-superdesigndev-treg
web-design-md-hyperbrowser
web-originkit-dev
x-2077376352630845499
x-2087151807965401320
x-2087656088124719304
x-2088252062454751483
x-2088742864310481025
x-2090031918523842766
x-2091362595844567436
x-2091722166685610284
x-2092040265234260091
x-2093012548031254932
x-2093364419044794836
x-2093729321131368744
x-2094377838774472944
x-2094826117056414132
x-2095156045303701766
x-2095502642218664004
```

## IDs done (19/19)

All 19 `card.json` files written and validated (`python3 scripts/analysis/validate_cards.py analysis/items/<id>` → exit 0).

| Disposition | Count | IDs |
|-------------|-------|-----|
| analyze | 16 | all except three shelved below |
| shelf | 3 | `github-deedy-qr-data-transfer`, `x-2077376352630845499`, `x-2091362595844567436` |

### Readiness breakdown (analyze)

| Readiness | Count | Notes |
|-----------|-------|-------|
| ready | 3 | `github-superdesigndev-treg`, `web-design-md-hyperbrowser`, `web-originkit-dev` |
| ready-with-gaps | 13 | All X items — `thread-failed` (no `thread.json` yet) |
| shelved | 3 | shelf disposition |

## Blocked / failed

None. No items blocked on card writing.

**Deferred to thread worker:** All 13 analyzed X posts list `thread-failed` in `gaps` because `thread.json` is absent. Cards are `ready-with-gaps` until threads land.

**Media notes:**
- `x-2093012548031254932/media/media_0.jpg` and `x-2093364419044794836/media/media_0.jpg` are MP4 containers saved with `.jpg` extension; typed as `video` in `media[]`.
- `x-2094826117056414132` has `thumb.jpg` (image) + `video.mp4` (video).

## Alias proposals

```json
[
  {"from": "bess-3d-flythrough", "to": "blockout-to-video-flythrough", "why": "Legacy topic slug on x-2094826117056414132 source.json; not a subjects.json slug."},
  {"from": "seo-agents", "to": "serp-ai-visibility", "why": "Legacy topic on several items (treg, AEO case); maps to SERP/AEO subject."},
  {"from": "keyboard-pcb", "to": "ai-cad-hardware", "why": "Legacy topic on x-2088252062454751483; enclosure/rack CAD fits ai-cad-hardware inclusion rule."}
]
```

## Reclass proposals

```json
[
  {"id": "github-deedy-qr-data-transfer", "from": "shelf:out-of-scope", "to": "landing-ui-motion", "why": "Could be reclassified as analyze/example if taxonomy adds browser craft utilities; currently no subject covers air-gapped QR transfer."},
  {"id": "x-2087656088124719304", "from": "design-agent-skills", "to": "landing-ui-motion", "why": "pdfcn is a shadcn component kit; landing-ui-motion may be equally valid primary if subject worker prefers component-library placement."}
]
```

## Primary subject assignments (analyze)

| ID | primary_subject |
|----|-----------------|
| github-superdesigndev-treg | mcp-and-agent-browsers |
| web-design-md-hyperbrowser | design-agent-skills |
| web-originkit-dev | landing-ui-motion |
| x-2087151807965401320 | agent-harness-loops |
| x-2087656088124719304 | design-agent-skills |
| x-2088252062454751483 | ai-cad-hardware |
| x-2088742864310481025 | design-agent-skills |
| x-2090031918523842766 | design-agent-skills |
| x-2091722166685610284 | blockout-to-video-flythrough |
| x-2092040265234260091 | code-motion-graphics |
| x-2093012548031254932 | web-3d-scenes |
| x-2093364419044794836 | landing-ui-motion |
| x-2093729321131368744 | serp-ai-visibility |
| x-2094377838774472944 | gaussian-splatting |
| x-2094826117056414132 | gaussian-splatting |
| x-2095156045303701766 | ai-video-generation |
| x-2095502642218664004 | image-to-3d-world |
