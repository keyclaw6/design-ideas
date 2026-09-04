# Gojiberry Mcp

**Slug:** `gojiberry-mcp` · **Kind:** repo · **URL:** https://github.com/romangojiberryAI/gojiberryai-sales-os · **Canonical item:** [github-romangojiberryAI-gojiberryai-sales-os](../items/github-romangojiberryAI-gojiberryai-sales-os/card.md)
**Subjects:** [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md), [outbound-gtm-agents](../subjects/outbound-gtm-agents/brief.md)
**Referenced by (2):**
- [GojiberryAI Sales OS — 13-agent outbound stack on hosted MCP](../items/github-romangojiberryAI-gojiberryai-sales-os/card.md) — tool, example — outbound-gtm-agents
- [Gojiberry CEO launch — 13-agent outbound tree on hosted MCP for Grok Bot](../items/x-2094892848042725416/card.md) — example, claim-source — outbound-gtm-agents

<!-- NOTES:START -->

**2026-09-04 capture — repo + hosted MCP hello.** Clone `romangojiberryAI/gojiberryai-sales-os`. **13** agent markdown files: `account-researcher`, `follow-up-agent`, `head-of-sales`, `icp-analyst`, `intent-scorer`, `lead-enricher`, `linkedin-copywriter`, `meeting-qualifier`, `outreach-operator`, `pipeline-analyst`, `reply-agent`, `sales-manager`, `signal-hunter`. README: “No MCP, no live pipeline.” Hosted URL `https://mcp.gojiberry.ai/mcp` GET hello: `{"name":"Gojiberry AI","version":"1.0.0","status":"ok","docs":"https://ext.gojiberry.ai/documentation"}`. Unauthed `initialize` → JSON-RPC `-32001 Authentication required`.

`skills/sales-os/references/mcp.md` maps (not a live `tools/list`): `UserExternalController_getMe`, `getMyPermissions`; `OrganizationExternalController_getOrganization`, `getOrganizationMembers`; `ContactExternalController_findMany`, `findOne`, `create`, `update`, `enrichEmail`, `getIntentTypeCounts`, `addManyToList`, `removeManyFromList`; `ListExternalController_findAll` / `findOne` / `create`; `CampaignExternalController_findAll` / `findOne` / `update`; `AgentExternalController_findAll` / `findOne` / `update` / `findLogs`; `UniboxExternalController_getThreads`, `getThreadMessages`, `getMessagesByContactId`, `sendMessage`. Writes are approval-gated in the map.

<!-- NOTES:END -->
