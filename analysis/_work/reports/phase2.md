# Phase 2 report

Generated after `validate_cards.py` (clean), `build_registry.py`, `render.py`, `build_index.py`.

## Counts

| Metric | Value |
|---|---|
| Cards | 388 |
| Analyze / shelf | 345 / 43 |
| Shelf breakdown | noise 28, out-of-scope 10, duplicate 5, uncategorized 0 |
| Threads | 311 (captured_full 19, captured_partial 270, empty 14, failed 8) |
| Failed thread cap | 8 ≤ 62 |
| Tools (pre-alias) | 201 |
| Techniques (pre-alias) | 268, 96.6% singleton |

## Subject primaries vs expected

| slug | n | expected | flag |
|---|---|---|---|
| serp-ai-visibility | 28 | 28–45 | |
| outbound-gtm-agents | 15 | 12–22 | |
| gaussian-splatting | 17 | 14–22 | |
| image-to-3d-world | 14 | 12–22 | |
| blockout-to-video-flythrough | 23 | 18–30 | |
| ai-video-generation | 20 | 14–24 | |
| code-motion-graphics | 14 | 10–16 | |
| web-3d-scenes | 18 | 14–22 | |
| landing-ui-motion | 35 | 28–45 | |
| design-agent-skills | 50 | 38–55 | |
| image-prompt-galleries | 8 | 7–12 | |
| agent-harness-loops | 35 | 24–36 | |
| agent-memory-knowledge | 16 | 12–18 | |
| mcp-and-agent-browsers | 11 | 9–16 | |
| infographics-diagrams | 14 | 12–18 | |
| ai-cad-hardware | 17 | 14–20 | |
| local-inference-models | 10 | 8–13 | |

All 17 subjects sit inside both the 6–60 grain band and the expected range. No merge required.

## Technique alias collapse (registry)

Card workers invented nearly-unique technique slugs. `scripts/analysis/alias_techniques.py` mapped them to 44 shared methods. After `build_registry.py` rewrite: 44 techniques, singleton rate 2.3% (cap 15%). Alias keys are absent from cards.

## Readiness

ready 80 · ready-with-gaps 265 · shelved 43 · blocked 0.

`ready-with-gaps` is almost entirely `thread-partial` on logged-out X captures.

## Legacy filtered (47)

Re-judged at card time: 10 re-entered as analyze, 37 stayed shelf. None missing.

## Alias / reclass proposals from card handoffs

Absorbed into `registry/aliases.json` (technique slugs). No uncategorized items for the shelf auditor. Subject generator wrote no reclass records.
