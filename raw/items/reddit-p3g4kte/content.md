# Cheap KVM options

> Source: https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3g4kte/
> Parent post: https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/
> Parent post author: u/_moldu
> Saved comment author: u/n_dion
> Parent post posted: 2026-08-13T10:11:43+00:00
> Saved comment posted: 2026-08-13T14:09:17+00:00
> Captured: 2026-10-15T08:55:18+00:00
> Score: 3 · Comments: 26
> Community: r/homelab

## Post

Hi! I’m looking for some kind of KVM options for my homelab. I’d like something as cheap as possible.

I’m trying to find some kind of USB KVM devices that connect to a computer and has some kind of interface that streams an HDMI input to a web browser and emulates a keyboard. Like if I’m not at home and I want to connect to my 4 servers and the networking for those is down for some reason or an SSH connection is not enough, I could log in over a VPN to a machine home and use that as a kind of a gateway for the four servers. I do have a computer that can be used just for that. I know that this setup is basically an IP KVM with 4 ports but one of that is very expensive. I’d like a solution that costs <75€.

What would you guys recomend?

## Saved Comment

> u/n_dion · 2026-08-13T14:09:17+00:00 · score 5 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3g4kte/)

It depends on how important is access for you. I've two PiKVM devices. One original v3 kickstarter that is running for \~4 years.. Plus one PiKVM v4, JetKVM. I also had  NanoKVM that I returned almost immediately. 

From my experience PiKVM is most stable and trusted thing. As I said v3 works for \~4 years far away in another country in my parent's house with zero issues. Yes it's more expensive but it's very good hardware plus it's way overpowered for what it's supposed to do.. You can easily host more things on it.. Like 'backup/emergency' VPN server/gateway, tailscale node, MQTT gateway or simple docker containers like backup DNS. With these extra features it's much easier to justify price. PiKVM now also have "official" switch/extender so that you can connect more than one machine at the same time with full UI integration. I don't have it myself because it's too expensive for me..

What I don't like about PiKVM is case. it's totally fine for put and forget.. But it's metal case with sharp edges. I was able to scratch my desk with v3 case... Definitely not EDC/travel friendly gadget. 

Now JetKVM. This visually looks much better and it's much more travel friendly or more like EDC gadget. Software is less polished, less amount of features and much more bugs. But my main concern with JetKVM is that it's significantly more fragile. Even in simplest case (just short HDMI cable with no VGA adapters, etc) sometimes it just displays noise instead of picture. Unplugging and plugging back HDMI cable sometimes works. Usually reboot of JetKVM from web UI helps.. Huge plus is that usually there is no need for external power supply. it gets power from target machine.. Right now I'm using it as "semi-EDC" gadget on my work desk when I need to plug monitor somewhere but I don't have second one. In such scenario it's pretty ok. It also can run tailscale but don't expect much. It's very low power device with small amount of RAM. Just enough for KVM. Unfortunately it has no wifi (normally I prefer to use ethernet everywhere but for this particular use case wifi would be huge plus for me). Also my verison is original one with miniHDMI cable.. less popular than normal HDMI.

NanoKVM was my worst experience. It was very unstable, sometimes there was no Ethernet, sometimes no picture, etc. I found that it sort of works if HDMI cable is plugged after power/usb data. Maybe they fixed it in new hardware revision.

  
Personally myself I would choice PiKVM for anything critical where it would be difficult to get physical access to machine. It's ok to use it with cheapest 4 port KVM that can do port switching via hotkey to reduce per-device cost. it's like a workhorse, mature and stable product. 

But at home where I'm just too lazy to plug monitor but fine to power cycle if needed JetKVM is good enough. just add extra smart plug :) And JetKVM is cheaper even if you buy device for every machine. 

PS. JetKVM was recently updated with normal HDMI port, optional PoE, microsd card instead of built-in memory. But there was post somewhere that it now have even smaller mount of RAM.. I'm not sure that tailscale will work on newer JetKVM device if it has less RAM.. My device is original one with miniHDMI port 

## Thread

> u/_moldu · 2026-08-13T10:16:35+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3eyy0h/)

one of those is 100$ and I would need 4 🥀 I’ve heard of it. It’s a good product.

> u/_moldu · 2026-08-13T11:33:55+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3facvh/)

thanks for the advice. I will start with a jetkvm with a regular 4 way kvm then gradually I will invest in more jetkvms, so in two years’ time each machine will have its own standalone device with ATX and all the goodies.

> u/_moldu · 2026-08-13T10:30:25+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f0uct/)

I think I could use one of these, find a basic 4x1 kvm and use an esp32 to switch over the video and usb signals. I think this will be under the budget. Thanks you!

## Comments

> u/scorp123_CH · 2026-08-13T10:14:43+00:00 · score 6 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3eyowo/)

I am happy with JetKVM .... ❤️ 

> u/Phipol · 2026-08-13T10:52:30+00:00 · score 4 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f3zuv/)

If you need four you can use a regular no IP KVM "after" it, as long as it is hotkey switchable.
So basically JetKVM -> PlainoldKVM -> Nodes
For mere keyboard/mouse control+Video Input that works.

