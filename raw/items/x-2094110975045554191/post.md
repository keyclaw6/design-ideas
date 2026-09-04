# everyone showing off their six agent company is showing off one login. I counted what mine actually did in twenty minute

**Author:** fini (@0xfini)
**URL:** https://x.com/0xfini/status/2094110975045554191

everyone showing off their six agent company is showing off one login.

I counted what mine actually did in twenty minutes. 23,999 actions. Peak rate 38 per second. Six bots on the board.

One profile.

That is the whole thing. Six names in a sidebar, one browser session underneath, and every one of them inherits it.

The header on my own dashboard, which I built and then did not want to look at:

PROFILES 1. SHARED LOGIN yes. SPEND CAP none. AUDIT pending.

While I watched, the access ledger filled in on its own. Mail 624 actions. Drive 362. CRM 245. Ad manager 148. Billing 113. Crash reports 149. Eight systems reachable from one login, and I authorized exactly one of them, once, in an evening.

The blast radius counter went from 1 to 8 in the time it takes to make coffee.

Then the log line that ended it for me.

session: still open. no expiry.

I deleted a bot to test it. The session it was using did not die with it. Separate bots are not a security boundary. That is not my opinion, it is in the docs nobody opens.

So before you add a seventh agent, six things worth twenty minutes:

→ count your profiles, not your bots
→ list every system reachable from that one login. write the number down
→ set a spend cap before you set a schedule
→ delete a test bot, then check whether its session actually died
→ find your peak actions per second, then ask what twenty minutes at that rate touches
→ turn audit on before you need it, not after

None of this makes your fleet slower. It makes it something you can still switch off.

Twenty four thousand actions is not a flex. It is a number you should be able to explain.
