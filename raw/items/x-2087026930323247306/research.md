# Research

## What it is
Pointer to Anthropic’s Dynamic Workflows cookbook: Claude writes the orchestration script and can spawn up to 1,000 subagents per run.

## How it works
- Notebook: `anthropics/claude-cookbooks` → `claude_agent_sdk/08_Dynamic_workflows.ipynb`
- Agent authors the control script instead of a human wiring a static graph.
- Fan-out: large subagent pools for bounded tasks; results fold back to the parent.
- Official SDK pattern, not a random tweet recipe.

## Why saved
Canonical fan-out design for harvest/research/SEO crawl jobs. Complements pi-shepherdr (tiny orchestration surface) and the Stanford control-plane paper.

## Topics
- `agent-skills`

## Related
- `x-2087232392209531166` — pi-shepherdr (tiny master/worker surface)
- `x-2086790895538700379` — loop-library templates
- `x-2087254502210490739` — why naive multi-agent handoffs rot context
- `web-anthropic-claude-self-service-data` — Anthropic’s own agent+data pattern

## Use when
You need official Claude Agent SDK fan-out, or to contrast “1k subagents” with a small shepherd CLI.
