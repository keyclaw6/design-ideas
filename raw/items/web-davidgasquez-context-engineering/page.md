# Context Engineering Is a Data Problem

**URL:** https://davidgasquez.com/context-engineering-is-a-data-problem  
**Author:** David Gasquez

Short essay arguing organizational context should be built like a data warehouse — not owned by hosted agents.

## Core claim

Companies want your data and context because **context is their moat**. Products that own context can force you onto their agent — and hosted agents rarely match self-owned harness quality.

Organizations need a **model-agnostic knowledge base** (ontology / company brain) for the same reasons they maintain a warehouse: curated normalized layer helps humans and agents make sense of structure that outlives any model, harness, or product.

> *Context engineering is that same work: extracting, filtering, curating, modeling, and publishing artifacts to help the organization make better decisions.*

Intelligence-product architecture diagrams look like 2018 Fivetran/dbt pages because the problem is the same.

## Knowledge Build System (ETL pattern)

Knowledge base as **compiler for agents** — raw sources → LLM-optimized representations.

1. **Extract** — raw data to filesystem/DB preserving source shape (Slack JSON, Slides as PDF, …)
2. **Transform** — org-specific modeling; summarize, extract, clean (cf. Cerebras Slack distillation). No universal "correct" company knowledge representation.
3. **Publish** — curated text files + optional embeddings (index only; disposable)

> *Connecting Looker to every raw source never solved analytics — same for agents reading every raw source.*

Direct access can beat a poorly maintained KB, but eventually you need a process to **derive meaning and codify truth** — otherwise agents read three conflicting OKR definitions and proceed.

Parallel to dbt: once "key action" is defined, it lives in a model downstream teams evolve. Curated text files = **materialized views optimized for LLM consumption**.

## Operational responsibilities

- Represent knowledge so anticipated questions are easier to answer (cf. Anthropic contextual retrieval)
- Curate/filter sources per entity accuracy
- Build **marts** per area/team — no universal "company context" package
- Analyze recurring questions → update models
- Fight **context debt** — ambiguity, staleness, untraceable interpretation

> *Ingestion is not the product. Sense-making, modeling, and coordination are what allow organizational knowledge to compound.*

## Footnote

Context is finite (for now) with diminishing returns.

## Cross-links in capture-8 cluster

- Cerebras KB blog — transform step example
- Macomber post-AI stack — agent-readable artifacts + harness
- Anthropic analytics post — governed semantic layer
