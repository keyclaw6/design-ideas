# i always disable all permission checks for my agents - i don't even do auto review. many people saw that in my videos an

**Author:** Kun Chen (@kunchenguid)
**URL:** https://x.com/kunchenguid/status/2082316720086405524

i always disable all permission checks for my agents - i don't even do auto review. many people saw that in my videos and asked me how i dare do that, and that's actually a really good question

on a high level, there are 3 things that allowed me to do that -

1. a mindset shift - my machine is not mine

i now treat it as my employee's device. if i hired a human employee and bought a laptop for them, i would never tell them to ask me for approval each time they wanted to run a shell command on it

if you worked in IT for any big enough company, you would know that humans destroy their devices a lot more often than agents

the solution is not to introduce an approval process that constantly blocks my employees from doing their work. it's to be ready to wipe the whole thing any time, which leads to -

2. fully reproducible config

i showed this in my video and my public dotfiles repo - https://github.com/kunchenguid/dotfiles/

i use nix-darwin and home-manager to make my entire machine instantly reproducible. if anything goes wrong, i wipe the whole thing, clone my dotfiles, run rebuild, and a few minutes later everything's up and running again

3. isolate all secrets

production secrets and credentials should never live in plain text on an employee's machine. i always lock down all my secrets behind a gate that only i can authorize

i showed this in my latest video that my latest go-to solution for this is @AutomicVault - every time my agents need to access a secret, they go through me and i can decide whether i allow it or not based on the command they are trying to run that needs to secret

with this setup, my agents can work in a trusted by constrained manner, allowing them to move freely yet there's no way for them to create a disastrous outcome
