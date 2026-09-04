# Kun Chen YOLO-agent ops: disposable Nix machine plus gated secrets

`x-2082316720086405524` · x · thread · en · [source](https://x.com/kunchenguid/status/2082316720086405524) · [raw](../../../raw/items/x-2082316720086405524/)
**Author:** Kun Chen (@kunchenguid) · **Published:** — · **Captured:** 2026-09-04T06:35:34Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** technique, claim-source · **Platforms:** cursor, codex, cli

**Summary.** Kun Chen explains running coding agents with all permission checks off by treating the laptop as a disposable employee device, rebuilding from nix-darwin dotfiles, and routing secrets through AutomicVault human approval gates.
**Question it answers.** How can you safely run agents with permission checks disabled on a local machine?

**Claims.**
- `x-2082316720086405524#c1` (opinion, stated) Author disables all agent permission checks and skips auto-review, treating the machine as an employee laptop not a personal device. — evidence: "i always disable all permission checks for my agents - i don't even do auto review." [post]
- `x-2082316720086405524#c2` (recipe, stated) Recovery path is nix-darwin plus home-manager dotfiles: wipe, clone, rebuild in minutes. — evidence: "i use nix-darwin and home-manager to make my entire machine instantly reproducible." [post]
- `x-2082316720086405524#c3` (recipe, stated) Production secrets stay off disk; AutomicVault gates each secret access while agents run commands freely. — evidence: "every time my agents need to access a secret, they go through me and i can decide whether i allow it or not" [post]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md), [session-hardening](../../techniques/session-hardening.md)
**Tools.** [nix-darwin](../../tools/nix-darwin.md), [automicvault](../../tools/automicvault.md)
**Links.** repo (https://github.com/kunchenguid/dotfiles/)
**Related items.** [web-blume-codes](../web-blume-codes/card.md), [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md)
**Media.** —
**Thread.** captured_partial · reported 41 · captured 3 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: [] · compare with: —
