# Introducing Headlong, an open source microharness for persistent agents: self-guided agents that think continuously. Mos

@andykonwinski

Introducing Headlong, an open source microharness for persistent agents: self-guided agents that think continuously.

Most agent harnesses are reactive: you send a task, the agent completes it, and then it sits frozen until the next request. Cron jobs and heartbeats wake it up to run a checklist and put it back to sleep.

A Headlong agent is never asleep. It keeps generating thoughts about whatever it decides is interesting, in a self-guided loop inspired by human inner monologue. Your message doesn't start a session. It's one more observation that lands in the agent's thought stream, and the agent decides if and when to reply.

Headlong is built on the idea of persistent agency: continuous inner thought generation between external interactions. The agent sets its own interests and priorities, comes up with its own projects, and sometimes pings you unprompted with progress.

To keep our prototype as simple and small as possible, we implemented Headlong as a microharness: a complete agent harness in under 10K lines of Bash, organized as a handful of small executables. It includes a loop that generates the next thought, shellm (a recursive language model written in Bash), a trajectory stored as a DAG of jsonl files, and context as a projection of that trajectory.

We've been running one Headlong agent internally at Laude for several weeks. The whole team talks to it over Slack and Telegram, and every conversation lands in its single stream of thought. It works in its own fork of Headlong and we've pulled over 50 of its commits into main.

One night, with nobody talking to it, it went back to check whether a recall process it had built was actually wired into its mind, found that it wasn't, diagnosed and fixed the bug, and verified the fix end to end. 48 minutes, no human asked for the fix or was in the loop at any point. Every step is a timestamped line in its log.

Things broke too, and we wrote those up. Background thinking costs us $1 to $2 an hour, our agent stopped its own service three times by accident, and self-delegation died on day one. Details in the post.

One line installs everything and starts an agent. Use a dedicated sandbox and spend-capped API key; it runs real shell commands and thinks around the clock.

Headlong is research software, be careful!

curl -fsSL https://headlong.ai/install.sh | bash

Launch post: https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents

Repo: https://github.com/laude-institute/headlong

Headlong is a @LaudeInstitute  / MIT collaboration.
