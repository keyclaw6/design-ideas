# Image-gen prompt galleries and prompt-as-skill (image-prompt-galleries)

## image-prompt-galleries — scope

GPT Image 2 / Nano Banana / Sol prompt collections, prompt-as-code template engines, prompt-gallery skills and CLIs, prompt marketplaces.

Exclusion: Prompts for websites/UI → design-agent-skills. Video prompts → ai-video-generation.

Priority `standard`. Owner aliases: prompt gallery, nano banana, GPT Image.
Expected primary range [7, 12]. This roster has **8** primary and **2** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## image-prompt-galleries — what the owner is trying to decide

Decide whether GPT Image / Nano Banana / Sol galleries are a separate skill surface or should fold into design-agent-skills. Website/UI prompts do not belong here.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## image-prompt-galleries — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=5, technique=1, example=4, claim-source=0, reference=3.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (3):
- [GPT Image 2 prompt gallery, agent skill, and CLI](../../items/github-wuyoscar-gpt-image2-skill/card.md) — tool, reference — MIT repo bundling a curated GPT Image 2 prompt gallery with an agent skill and Python CLI
- [YouMind Nano Banana Pro prompt recommender skill (10k+ prompts)](../../items/github-youmind-openlab-nano-banana-pro-prompts/card.md) — tool — MIT agent skill searching 10,000+ curated Nano Banana Pro (Gemini image) prompts via grep-style lookup, returning top three matches with…
- [MeiGen: cross-model prompt gallery with MCP for GPT Image, Seedance, Nano Banana](../../items/web-meigen-ai/card.md) — tool, reference — MeiGen (meigen.ai) is a free community prompt gallery spanning GPT Image 2, Seedance, Nano Banana, and Midjourney with publish-to-earn…

First role `technique` (1):
- [GPT brand-campaign prompt template with PRYNE examples](../../items/x-2092979866836648104/card.md) — technique, example — Thread sharing a reusable 16:9 editorial+glossy-3D campaign prompt plus a one-line brand fill-in pattern, demonstrated on PRYNE math…

First role `example` (3):
- [Imageory.in ChatGPT prompt gallery promo with surreal blue-statue stills](../../items/x-2095085408208196006/card.md) — example, tool — Palakonweb promotes Imageory.in as a ChatGPT prompt source, attaching four surreal monochrome-blue classical-statue images with red…
- [GPT 5.6 Sol website prompt demo video (prompt not captured)](../../items/x-2095368133070700884/card.md) — example — Faisal Ahmed teases a GPT 5.6 Sol website-generation prompt with a short result video, but the prompt text itself was not captured in…
- [GPT 5.6 Sol website prompt teaser (marketplace link)](../../items/x-2095451624139567162/card.md) — example — Teaser post for a GPT 5.6 Sol website-generation prompt; quoted tweet links to a one-click marketplace for unlimited site prompts but…

First role `reference` (1):
- [awesome-gpt-image-2 — prompt-as-code library for GPT Image 2 templates](../../items/x-2092222199620833420/card.md) — reference, tool — Trending-repo alert for freestylefly/awesome-gpt-image-2: an industrial-grade prompt engine and template library for GPT-Image2 with…

Secondary membership (2), not in the primary count:
- [fal.ai unified generative media API and GPU platform](../../items/web-fal-ai/card.md) — primary `ai-video-generation`
- [GPT Image 2 face-swap stills plus Seedance 2.5 for realistic character video](../../items/x-2094819241916801165/card.md) — primary `ai-video-generation`

## image-prompt-galleries — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [prompt-to-html-landing](../../techniques/prompt-to-html-landing.md) — A named prompt or pattern that emits a full landing page in HTML/React.
- [taste-skill-encoding](../../techniques/taste-skill-encoding.md) — Installable taste/Impeccable/MengTo skills that change defaults, not just prompts.
- [prompt-as-code](../../techniques/prompt-as-code.md) — Image prompts stored as templates or searchable galleries, not chat paste.

## image-prompt-galleries — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [nano-banana-pro-prompts-recommend](../../tools/nano-banana-pro-prompts-recommend.md)
- [clawhub](../../tools/clawhub.md)
- [gpt-image-2](../../tools/gpt-image-2.md)
- [gpt-image](../../tools/gpt-image.md)
- [gpt-5-6-sol](../../tools/gpt-5-6-sol.md)

