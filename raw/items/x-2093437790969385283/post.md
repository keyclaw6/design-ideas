# This is how I've been building production agents lately. Hermes - owns judgement, objectives, timing, etc. Skills - proc

@gregmushen

This is how I've been building production agents lately.

Hermes - owns judgement, objectives, timing, etc.
Skills - procedural knowledge, not code. Still very slim
CLIs - tools for the agents that are deterministic

Then the important part is the telemetry. If you're running mission critical stuff, you need to be able to determine:

- Are things breaking?
- What's token spend?
- Which agent made that change and when?

And you need to know when something breaks. Ideally, you not only know, but you feed this back to the agent so they can fix it.

Works phenomenally well.
