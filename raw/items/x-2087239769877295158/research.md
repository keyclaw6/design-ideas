# Research

## What it is
Sentrux: a real-time architectural sensor. Watches a codebase as a live treemap, folds structure/deps into one quality score so the next agent session starts from a map instead of grep.

## How it works
- Loop: scan structure + dependencies → five root-cause metrics → one signal → agent sees where risk concentrates.
- Zero built-in language knowledge in the binary; 52 languages live in `plugin.toml` + `tags.scm` (new language = no Rust).
- Limitation: scores structure only; will not explain *why* a cycle exists.
- Pure Rust, no runtime deps — meant to sit between agent and repo as one binary.

## Why saved
Persistent architecture context is the same problem as DESIGN.md and system-atlas. Useful before `/improve-codebase-architecture`.

## Topics
- `agent-skills`

## Related
- `x-2086838432102228008` — `/improve-codebase-architecture`
- `x-2091559663833924082` — system-atlas isometric map skill
- `github-google-labs-code-design-md` — design contract
- `web-davidgasquez-context-engineering` — context as pipeline

## Use when
An agent must not re-learn repo shape every session, or you want a CI-like architecture score next to tests.
