## What it is

Laosan breakdown of YousufSoomroDev's open-source portfolio carousel: cards enter with swing and inertia rather than sliding on a flat track.

## How it works

- Motion grammar: fast entry → overshoot/swing → 1–2 decaying rebounds to rest (not long spring loops).
- Feels hung/thrown into frame; suited to photography, posters, case-study cards where the card is the hero.
- Author warning: too many oscillations kill browse throughput — cap rebound count.
- Component is described as open-sourced for reuse as a work-showcase module (original author @YousufSoomroDev).
- Capture is Chinese-language craft notes — keep the physics spec even if the repo URL was not in the tweet body.

## Why saved

BESS/marketing case-study strips need non-slop motion; this is a concrete spring recipe, not a generic 'animate carousel'.

## Topics

`ui-motion`, `design`

## Related

`github-nateherkai-scroll-craft`, `github-nexu-io-motion-anything`, `web-animos-editor`, `x-2089775679600812150`

## Use when

Building a portfolio or project carousel and the default easing looks like AI-template sliding; or documenting spring/inertia rules in a motion skill.
