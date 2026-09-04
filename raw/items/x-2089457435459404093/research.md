## What it is

Nate Jones PSA: point the agent at Google's Developer Docs Style Guide and wrap it as a skill to kill Claude-lish/Chat-lish; claims it beats an ASD-STE100 Simplified Technical English skill.

## How it works

- Canonical source: developers.google.com/style (voice, headings, lists, code samples, not-robot rules).
- Mechanism: retrieve/style-guide → skill markdown → apply on docs, READMEs, research.md, marketing copy.
- Author argues labs should invest in comms skills; RLVR-good agents still fail if they cannot write.
- Different from anti-slop writing lists: this is a professional docs register, not just 'sound human'.
- Pairs with DESIGN.md (visual contract) as a verbal contract.

## Why saved

KB's catalog and agent outputs need a default English register; Google's guide is a known, stable corpus.

## Topics

`agent-skills`, `design`

## Related

`github-leonxlnx-taste-skill`, `x-2090834948332655011`, `github-google-labs-code-design-md`, `x-2088742864310481025`

## Use when

Outputs read as LLM-ese, or when authoring a docs/voice skill. Prefer this over STE100 if the comparison in the tweet holds for your corpus.
