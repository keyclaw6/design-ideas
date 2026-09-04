# Research

## What it is
Paul Bakaus’ Impeccable 4.1 release notes: design-critique skill pack with better chat critique, calmer hooks, native-app reviews, Windows/plugin fixes, and live-mode on non-localhost hosts.

## How it works
- Install: `npx impeccable install` — http://impeccable.style — 43 PRs since last release.
- Core: critique prints in chat before questions; design hook nags less (ignores persist); reduced-motion guidance restored.
- Greenfield: pick comps before code or skip mockups; bolder/safer ideation; consistent new-page mockups; better no-image-gen fallback.
- Native: iOS/Android reviewed against native conventions; polish uses native evidence not browser screenshots; web-only checks stay off native code.
- Platform: Windows install/decision/roll; four subagents actually load; Hermes + Antigravity support.
- Detectors: no false low-contrast on gradients/images; `data-impeccable-ignore` is element-scoped; live mode on ddev/valet; Svelte variants fixed.

## Why saved
Primary design-skill in the library (`github-pbakaus-impeccable`). This tweet is the 4.1 changelog an agent should read before `npx impeccable install`.

## Topics
`agent-skills`, `design`, `ui-motion`

## Related
- `github-pbakaus-impeccable` — **primary repo**
- `github-emilkowalski-skills` — sibling design/motion pack
- `github-leonxlnx-taste-skill` — taste skill
- `x-2086715093707063445` — “only 4 design skills I keep,” Impeccable first
- `github-google-labs-code-design-md` — DESIGN.md contract Impeccable enforces

## Use when
Installing or upgrading Impeccable, auditing a marketing/native UI, or enabling live mode on ddev/valet. Prefer this changelog plus the GitHub item over older tweets.
