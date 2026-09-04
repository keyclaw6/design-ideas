# cards-13

Worker for batch 13 (`analysis/_work/reports/batch-13.txt`).

## Owned (19)

github-nateherkai-scroll-craft, web-aura-build, web-getlayers-ai, web-tinyshots, x-2086537093120164177, x-2087263510090874911, x-2087893705059356898, x-2088308976278790258, x-2089400082550620636, x-2090834948332655011, x-2091570990048276897, x-2091918691747189053, x-2092656414351118647, x-2093064017468145963, x-2093563796237471912, x-2093986548404428942, x-2094558408259272998, x-2094984529853530345, x-2095288402606514424

## Done (19)

All 19 `card.json` files written and validated (`python3 scripts/analysis/validate_cards.py analysis/items/<id>` exit 0).

| disposition | count | ids |
|-------------|------:|-----|
| analyze | 16 | github-nateherkai-scroll-craft, web-aura-build, web-getlayers-ai, web-tinyshots, x-2086537093120164177, x-2087263510090874911, x-2088308976278790258, x-2089400082550620636, x-2090834948332655011, x-2092656414351118647, x-2093064017468145963, x-2093563796237471912, x-2093986548404428942, x-2094558408259272998, x-2094984529853530345, x-2095288402606514424 |
| shelf | 3 | x-2087893705059356898 (out-of-scope), x-2091570990048276897 (noise), x-2091918691747189053 (out-of-scope) |

## Blocked / failed

None.

## Alias proposals

```json
[
  {
    "from": "cadxstduio.in",
    "to": "cadxstudio.in",
    "why": "Typo in x-2088308976278790258 tweet URL; canonical CadX domain is cadxstudio.in per research.md."
  }
]
```

## Reclass proposals

```json
[
  {
    "id": "x-2087893705059356898",
    "from": "legacy filtered",
    "to": "shelf:out-of-scope/real-artifact-no-subject",
    "why": "Re-judged: 44-page agency sales PDF lead magnet has no PDF in capture and no taxonomy fit; outbound GTM is a different subject."
  },
  {
    "id": "x-2092656414351118647",
    "from": "design-agent-skills primary only",
    "to": "design-agent-skills + serp-ai-visibility secondary",
    "why": "avoid-ai-writing is anti-slop prose tooling with SEO/content pipeline adjacency per source category_note."
  },
  {
    "id": "x-2091918691747189053",
    "from": "camera-control topic",
    "to": "shelf:out-of-scope",
    "why": "Marmoset Toolbag SpaceMouse viewport update is DCC product news, not blockout-to-video camera technique reference."
  }
]
```

## Notes

- x-2086537093120164177: prompt method promised in comments but `comments.md` empty; quoted tweet in `thread.json` carries partial recipe. Gap: `thread-partial`.
- x-2095288402606514424: note.com article not ingested; gaps `translation-needed`, `linked-page-unfetched`.
- web-aura-build: SPA shell only; gap `linked-page-unfetched`.
