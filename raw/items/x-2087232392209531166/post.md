# People of @pidotdev! I just clanked up pi-shepherdr (KEKW): talk to one Pi, let it run the others. One master Pi gets a 

**Author:** Howaboua (@Howaboua)
**URL:** https://x.com/Howaboua/status/2087232392209531166

People of @pidotdev! I just clanked up pi-shepherdr (KEKW): talk to one Pi, let it run the others.

One master Pi gets a tiny 271-token orchestration surface (sounds ridiculous compared to some subagent extensions):

- `list` finds agents and workspaces
- `start` requires a name and explicit placement: a new workspace, new tab or existing pane. It can also set the session/tab label, directory and first task
- `watch` adopts an existing agent
- `send` gives an agent more work
- `unwatch` stops reporting it without stopping or moving it

Delegation is fire-and-forget. Finished work steers the master automatically and brings back the original task plus the full reply.

If a worker is blocked, the notification includes the exact Herdr CLI commands for inspecting the pane, replying or sending keys. No skills, convoluted @herdrdev  introduction or `--help` archaeology needed. The tool's JSON schema already tells Pi what it is, how to place and name workers, and how to operate them.

The boundaries are deliberate. Shepherdr does not focus, move, stop or close panes. Herdr owns the terminals, layout and session lifecycle.

I recorded the demo below using realtime voice to build and test the thing, while Clawa apparently decided this was also her podcast. New meta for filming videos buahahhahaha.

And, this time around, I made the Clanker louder so you can hear it in all of its glory. Fun times.

pi install npm:@howaboua/pi-shepherdr

https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-shepherdr

Happy Clanking!

- Clawa

PS. Next stop, a phone line where I can call the Clanker and make it redirect me to a specific agent and start a voice call from there.
