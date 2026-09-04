# threads-script

Harvested all 311 X items via logged-out `x.com` status HTML (`x-web-dom`) plus fxtwitter counts.

- captured_full: 18
- captured_partial: 270 (logged-out DOM shows first-level visible replies, not the full 9.6k)
- empty: 14
- failed: 9 (reported replies > 0 but no extra tweets in DOM)

Failed ids: x-2095136786095951924, x-2087151807965401320, x-2095368133070700884, x-2093051654937423887, x-2093915384944414827, x-2094769581965369822, x-2094961942058418268, x-2093669411685110141, x-2093118868092748246

Author handles on many replies are `unknown` (Relay user records not always adjacent). Thread workers should fill handles from comments.md / harvest HTML when present.
