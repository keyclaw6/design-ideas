# The Shape and Feel of the Post-AI Data Stack

**URL:** https://www.iandmacomber.com/blog/post-ai-data-stack  
**Author:** Ian Macomber (Ramp)  
**Published:** 2026-08-30

Essay on how each data-stack era expanded the data scientist's blast radius — and what changes when AI makes analysis cheap but consensus expensive.

## Thesis (~2026)

AI makes producing analysis cheap. It does **not** make agreeing on reality cheap.

Post-AI data teams have two jobs:

1. Enable everyone to build with data and AI — accurately, powerfully, independently.
2. Build and champion the singular reality the company operates on.

Shift: from **producer of analysis** to **builder of company reality** (what's true, what matters, why).

## Historical arc

| Era | ~Year | Expansion |
|-----|-------|-----------|
| Pre-modern | 2013 | Data moats, small structured data on one server; no cross-DB joins, no JSON clickstream, big queries took down reporting |
| Cloud warehouse | 2016 | Infinite storage/compute; semi-structured JSON; "all company data" in one place |
| Modern Data Stack | 2020 | Managed ETL + Reverse ETL; data scientists become operators (Iterable, Salesforce, product changes) not just reporters |

## Post-AI stack diagram (2026)

Everything inside the boundary — including unstructured data (Gong, email, docs, code). New pieces:

- **Data agent harness** — tools, models, skills between stores and interfaces (coworkers, coding agents, Slack bots, AI-native BI).
- **Company context** — semantic layer, lineage, domain docs, activity metadata → harness via progressive disclosure.
- **Feedback loop** — artifacts, analysis, decisions, usage, evals route back into context.

## Key requirements (selected)

### Agent-readable artifacts

Dashboards become repositories of facts, contracts, and explanations — not destinations. Analog: SNL skits decomposed for TikTok/algorithm feeds.

Practices:

- Per-data-product `llms.txt` in markdown — code, filters, owners, entry points, rendered values.
- Provenance instructions linking queries to models, code, business context.

### Semantic layer as contract

Agents need governed metrics; without it they invent definitions. Semantic layer + dbt tests as the contract layer.

### Knowledge base / RAG

Internal corpus with hybrid retrieval (full-text + embeddings + IDF + age decay) — cites Cerebras blog as parallel build.

### Evals for agents

Treat agent outputs like ML: golden questions, regression when context changes.

## Ramp-specific notes

Author describes building Ramp Intelligence / internal agent harness with progressive disclosure of company context — details in full post with architecture diagrams (`datastack-premodern.png` through `datastack-postai.png` on site).

## Pull quotes

> *Coding agents, AI-native vendors, and Slackbot analysts have made it easy for anyone to answer their own questions and generate their own narratives.*

> *The scarce resource becomes company-wide consensus.*
