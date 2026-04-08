# AI Avatar

A VRM 3D character in your VS Code sidebar that reacts to Claude Code / GitHub Copilot AI activity. Animations and speech bubbles all run without AI too.

![idle](https://img.shields.io/badge/state-idle-blue)  ![happy](https://img.shields.io/badge/state-happy-green)

🛒 **[Download from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=web-developer-hyper.ai-avatar)**

🛒 **[Download from Chrome Web Store](https://chromewebstore.google.com/detail/ai-avatar/afmcfaeaaojalninahhhjnonhmlmiidi)**

📖 Read the story behind this project on DEV.to:
- **v1** → [AI Avatar (VS Code Extension)](https://dev.to/webdeveloperhyper/ai-avatar-meet-your-ideal-girlfriendboyfriend-for-free-21n5)
- **v2** → [AI Avatar v2 with Pose Editor (VS Code Extension)](https://dev.to/webdeveloperhyper/ai-avatar-v2-with-pose-editor-vs-code-extension-38n2)
- **v4** → [😊How to Get Cheered Up 24/7 (AI Avatar v4 with Animation Editor (Chrome Extension + VS Code Extension))](https://dev.to/webdeveloperhyper/how-to-get-cheered-up-247-ai-avatar-v4-with-animation-editor-chrome-extension-vs-code-2f07) 

---

## Features

- 🎭 **Live reactions** — character automatically reacts when Claude Code / GitHub Copilot is thinking or responds
- 🔀 **Watcher switching** — switch between watching Claude Code or GitHub Copilot *(v2)*
- 🔄 **Change Avatar** — swap your VRM character anytime with the button at the top
- 💃 **Animations** — play `.vrma` motion clips or custom JSON poses; 3-state button: off / Default / Custom *(v2)*
- 🎬 **Animation Editor** — create multi-keyframe animations with in / hold / out timing *(v4)*
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

**Option 1 — Button in the panel:**
Click the **Change Avatar** button at the top of the sidebar to pick a `.vrm` file.

**Option 2 — Settings:**
1. Open VS Code settings (`Ctrl+,`)
2. Search `vroidCompanion.vrmFilePath`
3. Set the absolute path to your `.vrm` file

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

## Animation Editor *(v4)*

Click **Edit Animation** to open the animation editor overlay:

- Select a body part from the dropdown
- Use the **axis button** to switch between X / Y / Z rotation
- Drag the **slider** (or type a value) to rotate the bone
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

## Settings

| Setting | Description | Default |
|---|---|---|
| `vroidCompanion.vrmFilePath` | Absolute path to your `.vrm` file | bundled sample |
| `vroidCompanion.activeWatcher` | Which AI to watch: `claude` or `copilot` | `claude` |
| `vroidCompanion.speechMessages` | Messages shown in the speech bubble | `["You can do it!", "Nice work!", "Love that fix!"]` |
| `vroidCompanion.thinkingTimeoutMs` | Milliseconds before thinking state auto-reverts to idle | `30000` |
| `vroidCompanion.copilotWatcherDebug` | Enable verbose debug logging for the Copilot watcher | `false` |

---

## Commands

Open Command Palette (`Ctrl+Shift+P`):

| Command | Description |
|---|---|
| `AI Avatar: Set Happy State` | Character looks happy |
| `AI Avatar: Set Idle State` | Return to idle |
| `AI Avatar: Set State (Quick Pick)` | Pick from a menu |

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

**v5** — coming soon
- 🎉 More fun updates
