## What they are actually doing

Jokker is amplifying **Obscura**, a Rust headless browser. The note-tweet ends “REPOO 👇”; the self-reply is the repo URL.

**What the post claims** (quoted, not independently benchmarked): a Rust browser for automation, scraping, and AI agents; 30 MB RAM; 85 ms page loads; auto-blocks 3,500+ trackers; avoids ads/analytics/tracking scripts; native rendering without Chromium; per-session randomized GPU/canvas/audio/battery fingerprint; “detectors can’t catch it because it behaves exactly like real Chrome”; drop-in for Puppeteer and Playwright; no Node, no deps, one binary; 22k+ GitHub stars; 100% OSS; free.

**Repo from the self-reply** — https://github.com/h4ckf0r0day/obscura (23,982★ / 1,762 forks at capture, Apache-2.0, language Rust, created 2026-04-13, homepage https://obscura.sh). README description: “The open-source headless browser for AI agents and web scraping.” Docs: https://docs.obscura.sh. Attached PNG is a crop of that README (Trendshift daily #1 badge + the same 30 MB / 85 ms / Puppeteer table). Site copy positions it as a Chrome replacement for machine sessions (boot, isolation, CDP). Community MCP/skill wrappers exist on GitHub search; they are not in the tweet.

Uriel asked whether Codex needs a custom skill vs an official plugin; no answer in the captured replies.

## Open questions

- How the tweet’s “+3.500 trackers” / “no Node / one binary” lines line up with the README (binary size listed as 70 MB; V8 + CDP).
- Official Codex/Claude plugin vs the unofficial wrappers Uriel is asking about.
- Relationship to Obscura Cloud waitlist / Cloudflare Kitesurf mention on the README (follow-on, not this tweet).
