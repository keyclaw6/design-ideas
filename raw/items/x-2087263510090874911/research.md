# Research

## What it is
A personal Pi/Cursor workflow: AGENTS.md auto-loads four skills (ponytail, grilling, wayfinder, ask-matt), the agent grills the human for a hundred questions, then a custom `/handoff` extension dumps a continuation doc at 100k context and resumes.

## How it works
- Default skills bias toward lazy-but-correct (ponytail), interrogation (grilling), navigation (wayfinder), and an “ask-matt” taste/oracle.
- Human is forced to make decisions up front instead of vibe-coding past them.
- `/handoff` at 100k: model writes a handoff document → next session continues (same idea as session-migrate elsewhere).
- Thesis: human judgment/taste still beats fully autonomous “Fable” coding.

## Why saved
Documents how this user (and similar) actually run Pi: grill → decide → handoff. Directly relevant to design-quality work.

## Topics
- `agent-skills`
- `design`

## Related
- `x-2086715093707063445` — which design skills to keep
- `github-leonxlnx-taste-skill` — taste pack
- `x-2087304957011911157` — pi-clarify (rewrite bad prompts)
- `x-2082316720086405524` — YOLO permissions + wipeable machine

## Use when
Setting up AGENTS.md for a design-heavy repo, or adding a context-window handoff. Combine with pi-shepherdr for multi-session work.