It has it's downsides in terms of reliability,but it works.
I would gradually invest in more proper KVMs,though, due to the other advantages of proper KVMs (ATX/Rebooting- this partially can be circumvented with a switchable PDU,though, USB Mounting,etc.).

I have tried nearly every "homelab" grade KVM and tbh, JetKVM is by far the most solid one.
PiKVM/BliKVM is less reliable(and bloody expensive), NanoKVM is a nightmare, Luckyfox is not quite there yet either.
I hate the form factor of the JetKVM but Hard- and Softwarewise they are the most solid atm.

The only better solution is a proper IPMI mainboard but these,well, come at a price. 

> u/Luckybob83 · 2026-08-13T10:52:01+00:00 · score 5 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f3x94/)

Find a cheap one port IP KVM, then get a regular KVM that supports hotkey to switch between inputs.

> u/OurManInHavana · 2026-08-13T11:20:05+00:00 · score 3 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f85uy/)

I like the NanoKVM line (especially their PCIe versions)... but they have a "Lite" version as well. Those were [$40-$45 each](https://www.aliexpress.com/item/1005007369816019.html).

A ton of IPKVMs have come out in the last year: but 4-systems-for-$75 is going to be hard. You could definitely do something like 4 Lites for under 200€ though.

> u/korywithawhy · 2026-08-13T10:23:44+00:00 · score 2 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3ezxge/)

[Luckfox PicoKVM Lightweight IP KVM Remote Management Tool, Supports 1920 × 1080@60fps HDMI Video Input and HID Signal Output for Device Control](https://www.luckfox.com/Luckfox-PicoKVM-Base?search=kvm&category_id=0)

this is about as cheap as can be. 

> u/cruzaderNO · 2026-08-13T10:53:00+00:00 · score 2 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f42de/)

They usualy have a hotkey combination to switch, there is not really a need for anything extra to switch.

> u/RB-27 · 2026-08-13T10:35:39+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f1kvm/)

On AliExpress, you can find them as “Choice” deals starting at just €16. I've had good experiences with deals like this so far, but I can't say anything about this specific one. Just search for “IP KVM” and it should come up.

> u/Valuable-Fondant-241 · 2026-08-13T11:55:22+00:00 · score 2 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3fdx6s/)

The actual product or a motherboard support for 16€?

> u/ZHX_Proto · 2026-08-13T10:33:16+00:00 · score 2 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3f18tz/)

GL.iNet has a 4port one for 295€.

for 4 computers it's going to be hard under 75€. You can maybe find picokvm for ~40€ each without power supply

> u/pain00794 · 2026-08-13T13:02:18+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3fqd9c/)

Radxa has a small 45 dollar KVM which was released recently https://radxa.com/products/linkr/linkr/

> u/jimger · 2026-09-18T10:27:30+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/pajmd0a/)

seems fair. can' find with 45 usd though



> u/MurphPEI · 2026-08-13T13:14:32+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3fsubk/)

There is a Youtuber (whos name I forget) who breaks down gear (both the hardware and the code) and he has several videos tearing up the humorously ridiculous security flaws in many of the the cheaper KVMs.  I don't use them as SSH is enough for me but I watched a couple for entertainment and it was an eye opener.   Just be careful.  I think the posters saying start with 1 Jet plus a hardware KVM for now is the safer bet.

> u/SoulkeepHL · 2026-08-13T19:32:00+00:00 · score 3 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3i8j0i/)

pretty sure the youtuber you're referring to is apalrdsadventures 

> u/MurphPEI · 2026-08-13T20:18:41+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3ij81g/)

Yes. That is him.  Thanks.

> u/SoulkeepHL · 2026-08-15T06:14:03+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3sl7u5/)

excellent! (otherwise, I'd have wanted to know who else was doing similar things 😅)

> u/Anti-Hero25 · 2026-08-13T13:56:15+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3g1pnz/)

Following 

> u/Anti-Hero25 · 2026-08-13T14:10:03+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3g4r1m/)

I know nothing about this but saw this after reading your post….  


https://preview.redd.it/2gis1lkvg5jh1.jpeg?width=1206&format=pjpg&auto=webp&s=9e22999ab3293d80a7221038162a240eb7e25aa3

> u/azlan121 · 2026-08-13T16:38:22+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3h3db5/)

NDI KVM, novnc or rustdesk are probably the sensible options for doing it cheaper than the already cheap hardware options like the gl-comet, jetkvm etc...

> u/positionsixnine · 2026-08-22T22:55:16+00:00 · score 1 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p5b2pw2/)

I recently built me own KVM using a raspberry pi 5, HDMI to USB video capture dongle and a USB-C power data splitter. I call it pi-micro-kvm and everything can be found on my github. mgaither98-boop/pi-micro-kvm. 

You plug the hdmi and USB from the splitter into the back of the server and you can access it through any browser via the ip address. 

> u/kevinds · 2026-08-13T15:40:01+00:00 · score -2 · [comment](https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/p3gpjbt/)

>I’d like a solution that costs <75€.

I suggest you go back to sleep.

## Links

- https://www.reddit.com/r/homelab/comments/1vn6mlo/cheap_kvm_options/
