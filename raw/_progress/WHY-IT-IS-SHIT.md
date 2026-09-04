# Why this idea bank is unusable for analysis

Diagnosis of `keyclaw6/design-ideas` as of 2026-09-04, before the preparation rewrite.

This repo was supposed to make it easy for a later agent to **read every saved post and uploaded resource, then synthesize and judge**. It is a harvest dump with a navigation skin. It is not an analysis corpus.

## What the last pass actually did

The previous work marked the catalog “complete” (`catalog/PLAN.md`). It built:

- 387 item folders + 1 long-form note
- 12 topic slugs and markdown briefs
- `catalog/index.md` / `filtered.md` / `patterns.md`
- a Graphify run (`graphify-out/`, 4247 nodes)

It did **not** finish the job that makes analysis possible.

## Failure 1 — X threads and comments were not captured

On X, the useful unit is almost never the root tweet. Authors continue the post in self-replies. Other people drop the actual recipe, repo, prompt, or counter-claim underneath. Those replies **are part of the source**.

Audit of 311 `raw/items/x-*/comments.md` files:

| Bucket | Count | What it is |
|--------|------:|------------|
| `<= 20` bytes | 181 | Literally `# Comments\n` |
| 21–80 bytes | 97 | Near-empty stub |
| 201–600 bytes | 2 | API-failure notes, no replies |
| 601–1500 bytes | 15 | Mixed stubs / thin captures |
| `> 1500` bytes | 16 | Real-ish thread text |
| Files with `###` reply headings | **24** | Structured replies |
| Files with 2+ `###` headings | **23** | More than one reply |

Only ~24/311 posts have a real comment capture. ~278 are empty or a stub.

The harvest skill (`skills/x-harvest-clear/SKILL.md`) writes `comments.md` as a **“replies stub”** and pulls the root tweet from `api.fxtwitter.com`. That API returns a **reply count**, not the conversation. Later agents documented the failure in a handful of files (`fx/vx return counts only`, jina blocked on x.com, Threadreader login wall) and then stopped. They did not come back with a working conversation fetch.

`extra.replies` exists on only 33 items. 280 X items have no reply count at all, so an analysis agent cannot even see which threads are missing.

**Verdict:** the last model did **not** go through posts and recover the comments that belong to the original post.

## Failure 2 — subjects are a junk drawer, not analysis lanes

User-named areas that must be first-class (spoken as “syrups / SERP optimization”, “freedom modeling”, “Gaussian splatting”) are either flattened or drowned:

| Slug | Item count | Problem |
|------|----------:|---------|
| `agent-skills` | 218 | Default tag. Almost everything an agent touched got this. |
| `design` | 135 | Second junk drawer |
| `seo-agents` | 43 | Closest to SERP / AEO / GEO — buried under “agents” |
| `gaussian-splatting` | 18 | Real cluster, but brief + auto-list only |
| `bess-3d-flythrough` | 17 | Project-specific, mixed with generic 3D |
| `keyboard-pcb` | 9 | Explicitly “later” |

Topics are non-exclusive tags with no **role** (tool vs technique vs example vs noise), no **primary subject**, and no **question the item helps answer**. An analysis agent opening `catalog/topics/agent-skills.md` gets a 271-line auto dump.

47 items were filtered because they did not fit the 12-slug SCHEMA, not because they were useless (local inference engines, FreeCAD, GTM playbooks). Filter reasons like “Filtered noise — see post.md” are not reasons.

## Failure 3 — there is no analysis layer

`catalog/PLAN.md` and `AGENTS.md` say: no judgment, do not pad `research.md`, navigation over prose.

Result:

- 161 empty `research.md` files
- 226 “real” research files that are mostly harvest notes, not extractable claims
- Titles in the index are truncated tweet text
- `patterns.md` is a decent start (cross-lane recipes with ids) but it is a human essay, not a machine index another agent can query
- No `claims[]`, no `techniques[]`, no comparable cards, no “what would I do with this” field

A judge agent still has to re-read ~311 posts + 76 web/github pages from scratch. The catalog does not reduce that work.

## Failure 4 — Graphify was dropped on the wrong substrate

`graphify-out/GRAPH_REPORT.md`:

- 4247 nodes, 3218 edges, **1128 communities**
- 100% EXTRACTED, 0% INFERRED
- Community hubs: “Research”, “Comments / thread”, “Replies”, repeated dozens of times, plus harvest-script names

Graphify parsed markdown headings in 387 near-identical item folders. It did not graph subjects, techniques, tools, or claims. The overlay makes search *worse* than `catalog/index.md`.

## Failure 5 — schema and metadata are inconsistent

`source.json` `extra` is an unbounded junk object (tweet metrics on 33 items, `category_note` on 309, `related_items` on 217, one-off keys for npm, arxiv, mcp probes, video byte counts…). An analysis agent cannot rely on any extra field existing.

There is no:

- `thread_status` (`missing` / `empty` / `author_thread` / `replies_captured` / `failed`)
- `primary_subject`
- `roles[]` (`tool`, `technique`, `example`, `claim-source`, `noise`)
- `analysis_ready` flag
- JSON/JSONL index of the whole bank

## What “good” must mean for the next agent

If you had to **synthesize and judge** this bank, you would want:

1. **Subject lanes that match how you think**, not how harvest tagged. SERP/AEO/GEO, 3D reconstruction / modeling / Gaussian splatting, video flythrough, agent design skills, MCP, motion/UI, etc. — discovered from content, not frozen at 12 slugs.
2. **Every X item’s author thread + relevant replies in one file**, with explicit empty/failed status and reply counts.
3. **A card per item** an agent can scan in ~10 seconds: what it is, subject, role, one-line claim, links, whether the thread was recovered, whether to ignore it.
4. **A claims/techniques index per subject** so judgment is compare-and-rank, not re-read-the-internet.
5. **A graph over those cards and claims**, not over `# Research` headings.
6. **Honest filters** with a reason an analyst can audit, including a “out of current focus but keep” shelf.

This rewrite is **preparation only**. No ranking of “best tool” yet. The output is a corpus another agent can actually reason over.
