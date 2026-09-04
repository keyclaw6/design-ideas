# Subject worker instructions

You own one subject slug. Read `docs/ANALYSIS_STRUCTURE.md` §4.3, §4.3.1, §5, §7.3.

## Inputs

- `analysis/subjects.json` for your slug
- After Phase 2 render: `analysis/subjects/<slug>/items.jsonl` and `claims.jsonl`
- Every `analysis/items/<id>/card.md` listed there
- Legacy `catalog/topics/` only as input

## Writes

- `analysis/subjects/<slug>/brief.json` (§4.3 — all keys)
- `analysis/subjects/<slug>/brief.md` with the ten H2 headings **exactly**:
  `## <slug> — scope` through `## <slug> — adjacent subjects` (see spec)
- NOTES blocks of `analysis/techniques/<t>.md` where `owner_subject = <slug>` (3–10 lines)
- Optional reclass records in `analysis/_work/reclass/<slug>.jsonl`

## Rules

- H1: `# <name> (<slug>)`
- No H3+. Length 120–400 lines.
- Roster lists every primary item.
- `must_read` ≤ 12 via reclass records (`judge_hints.must_read`)
- Comparison axes: 3–8 criteria, no words `best`, `winner`, `recommended`
- Do not edit `card.json` directly
- Handoff: `analysis/_work/handoffs/subject-<slug>.md`
- Commit: `feat(subject-<slug>): brief and technique notes`
