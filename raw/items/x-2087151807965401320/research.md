# Research

## What it is
HuggingPapers blurb on Ouroboros, a self-improving coding agent that evolves its own tools, prompts, and architecture through reviewed commits. Claims SOTA on Terminal-Bench 2.1 (86.74%), OSWorld-Verified (90.69%), CL-Bench (0.2301).

## How it works
- Self-modification is gated by reviewed commits (not silent self-rewrite).
- Search space: tools, prompts, architecture — same as meta-harness.
- Benchmarks are terminal/OS/agent suites, not UI.
- Tweet has no repo URL; identify by name “Ouroboros coding agent” if hunting the paper.

## Why saved
Another data point that self-modifying agents are a real lane, with eval numbers. Pair with ReasoningBank (what to remember) and Hyperspace (how to swarm).

## Topics
- `agent-skills`

## Related
- `x-2032671842230501729` — swarm self-improvement
- `x-2080856252687745093` — harness search taxonomy
- `x-2074912810803560497` — measured kernel loop
- `x-2087143369181114868` — memory of failures during self-improve

## Use when
Comparing self-improving coding agents or designing a review gate on agent-authored commits.
