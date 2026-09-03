## What they are actually doing

**Atlas Fields Studio** is Arena Physica’s public beta **3D EM field viewer** for Heaviside-1. Desktop-only (jina of the app URL shows a “only available on web / open on a computer” gate, ToS checkbox, then a WebGL-style studio: Design / Explore / Create, PCB + `.msh` upload, E/H/S fields, vec/stream/far render, slice box, S-param inset, Smith chart). Claim on the splash: predicted E/H update in milliseconds vs hours for a commercial solver.

**Heaviside-1** (2026-09-01 paper: `https://www.arenaphysica.com/publications/heaviside-1`)

- Foundation model for electromagnetism (RF → photonics), not an LLM. 350M params (>10× Heaviside-0 / ~GPT-2 size).
- Inputs: 3D geometry + materials + excitation (not 2.5D planar stacks).
- Outputs: full complex E/H near-fields at arbitrary probe points, not just S-parameters.
- Train: 250k unique designs, 500B field samples (~20 TB). Speed claim: 10⁵× vs commercial solvers; accuracy within 1 dB; OOD S-param error 0.99 → 0.53 dB with field supervision.
- Examples in the paper: distorted BGA solder balls; hairpin bandpass at 16 GHz (sim vs pred).
- Heaviside-0 (March, Atlas RF Studio) was planar + S-params. Studio email: studio@arenaphysica.com.

Neal asked for generated-vs-measured comparison; Arena pointed at the paper rather than posting a new table in-thread.

## Open questions

- Renderer stack (Three.js vs custom WebGL) not named in the captured pages.
- Measured-vs-predicted plots live in the paper; not extracted figure-by-figure here.
- Author Heaviside tweet appears truncated at 280 chars (fx did not expand a note-tweet).
