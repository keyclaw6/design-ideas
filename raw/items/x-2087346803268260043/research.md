# Research

## What it is
A one-line prompt recipe for killing LLM “slop” prose: force Google-developer-docs voice — dead, simple, no aphorisms.

## How it works
- Author (@aaronvi) claims slop writing is mostly solved by a style constraint, not a new model.
- Exact prompt in the post: “Can you make it like google dev docs style. More dead prose. No aphorisms, no flourishes. Simple.”
- Attached diff shows the rewrite applied to BAML Project Studio docs: punchy section titles (“The one idea”) become functional ones (“Two layers of records”); marketing throat-clearing is cut; scope exclusions are stated in plain sentences.
- Mechanism is editorial, not tooling: a standing instruction in AGENTS.md / DESIGN.md / a skill that prefers Google-style technical English.
- Pairs with anti-slop skills (`/no-ai-slop`, Impeccable detectors) but this one is specifically about documentation tone, not UI chrome.

## Why saved
KB’s agent stack writes a lot of docs and landing copy. A short, copy-pasteable constraint that actually changes voice is cheaper than a full taste skill when the problem is prose, not pixels.

## Topics
`agent-skills`, `design`

## Related
- `github-google-labs-code-design-md` — DESIGN.md as the agent contract for visual/verbal rules
- `github-pbakaus-impeccable` — detectors for generic-AI tells
- `github-leonxlnx-taste-skill` — taste pack for UI and copy
- `x-2085006701984698712` — /no-ai-slop and /human-review skills

## Use when
Drafting or rewriting technical docs, changelog, or DESIGN.md copy and the agent is producing flourishy blog-post English. Drop this constraint into the prompt or a standing rule.