## image-prompt-galleries — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-wuyoscar-gpt-image2-skill#c1` | CLI gpt-image -p runs text-to-image and multi-reference edits via OpenAI image endpoints. | demonstrated | [GPT Image 2 prompt gallery, agent ski…](../../items/github-wuyoscar-gpt-image2-skill/card.md) |
| `github-wuyoscar-gpt-image2-skill#c2` | Gallery covers research figures, posters, UI mockups, anime, typography, maps, and tattoos. | stated | [GPT Image 2 prompt gallery, agent ski…](../../items/github-wuyoscar-gpt-image2-skill/card.md) |
| `github-youmind-openlab-nano-banana-pro-prompts#c1` | Skill searches 10,000+ curated Nano Banana Pro prompts and returns the top three matches with sample images. | stated | [YouMind Nano Banana Pro prompt recomm…](../../items/github-youmind-openlab-nano-banana-pro-prompts/card.md) |
| `github-youmind-openlab-nano-banana-pro-prompts#c2` | Token-efficient grep-style search avoids loading full category files. | stated | [YouMind Nano Banana Pro prompt recomm…](../../items/github-youmind-openlab-nano-banana-pro-prompts/card.md) |
| `web-meigen-ai#c1` | MeiGen MCP repo advertises 1,446+ curated prompts and nine MCP tools. | stated | [MeiGen: cross-model prompt gallery wi…](../../items/web-meigen-ai/card.md) |
| `web-meigen-ai#c2` | Gallery spans GPT Image, Seedance, Nanobanana, and Midjourney with category browse and publish-to-earn credits. | stated | [MeiGen: cross-model prompt gallery wi…](../../items/web-meigen-ai/card.md) |
| `x-2092222199620833420#c1` | awesome-gpt-image-2 is a prompt-as-code engine with 530+ reverse-engineered examples and 20+ templates for GPT-Image2. | stated | [awesome-gpt-image-2 — prompt-as-code …](../../items/x-2092222199620833420/card.md) |
| `x-2092222199620833420#c2` | The repo gained 2,449 stars in the last 24 hours for a total of 16,477 stars at capture. | stated | [awesome-gpt-image-2 — prompt-as-code …](../../items/x-2092222199620833420/card.md) |
| `x-2092979866836648104#c1` | Base prompt specifies premium 16:9 editorial+glossy 3D style with bold typography and high-end materials. | demonstrated | [GPT brand-campaign prompt template wi…](../../items/x-2092979866836648104/card.md) |
| `x-2092979866836648104#c2` | Authors add one line naming brand, product type, count, theme, and palette to specialize the template. | demonstrated | [GPT brand-campaign prompt template wi…](../../items/x-2092979866836648104/card.md) |
| `x-2095085408208196006#c1` | Author made attached stills with ChatGPT and points to Imageory.in for prompts. | stated | [Imageory.in ChatGPT prompt gallery pr…](../../items/x-2095085408208196006/card.md) |
| `x-2095368133070700884#c1` | Post advertises a GPT 5.6 Sol prompt with a demo video but does not include the prompt body in the capture. | stated | [GPT 5.6 Sol website prompt demo video…](../../items/x-2095368133070700884/card.md) |
| `x-2095451624139567162#c1` | Quoted follow-up advertises unlimited prompts for AI websites via an external marketplace link. | stated | [GPT 5.6 Sol website prompt teaser (ma…](../../items/x-2095451624139567162/card.md) |

Full set: claims.jsonl (23 rows)

## image-prompt-galleries — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- model family named (GPT Image, Nano Banana, Sol)
- prompts stored as code or searchable gallery
- reproducible parameters
- license / attribution of examples

## image-prompt-galleries — thread coverage

X items in primary roster: 5. captured_full=0, captured_partial=3, empty=1, failed=1.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2092222199620833420](../../items/x-2092222199620833420/thread.md) | empty | 0 | 0 | 0 |
| [x-2092979866836648104](../../items/x-2092979866836648104/thread.md) | captured_partial | 9 | 1 | 1 |
| [x-2095085408208196006](../../items/x-2095085408208196006/thread.md) | captured_partial | 8 | 3 | 1 |
| [x-2095368133070700884](../../items/x-2095368133070700884/thread.md) | failed | 1 | 0 | 0 |
| [x-2095451624139567162](../../items/x-2095451624139567162/thread.md) | captured_partial | 3 | 1 | 0 |

## image-prompt-galleries — gaps and open questions

Primary readiness: ready=4, ready-with-gaps=4. Gap tags: thread-partial=2, thread-failed=1, linked-page-unfetched=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Do gallery skills beat a folder of .md prompts for GPT Image 2?
- Should this subject merge into design-agent-skills after the next pass?

If this subject drops below 6 primary items after a future reclass, merge it into `design-agent-skills` and delete the folder.

## image-prompt-galleries — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [design-agent-skills](../design-agent-skills/brief.md)
- [ai-video-generation](../ai-video-generation/brief.md)

