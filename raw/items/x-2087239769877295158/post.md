# you don't need to re-explain your codebase's architecture to your agent every session. most tools stop at telling you wh

**Author:** Simplifying AI (@simplifyinAI)
**URL:** https://x.com/simplifyinAI/status/2087239769877295158

you don't need to re-explain your codebase's architecture to your agent every session.

most tools stop at telling you what broke.

sentrux is a real-time architectural sensor, it watches your codebase as a live treemap and turns file structure and dependencies into one continuous quality score.

the loop is simple:
codebase > agent scans structure and dependencies > sentrux scores 5 root cause metrics into one signal > agent sees exactly where risk concentrates > next session starts from a live map instead of a blind grep

the binary carries zero built-in language knowledge, all 52 languages live in plugin.toml and tags.scm query files, so a new language needs zero rust code.

small catch: it only scores the structure, it won't tell you why the cycle happened, that part's still on you.

built pure Rust with no runtime dependencies, specifically so it could sit as one binary between an agent and a codebase without adding friction.
