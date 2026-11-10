# 20 things for Speedmaxxing your vibe coded app:
> Source: https://x.com/suraj_sharma14/status/2109501816853467246
> Author: Suraj Sharma (@suraj_sharma14)
> Posted: 2026-10-12T04:30:00+00:00
> Captured: 2026-10-15T09:02:28+00:00
> Stats at capture: 32,887 views · 622 likes · 24 replies · 30 reposts · 1,064 bookmarks · 1 quotes

## Post

20 things for Speedmaxxing your vibe coded app:

- Measure first: run Lighthouse and PageSpeed on mobile
- Compress every image to WebP or AVIF
- Lazy-load images below the fold
- Serve static files from a CDN
- Remove packages your AI added but never used
- Split your JavaScript so pages load only what they need
- Preload your main font, and use only 1–2 fonts
- Add database indexes on columns you filter by
- Fix N+1 queries
- Paginate lists instead of loading everything
- Cache API responses that rarely change
- Stream AI responses instead of waiting for the full answer
- Show skeletons and loading states, not blank screens
- Move heavy work to background jobs
- Put your server close to your users
- Kill cold starts on your main routes
- Debounce search inputs
- Remove third-party scripts you don't need
- Test on a cheap Android phone on 4G
- Ask your AI: "What makes this app slow?"

Users don't wait.
A 1-second delay is a lost signup.

Bookmark this + send it to someone shipping this week.

## Media

![](media/image-01.jpg) — Reply 2109533937911611787 media 1. Source media: https://pbs.twimg.com/media/HUaR738XUAA-xyz.jpg
![](media/image-02.jpg) — Reply 2109533937911611787 media 2. Source media: https://pbs.twimg.com/media/HUaR735XEAA6L2r.jpg

## Thread

### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109833553928446407)) — 2026-10-13T02:28:12+00:00

@realoveio Optimistic updates help here but the cache still needs a clear revalidation strategy when mutations succeed or fail.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109626658659700944)) — 2026-10-12T12:46:05+00:00

@jamiejreach Developers optimize for their own setup by default. Testing on low-end hardware forces you to see the product through your users' eyes.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109834055093231901)) — 2026-10-13T02:30:12+00:00

@oleh_bernatskyi Especially when one package pulls in a whole tree of dependencies for a tiny feature.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109645576182862202)) — 2026-10-12T14:01:15+00:00

@simplydt A fast laptop on Wi-Fi is the easiest environment to fool yourself in.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109626457450512575)) — 2026-10-12T12:45:17+00:00

@dcsan Fast on fiber means nothing if the app struggles on 4G and budget hardware.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109833958091530349)) — 2026-10-13T02:29:49+00:00

@Rachel_hkz Measure first then fix the biggest bottleneck. Otherwise you're just optimizing what feels slow instead of what actually is.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109833756316197076)) — 2026-10-13T02:29:00+00:00

@bradvin Hope it saves you a few hours of debugging performance issues later.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109626567802618157)) — 2026-10-12T12:45:43+00:00

@George_Vasi_ Realistic data exposes bottlenecks that synthetic benchmarks often miss.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109544667297837331)) — 2026-10-12T07:20:16+00:00

@aniketmaurya Fast builds plus reliable tests is the real combo. Shipping quickly without breaking things is the goal.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109534211770347749)) — 2026-10-12T06:38:43+00:00

@SlimAssiliX Speed and unit economics need to improve together. Otherwise growth just makes the bill bigger.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109626236029063208)) — 2026-10-12T12:44:24+00:00

@nicklaunches Ship fast but make sure the app feels fast too. That’s what keeps users around.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109833652712673762)) — 2026-10-13T02:28:36+00:00

@itsthedonhashim Definitely worth doing, especially when paired with gzip or Brotli compression to reduce transfer sizes.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109506209476976962)) — 2026-10-12T04:47:27+00:00

@bkarishma360 AI makes building cheaper. Performance is still an engineering problem you can't prompt your way out of.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109645750141694247)) — 2026-10-12T14:01:56+00:00

@nikhilchhajar This is how you make good engineering habits repeatable instead of relying on memory.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109534445011411047)) — 2026-10-12T06:39:39+00:00

@dev_with_sam_ That's why checking the bundle after every AI-built feature should be part of the workflow. The hidden cost adds up fast.
### Suraj Sharma ([@suraj_sharma14](https://x.com/suraj_sharma14/status/2109626365666644391)) — 2026-10-12T12:44:55+00:00

@BreezeOg1 One of those bugs that teaches you to check query counts before blaming the frontend.

## Comments

### Realove ([@realoveio](https://x.com/realoveio/status/2109708660079509873)) — 2026-10-12T18:11:55+00:00

@suraj_sharma14 When caching API responses, test what happens immediately after someone edits their data. A fast response still needs to reflect the change they just made.
### Jamie ([@jamiejreach](https://x.com/jamiejreach/status/2109556065159499845)) — 2026-10-12T08:05:34+00:00

@suraj_sharma14 Testing on a cheap Android phone over 4G is the item most worth keeping, because your own laptop on fast Wi-Fi hides exactly the slowness a new user hits.
### Oleg Bernatskyi ([@oleh_bernatskyi](https://x.com/oleh_bernatskyi/status/2109710338367095292)) — 2026-10-12T18:18:35+00:00

