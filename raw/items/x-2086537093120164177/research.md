# Research

## What it is
Day-15 build log: steering Opus 5 into a precise, fully interactive 3D terrain vehicle (jeep-like) with panels, buttons, moving parts — textureless render. Method claimed in unreaped comments: recursive loop + subagent QC under 300k context.

## How it works
- Recursive generation loop rather than one-shot mesh.
- Subagent QC pass to keep detail/interactivity inside a 300k context budget.
- Textureless demo isolates form/rig vs lookdev (lookdev can come later, e.g. kokraf).
- Prompt/method was promised in comments; this harvest’s `comments.md` is empty — treat as a pattern pointer, not a copy-paste prompt.

## Why saved
Shows an agent can build *interactive* 3D (not just a still) — relevant to product configurators and 3D landings.

## Topics
- `three-js`
- `agent-skills`
- `design`

## Related
- `github-scottstts-threejs-awesome-graphics-agent-skills` — web-3D skills
- `github-mengto-complete-shelf` — 3D/product shelf
- `x-2086599657925329347` — Claude 3D website course
- `x-2057113327508345047` — AI texturing after gray model

## Use when
Generating interactive Three.js/R3F objects with a QC subagent loop. Re-fetch the X thread if you need the actual prompt.
