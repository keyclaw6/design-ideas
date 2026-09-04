# Research

## What it is
Blog pointer: Sankalp used Codex in GPU Mode’s `qr_v2` problem to auto-kernel QR decomposition and claims 212× over baseline. Post: https://sankalp.bearblog.dev/autoresearch/

## How it works
- Treat kernel search as an autoresearch loop: agent proposes kernel variants, runs them, keeps winners.
- Domain is GPU kernels (QR), not product UI — the transferable bit is the harness (fixed eval, iterate until metric moves).
- Codex as the proposer; GPU Mode supplies the problem + timing oracle.
- Write-up is the primary artifact (tweet is an announcement).

## Why saved
Best “I actually measured an auto-research loop” item next to the Aman primer. Useful when designing evals for skills, SEO crawls, or motion templates.

## Topics
- `agent-skills`

## Related
- `x-2080856252687745093` — primer: propose/run/evaluate + meta-harness
- `x-2032671842230501729` — generic swarm version of the same idea
- `x-2087151807965401320` — Ouroboros self-modifying agent
- `web-chatgpt-training` — Codex walkthroughs

## Use when
Building a closed-loop optimizer around a coding agent (kernel, crawl, design lint). Read the blog, not just this tweet.
