# ANALYSIS_STRUCTURE — binding spec for the analysis layer

Status: **binding**. Workers follow this file literally. Where this file and any other file in the repo disagree (`SCHEMA.md`, `AGENTS.md`, `catalog/*`), this file wins.

Scope: preparation only. Nothing here ranks tools or picks winners. The output is a corpus + indexes that a later judge agent can reason over one subject at a time.

Numbers that this spec is built on (measured 2026-09-04): 387 item folders under `raw/items/` (311 `x-*`, 50 `web-*`, 26 `github-*`) + 1 note under `raw/notes/` = **388 analysis units**. Of the 311 X items, 24 have a structured reply capture, 29 are "failed stub" notes, 257 are empty or near-empty.

---

## 1. Diagnosis

The current bank is a harvest with a table of contents. It fails an analysis agent for five concrete reasons:

1. **The unit of analysis is wrong.** The bank's unit is the item folder; the analyst's unit is the subject. There is no file that lets an agent load one subject and see every item, every recurring technique, every tool, and every checkable claim in that subject. `catalog/topics/*.md` comes closest but is a curated top + an auto-dumped list of truncated tweet titles.
2. **X posts are half-captured.** Author continuations and the replies that carry the repo / prompt / correction are missing on ~287 of 311 X items, and the absence is not recorded in any queryable field. An analyst cannot tell `x-2095159781883597031` (comments never fetched) from a post that genuinely has zero replies.
3. **Tags are not roles.** `topics[]` says "this is near SEO" but never says whether the item is a tool, a technique, a worked example, or a claim to verify. `agent-skills` is on 218 items, so it carries no information. 47 filtered items were shelved for not fitting 12 slugs, not for being useless, and 12 of them carry the non-reason "Filtered noise — see post.md".
4. **No extracted layer exists.** No claims, no numbers, no recipe steps, no comparable fields. `research.md` is 161× empty and otherwise unstructured harvest notes. `patterns.md` has the right idea (recipes with item ids) but is a human essay, not queryable.
5. **The graph was built over the wrong text.** Graphify parsed 387 near-identical folders with `# Research` / `# Comments` headings and produced 1128 communities named after those headings. The graph currently makes search worse than `catalog/index.md`.

Underlying cause: every previous pass optimised for "navigable", never for "extractable". The rewrite must produce extractable records first and navigation as a rendered by-product.

---

## 2. Design principles

If I had to synthesize and judge this bank, I would want the following, and this spec enforces each one:

1. **Subject is the primary axis; role is the secondary axis.** Every analyzed item has exactly one `primary_subject` and 1–3 `roles`. Loading one subject folder must be sufficient to analyze that subject.
2. **JSON is authoritative, Markdown is rendered.** Workers write `card.json`, `thread.json`, `brief.json`. Scripts render `card.md`, `thread.md`, `items.jsonl`, `claims.jsonl`, `index.jsonl`, tool pages, technique pages. Hand-written Markdown exists in exactly two places: subject `brief.md` and the free-notes block of technique pages. This removes drift and makes verification mechanical.
3. **The conversation is part of the post.** Every X item has a thread record with an honest status (`captured_full | captured_partial | empty | failed`), a reported reply count, and a fetch log. "We did not try" is not a permitted end state.
4. **Claims are the atoms the judge compares.** Each analyzed item yields ≥1 claim with quoted evidence and a confidence tag. Subject-level `claims.jsonl` is the judge's worksheet; nobody re-reads 311 tweets.
5. **Entities are files, not headings.** Subjects, tools, and techniques each have one file with one H1. Cards link to those files. Graphify then sees a graph of items → tools / techniques / subjects instead of 387 islands.
6. **Filters are auditable.** Every shelved item keeps a card and a reason that names something observable in the post. Four shelves: `noise`, `duplicate`, `out-of-scope`, `uncategorized`. Nothing is deleted.
7. **Raw is frozen, analysis is the entry point.** `raw/` is append-only (thread payloads only). All reading starts in `analysis/`. `catalog/` becomes legacy input, not a destination.
8. **Ownership is by path.** Each parallel worker owns a disjoint set of paths for the whole phase. Cross-owner changes go through request files, never direct edits.
9. **Every rule is checkable by a script.** If a rule cannot be verified with `jq`/Python over the tree, it is not in this spec.

---

## 3. Directory tree

Exact paths. `<id>` is the existing raw folder name (e.g. `x-2094553318031024285`, `github-nv-tlabs-ArtiFixer`, `web-crowdreply`) or `note-<name>` for notes. `<subject>`, `<tool>`, `<technique>` are lowercase ASCII slugs `[a-z0-9]+(-[a-z0-9]+)*`, max 48 chars.

```
/workspace
├── docs/
│   └── ANALYSIS_STRUCTURE.md            # this file
├── analysis/                            # THE ONLY TREE AN ANALYST READS; the only tree Graphify ingests
│   ├── README.md                        # entry point (§3.1)
│   ├── subjects.json                    # taxonomy registry (§5), hand-maintained by the parent only
│   ├── index.jsonl                      # GENERATED — one line per analysis unit (388 lines)
│   ├── items/
│   │   └── <id>/
│   │       ├── card.json                # WORKER-WRITTEN (card worker) — authoritative
│   │       ├── card.md                  # GENERATED from card.json (+ thread.json)
│   │       ├── thread.json              # WORKER-WRITTEN (thread worker) — x-* items only
│   │       └── thread.md                # GENERATED from thread.json — x-* items only
│   ├── subjects/
│   │   └── <subject>/
│   │       ├── brief.md                 # WORKER-WRITTEN (subject worker) — the one hand-written prose file
│   │       ├── brief.json               # WORKER-WRITTEN (subject worker)
│   │       ├── items.jsonl              # GENERATED — slice of index.jsonl where primary or secondary = <subject>
│   │       └── claims.jsonl             # GENERATED — every claim from every item in items.jsonl
│   ├── tools/
│   │   └── <tool>.md                    # GENERATED stub + preserved NOTES block (registry worker owns)
│   ├── techniques/
│   │   └── <technique>.md               # GENERATED stub + hand-written NOTES block (owner subject worker)
│   ├── registry/
│   │   ├── tools.jsonl                  # GENERATED from cards, then aliases applied
│   │   ├── techniques.jsonl             # GENERATED from cards, then aliases applied
│   │   └── aliases.json                 # HAND-MAINTAINED by registry worker: slug merges {"from":"to"}
│   ├── shelf/
│   │   ├── shelf.jsonl                  # GENERATED — every card with disposition=shelf (§4.5 record)
│   │   ├── noise.md                     # GENERATED tables per shelf
│   │   ├── duplicate.md
│   │   ├── out-of-scope.md
│   │   └── uncategorized.md
│   └── _work/                           # orchestration state; Graphify ignores; committed
│       ├── batches.json                 # id → batch number (§7)
│       ├── handoffs/<worker-id>.md      # one per worker
│       ├── reclass/<subject>.jsonl      # subject workers' reclassification requests
│       ├── requests/<worker-id>.md      # cross-owner change requests
│       └── reports/                     # validator/verify outputs
├── scripts/
│   └── analysis/
│       ├── make_batches.py              # writes analysis/_work/batches.json
│       ├── validate_cards.py            # schema + enum checks on card.json / thread.json / brief.json
│       ├── build_registry.py            # cards → registry/*.jsonl (applies aliases.json)
│       ├── render.py                    # card.md, thread.md, tools/*.md, techniques/*.md, subjects/*/items.jsonl, claims.jsonl, shelf/*
│       ├── build_index.py               # analysis/index.jsonl
│       ├── apply_reclass.py             # applies _work/reclass/*.jsonl to card.json, then re-render
│       └── verify.py                    # §9 checklist, prints numbered PASS/FAIL, exit code
├── raw/                                 # FROZEN harvest. Only permitted write: raw/items/<id>/thread-raw/
│   ├── items/<id>/…                     # unchanged
│   ├── items/<id>/thread-raw/           # NEW, x-* only: raw fetch payloads (JSON/HTML), one file per attempt
│   ├── notes/…                          # unchanged
│   └── _progress/…                      # unchanged (legacy)
├── catalog/                             # LEGACY. Read-only input for subject workers. Banner added to README.md only.
├── graphify-out/                        # REBUILT over analysis/ only (§8)
├── .graphifyignore                      # REPLACED with §8 content
├── AGENTS.md                            # §3.2 replacement
└── SCHEMA.md                            # one pointer line added at top (§3.2)
```

### 3.1 `analysis/README.md` — required content

Must contain, in this order, with these exact H2 headings:

1. `## Analyze one subject in five reads` — the procedure: (1) `subjects.json` → pick slug; (2) `subjects/<slug>/brief.md`; (3) `subjects/<slug>/claims.jsonl`; (4) the technique pages listed in the brief; (5) `items/<id>/card.md` for ids the brief marks `must_read`. Rule stated verbatim: **"Do not open `raw/` unless the card's `readiness` is `ready-with-gaps` or `blocked`."**
2. `## Machine access` — `jq` one-liners against `index.jsonl` (filter by `primary_subject`, `roles`, `thread.status`, `readiness`).
3. `## Files and who writes them` — the GENERATED vs WORKER-WRITTEN table from §3.
4. `## Shelves` — the four shelves and what each means.
5. `## Graph` — `graphify query` / `explain` / `path` and the statement that the graph covers `analysis/**/*.md` only.

### 3.2 Legacy file edits (exact)

