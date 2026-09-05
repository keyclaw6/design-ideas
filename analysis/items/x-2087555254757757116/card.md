# KERNEL agent browsers add custom proxy CA bundle install

`x-2087555254757757116` · x · announcement · en · [source](https://x.com/usekernel/status/2087555254757757116) · [raw](../../../raw/items/x-2087555254757757116/)
**Author:** usekernel (@usekernel) · **Published:** — · **Captured:** 2026-09-04T07:07:43Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** — · **Roles:** tool, claim-source · **Platforms:** browser, mcp

**Summary.** KERNEL cloud agent browsers now accept a custom proxy with a CA bundle at creation time, automatically installing the certificate into the browser trust store for TLS interception, corporate MITM proxies, and private PKI staging sites.
**Question it answers.** How do KERNEL agent browsers trust custom TLS certificates behind corporate proxies?

**Claims.**
- `x-2087555254757757116#c1` (capability, stated) KERNEL browsers support custom proxies with CA bundles passed at proxy creation. — evidence: "KERNEL browsers now support custom proxies with CA bundles." [post]
- `x-2087555254757757116#c2` (recipe, stated) The supplied CA bundle is installed into the browser trust store automatically. — evidence: "pass your CA bundle in when you create the proxy and it will be installed in the browser's trust store automatically." [post]
- `x-2087555254757757116#c3` (capability, demonstrated) onkernel.com / kernel.sh homepage 200 / 103,733 B: sandboxed Chromium cold start advertised as <30ms; stealth “manage proxies”; SOC2/HIPAA; GPU acceleration; session MP4s. Docs index 335,184 B names Create/Control/Observe + MCP — strings CA bundle / trust store / custom proxy are absent. Tweet CA-install stays tweet-only. — evidence: "GET https://www.onkernel.com/ 103733 B; /docs 335184 B. leftover5-2026-09-05.json" [note]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** [kernel-browser](../../tools/kernel-browser.md)
**Links.** —
**Related items.** [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md), [web-obscura-sh](../web-obscura-sh/card.md), [github-punkpeye-awesome-mcp-servers](../github-punkpeye-awesome-mcp-servers/card.md)
**Media.**
`raw/items/x-2087555254757757116/media/media_0.jpg` (video, carries_technique=false) — Short screen recording showing KERNEL proxy settings UI where a CA bundle file is uploaded and applied to an agent browser session.
**Thread.** captured_partial · reported 6 · captured 1 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md), [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md)
