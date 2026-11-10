# We open sourced BrowserSkill, a bridge between your agent and your actual browser. most tools give the agent a blank

> Source: https://x.com/TencentAI_News/status/2100143086429217278 — @TencentAI_News — captured 2026-09-21T12:52:00Z
> Author: Tencent AI (@TencentAI_News)
> Posted: Wed Sep 16 08:41:45 +0000 2026
> Stats (at capture): 361482 views · 2709 likes · 134 replies · 322 reposts · 3521 bookmarks
> Captured: 2026-09-21T12:52:00Z

## Post

@TencentAI_News

We open sourced BrowserSkill, a bridge between your agent and your actual browser.

most tools give the agent a blank browser. We let it borrow a tab from yours, then hand it back.

> login state is already there, it just works where you're signed in
> captchas and confirmation dialogs come back to you, then it continues
> it's a CLI, not an MCP server => any agent that can run a shell can use it, and you see every call it makes

one thing that's easy to miss: the agent asks before borrowing a tab, and that switch lives in your browser settings, not in a flag, so it can't be talked around.

one line to install, works with Cursor, Claude Code, Codex, Hermes, Openclaw, CodeBuddy, WorkBuddy. Everything runs locally, MIT.

http://github.com/Tencent/BrowserSkill

## Author bio (at capture)

The official @Tencentglobal newsroom for AI updates and developer resources.

## Links

- http://github.com/Tencent/BrowserSkill
