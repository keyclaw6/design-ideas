# FFmpeg Skill v0.9.2→v0.12.0: 28 tools, pre-checks, track-aware subs, MCP, Claude Code/Cursor

> Source: https://x.com/kebura_P/status/2096964158994755604
> Author: shogo kajiyama (@kebura_P)
> Posted: 2026-09-07T14:09:49Z
> Stats (at capture): 144,607 views · 2,393 likes · 24 replies · 263 reposts · 3,863 bookmarks · 12 quotes
> Captured: 2026-09-21T15:33:42Z via api.fxtwitter.com
> Author bio (at capture): Video & Audio Engineer turned AI Developer. / Building AI Agents & Skills to automate video production. / Claude Code • FFmpeg • Open Source
> Author website: https://seventh-well.com

## Post

FFmpeg Skill Update 🎬

Ver.0.9.2→Ver.0.12.0

「この動画を9:16にして」「無音カットして」「字幕入れて」
に加えて、今はこんな指示もできます。

「この部分だけピクセル単位でクロップして」
「この写真、ズームしながらクリップにして」(Ken Burns風)
「動画を回転/反転して」
「この動画にロゴ動画を合成して」「グリーンバックを抜いて」
「この動画、逆再生にして」
「手ブレを直して」
「連番の画像から動画作って」
「単色/グラデーションの背景クリップ作って」
「劣化なしでそのまま書き出して」
「字幕は画質そのままで、後から切り替えられる形で入れて」
「ハイライトは音量じゃなくて長さで選んで」
「AI解析用に軽い解像度でプレビュー書き出して」

できることが21→28個のツールに増えました。

🔍 AIが「わかった上で」処理するように

・「今この環境でこのツールが実際に使えるか」を実行前に事前チェック
・GPUエンコーダー/フォント代替の有無も把握
・複数の音声トラックを持つファイル(吹き替え・別言語版など)で、使うトラックをほぼ全ツールで指定可能に
・字幕トラックの言語などの詳細も読み取れるように
・字幕タイミングをタイムコード(hh:mm:ss:ff)形式でも指定可能に
・9:16化などのクロップで、切り取る位置(左寄せ/右寄せなど)も指定可能に
・音声を再エンコードするかしないか、各ツールが正直に申告するように

✅ 「壊れない・嘘をつかない」を徹底

・書き出しが本当に成功したか毎回確認してから「完了」と報告、失敗時のゴミファイルも残さない
・元の動画ファイルを誤って上書き・破損させない安全策
・失敗した時、原因とやり直せるかをAIが判別
・色変換で再エンコードが必要になった場合も、字幕や追加の音声トラックをできる限り残すように
・同期のズレを検出した時、信頼度が低い場合はAIに警告
・最新FFmpeg / Windows環境でも安定動作(Windowsのパス周りのバグ修正含む)

🛠️ 開発・保守の仕組みも強化

・「AIがして良いこと/判断すべきでないこと」を明文化(勝手にAIが「見た目の良さ」を判断しない設計)
・生FFmpegコマンドへの逃げ道を塞ぐテストを追加
・ドキュメントと実際のコードの挙動がズレたら自動テストで検知
・OSSとしてのContributing手順を整備、バージョンタグを打つとGitHub Releaseが自動生成される仕組みを追加
・GPU対応について「対応してるとは言うが動作保証はしない」ことを正直に明記

Claude Code / Cursor / Codex対応、MCPあり、ローカル処理でクラウド不要は変わらず。

Current: v0.12.0

https://github.com/kajisho5/ffmpeg-skill?v=0.12.0

#FFmpeg #AIVideo #AI #MCP #ClaudeCode #OpenSource

## Media

No media on this post.

## Thread

No author self-replies visible at capture (conversation replies did not load in the logged-in bridge session; X conversation endpoint rate-limited, 13/13 pages returned the main post only).

## Comments

24 replies counted by API; none retrievable at capture (bridge n=1 article on URL-verified page after 4–6 scroll rounds; r.jina.ai x.com access blocked until 2026-09-21T15:59:15Z).

## Links

- https://github.com/kajisho5/ffmpeg-skill?v=0.12.0