- `AGENTS.md`: replace the "Query order" section with: `1. analysis/README.md 2. analysis/subjects.json 3. analysis/subjects/<slug>/brief.md 4. analysis/index.jsonl 5. analysis/items/<id>/card.md 6. raw/ only when card.readiness != ready`. Keep the X harvest and Graphify sections; change `graphify update .` note to "graph covers analysis/ only".
- `catalog/README.md`: prepend one line: `> LEGACY (2026-09). Superseded by ../analysis/README.md. Kept as input; do not edit.`
- `SCHEMA.md`: prepend one line: `> Raw capture schema only. Analysis-layer schemas: docs/ANALYSIS_STRUCTURE.md §4.`
- `README.md` (root): replace the "Agent entry point" line to point at `analysis/README.md`.

No other legacy files are modified.

---

## 4. Schemas

Conventions for all JSON in `analysis/`:

- UTF-8, 2-space indent for `.json`; one compact object per line for `.jsonl`.
- Timestamps ISO-8601 UTC with `Z`.
- `schema_version` is the string `"1"` everywhere in this pass.
- Absent optional values are `null`, never omitted (validator checks key presence).
- All paths are repo-relative POSIX strings.
- Enum values are lowercase kebab-case exactly as listed. Unknown enum values fail validation.

### 4.1 `analysis/items/<id>/card.json` — per-item analysis card

Written by the card worker. One per analysis unit (388).

| Field | Type | Required | Rule |
|---|---|---|---|
| `schema_version` | string | yes | `"1"` |
| `id` | string | yes | equals folder name; equals `raw` id |
| `source_type` | enum | yes | `x \| github \| website \| note` |
| `url` | string | yes | canonical URL from `source.json`; for notes the repo path |
| `title` | string | yes | English, ≤ 90 chars, **not** truncated tweet text. Must name the artifact or the claim ("Splat2Mesh — free Windows 3DGS PLY → OBJ/GLB converter", not "3DGSは見た目が…") |
| `author` | object | yes | `{ "name": string\|null, "handle": string\|null, "url": string\|null }` |
| `published_at` | string\|null | yes | from `extra.created_at` / repo metadata / page; null if unknown |
| `captured_at` | string | yes | copy of `source.json.captured_at` |
| `lang` | string | yes | BCP-47 of the primary text (`en`, `ja`, `zh`, `es`, …) |
| `disposition` | enum | yes | `analyze \| shelf` |
| `shelf` | enum\|null | yes | null when `analyze`; else `noise \| duplicate \| out-of-scope \| uncategorized` |
| `shelf_reason_code` | enum\|null | yes | see §4.5; null when `analyze` |
| `shelf_reason` | string\|null | yes | ≥ 60 chars when shelved; must contain a noun phrase quoted or paraphrased from the post; banned substrings (case-insensitive): `see post.md`, `filtered noise`, `no matching topic`, `out of taxonomy` |
| `duplicate_of` | string\|null | yes | item id; required iff `shelf = duplicate`; target must have `disposition = analyze` |
| `primary_subject` | string\|null | yes | slug from `subjects.json`; **required when `analyze`**, null when shelved |
| `secondary_subjects` | string[] | yes | 0–2 slugs from `subjects.json`, ≠ primary; `[]` when shelved |
| `roles` | enum[] | yes | 1–3 of `tool \| technique \| example \| claim-source \| reference`; `[]` when shelved |
| `artifact_type` | enum | yes | `repo \| product \| paper \| article \| thread \| demo-video \| demo-image \| dataset \| course \| announcement \| opinion \| note` |
| `platforms` | enum[] | yes | 0–4 of `claude-code \| codex \| cursor \| grok-bot \| gemini \| pi \| blender \| unreal \| three-js \| react \| remotion \| comfyui \| fal \| runway \| higgsfield \| kicad \| fusion \| openscad \| browser \| cli \| mcp \| other` |
| `summary` | string | yes | English, 1–2 sentences, 80–320 chars, states what the artifact IS and what it DOES. No hype adjectives copied from the post |
| `question_it_answers` | string\|null | yes | one line, the analyst question this item helps answer ("How do I get a brand cited on pages ChatGPT already uses?"); required when `analyze` |
| `claims` | Claim[] | yes | ≥ 1 when `analyze`; `[]` allowed when shelved. Schema §4.1.1 |
| `recipe_steps` | string[] | yes | ordered steps if the item contains a how-to; `[]` otherwise. Each ≤ 200 chars |
| `numbers` | Number[] | yes | every quantitative claim as `{ "label": string, "value": string, "unit": string\|null, "source": EvidenceSource }`; `[]` if none |
| `techniques` | string[] | yes | technique slugs (§4.6 naming); 0–5; `[]` when shelved |
| `tools` | string[] | yes | tool slugs (§4.6 naming); 0–8; `[]` when shelved |
| `links` | object | yes | `{ "canonical": string, "repo": string\|null, "paper": string\|null, "product": string\|null, "other": string[], "related_items": string[] }`. `related_items` = item ids seeded from `source.json.extra.related_items`, pruned to those that actually relate |
| `media` | Media[] | yes | one entry per file in `raw/items/<id>/media/`; `[]` if none. Schema §4.1.2 |
| `raw` | object | yes | `{ "folder": "raw/items/<id>", "post": "raw/items/<id>/post.md"\|"…/page.md"\|"raw/notes/<name>.md", "comments": "raw/items/<id>/comments.md"\|null, "research": "raw/items/<id>/research.md"\|null, "legacy_topics": string[], "legacy_filtered": bool }` |
| `readiness` | enum | yes | `ready \| ready-with-gaps \| blocked \| shelved` (§4.1.3) |
| `gaps` | enum[] | yes | 0+ of `thread-failed \| thread-partial \| media-undescribed \| linked-page-unfetched \| translation-needed \| paywalled` |
| `judge_hints` | object | yes | `{ "compare_with": string[] (item ids, 0–6), "must_read": bool, "why_must_read": string\|null }`. `must_read` true for at most 12 items per subject |
| `worker` | string | yes | worker id, e.g. `cards-07` |
| `written_at` | string | yes | timestamp |

#### 4.1.1 Claim

| Field | Type | Rule |
|---|---|---|
| `id` | string | `<item-id>#c<n>`, n from 1, unique in file |
| `text` | string | one declarative English sentence, ≤ 240 chars, no hedging words added by the worker |
| `kind` | enum | `result \| recipe \| capability \| benchmark \| pricing \| availability \| opinion \| counter-claim` |
| `evidence` | string | verbatim quote (original language allowed) or exact number, ≤ 400 chars |
| `evidence_source` | EvidenceSource | `post \| author-thread \| reply \| quoted-post \| linked-page \| media \| note` |
| `evidence_ref` | string\|null | reply id / URL / media path the evidence came from; null when `post` |
| `confidence` | enum | `demonstrated` (shows output/screenshot/repo), `stated` (asserted, no proof), `contested` (a reply disputes it), `unverified` (from a third party or promo) |
| `subject` | string | subject slug this claim belongs to (primary or a secondary of the item) |

#### 4.1.2 Media

| Field | Type | Rule |
|---|---|---|
| `path` | string | `raw/items/<id>/media/<file>` |
| `type` | enum | `image \| video \| gif \| other` |
| `description` | string\|null | ≥ 20 chars, what is visible and what it proves; **required for `image`**; for `video` use thumb + post text, ≥ 20 chars or null with `skip_reason` |
| `skip_reason` | string\|null | required iff `description` is null |
| `carries_technique` | bool | true when the image/video contains the actual recipe, prompt, UI, or result that the text does not |

#### 4.1.3 Readiness computation (deterministic; `validate_cards.py` recomputes and overwrites)

- `shelved` iff `disposition = shelf`.
- `blocked` iff `analyze` and any of: `summary` missing/short, `claims` empty, `primary_subject` null, any `image` media without description and without `skip_reason`, `question_it_answers` null.
- `ready-with-gaps` iff `analyze`, not blocked, and (`source_type = x` and `thread.status ∈ {failed, captured_partial}`) or `gaps` non-empty.
- `ready` otherwise.

### 4.2 `analysis/items/<id>/thread.json` — conversation record (x-* only, 311 files)

Written by the thread worker.

| Field | Type | Rule |
|---|---|---|
| `schema_version` | string | `"1"` |
| `id` | string | item id |
| `tweet_id` | string | numeric string |
| `root_author_handle` | string | without `@` |
| `status` | enum | `captured_full \| captured_partial \| empty \| failed` (§6.3) |
| `author_thread_status` | enum | `none \| captured \| partial \| unknown` |
| `reply_count_reported` | int\|null | from platform (fx/vx/GraphQL). null only with `count_unavailable_reason` |
| `count_unavailable_reason` | string\|null | required iff `reply_count_reported` null |
| `quote_count_reported` | int\|null | |
| `replies_captured` | int | length of `replies` |
| `replies_relevant` | int | count where `relevance = relevant` |
| `replies_dropped_unfetched` | int\|null | `reply_count_reported − replies_captured` when both known |
| `truncated` | bool | true when more than 50 relevant replies existed and only 50 stored |
| `author_thread` | Post[] | root author's self-reply chain in order (root excluded) |
| `replies` | Reply[] | non-author replies + author replies-to-others, captured order |
| `quoted` | Post[] | tweets quoted by the root or by author_thread posts |
| `fetch_log` | Fetch[] | ≥ 1 entry; ≥ 2 distinct `method` values when `status = failed` |
| `raw_payloads` | string[] | paths under `raw/items/<id>/thread-raw/` |
| `worker` | string | |
| `written_at` | string | |

