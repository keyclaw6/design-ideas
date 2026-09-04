## What it is

Wafer AI announcing DeepSeek-V4-Flash-0731-Fast as a provider on Vercel AI Gateway (screenshot dated 2026-08-15).

## How it works

- Distribution path is Vercel AI Gateway, not a bespoke SDK — one base URL / provider switch.
- Pick `wafer_ai` as the gateway provider to hit this Flash-Fast variant.
- Same model family as the RunInfra BF16 post; this one is the Fast/gateway SKU.
- A shorter follow-up tweet (`x-2088706415586377792`) restates the same news with no new facts — treat that as duplicate.
- Practical for Next.js / Vercel-hosted agent UIs that already speak the AI Gateway API.

## Why saved

Saved as a routing option: keep DeepSeek in the Vercel stack without a new vendor integration.

## Topics

`agent-skills`

## Related

`x-2088594942482374759`, `x-2088706415586377792`, `x-2089165107364278341`, `github-superdesigndev-treg`

## Use when

An app already on Vercel AI Gateway needs DeepSeek V4 Flash, or when comparing gateway providers (Wafer vs RunInfra vs local GGUF).
