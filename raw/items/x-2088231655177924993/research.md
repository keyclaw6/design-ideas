# Research

## What it is
Obsidian Mind — OSS Obsidian vault that gives coding agents (Claude Code, Codex CLI, Gemini CLI) persistent memory across sessions: projects, decisions, tasks, notes.

## How it works
- Repo (tweet obfuscated): https://github.com/breferrari/obsidian-mind
- Vault-as-memory: markdown the agent reads/writes instead of a proprietary memory API.
- Amplifier post (“follow me for more”) but the vault pattern is real and matches this library’s own raw/items + research.md approach.
- Works across CLIs that can read the filesystem; no extra MCP required if the agent already has file tools.
- Compare to Memoria (snapshots/branches) and ReasoningBank (trajectory memory).

## Why saved
KB already uses markdown as agent memory. A packaged Obsidian vault with conventions for decisions/tasks is a drop-in layout for project memory beside DESIGN.md.

## Topics
`agent-skills`

## Related
- `x-2087955721732460791` — Type.com hosted multi-layer memory
- `x-2087208634493095978` — Memoria versioned memory
- `x-2087143369181114868` — ReasoningBank experience memory
- `web-davidgasquez-context-engineering` — treat context as ETL

## Use when
Giving Claude Code / Codex / Gemini a durable project brain in git, or choosing vault-files vs hosted company-brain vs git-like memory.