Post: `{ "id": string, "author_handle": string, "created_at": string|null, "text": string, "text_en": string|null, "urls": string[], "media_urls": string[], "metrics": { "likes": int|null, "replies": int|null, "reposts": int|null, "views": int|null } }`

Reply = Post + `{ "parent_id": string, "depth": int (1 = reply to root), "is_author": bool, "relevance": "relevant" | "noise", "relevance_kind": null | "link" | "recipe" | "number" | "correction" | "counter-claim" | "alternative-tool" | "answered-question" | "author-continuation" | "fact-check", "downloaded_media": string[] }`

Fetch: `{ "at": string, "method": enum, "target": string (URL or id), "outcome": enum, "note": string|null }` with `method ∈ { x-graphql-tweetdetail, x-web-dom, fxtwitter-api, vxtwitter-api, jina-fixupx, syndication-embed, nitter, threadreader, other }` and `outcome ∈ { ok, partial, empty, blocked, login-wall, rate-limited, error }`.

### 4.3 `analysis/subjects/<subject>/brief.json` — per-subject brief metadata

Written by the subject worker after cards exist.

| Field | Type | Rule |
|---|---|---|
| `schema_version` | string | `"1"` |
| `slug` | string | equals folder; exists in `subjects.json` |
| `name` | string | human name |
| `owner_aliases` | string[] | spoken names ("syrups", "SERP optimization", "freedom modeling") |
| `priority` | enum | copied from `subjects.json` |
| `inclusion_rule` | string | one paragraph, copied then refined from `subjects.json` |
| `exclusion_rule` | string | what goes to which neighbour |
| `item_count_primary` | int | equals count in `items.jsonl` where `primary_subject = slug` |
| `item_count_secondary` | int | |
| `role_counts` | object | `{ "tool": n, "technique": n, "example": n, "claim-source": n, "reference": n }` |
| `thread_coverage` | object | `{ "x_items": n, "captured_full": n, "captured_partial": n, "empty": n, "failed": n }` |
| `techniques` | string[] | technique slugs used by ≥ 1 item in the subject |
| `tools` | string[] | tool slugs used by ≥ 1 item in the subject |
| `must_read` | string[] | ≤ 12 item ids, equals cards with `judge_hints.must_read = true` and this primary |
| `comparison_axes` | string[] | 3–8 criteria a judge should score on (e.g. "time-to-first-citation", "requires paid API", "local-only"). **No verdicts.** |
| `open_questions` | string[] | ≥ 1 |
| `adjacent_subjects` | string[] | slugs |
| `written_by` | string | |
| `written_at` | string | |

#### 4.3.1 `brief.md` — required structure

H1: `# <name> (<slug>)`. Then these H2 headings **exactly, each prefixed with the slug** so no two subjects share a heading string:

```
## <slug> — scope
## <slug> — what the owner is trying to decide
## <slug> — roster by role
## <slug> — techniques
## <slug> — tools
## <slug> — claims to adjudicate
## <slug> — comparison axes
## <slug> — thread coverage
## <slug> — gaps and open questions
## <slug> — adjacent subjects
```

Rules: roster lists every primary item as `- [title](../../items/<id>/card.md) — roles — one clause`; techniques/tools link to `../../techniques/<slug>.md` / `../../tools/<slug>.md`; the claims section is a table of ≤ 15 rows (`claim id | text | confidence | item`) plus the line `Full set: claims.jsonl (N rows)`; comparison axes are criteria only. Length 120–400 lines. No headings deeper than H2.

### 4.4 `analysis/index.jsonl` — machine index (GENERATED, 388 lines)

One object per analysis unit, sorted by `id`. Fields are a strict projection of `card.json` + `thread.json`:

```
id, source_type, url, title, author.handle, published_at, lang,
disposition, shelf, shelf_reason_code, duplicate_of,
primary_subject, secondary_subjects, roles, artifact_type, platforms,
summary, question_it_answers,
claim_count, claim_ids, techniques, tools,
thread: { status, author_thread_status, reply_count_reported, replies_captured, replies_relevant } | null,
media_count, media_described_count,
readiness, gaps,
judge_hints.must_read, judge_hints.compare_with,
paths: { card: "analysis/items/<id>/card.md", card_json, thread_json|null, raw_folder },
legacy: { topics: string[], filtered: bool }
```

`analysis/subjects/<subject>/items.jsonl` is the same record type filtered to `primary_subject = <subject>` OR `<subject> ∈ secondary_subjects`, with an added field `membership: "primary" | "secondary"`, sorted primary-first then by id.

`analysis/subjects/<subject>/claims.jsonl` is every Claim (§4.1.1) whose `subject = <subject>`, each augmented with `item_id`, `item_title`, `roles`, `thread_status`.

### 4.5 Shelf record — `analysis/shelf/shelf.jsonl` (GENERATED from shelved cards)

```
id, title, shelf, shelf_reason_code, shelf_reason, duplicate_of, legacy_filtered, worker, written_at, raw_folder
```

`shelf_reason_code` enum by shelf:

