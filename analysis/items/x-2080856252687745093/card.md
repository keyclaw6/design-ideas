# Aman Chadha autoresearch and Meta-Harness engineering primer

`x-2080856252687745093` · x · article · en · [source](https://x.com/i_amanchadha/status/2080856252687745093) · [raw](../../../raw/items/x-2080856252687745093/)
**Author:** Aman Chadha (@@i_amanchadha) · **Published:** — · **Captured:** 2026-09-04T06:49:24Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** reference, technique · **Platforms:** cli, other

**Summary.** X thread promoting autoresearch.aman.ai. That host still times out; the live primer is aman.ai/primers/ai/autoresearch-and-metaharness (propose-run-evaluate loop, filesystem experiment memory, Meta-Harness search beyond model weights).
**Question it answers.** What is the end-to-end vocabulary for autoresearch loops and Meta-Harness system optimization?

**Claims.**
- `x-2080856252687745093#c1` (capability, stated) Autoresearch turns manual experimentation into a continuous propose-run-evaluate-learn loop. — evidence: "it turns manual experimentation into a continuous loop where agents propose changes, run experiments, evaluate results, and learn from each attempt." [post]
- `x-2080856252687745093#c2` (capability, stated) Meta-Harness extends search to prompts, retrieval, memory, tools, state, parsers, and control flow. — evidence: "it extends this idea beyond model training to the entire system around an LLM, including its prompts, retrieval, memory, tools, state, parsers, and control flow." [post]
- `x-2080856252687745093#c3` (result, demonstrated) autoresearch.aman.ai still connect-times-out; aman.ai/autoresearch is HTTP 404. The live primer is a different path on aman.ai. — evidence: "curl 12s timeout on autoresearch.aman.ai; aman.ai/autoresearch 404. See autoresearch-loop NOTES." [note]
- `x-2080856252687745093#c4` (availability, demonstrated) The live Chadha/Jain primer is https://aman.ai/primers/ai/autoresearch-and-metaharness/ (HTTP 200, 308,037 B; 14 H2 / 143 H3). Homepage aman.ai lists that href. Do not treat the timed-out autoresearch.aman.ai host as this page. — evidence: "GET 200 308037 B title Aman's AI Journal • Primers • Autoresearch and Metaharness. aman.ai homepage 64480 B includes primers/ai/autoresearch-and-metaharness. See autoresearch-loop NOTES." [note]
- `x-2080856252687745093#c5` (capability, demonstrated) Primer working definition: five components (bounded sandbox, editable artifact, proposer, evaluator, durable memory). Meta-Harness 'What gets optimized' names Prompt construction, Retrieval policy, Memory update, Tool orchestration, and Output parsing and repair. Harness is a policy over context and control flow. Concrete example is karpathy/autoresearch (train.py, 5-minute runs, val_bpb). — evidence: "Working definition + What gets optimized labels + karpathy/autoresearch train.py / val_bpb / 5-minute. Lee et al. 2026 cited for Meta-Harness. Bibtex year on the page is 2020. See NOTES." [note]
- `x-2080856252687745093#c6` (opinion, stated) Reply 2081160818394034487 (@papersdatacode) names Arbor (arXiv:2606.11926) as a hypothesis-tree autoresearch loop and proposes embedding edges so sibling branches can share lessons sideways. Thread is now captured_full (4/4). — evidence: "fxtwitter reply text: it runs the whole loop as a hypothesis tree. Insights only flow up the lineage to ancestors, so sibling branches never share." [reply]
- `x-2080856252687745093#c7` (benchmark, demonstrated) Arbor paper Toward Generalist Autonomous Research via Hypothesis-Tree Refinement (arXiv:2606.11926): coordinator + executors + HTR tree. Best held-out on all six Autonomous Optimization tasks; more than 2.5x average relative held-out gain vs Codex and Claude Code. MLE-Bench Lite 86.36% Any Medal with GPT-5.5. Abs 44,678 B; ar5iv 645,538 B. — evidence: "GET https://arxiv.org/abs/2606.11926 200 44678 B. Abstract: best held-out result on all six tasks; more than 2.5x … Codex and Claude Code; 86.36% Any Medal with GPT-5.5." [note]
**Numbers.** Arbor MLE-Bench Lite Any Medal: 86.36 percent (note)
**Recipe.** —
**Techniques.** [autoresearch-loop](../../techniques/autoresearch-loop.md)
**Tools.** —
**Links.** repo (https://github.com/karpathy/autoresearch), paper (https://arxiv.org/abs/2606.11926), product (https://aman.ai/primers/ai/autoresearch-and-metaharness/), https://aman.ai/primers/ai/autoresearch-and-metaharness/, https://aman.ai/, https://arxiv.org/abs/2606.11926
**Related items.** [x-2074912810803560497](../x-2074912810803560497/card.md), [x-2032671842230501729](../x-2032671842230501729/card.md), [x-2086790895538700379](../x-2086790895538700379/card.md), [x-2087026930323247306](../x-2087026930323247306/card.md)
**Media.**
`raw/items/x-2080856252687745093/media/media_0.jpg` (image, carries_technique=true) — Screenshot of autoresearch.aman.ai primer table of contents covering autoresearch loops and Meta-Harness architecture sections.
**Thread.** captured_full · reported 4 · captured 4 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2074912810803560497](../x-2074912810803560497/card.md), [x-2032671842230501729](../x-2032671842230501729/card.md)
