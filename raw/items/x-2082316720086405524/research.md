# Research

## What it is
Kun Chen’s rationale for running coding agents with all permission checks off: treat the machine as an employee laptop, make it instantly reproducible, and keep secrets off the agent’s disk.

## How it works
- Mindset: the box is disposable; humans trash machines more than agents; don’t block every shell call.
- Repro: nix-darwin + home-manager; wipe → clone https://github.com/kunchenguid/dotfiles/ → rebuild.
- Secrets: production creds never in plaintext; AutomicVault (or equivalent) gates each secret use so the human still authorizes *secret* access even when the agent can run any command.
- Result: unconstrained execution inside a constrained blast radius.

## Why saved
Practical ops for unattended Cursor/Codex/Pi agents on a local box — relevant if BESS/SEO agents need long runs without babysitting y/n prompts.

## Topics
- `agent-skills`

## Related
- `web-blume-codes` — sidecar monitoring of coding agents
- `github-h4ckf0r0day-obscura` — isolate the agent in its own browser
- `web-obscura-sh` — same isolation product
- `x-2087263510090874911` — AGENTS.md + handoff when context fills

## Use when
Configuring YOLO/auto-run for a local agent, writing wipe/rebuild docs, or designing a secrets proxy. Not a design or 3D technique.