| shelf | codes |
|---|---|
| `noise` | `engagement-bait` (no artifact, asks for follow/bookmark), `promo-no-artifact` (marketing with no technique or product page), `availability-announcement` ("X is now live on Y", pricing/discount only), `empty-capture` (no text, no media), `unrelated-personal` (skincare, politics, anecdotes) |
| `duplicate` | `same-artifact-no-new-angle` (must set `duplicate_of`) |
| `out-of-scope` | `real-artifact-no-subject` (a real tool/technique that no subject in §5 covers and that the owner's stated focus does not need). Reason must name the artifact and the nearest rejected subject |
| `uncategorized` | `needs-triage` (card worker could not decide). **Transitional**: after the shelf auditor pass, ≤ 19 items (5%) may remain here, each with a reason naming the two candidate subjects considered |

Shelved items still get a full `card.json` with `disposition = shelf`, `summary`, `artifact_type`, `media[]` (descriptions optional), `raw{}`. Empty `claims`, `roles`, `techniques`, `tools`.

### 4.6 Registry records and slug naming

`analysis/registry/tools.jsonl` (GENERATED): `{ slug, name, kind: "product|repo|model|library|service|api|hardware", canonical_url|null, canonical_item|null (item id whose artifact IS this tool), item_ids: string[], subjects: string[], first_seen_worker }`

`analysis/registry/techniques.jsonl` (GENERATED): `{ slug, name, item_ids: string[], subjects: string[], owner_subject: string (the subject with most items; tie → alphabetical), singleton: bool (item_ids.length == 1) }`

`analysis/registry/aliases.json` (HAND): `{ "crowd-reply": "crowdreply", "3dgs-mesh-converter": "3dgs-mesh-converter", … }` — maps every slug that appears in any card to its canonical slug. `build_registry.py` rewrites card slugs through this map before generating pages.

Slug naming rules (workers apply these before the alias pass):

- Tools: the product/repo name as written by its maker, lowercased, spaces and punctuation → `-`, drop "the"/".ai"/".dev" suffixes when the name is unambiguous without them: `crowdreply`, `grok-bot`, `blender-mcp`, `splat2mesh`, `lichtfeld-studio`, `minimax-h3`, `seedance-2-5`, `artifixer`, `impeccable`, `design-md`, `scroll-craft`, `openseo`, `dataforseo`, `tinyshelf`, `tinylaunch`, `treg`, `gojiberry-sales-os`, `obscura`, `remotion`, `hyperframes`, `world-labs-atlas`, `spark-js`, `three-js`, `higgsfield`, `unreal-mcp`, `cozyclay`, `mint-studio`, `cadxstudio`, `smith`, `openscad`, `kicad`. Model versions keep the version: `deepseek-v4-flash`, `qwen3-8-27b`.
- Techniques: verb-or-noun phrase naming the move, 2–5 words: `citation-outreach`, `directory-backlink-dr-lift`, `free-tool-pages-for-seo`, `topical-map-content`, `reddit-comment-ranking`, `ai-crawler-ua-allowlist`, `blockout-then-video-model`, `first-last-frame-conditioning`, `depth-pass-motion-reference`, `mcp-driven-scene-build`, `splat-to-mesh-export`, `splat-repair-diffusion`, `one-image-to-world`, `panorama-to-city-mesh`, `designmd-as-agent-contract`, `anti-slop-skill-pack`, `scroll-driven-3d-hero`, `layered-parallax-from-imagegen`, `html-as-video-render`, `shot-recipe-cards`, `autoresearch-loop`, `agent-memory-versioning`, `text-to-cad-prompting`, `directory-of-prompts-as-skill`.

A technique slug may be used only if ≥ 2 items share it **or** the worker sets it anyway and `build_registry.py` marks `singleton: true`; singletons are allowed but the subject worker must either merge them via `aliases.json` request or keep them with a one-line justification in the technique page NOTES block.

### 4.7 Tool and technique pages (GENERATED with preserved NOTES)

`analysis/tools/<tool>.md`:

```
# <name>

**Slug:** `<slug>` · **Kind:** <kind> · **URL:** <canonical_url or —> · **Canonical item:** [<id>](../items/<id>/card.md) or —
**Subjects:** [<subject>](../subjects/<subject>/brief.md), …
**Referenced by (N):**
- [<title>](../items/<id>/card.md) — <roles> — <primary_subject>
…
<!-- NOTES:START -->
(free text, no headings; preserved across re-renders)
<!-- NOTES:END -->
```

`analysis/techniques/<technique>.md` has the same shape with `**Owner subject:**` and, in NOTES, a required 3–10 line description written by the owner subject worker: what the move is, preconditions, what it produces, which items demonstrate vs merely state it. Singletons: one line justifying why it is not merged.

Both page types: exactly one heading (the H1). No H2+.

### 4.8 `card.md` render template (GENERATED)

```
# <title>

`<id>` · <source_type> · <artifact_type> · <lang> · [source](<url>) · [raw](../../../raw/items/<id>/)
**Author:** <name> (@<handle>) · **Published:** <published_at> · **Captured:** <captured_at>
**Disposition:** analyze | shelf:<shelf> (<shelf_reason_code>) · **Readiness:** <readiness> · **Gaps:** <gaps or —>
**Subject:** [<primary>](../../subjects/<primary>/brief.md) · **Also:** [<secondary>](…), … · **Roles:** <roles> · **Platforms:** <platforms>

**Summary.** <summary>
**Question it answers.** <question_it_answers>

**Claims.**
- `<claim id>` (<kind>, <confidence>) <text> — evidence: "<evidence>" [<evidence_source>]
…
**Numbers.** <label>: <value> <unit> (<source>); …
**Recipe.** 1. … 2. …
**Techniques.** [<slug>](../../techniques/<slug>.md), …
**Tools.** [<slug>](../../tools/<slug>.md), …
**Links.** repo · paper · product · other…
**Related items.** [<id>](../<id>/card.md), …
**Media.** `<path>` (<type>, carries_technique) — <description>
**Thread.** <status> · reported <n> · captured <n> · relevant <n> · author thread: <author_thread_status> → [thread.md](thread.md)   (x-* only)
**Judge hints.** must_read: <bool> · compare with: [<id>](../<id>/card.md), …
**Shelf reason.** <shelf_reason>   (shelved only)
```

Exactly one heading (the H1). Every other label is bold text. This is what makes the graph work (§8).

### 4.9 `thread.md` render template (GENERATED, x-* only)

```
# Thread — <title> (<id>)

**Status:** <status> · **Author thread:** <author_thread_status> · **Replies reported:** <n> · **Captured:** <n> · **Relevant:** <n> · **Unfetched:** <n> · **Truncated:** <bool>
**Fetch log:** <method>→<outcome> (<at>); …
**Raw payloads:** `raw/items/<id>/thread-raw/…`

**Author continuation (N posts).**
> **@<handle>** · <id> · <created_at>
> <text>
…
**Quoted.**
> **@<handle>** · <id>
> <text>

**Relevant replies (N of M captured).**
> **@<handle>** · <id> · depth <d> · <relevance_kind>
> <text>
…
**Dropped as noise:** <count> replies (praise, emoji, bots, unrelated promo).
```

Exactly one heading. Replies are blockquotes, never headings.

### 4.10 Graphify overlay inputs

Graphify ingests **only**: `analysis/**/*.md` except `analysis/_work/**`. That is: `README.md`, 388 `card.md`, 311 `thread.md`, ~16 `brief.md`, all `tools/*.md`, all `techniques/*.md`, `shelf/*.md`.

Graphify must ignore: everything under `raw/`, `catalog/`, `docs/`, `scripts/`, `skills/`, `agent-tools/`, `.orchestrate/`, all `*.json` and `*.jsonl` anywhere, `analysis/_work/**`, media of any kind, `graphify-out/` itself.

Why this works: every ingested file has exactly one heading (the entity name) except `brief.md`, whose H2s are slug-prefixed and therefore unique. Cross-file edges come from the relative links in cards → subjects/tools/techniques/other cards. Hubs become subject briefs, tool pages, technique pages. Exact commands and checks in §8.

---

## 5. Subject taxonomy

Discovered from `raw/_progress/item-inventory.md` plus the topic briefs. Seventeen primary subjects (target grain 14–17 after merges), four shelves. Grain rule: a primary subject has 6–60 analyzed items; if after classification a subject has < 6 primary items, the parent merges it into its `fallback` and removes it from `subjects.json`.

Every analyzed item has **exactly one** primary subject. Ties are broken by the question "which subject's judge would be worst off without this item?". Secondary subjects (0–2) record real overlap, not vibes.

`analysis/subjects.json` is an array of objects `{ slug, name, owner_aliases[], priority, inclusion_rule, exclusion_rule, fallback, seed_items[], expected_range: [lo, hi] }`. Priority ∈ `now | standard | later`. The table below is its normative content; the parent writes the JSON from it verbatim.

| # | slug | name | priority | inclusion rule | goes elsewhere | fallback | seed items (not exhaustive) | expected |
|---|---|---|---|---|---|---|---|---|
| 1 | `serp-ai-visibility` | SERP & AI-answer visibility (SEO / AEO / GEO) | now | Getting a site or brand ranked or cited: classic SEO tooling and audits, AEO/GEO citation outreach, directory/backlink DR plays, indexing submissions (Brave/Bing/IndexNow/GSC), topical maps, free-tool pages, Reddit/LinkedIn ranking hacks, AI-crawler user-agent handling, visibility tracking (CrowdReply, OpenSEO, DataforSEO). Owner aliases: "syrups", "SERP optimization" | Outbound prospecting and cold email → 2. MCP wiring of SEO tools stays here (tool role) | — | `web-crowdreply`, `github-iannuttall-seo`, `web-tinyshelf`, `web-tinylaunch-directories`, `x-2094553318031024285`, `x-2094328961522397530`, `x-2094684433546985907`, `x-2094770895021572502`, `x-2094771557864292784`, `x-2095130625976176754`, `x-2093013941412852083`, `x-2087827123331383751`, `x-2093624705030959554`, `x-2093713466955649145`, `x-2093964632562253866`, `x-2094688982940741816`, `web-brave-submit-url`, `web-known-agency`, `web-nqz-ai-search-prompt-generator`, `web-seowins-io`, `x-2094148909253943322`, `x-2093990583576486268`, `x-2094742312433684496`, `x-2090837707069014224`, `x-2088046188037902579`, `x-2093729321131368744`, `x-2094450512938856802` | 28–45 |
| 2 | `outbound-gtm-agents` | Outbound / GTM agent stacks | standard | Prospecting, people search, lead data, cold email/call sequencing, sales-OS agent teams, LinkedIn lead magnets, marketing agent bundles (Grok bots for ads/outbound) | Anything whose goal is ranking/citation → 1 | `serp-ai-visibility` | `github-romangojiberryAI-gojiberryai-sales-os`, `x-2094892848042725416`, `x-2095081419202560010`, `x-2094326291906310180`, `x-2094740953554932149`, `web-treg-people-search`, `github-LessieAI-people-search-bench`, `web-arxiv-2603-27476`, `x-2094893065202803014`, `x-2094927852399624557`, `x-2095214420398121034`, `x-2089377925086982281`, `x-2095060844547592437`, `x-2093776000781869278`, `x-2094162743985308047`, `x-2094424821450817563`, `x-2087893705059356898`, `x-2095231184531828762`, `web-graphed` | 12–22 |
| 3 | `gaussian-splatting` | Gaussian splatting (3DGS) capture, edit, export | now | 3DGS training/viewers/editors (Splat.js, LichtFeld Studio, SplatPaint, brush selection), splat→mesh (Splat2Mesh, 3DGS Mesh Converter), splat repair (ArtiFixer), splat research (GaussianGPT, LightFuse), streaming/LOD, camera animation and 4K export from splats, splat→3D print | Reconstruction that does not produce/consume splats → 4 | `image-to-3d-world` | `github-nv-tlabs-ArtiFixer`, `web-arcana-splat2mesh`, `x-2094929928865341832`, `x-2094826117056414132`, `x-2094648474377839018`, `x-2095136786095951924`, `x-2095336950890983773`, `x-2095375790875840593`, `x-2093179838249251011`, `x-2090839282831270173`, `x-2091899114153754949`, `x-2091943679317463153`, `x-2093397098544648516`, `x-2093563796237471912`, `x-2094769581965369822`, `x-2094377838774472944`, `x-2090589293677023507` | 14–22 |
| 4 | `image-to-3d-world` | Image/video → 3D world, mesh, scene ("freedom modeling") | now | One image / panorama / video → navigable world, editable engine scene, mesh, or posed assets (World Labs Atlas, Hyper3D WorldGen, Lumera, Lucida, Magnific 3D Motion); image→3D model generators and arenas (Hitem3D, Meshy, Tripo); AI texturing / materials (I2M); mesh cleanup, retopo, baking (Customuse, BQR, Needle); Blender MCP builds from photo/panorama input. Owner alias: "freedom modeling" (interpreted as free-form world/mesh modeling from captures) | Splat-native pipelines → 3. Blockout for video → 5 | `gaussian-splatting` | `x-2094864872853119216`, `x-2095437841958314100`, `x-2093937170717585657`, `x-2094961942058418268`, `x-2088299905324396589`, `x-2091913781236683162`, `x-2095512142766342624`, `x-2095159781883597031`, `x-2092242135504552118`, `x-2087905319255257296`, `x-2057113327508345047`, `x-2093018082293813509`, `x-2093421870951387625`, `x-2095502642218664004`, `x-2091927587471712274` | 12–22 |
| 5 | `blockout-to-video-flythrough` | Blender/Unreal blockout + agent camera → video model | now | The BESS marketing pipeline: LLM/MCP-driven Blender or Unreal scene build, camera path authoring, depth/reference renders, first/last-frame or motion-reference conditioning into Seedance / MiniMax H3 / Veo / Kling / Runway; browser 3D camera stages (Mint Studio, MiniMax 3D Director, Higgsfield in Blender, CozyClay previs); camera-technique references | Video generation without a 3D camera stage → 6. Web 3D scroll heroes → 8 | `ai-video-generation` | `note-blender-minimax-h3-video-generation`, `x-2087565352372723955`, `x-2093377271771865267`, `x-2093374092795846745`, `x-2092679517588574690`, `x-2093663876692754713`, `x-2065843739340509693`, `x-2092255768770920506`, `x-2091497597743612379`, `x-2092008677834387672`, `x-2093064017468145963`, `x-2093047548550525165`, `x-2092009056164872620`, `x-2093051654937423887`, `x-2093380307735232543`, `x-2093053568748319181`, `x-2092657951618249080`, `x-2095288402606514424`, `x-2093986548404428942`, `x-2091577179914338583`, `x-2091722166685610284` | 18–30 |
| 6 | `ai-video-generation` | AI video models, tools, and launch-video craft | standard | Model announcements with usable detail (MiniMax H3 / H3 Max, Seedance), audio fixes, story/consistency tools (OpenStory, Calliope), agent video editing (video-use), launch-video breakdowns, faceless/TikTok pipelines, product-render-via-video-model | Code-rendered motion → 7. Anything with a Blender/Unreal camera stage → 5 | `blockout-to-video-flythrough` | `x-2090098441200517416`, `x-2091924963288580539`, `x-2091957150793023651`, `x-2091519705911795761`, `x-2095427702325231977`, `x-2095483352375837020`, `x-2092702228947902622`, `x-2091713204418490406`, `x-2093481253043380418`, `x-2092980272819999227`, `x-2094061655990702150`, `x-2093236801079279978`, `x-2093681908227936745`, `x-2095521587785081193`, `x-2095202138854977756`, `x-2095156045303701766`, `x-2094819241916801165`, `web-fal-ai`, `x-2091622751756751211` | 14–24 |
| 7 | `code-motion-graphics` | Code-rendered motion graphics and HTML-as-video | standard | Remotion, HyperFrames / html-video, Motion Prompt, motion-anything, Claude for motion graphics, glif motion skill, CoAnimator, shot-recipe cards, Lottie/motion template libraries, After Effects → video model hand-offs, logo videos | Scroll/UI motion on a web page → 9 | `landing-ui-motion` | `github-nexu-io-html-video`, `github-nexu-io-motion-anything`, `x-2086030681772376399`, `x-2088155107544191339`, `x-2094164487381414344`, `x-2093081833911058772`, `x-2095204640690147487`, `x-2095111032171876470`, `x-2092040265234260091`, `x-2091441060153278565`, `x-2093129469926215800`, `web-animos-editor`, `web-lottiefiles`, `x-2091688420695564296` | 10–16 |
| 8 | `web-3d-scenes` | Three.js / WebGL / WebGPU / Spline scenes on the web | now | Three.js and R3F sites and templates, graphics agent skills for Three.js, WebGPU shader libraries, scroll-world 3D heroes, Spline, 3D component packs, 3D-driven landing pages, 3D diagram editors that ship as web scenes | Splat viewers → 3 unless the item is about the web scene itself. Non-3D landing motion → 9 | `landing-ui-motion` | `github-scottstts-threejs-awesome-graphics-agent-skills`, `x-2088738850705113398`, `github-oso95-scroll-world`, `github-mengto-complete-shelf`, `x-2086599657925329347`, `x-2088265078919282836`, `x-2089400082550620636`, `x-2089602918605619401`, `x-2091571624390881664`, `x-2091748299975880994`, `x-2093012548031254932`, `x-2090526692427104508`, `web-utsubo`, `x-2089740155179643231`, `web-feralui-dev`, `web-oryzo-ai`, `web-getlayers-ai`, `x-2086537093120164177`, `x-2088240171565412733` | 14–22 |
| 9 | `landing-ui-motion` | Landing pages, UI component libraries, scroll motion, visual reference | now | Finished-page examples and breakdowns, scroll-driven sections, parallax, component/animation libraries (reactbits, originkit, cult-ui, great-ui, aicss, Mono-style kits), fonts/gradients, templates, design-inspiration sites, brand pages used as reference, screenshot polish tools | Skills that change how the agent designs → 10. 3D-first scenes → 8 | `design-agent-skills` | `github-nateherkai-scroll-craft`, `x-2094978216146452971`, `x-2094984529853530345`, `x-2094524951025914278`, `x-2087812720762425743`, `x-2089263766428950683`, `web-originkit-dev`, `web-cult-ui`, `x-2089182103153897532`, `x-2089775679600812150`, `x-2089223944700326052`, `x-2089618415493218381`, `x-2091479075697430784`, `web-vengence-ui`, `web-recent-design`, `x-2092996828752916622`, `x-2095207624396652956`, `x-2093767075131220005`, `x-2093900284896657841`, `x-2093915384944414827`, `x-2095429087141515616`, `x-2095123902947090682`, `x-2093024468209733756`, `x-2092624919653671200`, `web-cartier-ballon-bleu`, `x-2091560960066793483`, `x-2093364419044794836`, `x-2091616414063022208`, `web-dicebear`, `web-flowmapp`, `web-tinyshots`, `x-2090079734571098131` | 28–45 |
| 10 | `design-agent-skills` | Design skills, DESIGN.md contracts, vibe-design workspaces, anti-slop | now | Installable design/taste/motion skill packs (Impeccable, Emil, Taste, interfaces.dev, MengTo, unlazy, /vision, /bro, no-ai-slop), DESIGN.md spec/extractors/collections, vibe-design and AI site builders (OpenDesign, Aura, Neuform, AIDesigner MCP, Orca design mode), UI prompt libraries for websites (SceneAI, typeui, "590+ prompts"), anti-slop prose skills (Google dev-docs style, AI-tells lists, avoid-ai-writing) | Image prompt galleries → 11. Component libraries → 9. Generic agent harness → 12 | `landing-ui-motion` | `github-emilkowalski-skills`, `github-leonxlnx-taste-skill`, `github-pbakaus-impeccable`, `github-jakubkrehel-skills`, `github-mengto-skills`, `github-google-labs-code-design-md`, `web-getdesign-md`, `web-designmd-me`, `web-designmd-supply`, `web-styles-refero-design`, `web-sokosumi-design-md`, `web-design-md-hyperbrowser`, `x-2091934379648110784`, `x-2093766772029559077`, `x-2095078647652917329`, `x-2086715093707063445`, `x-2088254428730085690`, `x-2088290952704151671`, `x-2090834948332655011`, `x-2085006701984698712`, `x-2086845465140842638`, `x-2088742864310481025`, `x-2091125349308399923`, `x-2089189790881382676`, `x-2091865940581638285`, `x-2094069236524061059`, `github-nexu-io-open-design`, `web-open-design-ai`, `web-aidesigner-mcp`, `x-2094467179320119498`, `web-aura-build`, `web-neuform-ai`, `x-2087708050002239702`, `web-checklist-design`, `web-opale-ui-taste`, `x-2093669411685110141`, `web-sceneai-art`, `web-typeui-sh`, `x-2091689598883934666`, `x-2094009989220430084`, `x-2093583622691283018`, `x-2095549461737111905`, `x-2087346803268260043`, `x-2089457435459404093`, `x-2093654908322951447`, `x-2092656414351118647` | 38–55 |
| 11 | `image-prompt-galleries` | Image-gen prompt galleries and prompt-as-skill | standard | GPT Image 2 / Nano Banana / Sol prompt collections, prompt-as-code template engines, prompt-gallery skills and CLIs, prompt marketplaces | Prompts for websites/UI → 10. Video prompts → 6 | `design-agent-skills` | `github-wuyoscar-gpt-image2-skill`, `github-youmind-openlab-nano-banana-pro-prompts`, `x-2092222199620833420`, `web-meigen-ai`, `x-2095085408208196006`, `x-2095368133070700884`, `x-2095451624139567162`, `x-2095482056180638142`, `x-2092979866836648104` | 7–12 |
| 12 | `agent-harness-loops` | Agent harnesses, autoresearch loops, orchestration, agent ops | standard | Autoresearch and self-improving loops, harness design (Pi, Hermes, Headlong, loop-library, managed deep agents), orchestration cookbooks, multi-agent papers, permission stances, session/tool migration, agent observability (sideshow, Blume), curated repo lists, training pages, prompt-wording results | Memory/knowledge systems → 13. MCP servers and agent browsers → 14 | `agent-memory-knowledge` | `x-2032330665081839791`, `x-2032671842230501729`, `x-2080856252687745093`, `x-2074912810803560497`, `x-2087151807965401320`, `x-2087444616832594022`, `x-2086790895538700379`, `x-2087232392209531166`, `x-2087304957011911157`, `x-2087714580491370655`, `x-2091970263088816272`, `x-2091990178638496195`, `x-2093437790969385283`, `x-2088345102540587356`, `x-2087026930323247306`, `x-2089165107364278341`, `x-2087254502210490739`, `x-2082316720086405524`, `x-2086838432102228008`, `x-2090858571613470919`, `x-2094110975045554191`, `x-2087178722420171020`, `x-2088116807869854126`, `x-2091157554919280688`, `x-2088634091671531923`, `x-2088260067204137135`, `x-2091118605392019658`, `x-2091622497393225801`, `web-blume-codes`, `web-chatgpt-training`, `x-2095133695480873023`, `x-2091686636698657080`, `x-2087263510090874911` | 24–36 |
| 13 | `agent-memory-knowledge` | Agent memory, second brains, company knowledge bases | standard | Memory systems (GBrain, Memoria, ReasoningBank, Obsidian Mind, Type), company-brain/KB essays, context-engineering-as-ETL, semantic-layer analytics, enterprise knowledge connectors, post-AI data stack, intelligence-layer arguments | Harness/loop mechanics → 12 | `agent-harness-loops` | `x-2094462971598754010`, `x-2087208634493095978`, `x-2087143369181114868`, `x-2088231655177924993`, `x-2091169290661838965`, `x-2087955721732460791`, `x-2092918452423983363`, `x-2093677274641969390`, `x-2086920236079681607`, `x-2087239769877295158`, `web-davidgasquez-context-engineering`, `web-cerebras-knowledge-base`, `web-anthropic-claude-self-service-data`, `x-2088623462109593792`, `x-2094558408259272998`, `web-iandmacomber-post-ai-data-stack` | 12–18 |
| 14 | `mcp-and-agent-browsers` | MCP servers, tool routers, agent browsers, computer-use | standard | MCP server catalogs, tool routers (treg), headless/agent browsers (Obscura, Kitesurf, Kernel), mock stacks (aimock), screen parsers (OmniParser), free search/fetch APIs for agents, open Grok-Bot alternatives | Domain MCPs (Blender MCP, CrowdReply MCP, Fusion MCP) are primary in their domain subject with `mcp` platform tag; this subject is secondary for them | `agent-harness-loops` | `github-punkpeye-awesome-mcp-servers`, `github-superdesigndev-treg`, `github-h4ckf0r0day-obscura`, `web-obscura-sh`, `x-2094427822064279870`, `web-cloudflare-kitesurf`, `x-2087555254757757116`, `x-2087151521121419648`, `x-2093153416214114558`, `x-2093050916953903451`, `x-2087898602890744089` | 9–16 |
| 15 | `infographics-diagrams` | Infographics, diagrams-as-content, charts | standard | Diagram/infographic skills and frameworks (AntV, diagram-design, archify, pretty-mermaid, system-atlas), chart ILs (Flint), chart component kits (Mono Charts), fast dataviz, codebase visual maps, social carousels, layer-diagram-as-argument | A diagram that only illustrates an SEO claim → 1 primary, this secondary | `landing-ui-motion` | `github-antvis-infographic`, `github-cathrynlavery-diagram-design`, `x-2093309791120543846`, `x-2087329201451855933`, `x-2091559663833924082`, `web-flint-chart`, `x-2088599468698751328`, `x-2087205167662088363`, `x-2088016749849682120`, `x-2088590355440476343`, `x-2091767461058105402`, `x-2089372767934115883`, `x-2092890365930131920`, `x-2089570022490263586` | 12–18 |
| 16 | `ai-cad-hardware` | AI CAD, text-to-CAD, PCB and keyboard hardware | later | Text-to-CAD tools and demos (CadXStudio, Smith, VibeCAD, OpenSCAD+skills, Fusion MCP, text-to-cad), FreeCAD internals, PCB autorouting, KiCAD+OpenEMS simulation, AI schematic design, EM field visualisation for boards, ergonomic keyboards. Owner said keyboards are "later" — priority reflects that | Web 3D engine demos → 8 | `image-to-3d-world` | `x-2087272209429766596`, `x-2089717063921332378`, `x-2090535643353153833`, `x-2089802212000362939`, `x-2088277946918142211`, `x-2088252062454751483`, `x-2088296314484162719`, `x-2088308976278790258`, `x-2093305736717545869`, `x-2095193896687177873`, `x-2095352925597884465`, `x-2095548418533798086`, `x-2091564966797029541`, `x-2091621183422943726`, `x-2091891133286605067`, `x-2093020107509514674`, `x-2092106682302140648`, `x-2094840529997410525` | 14–20 |
| 17 | `local-inference-models` | Local / edge inference, open-weight model releases | later | Open-weight model releases with runnable detail (Qwen GGUFs, Unsloth, Bonsai, Edge8), inference engines (FreeToken, MLX tricks), cheap hosted endpoints with numbers (RunInfra, AMD Token Factory), VRAM math. Pure "now live on gateway X" or discount posts are `noise/availability-announcement` | — | shelf `out-of-scope` | `x-2087240056037908509`, `x-2087562269807030754`, `x-2087962842985058365`, `x-2088281537427235320`, `x-2090103470015828184`, `x-2088594942482374759`, `x-2088695568474546387`, `x-2090930324817498246`, `x-2091150763418620133`, `x-2093160779960774982`, `x-2093429897188299113`, `x-2091554449323958423` | 8–13 |

Seventeen rows; the most likely merges are `image-prompt-galleries` → `design-agent-skills` and `local-inference-models` → shelf `out-of-scope` if either lands below 6. Shelves (§4.5): `noise`, `duplicate`, `out-of-scope`, `uncategorized`.

Rules for classification workers:

1. Use the inclusion rule, then the exclusion rule, then the seed list. Seeds are hints; an item listed as a seed may still be shelved with a reason.
2. Legacy `topics[]` is **not** an input to `primary_subject`. Record it in `raw.legacy_topics` and move on.
3. Legacy `extra.filtered = true` is **not** a shelf decision. Re-judge every one of the 47 against §4.5 codes. Expected outcome: ~30 stay `noise`, ~5 `duplicate`, ~10 re-enter as `analyze` (local inference, FreeCAD, GTM, AI character video).
4. When two subjects fit equally, primary = the one with the smaller `expected` range (rarer subject wins), the other goes secondary.
5. Blender MCP items: primary by output — mesh/world from a capture → 4; camera/video → 5; CAD part → 16. `mcp-and-agent-browsers` secondary.

---

## 6. Thread capture contract

Applies to every `x-*` item (311). Output: `analysis/items/<id>/thread.json` (§4.2) and raw payloads under `raw/items/<id>/thread-raw/`.

### 6.1 What belongs in the record

| Bucket | Definition | Where | Relevance |
|---|---|---|---|
| Author continuation | Every post by `root_author_handle` that replies to the root or to an earlier post in the same chain, in chronological order | `author_thread[]` | always part of the source; not filtered |
| Author replies to others | Root author's replies to someone else's reply (answers, links, corrections) | `replies[]` with `is_author = true` | forced `relevant`, kind `author-continuation` or `answered-question` |
| Quoted post(s) | The tweet(s) the root or the author chain quotes | `quoted[]` | always captured (text + author + id + urls); if the quoted post is an X article, capture title + first 1,000 chars of body if reachable |
| Other replies | First-level and nested replies by anyone else | `replies[]` | classified `relevant` or `noise` (§6.2) |
| Quote-tweets of the root by others | Optional; capture only when fetchable in the same pass | `replies[]` with `depth = 0` and `relevance_kind = counter-claim | alternative-tool | link` | classify like replies |

Text is stored verbatim in the original language. `text_en` is optional and must be marked as a translation by being non-null (no mixing). URLs are extracted to `urls[]`, t.co expanded when the fetch method returns expansions. Reply media is listed by URL; download only when `relevance_kind ∈ {recipe, link, correction}` and the image carries the artifact (prompt screenshot, config, result). Downloaded files go to `raw/items/<id>/media/reply-<reply_id>-<n>.<ext>` and are listed in `downloaded_media[]`.

### 6.2 Relevance rule

A non-author reply is `relevant` iff at least one holds; set `relevance_kind` to the first that applies:

1. `link` — contains a URL to a repo, paper, product, doc, or another post that is on-topic.
2. `recipe` — contains steps, a prompt, a config, a command, or a parameter set.
3. `number` — contains a metric, price, benchmark, or timing about the technique.
4. `correction` — corrects a fact in the root or author thread.
5. `counter-claim` — disputes the root's claim with an argument (not just "no").
6. `alternative-tool` — names a competing/adjacent tool by name.
7. `answered-question` — a question that the root author answered (store both; the question carries this kind, the answer is `is_author`).
8. `fact-check` — a bot or third party evaluating the claim (e.g. `@grok` "is this true"). Always relevant.

Otherwise `noise`: praise, emoji, "bookmarking", "following", giveaways, unrelated self-promo, "🔥", bot spam. Noise replies are kept in `replies[]` (so the record is auditable) but hidden from `thread.md` except as a count. Storage cap: after 50 relevant replies, stop storing further replies, set `truncated = true`, keep counting in `replies_captured`.

### 6.3 Status semantics

| `status` | Condition |
|---|---|
| `captured_full` | `reply_count_reported` known and `replies_captured ≥ min(reply_count_reported, 50)`, or the platform shows no more replies to load |
| `captured_partial` | ≥ 1 reply captured and fewer than reported |
| `empty` | `reply_count_reported = 0` confirmed by ≥ 1 method with outcome `ok` or `empty` (not `blocked`) |
| `failed` | 0 replies captured while `reply_count_reported > 0` or unknown; requires ≥ 2 `fetch_log` entries with distinct `method` and outcomes ∈ {blocked, login-wall, rate-limited, error} |

`author_thread_status`: `none` = a method with outcome `ok` showed no author self-replies; `captured` = full chain; `partial` = chain cut by fetch limits; `unknown` = every method failed. `unknown` is only legal when `status = failed`.

There is no "not attempted" status. A worker that runs out of time writes `failed` with its real `fetch_log`. The 33 items with `extra.replies` already have `reply_count_reported`; the other 278 must get a count from at least one API call.

### 6.4 Method order and logging

Try in this order until `captured_full` or every method is exhausted; log every attempt:

1. `x-graphql-tweetdetail` — authenticated session from `skills/x-harvest-clear/SKILL.md` (agent-browser + `auth_token`/`ct0`); GraphQL `TweetDetail` gives the full conversation with `in_reply_to` ids. Save the JSON payload to `thread-raw/`.
2. `x-web-dom` — same session, open `https://x.com/<handle>/status/<id>`, scroll, extract `article[data-testid="tweet"]` nodes; click "Show more replies" up to 5 times. Save the extracted JSON.
3. `fxtwitter-api` / `vxtwitter-api` — `https://api.fxtwitter.com/<handle>/status/<id>` for root metrics (`replies` count), quoted post, article payload. Never counts as a reply capture.
4. `jina-fixupx` — `https://r.jina.ai/http://fixupx.com/<handle>/status/<id>` for visible first-level replies; then per-reply status pages for nesting.
5. `syndication-embed` — `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=x` for root + `in_reply_to` fields when other routes are walled.

One payload file per attempt: `raw/items/<id>/thread-raw/<method>-<yyyymmddThhmmssZ>.<json|html|txt>`. Payloads ≤ 2 MB each; strip embedded base64.

### 6.5 Media and threads already partly captured

If `raw/items/<id>/comments.md` already contains structured replies (24 items with `###` headings), the worker must still run method 1 or 2 to get counts and missing nesting, then merge; the old `comments.md` is not edited.

---

## 7. Worker split

Four phases. Worker counts are for a 20–40 worker pool; batch size scales inversely. Every worker writes exactly one `analysis/_work/handoffs/<worker-id>.md` with: ids owned, ids done, ids with `failed`/`blocked`, alias proposals, reclass proposals, time spent.

### 7.0 Phase 0 — parent (serial, scripted)

1. Create `analysis/` skeleton, `analysis/subjects.json` from §5, empty `registry/aliases.json` (`{}`), `analysis/README.md` per §3.1.
2. `scripts/analysis/make_batches.py --batches 20` → `analysis/_work/batches.json`: `{ "batches": 20, "assignment": { "<id>": <n> } }`. Assignment rule: sort all 388 ids lexicographically, deal round-robin so each batch gets 19–20 ids and 15–16 `x-*` ids. Deterministic; committed before any worker starts.
3. Write `.graphifyignore` (§8), legacy banners (§3.2).
4. Commit `chore(analysis): scaffold analysis layer and batches`.

### 7.1 Phase 1 — item workers (parallel; 2 lanes × 20 = 40 workers, or 20 sequentially doubled)

Two independent lanes over the same batches. They share folders but never files.

| Worker id | Owns (write) | Reads | Must not touch |
|---|---|---|---|
| `threads-<nn>` (nn = batch 01–20) | `analysis/items/<id>/thread.json` for `x-*` ids in batch nn; `raw/items/<id>/thread-raw/*`; optional `raw/items/<id>/media/reply-*` | `raw/items/<id>/*` | any `card.json`, anything outside its ids |
| `cards-<nn>` | `analysis/items/<id>/card.json` for all ids in batch nn (incl. `note-*` if assigned) | `raw/items/<id>/*`, `thread.json` if already present, `catalog/topics/*.md`, `catalog/patterns.md`, `analysis/subjects.json` | any `thread.json`, other batches, `subjects.json`, `aliases.json` |

Folder creation: `mkdir -p analysis/items/<id>` is idempotent; both lanes may run it.

Card lane does not depend on the thread lane. If `thread.json` is absent when the card is written, `gaps` may still be computed later: `build_index.py` merges thread status at index time; `validate_cards.py` recomputes `readiness`. Card workers must read `raw/items/<id>/comments.md` and any `thread.json` present to source claims with `evidence_source = reply | author-thread`.

Per-item card procedure (fixed order): read `source.json` → `post.md`/`page.md` → `comments.md` → `thread.json` if present → `research.md` → view every image in `media/` → write `card.json` → run `python3 scripts/analysis/validate_cards.py analysis/items/<id>` → fix until clean.

Alias proposals: a card worker who is unsure about a slug writes it anyway and appends `{"from": "<their slug>", "to": "<likely canonical>", "why": "..."}` to their handoff. Nobody but the registry worker edits `aliases.json`.

### 7.2 Phase 2 — parent (serial, scripted) — after both Phase 1 lanes finish

```
python3 scripts/analysis/validate_cards.py analysis/items          # must be clean
python3 scripts/analysis/build_registry.py                           # registry/*.jsonl, owner_subject per technique
python3 scripts/analysis/render.py                                   # card.md, thread.md, tools/, techniques/, subjects/*/items.jsonl + claims.jsonl, shelf/
python3 scripts/analysis/build_index.py                              # index.jsonl
```

Then commit `feat(analysis): item cards and thread records (phase 1)`. Then produce `analysis/_work/reports/phase2.md`: per-subject counts vs `expected`, singleton techniques, `uncategorized` count, `failed` thread count, alias proposals collected.

### 7.3 Phase 3 — subject lanes (parallel; 17 + 2 = 19 workers)

| Worker id | Owns (write) | Reads | Must not touch |
|---|---|---|---|
| `subject-<slug>` (17) | `analysis/subjects/<slug>/brief.md`, `brief.json`; NOTES blocks of `analysis/techniques/<t>.md` where `owner_subject = <slug>`; `analysis/_work/reclass/<slug>.jsonl` | everything in `analysis/`, `catalog/topics/*.md`, cards' raw folders when a card is `ready-with-gaps` | any `card.json`, other subjects' files, tool pages, `aliases.json` |
| `registry` (1) | `analysis/registry/aliases.json`; NOTES blocks of `analysis/tools/*.md`; `analysis/_work/requests/registry.md` | all handoffs (alias proposals), registry jsonl | cards, briefs |
| `shelf-auditor` (1) | `analysis/_work/reclass/shelf.jsonl` (the only file it writes) | every card with `disposition = shelf`, especially `uncategorized`; every `analyze` card whose legacy `filtered = true` | everything else |

Reclass record (`_work/reclass/*.jsonl`): `{ "id", "field": "primary_subject|secondary_subjects|disposition|shelf|shelf_reason_code|shelf_reason|duplicate_of|judge_hints.must_read", "from", "to", "why" (≥ 40 chars), "by" }`. Subject workers may request changes only for items where their subject is `from` or `to`. The shelf auditor may request any disposition/shelf change and must resolve every `uncategorized` item to a subject or to `out-of-scope`/`noise` unless two candidate subjects are named in a ≥ 60-char reason.

Subject brief procedure: read `items.jsonl` → every card in it → `claims.jsonl` → legacy `catalog/topics/<nearest>.md` → write `brief.json` then `brief.md` → set `must_read` (≤ 12) via reclass records → write technique NOTES for owned techniques → handoff.

### 7.4 Phase 4 — parent (serial, scripted)

```
python3 scripts/analysis/apply_reclass.py     # applies all _work/reclass/*.jsonl in filename order; conflicts (same id+field, different to) → written to _work/reports/reclass-conflicts.md and left unapplied
python3 scripts/analysis/validate_cards.py analysis/items
python3 scripts/analysis/build_registry.py && python3 scripts/analysis/render.py && python3 scripts/analysis/build_index.py
```

Parent resolves conflicts by hand (rule: shelf-auditor wins on disposition/shelf; the subject named in `to` wins on primary if its `expected` range is smaller). Re-run the three scripts. Subject workers whose `items.jsonl` changed by > 3 items re-run their roster section. Commit `feat(analysis): subject briefs, registry pages, reclass (phase 3)`.

### 7.5 Phase 5 — graphify worker (1) and verifier (1)

`graphify` worker owns `.graphifyignore`, `graphify-out/`, `AGENTS.md` graph section; runs §8. Verifier owns nothing; runs §9 and writes `.orchestrate/design-ideas-prep/handoffs/verifier.md`.

### 7.6 Collision guarantees

- Item-level files: owner determined by `batches.json` and lane; no two workers write the same path.
- Subject-level files: owner determined by slug.
- Technique pages: owner = `owner_subject` from `registry/techniques.jsonl`; only the NOTES block is hand-edited; `render.py` preserves it.
- Tool pages: registry worker only.
- Shared files (`subjects.json`, `aliases.json`, `index.jsonl`, `items.jsonl`, `claims.jsonl`, `shelf/*`): single writer (parent script or registry worker).
- Git: each worker commits only its owned paths (`git add <paths>`), never `git add -A`. Commit message prefix by lane: `feat(threads-07): …`, `feat(cards-07): …`, `feat(subject-gaussian-splatting): …`.

---

## 8. Graphify overlay

Goal: communities = subjects, tools, techniques; hubs = brief/tool/technique pages; leaves = cards and threads.

### 8.1 `.graphifyignore` (replace the file with exactly this)

```
# Graph covers the analysis layer only.
*
!analysis/
!analysis/**
analysis/_work/
analysis/**/*.json
analysis/**/*.jsonl
graphify-out/
```

`.gitignore` is merged automatically; it already excludes `agent-tools/`, `.cursor/`, and `graphify-out/cache/`.

### 8.2 Build commands (run from repo root)

```bash
uv tool install graphifyy || pipx install graphifyy          # CLI command is `graphify`
git rm -r --cached graphify-out 2>/dev/null; rm -rf graphify-out # drop the old substrate; never `--update` over it
graphify . --no-viz                                          # fresh build, heuristic extraction, zero token cost
graphify . --wiki                                            # agent-crawlable wiki over the same graph
git add graphify-out .graphifyignore && git commit -m "feat(graph): rebuild graphify over analysis layer"
```

If the first build reports > 150 communities, run `graphify . --mode deep --no-viz` once and keep whichever build passes §8.3 with fewer communities. Do not hand-edit `graph.json`.

After any later change to `analysis/`: `graphify update .` (or `graphify . --update`).

### 8.3 Graph acceptance (mechanical)

Read `graphify-out/GRAPH_REPORT.md`:

1. `Corpus Check` file count ≤ (number of `*.md` under `analysis/` excluding `_work/`) + 2.
2. Community count between 10 and 150 inclusive.
3. None of the following strings appears as a hub name: `Research`, `Comments`, `Comments / thread`, `Replies`, `Thread`, `Claims`, `Tools`, `Techniques`, `Summary`, `Media`, `Links`.
4. Of the first 20 `Community Hubs`, ≥ 15 match the H1 of a file under `analysis/subjects/`, `analysis/tools/`, or `analysis/techniques/`.
5. Smoke queries return ≥ 1 node from the expected subject folder:
   - `graphify query "how to get a brand cited in ChatGPT answers"` → node in `analysis/subjects/serp-ai-visibility/` or `analysis/techniques/citation-outreach.md`
   - `graphify path "Splat2Mesh" "LichtFeld Studio"` → a path exists
   - `graphify explain "blockout-then-video-model"` → lists ≥ 3 neighbouring cards
6. `AGENTS.md` graph section states the graph covers `analysis/` only.

---

## 9. Acceptance checklist

`scripts/analysis/verify.py` implements every numbered check below, prints `CHECK <n> PASS|FAIL <detail>`, writes `analysis/_work/reports/verify.md`, exits non-zero on any FAIL. The verifier sub-agent runs it, then performs the two manual samples (checks 40–41), then writes `VERDICT: PASS|FAIL` with the failing check numbers to `.orchestrate/design-ideas-prep/handoffs/verifier.md`. The parent does not finish on FAIL.

Let `R` = set of folder names under `raw/items/` (387) ∪ `{note-<name>}` for each `raw/notes/*.md` (1); `|R| = 388`. Let `S` = slugs in `analysis/subjects.json`.

**Existence and counts**

1. `docs/ANALYSIS_STRUCTURE.md`, `analysis/README.md`, `analysis/subjects.json`, `analysis/index.jsonl`, `analysis/registry/tools.jsonl`, `analysis/registry/techniques.jsonl`, `analysis/registry/aliases.json`, `analysis/shelf/shelf.jsonl`, `analysis/shelf/{noise,duplicate,out-of-scope,uncategorized}.md`, `.graphifyignore`, `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.json` exist.
2. `analysis/items/<id>/card.json` and `card.md` exist for every id in `R`; no extra folders under `analysis/items/`. Count = 388.
3. `analysis/items/<id>/thread.json` and `thread.md` exist for every id in `R` starting with `x-`; count = 311; none exist for non-`x-` ids.
4. `raw/items/<id>/thread-raw/` exists with ≥ 1 file for every `x-*` id.
5. `analysis/index.jsonl` has exactly 388 lines, valid JSON each, `id` unique, sorted ascending, `id` set = `R`.
6. For every slug in `S`: `analysis/subjects/<slug>/{brief.md,brief.json,items.jsonl,claims.jsonl}` exist; no folder under `analysis/subjects/` whose name ∉ `S`. `|S|` between 14 and 17.
7. `analysis/_work/batches.json` exists; every id in `R` is assigned; batch sizes differ by ≤ 1.
8. `analysis/_work/handoffs/` contains one file per worker id referenced in any `card.json.worker`, `thread.json.worker`, `brief.json.written_by`.

**Card schema**

9. Every `card.json` validates against §4.1: all keys present, enums legal, `schema_version = "1"`, `id` equals folder, `source_type` matches the raw prefix (`x-`→`x`, `github-`→`github`, `web-`→`website`, `note-`→`note`).
10. `title` ≤ 90 chars; for `x-*` items the first 60 chars of `title` must not equal the first 60 chars of the post body in `raw/items/<id>/post.md` (i.e. not truncated tweet text).
11. `summary` length 80–320 chars.
12. If `disposition = analyze`: `primary_subject ∈ S`, `roles` length 1–3, `claims` length ≥ 1, `question_it_answers` non-null, `shelf` and `shelf_reason*` null.
13. If `disposition = shelf`: `shelf` non-null, `shelf_reason_code` legal for that shelf (§4.5), `shelf_reason` ≥ 60 chars and contains none of the banned substrings, `primary_subject` null, `roles/claims/techniques/tools` empty; if `shelf = duplicate` then `duplicate_of ∈ R` and that target has `disposition = analyze`.
14. `secondary_subjects` ⊂ `S`, length ≤ 2, excludes `primary_subject`.
15. Every `claims[].id` = `<id>#c<n>` with n consecutive from 1; every `claims[].subject ∈ {primary} ∪ secondary`; `evidence` non-empty; enums legal.
16. `media[]` has one entry per file in `raw/items/<id>/media/` (by exact path set equality, ignoring `reply-*` files); every `type = image` entry has `description ≥ 20` or non-null `skip_reason`.
17. `readiness` equals the recomputation of §4.1.3. Count of `blocked` among `analyze` cards = 0.
18. `judge_hints.compare_with` ⊂ `R`; per subject, count of `must_read = true` ≤ 12.
19. `raw.legacy_topics` equals `source.json.topics`; `raw.legacy_filtered` equals `bool(extra.filtered)`.

**Thread schema**

20. Every `thread.json` validates against §4.2: keys present, `status` and `author_thread_status` legal, `tweet_id` numeric and equal to the id suffix.
21. `reply_count_reported` is an int, or null with non-null `count_unavailable_reason`. Count of null across all 311 ≤ 15.
22. If `status = failed`: `replies_captured = 0` and `fetch_log` has ≥ 2 entries with distinct `method` and every outcome ∈ {blocked, login-wall, rate-limited, error}.
23. If `status = empty`: `reply_count_reported = 0` and some `fetch_log.outcome ∈ {ok, empty}`.
24. If `status ∈ {captured_full, captured_partial}`: `replies_captured ≥ 1` and `replies_captured = len(replies)`; `replies_relevant` = count of `relevance = relevant`.
25. `author_thread_status = unknown` only when `status = failed`.
26. Every `raw_payloads[]` path exists on disk.
27. Aggregate: count of `status = failed` ≤ 62 (20% of 311). If > 62, FAIL with the list; the thread subplanner re-runs those ids.
28. Every author reply (`is_author = true`) has `relevance = relevant`.

**Subjects, registry, shelves**

29. `brief.json` validates §4.3; `item_count_primary` equals the count in `items.jsonl` with `membership = primary`; `techniques`/`tools` equal the union over those items; `must_read` equals the card set; `comparison_axes` length 3–8 and none contains the words `best`, `winner`, `recommended`.
30. `brief.md`: first line is `# <name> (<slug>)`; the ten H2 headings of §4.3.1 appear in order, each prefixed `## <slug> — `; no H3+; 120–400 lines; every `../../items/<id>/card.md` link resolves; every primary item id in `items.jsonl` is linked in the roster section.
31. Every subject has 6–60 primary items (`image-prompt-galleries` may be absent if merged; then no card references it).
32. Σ over subjects of `item_count_primary` = count of `analyze` cards.
33. Every slug in any card's `tools[]` exists as `analysis/tools/<slug>.md` and in `registry/tools.jsonl`; same for `techniques[]` ↔ `analysis/techniques/<slug>.md`; no page exists without ≥ 1 referencing card. All slugs match `^[a-z0-9]+(-[a-z0-9]+)*$`, ≤ 48 chars.
34. Every `aliases.json` key is absent from all cards after Phase 4 (aliases were applied).
35. Every technique page NOTES block has ≥ 3 non-empty lines; `singleton: true` techniques ≤ 15% of techniques.
36. `shelf.jsonl` line count = count of `shelf` cards; `uncategorized` count ≤ 19; every legacy-filtered id (47) appears either in `shelf.jsonl` or as an `analyze` card (none missing).
37. `analysis/subjects/<slug>/claims.jsonl` line count = Σ claims with that `subject` across cards; every line carries `item_id`.

**Markdown / graph hygiene**

38. Every `card.md`, `thread.md`, `tools/*.md`, `techniques/*.md` contains exactly one line matching `^# ` and zero lines matching `^#{2,} `. `card.md` first line = `# ` + `card.json.title`. Every relative link in these files resolves to an existing file.
39. §8.3 checks 1–6 all pass (file count, community bounds, banned hubs, hub names, smoke queries, `AGENTS.md`).

**Manual samples (verifier sub-agent)**

40. Sample 10 `analyze` cards deterministically (sort the `analyze` ids ascending, N = their count, take index `floor(k·N/10)` for k = 0..9). For each: `summary` describes the artifact (not a hype quote), every claim's `evidence` is findable in the raw post/thread/linked page, `question_it_answers` is a question an analyst would actually ask, media descriptions match the images. ≥ 9 of 10 must pass; record misses by id.
41. Sample 10 `shelf` cards (same `floor(k·N/10)` rule over `shelf.jsonl` line order). Each reason names something observable in the post and the code fits. ≥ 9 of 10 must pass.

**Legacy and git**

42. `catalog/README.md` line 1 starts with `> LEGACY`; `SCHEMA.md` line 1 starts with `> Raw capture schema only`; `AGENTS.md` query order begins with `analysis/README.md`; root `README.md` points to `analysis/README.md`.
43. `raw/items/<id>/{source.json,post.md,page.md,comments.md,research.md}` byte-identical to the base commit for all ids (only `thread-raw/` and `media/reply-*` may be added). Check via `git diff --stat <base>..HEAD -- raw/ | grep -v thread-raw | grep -v 'media/reply-'` producing no file lines.
44. `git status --porcelain` is empty on the final commit; every file under `analysis/` is tracked.

Verdict rule: PASS iff checks 1–39 and 42–44 all PASS and checks 40–41 each score ≥ 9/10.
