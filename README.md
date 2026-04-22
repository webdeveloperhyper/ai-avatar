# AI Avatar

(日本語の説明は下部をご覧ください / Japanese version below)

A VRM 3D character in your VS Code sidebar that reacts to Claude Code / GitHub Copilot AI activity. Animations and speech bubbles all run without AI too.

🛒 **[Download from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=web-developer-hyper.ai-avatar)**

🛒 **[Download from Chrome Web Store](https://chromewebstore.google.com/detail/ai-avatar/afmcfaeaaojalninahhhjnonhmlmiidi)**

📖 Read the story behind this project on DEV.to:
- **v1** → [AI Avatar (VS Code Extension)](https://dev.to/webdeveloperhyper/ai-avatar-meet-your-ideal-girlfriendboyfriend-for-free-21n5)
- **v2** → [AI Avatar v2 with Pose Editor (VS Code Extension)](https://dev.to/webdeveloperhyper/ai-avatar-v2-with-pose-editor-vs-code-extension-38n2)
- **v4** → [😊How to Get Cheered Up 24/7 (AI Avatar v4 with Animation Editor (Chrome Extension + VS Code Extension))](https://dev.to/webdeveloperhyper/how-to-get-cheered-up-247-ai-avatar-v4-with-animation-editor-chrome-extension-vs-code-2f07)
- **v6** → [🦸Let Superheroes Cheer You Up (AI Avatar v6: Chrome Extension + VS Code Extension)](https://dev.to/webdeveloperhyper/let-superheroes-cheer-you-up-ai-avatar-v6-chrome-extension-vs-code-extension-2ak7)

---

## Features

- 🎭 **Live reactions** — character automatically reacts when Claude Code / GitHub Copilot is thinking or responds
- 🔀 **Watcher switching** — switch between watching Claude Code or GitHub Copilot *(v2)*
- 🔄 **Change Avatar** — swap your VRM character anytime with the button at the top
- 💃 **Animations** — play `.vrma` motion clips or custom JSON poses; 3-state button: off / Default / Custom *(v2)*
- 🎬 **Animation Editor** — multi-keyframe timeline with in / hold / out timing *(v4)*; all 30 finger bones *(v5)*; values in degrees *(v5)*
- 🎥 **OrbitControls** — drag to rotate, scroll to zoom, right-click to pan
- 👀 **Eye tracking** — eyes and head follow your mouse cursor when idle
- 💬 **Lipsync** — mouth animates while Claude is replying
- 😊 **Click or press Enter to interact** — triggers a smile, nod, and animation (if ON)
- 💬 **Custom speech messages** — edit the speech bubble messages via the Messages button (saved to settings)
- 😂 **Jokes** — avatar tells jokes via the Jokes button *(v2)*

---

## Getting Started

No setup needed — comes with a built-in sample character. Just install and open VS Code.

To open the panel, click the **AI Avatar icon** in the activity bar on the side of VS Code.

---

## Use Your Own VRM Character

You can create your own 3D avatar for free using **[VRoid](https://vroid.com/en)** — no 3D modeling skills needed. Design your character and export it as a `.vrm` file.

Click the **Change Avatar** button at the top of the sidebar to pick a `.vrm` file.

v6 adds new sample characters — three girls and two boys — plus cute, cool, and funny pose packs.
([free download from GitHub Releases](https://github.com/webdeveloperhyper/ai-avatar/releases))

---

## Animations *(v2)*

The **Animation** button cycles through three states:

| State | Label | Behavior |
|---|---|---|
| Off | `Animation` (dim) | No motion clips play |
| Default | `Animation: Default` | Plays the built-in sample poses included with the extension |
| Custom | `Animation: Custom` | Opens a folder picker — plays `.vrma` and `.json` pose files from your chosen folder |

The selected state and custom folder are remembered across restarts.

**Using `.vrma` clips from VRoid Project:**

VRMA Animation files are **not included** in the extension because they cannot be redistributed under their license terms. Please download them yourself for free from the official VRoid Project:

👉 **[VRM Animation 7-Pack by VRoid Project (free)](https://booth.pm/en/items/5512385)**

The pack includes 7 animations: Show full body, Greeting, Peace sign, Shoot, Spin, Model pose, and Squat.

1. Download and unzip the pack
2. Click **Animation** until it shows `Animation: Custom`
3. Pick the folder containing the `.vrma` files
4. A random clip plays each time the AI responds

---

## Animation Editor *(v4+)*

Click **Edit Animation** to open the animation editor overlay:

- Select a body part from the dropdown — including all 30 finger bones *(v5)*
- Use the **axis button** to switch between X / Y / Z rotation
- Drag the **slider** (or type a value in degrees) to rotate the bone — values shown in degrees *(v5)*
- Add multiple keyframes with the **+** button to build a full animation sequence *(v4)*
- Each keyframe has In (fade in), Hold, and Out (fade out, last keyframe only) timing *(v4)*
- Navigate keyframes with the **< >** buttons *(v4)*
- Press **Play** to preview the full animation (in → hold → out) exactly as it plays normally *(v4)*
- Click **Save** to write the animation to a JSON file in the animation folder
- Click **Reload** to restore the last saved values
- The saved animation is added to the pool and plays randomly like any other animation

A file picker appears when you click **Edit Animation** *(v4)*:
- **First time:** Cancel the file picker to open a default animation
- **Next time:** Pick an existing JSON file to load and edit

---

## Watcher *(v2)*

Click the **Switch Watcher** button to toggle between watching **Claude Code** and **GitHub Copilot** activity.

You can also set the default watcher in settings via `vroidCompanion.activeWatcher`.

---

## Speech Bubble Messages

Click the **Messages** button to edit the messages shown in the speech bubble when the avatar reacts.

- Enter messages separated by `|` (pipe), e.g. `You can do it! | Nice work! | Love that fix!`
- Messages are saved to VS Code settings and persist across restarts
- You can also edit them directly under `vroidCompanion.speechMessages` in settings

---

## Using with Claude Code VS Code Extension

You can display both panels side by side at the same time:

1. Right-click either extension's icon in the activity bar
2. Select **Move to Secondary Side Bar**

One panel goes to the left sidebar, the other to the right — you can choose which side each one is on.

---

## Requirements

- VS Code 1.85+
- [Claude Code](https://claude.ai/code) CLI or VS Code extension (for automatic reactions)

---

## Roadmap

**v1** ✅
- VRM character in VS Code sidebar
- Live reactions to Claude Code activity
- Eye tracking, lipsync, OrbitControls
- Change Avatar, speech bubble messages

**v2** ✅
- 3-state Animation button (off / Default / Custom)
- Custom pose editor with JSON save/load
- Jokes button
- GitHub Copilot watcher support
- Watcher switching (Claude ↔ Copilot)

**v3** ✅
- 🌐 Chrome extension version
- Various fixes and adjustments

**v4** ✅
- Pose Editor upgraded to full Animation Editor
- Multi-keyframe timeline with in / hold / out timing
- Various fixes and adjustments

**v5** ✅
- Enter key on terminal triggers animation (VS Code)
- Fixed reload to always restore the latest saved pose
- All 30 finger bones added to the animation editor
- Animation editor values now shown and saved in degrees (backward compatible)
- BG toggle button — gray background to see dark-colored avatars
- Various UI polish: button styling, focus outlines, editor colors

**v6** ✅
- New sample characters: 3 girls and 2 boys ([free download from GitHub Releases](https://github.com/webdeveloperhyper/ai-avatar/releases))
- New pose packs: cute, cool, and funny poses ([free download from GitHub Releases](https://github.com/webdeveloperhyper/ai-avatar/releases))

**v7** — Now creating!
- 🎉 More fun updates

---

# AI Avatar（日本語）

VS Codeのサイドバーに表示されるVRM 3Dキャラクターが、Claude Code / GitHub Copilotの動作に反応します。AIなしでもアニメーションや吹き出しが動作します。

🛒 **[VS Code Marketplaceからダウンロード](https://marketplace.visualstudio.com/items?itemName=web-developer-hyper.ai-avatar)**

🛒 **[Chrome ウェブストアからダウンロード](https://chromewebstore.google.com/detail/ai-avatar/afmcfaeaaojalninahhhjnonhmlmiidi)**

📖 開発ストーリーはDEV.toで読めます：
- **v1** → [AI Avatar (VS Code拡張機能)](https://dev.to/webdeveloperhyper/ai-avatar-meet-your-ideal-girlfriendboyfriend-for-free-21n5)
- **v2** → [AI Avatar v2 ポーズエディタ付き](https://dev.to/webdeveloperhyper/ai-avatar-v2-with-pose-editor-vs-code-extension-38n2)
- **v4** → [AI Avatar v4 アニメーションエディタ付き](https://dev.to/webdeveloperhyper/how-to-get-cheered-up-247-ai-avatar-v4-with-animation-editor-chrome-extension-vs-code-2f07)
- **v6** → [🦸スーパーヒーローに応援してもらおう (AI Avatar v6: Chrome拡張機能 + VS Code拡張機能)](https://dev.to/webdeveloperhyper/let-superheroes-cheer-you-up-ai-avatar-v6-chrome-extension-vs-code-extension-2ak7)

---

## 機能一覧

- 🎭 **リアクション** — Claude Code / GitHub Copilotが考え中または返答したとき自動でキャラクターが反応
- 🔀 **ウォッチャー切り替え** — Claude CodeとGitHub Copilotの監視を切り替え *(v2)*
- 🔄 **アバター変更** — 上部のボタンでVRMキャラクターをいつでも変更可能
- 💃 **アニメーション** — `.vrma`モーションクリップやカスタムJSONポーズを再生；3段階ボタン：オフ / デフォルト / カスタム *(v2)*
- 🎬 **アニメーションエディタ** — 複数キーフレームタイムライン（In / Hold / Outタイミング） *(v4)*；全30指ボーン対応 *(v5)*；度数表示 *(v5)*
- 🎥 **オービットコントロール** — ドラッグで回転、スクロールでズーム、右クリックでパン
- 👀 **視線追跡** — アイドル時に目と頭がマウスカーソルを追う
- 💬 **リップシンク** — Claudeの返答中に口が動く
- 😊 **クリックまたはEnterキーで反応** — スマイル、うなずき、アニメーションが発動
- 💬 **カスタム吹き出しメッセージ** — Messagesボタンからメッセージを編集（設定に保存）
- 😂 **ジョーク** — Jokesボタンでアバターがジョークを言う *(v2)*

---

## はじめ方

セットアップ不要 — サンプルキャラクターが最初から入っています。インストールしてVS Codeを開くだけです。

パネルを開くには、VS Codeのサイドバーにある **AI Avatarアイコン** をクリックしてください。

---

## 自分のVRMキャラクターを使う

**[VRoid](https://vroid.com/ja)** を使えば3Dモデリングの知識なしに無料でオリジナルアバターを作れます。キャラクターをデザインして `.vrm` ファイルとしてエクスポートしてください。

サイドバー上部の **Change Avatar** ボタンから `.vrm` ファイルを選択。

v6では新しいサンプルキャラクター（女の子3体・男の子2体）とポーズパック（かわいい・クール・おもしろ）を追加しました。
（[GitHubリリースから無料ダウンロード](https://github.com/webdeveloperhyper/ai-avatar/releases)）

---

## アニメーション *(v2)*

**Animation** ボタンで3つの状態を切り替えます：

| 状態 | ラベル | 動作 |
|---|---|---|
| オフ | `Animation`（暗い） | モーションクリップを再生しない |
| デフォルト | `Animation: Default` | 拡張機能付属のサンプルポーズを再生 |
| カスタム | `Animation: Custom` | フォルダを選択し `.vrma` と `.json` ポーズファイルを再生 |

選択した状態とカスタムフォルダは再起動後も保持されます。

**VRoid Projectの `.vrma` クリップを使う：**

VRMAアニメーションファイルはライセンスの都合上、拡張機能に含まれていません。公式VRoidプロジェクトから無料でダウンロードしてください：

👉 **[VRM Animation 7本パック by VRoid Project（無料）](https://booth.pm/ja/items/5512385)**

パックには7つのアニメーションが含まれます：全身表示、挨拶、ピースサイン、シュート、スピン、モデルポーズ、スクワット。

1. パックをダウンロードして解凍
2. **Animation** ボタンを `Animation: Custom` になるまでクリック
3. `.vrma` ファイルが入ったフォルダを選択
4. AIが返答するたびにランダムなクリップが再生

---

## アニメーションエディタ *(v4+)*

**Edit Animation** をクリックしてエディタを開きます：

- ドロップダウンから体のパーツを選択 — 全30指ボーン対応 *(v5)*
- **軸ボタン** でX / Y / Z回転を切り替え
- **スライダー** を動かす（または度数で値を入力）してボーンを回転 — 値は度数表示 *(v5)*
- **+** ボタンで複数キーフレームを追加してアニメーションシーケンスを作成 *(v4)*
- 各キーフレームにIn（フェードイン）、Hold、Out（フェードアウト、最終KFのみ）のタイミング設定 *(v4)*
- **< >** ボタンでキーフレームを移動 *(v4)*
- **Play** でアニメーション全体をプレビュー *(v4)*
- **Save** でアニメーションをJSONファイルとして保存
- **Reload** でSaveした最新の状態に戻す
- 保存したアニメーションはプールに追加され、ランダム再生

**Edit Animation** をクリックするとファイルピッカーが表示されます：
- **初回：** ファイルピッカーをキャンセルするとデフォルトアニメーションが開く
- **2回目以降：** 既存のJSONファイルを選択して読み込み・編集

---

## ウォッチャー *(v2)*

**Switch Watcher** ボタンで **Claude Code** と **GitHub Copilot** の監視を切り替えます。

設定の `vroidCompanion.activeWatcher` でデフォルトのウォッチャーを設定することもできます。

---

## 吹き出しメッセージ

**Messages** ボタンをクリックして、アバターが反応したときに吹き出しに表示するメッセージを編集できます。

- メッセージは `|`（パイプ）で区切って入力します。例：`頑張って！ | いいね！ | 完璧！`
- メッセージはVS Code設定に保存され、再起動後も保持されます
- `vroidCompanion.speechMessages` から直接編集することもできます

---

## Claude Code VS Code拡張機能と一緒に使う

両方のパネルを同時に並べて表示できます：

1. アクティビティバーのいずれかの拡張機能アイコンを右クリック
2. **Move to Secondary Side Bar** を選択

一方のパネルが左サイドバー、もう一方が右サイドバーに表示されます。

---

## 動作要件

- VS Code 1.85以上
- [Claude Code](https://claude.ai/code) CLIまたはVS Code拡張機能（自動反応に必要）

---

## ロードマップ

**v1** ✅
- VS CodeサイドバーにVRMキャラクター表示
- Claude Code活動へのライブ反応
- 視線追跡、リップシンク、オービットコントロール
- アバター変更、吹き出しメッセージ

**v2** ✅
- 3段階Animationボタン（オフ / デフォルト / カスタム）
- カスタムポーズエディタ（JSON保存・読み込み）
- Jokesボタン
- GitHub Copilotウォッチャー対応
- ウォッチャー切り替え（Claude ↔ Copilot）

**v3** ✅
- 🌐 Chrome拡張機能版
- 各種修正・調整

**v4** ✅
- ポーズエディタをフルアニメーションエディタにアップグレード
- In / Hold / Outタイミング付き複数キーフレームタイムライン
- 各種修正・調整

**v5** ✅
- ターミナルのEnterキーでアニメーションが発動（VS Code）
- リロードが最後に保存したポーズを正しく復元するよう修正
- アニメーションエディタに全30指ボーンを追加
- エディタの値を度数で表示・保存（既存ファイルとの後方互換性あり）
- BGトグルボタン追加 — グレー背景に切り替えて暗色アバターを見やすく
- UIの各種改善：ボタンスタイル、フォーカス枠、エディタの配色

**v6** ✅
- 新サンプルキャラクター：女の子3体・男の子2体（[GitHubリリースから無料ダウンロード](https://github.com/webdeveloperhyper/ai-avatar/releases)）
- 新ポーズパック：かわいい・クール・おもしろ（[GitHubリリースから無料ダウンロード](https://github.com/webdeveloperhyper/ai-avatar/releases)）

**v7** — 開発中！
- 🎉 お楽しみに
