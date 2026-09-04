## What it is

Launch writeup for /vision: a small skill that interviews the user with borderline feature ideas, then writes a VISION.md used to triage work and catch drift.

## How it works

- Thesis: as agents scale, humans cannot review all code, then cannot review all plans — influence must move up to vision.
- Skill inspects existing repo context, proposes 8–12 hypothetical borderline features to force yes/no, then drafts VISION.md.
- Intended uses: feature triage, implementation-drift detection in review, ambiguous product calls.
- Example file: kunchenguid/firstmate VISION.md. Skill repo: kunchenguid/vision.
- Sits next to DESIGN.md (how it should look/behave) as the 'where it should go' contract.

## Why saved

KB's idea bank and BESS/marketing work will spawn more agent-proposed features than a human can plan-review; a vision file is the missing gate.

## Topics

`agent-skills`, `design`

## Related

`github-google-labs-code-design-md`, `web-getdesign-md`, `web-davidgasquez-context-engineering`, `x-2088634091671531923`

## Use when

A repo needs a durable product north star, agents are implementing off-strategy ideas, or DESIGN.md exists but nothing says which features belong.
