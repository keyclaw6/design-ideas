# Research

## What it is
Long changelog for Pi realtime voice (Howaboua / Clawa): 16 hours of voice-driven build of Codex Conversion + GipPity so talking to Pi feels like a conversation, not yelling at a mic.

## How it works
- Pi extensions can `reportRealtimeVoicePrompt` with a stable id + natural-language instruction + active flag; the voice model announces events without canned lines.
- Spoken delegation acknowledgements, reasoning-summary fillers (only on silent completed tool steps; GPT-5 / Claude 4–5 / Gemini 3 / Grok 4.5–4.6; Completions path excluded), and compaction announcements are independently togglable.
- Audio follows system default routes (or pinned device IDs); `/codex voice setup` writes the choice. LAN GipPity controller, mute-preserving call recovery, mic-too-quiet warnings.
- Install: `pi install npm:@howaboua/pi-codex-conversion` or standalone `@howaboua/pi-gippity-control` (do not install both).
- Monorepo: https://github.com/IgorWarzocha/howaboua-pi-stuff — packages include pi-ask, pi-auto-trees, pi-shepherdr, pi-subagent-review.

## Why saved
KB uses Pi/Codex-style harnesses. This is the reference for voice as a first-class control surface (hands-busy plant walkthroughs, long coding sessions) and for the tiny extension API other tools should copy.

## Topics
`agent-skills`

## Related
- `x-2087232392209531166` — pi-shepherdr multi-agent voice orchestration
- `x-2087898602890744089` — Rakazo, OSS Grok Bot using the pi harness
- `web-blume-codes` — sidecar control plane for coding agents
- `x-2087304957011911157` — pi-clarify prompt skill for the same harness

## Use when
Wiring voice onto a Pi/Codex harness, adding extension-driven spoken events, or installing Howaboua’s Codex Conversion / GipPity packages.