@suraj_sharma14 "remove packages your ai added but never used" is the one people skip. it's usually the biggest win on the list
### David T Kramaley ([@simplydt](https://x.com/simplydt/status/2109633412331983057)) — 2026-10-12T13:12:55+00:00

@suraj_sharma14 testing on a cheap 4G phone is how you surface latency that dev laptops hide
### ˗ˏˋ DC ˎˊ˗ ([@dcsan](https://x.com/dcsan/status/2109598940631056583)) — 2026-10-12T10:55:56+00:00

@suraj_sharma14 Running Lighthouse on a low end 4G device catches latency you miss on a dev laptop
### Web制作出身のAI・Webアプリ開発者 ([@Rachel_hkz](https://x.com/Rachel_hkz/status/2109819897454940645)) — 2026-10-13T01:33:56+00:00

@suraj_sharma14 まず計測してから手を入れる順番がいいですね。体感ではなくボトルネックを見て、画像や不要な依存、N+1を順に潰せば、改善の効果も追いやすそうです。
### Brad Vincent ([@bradvin](https://x.com/bradvin/status/2109692597828714727)) — 2026-10-12T17:08:06+00:00

@suraj_sharma14 Handy list, saving this one
### George Vasilakopoulos ([@George_Vasi_](https://x.com/George_Vasi_/status/2109590344094585154)) — 2026-10-12T10:21:46+00:00

@suraj_sharma14 I'd run these checks on an account with months of data. Empty dashboards are suspiciously fast.
### Aniket Maurya ([@aniketmaurya](https://x.com/aniketmaurya/status/2109535973600280782)) — 2026-10-12T06:45:44+00:00

@suraj_sharma14 ..and run CI at speed of AGI on Celesto
### Simo | ai-costguard ([@SlimAssiliX](https://x.com/SlimAssiliX/status/2109525260068364594)) — 2026-10-12T06:03:09+00:00

@suraj_sharma14 Feels faster ≠ costs less. 
Measure both
### Nick Launches ([@nicklaunches](https://x.com/nicklaunches/status/2109606674063626282)) — 2026-10-12T11:26:40+00:00

@suraj_sharma14 Saving this one bro, thanks!
### Hussain Hashim | Building SundayBack ([@itsthedonhashim](https://x.com/itsthedonhashim/status/2109730932068426181)) — 2026-10-12T19:40:25+00:00

@suraj_sharma14 @suraj_sharma14 minify CSS and JS to reduce load times even further. Every byte counts when you're speedmaxxing!
### Karishma Bhardwaj ([@bkarishma360](https://x.com/bkarishma360/status/2109502537904869795)) — 2026-10-12T04:32:52+00:00

@suraj_sharma14 Vibe coding gets you to launch. 

Speedmaxxing gets users to stay.
### Nikhil Jain ([@nikhilchhajar](https://x.com/nikhilchhajar/status/2109630613578035440)) — 2026-10-12T13:01:47+00:00

@suraj_sharma14 Made a Claude Skill for this!
speedmaxx-vibe-app
### Sam ([@dev_with_sam_](https://x.com/dev_with_sam_/status/2109527186302738856)) — 2026-10-12T06:10:48+00:00

@suraj_sharma14 removing unused ai packages hits so close to home lol. openai loves to inject heavy deps u never touch
### BreezeOg ([@BreezeOg1](https://x.com/BreezeOg1/status/2109591563286511632)) — 2026-10-12T10:26:37+00:00

@suraj_sharma14 the n+1 one got me so many times, saving this
### Nguyễn Chí Trọng Nghĩa ([@hoatanhoano](https://x.com/hoatanhoano/status/2109773572931793113)) — 2026-10-12T22:29:52+00:00

@suraj_sharma14 Lazy-load mà vẫn giữ CDN — kiểu như ăn cơm trưa mà vẫn để tủ lạnh mở, nhưng chỉ dùng khi cần.
### BugByBug ([@bugbybughq](https://x.com/bugbybughq/status/2109523017512390853)) — 2026-10-12T05:54:15+00:00

@suraj_sharma14 Speed is great until a tiny change breaks something else in production 😭
Performance testing and debugging need to be part of the process too.
### Zerefs cosmos ([@phera46334652](https://x.com/phera46334652/status/2109533937911611787)) — 2026-10-12T06:37:38+00:00

@suraj_sharma14 https://t.co/vBuYzf9la5

So 

I think we need to stop https://t.co/jBkO4uW1Pq
![](media/image-01.jpg) — Source media: https://pbs.twimg.com/media/HUaR738XUAA-xyz.jpg
![](media/image-02.jpg) — Source media: https://pbs.twimg.com/media/HUaR735XEAA6L2r.jpg
### Doncalli ([@doncalli](https://x.com/doncalli/status/2109600826318622834)) — 2026-10-12T11:03:26+00:00

@suraj_sharma14 @threadreaderapp unroll

## Other returned timeline records

> The CLI did not expose reply relationships. These records do not start with a reply mention and were authored by someone other than the saved-post author. They may include recommendations or promoted posts; they are retained as source context, not verified replies.

### Starlink ([@Starlink](https://x.com/Starlink/status/2068115197718593741)) — 2026-06-19T23:34:21+00:00

Get connected with fast, reliable internet for streaming, video calls, online gaming and more.

Order online in minutes.
