# Research

## What it is
howaboua’s `pi-shepherdr`: talk to one Pi coding agent and let it run others. Tiny ~271-token orchestration surface; Herdr owns terminals/layout/lifecycle.

## How it works
- `list` — find agents and workspaces.
- `start` — name + placement (new workspace, tab, or pane), optional label/dir/first task.
- `watch` / `unwatch` — adopt or stop reporting without killing the worker.
- `send` — more work to a worker; finished work auto-steers the master with original task + full reply.
- Blocked workers include exact Herdr CLI commands in the notification.
- Deliberate non-goals: no focus/move/stop/close panes (Herdr’s job).
- Install: `pi install npm:@howaboua/pi-shepherdr` — https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-shepherdr

## Why saved
Minimal multi-agent for the Pi harness KB already uses (ponytail, clarify, handoff). Smaller than Anthropic’s 1k-subagent cookbook.

## Topics
- `agent-skills`

## Related
- `x-2087304957011911157` — pi-clarify (prompt rewrite before send)
- `x-2087026930323247306` — Claude dynamic workflows (heavier fan-out)
- `x-2087263510090874911` — Pi `/handoff` at 100k context
- `web-blume-codes` — watch agents from outside

## Use when
Running parallel Pi workers in Herdr without a huge orchestrator skill. Prefer this over inventing tmux scripts.
