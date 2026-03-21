# AI Avatar

A VRM 3D character in your VS Code sidebar that reacts to Claude Code AI activity. Animations and speech bubbles all run without Claude Code too.

![idle](https://img.shields.io/badge/state-idle-blue)  ![happy](https://img.shields.io/badge/state-happy-green)

🛒 **[Download from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=web-developer-hyper.ai-avatar)**

---

## Features

- 🎭 **Live reactions** — character automatically reacts when Claude Code is thinking or responds
- 💬 **Lipsync** — mouth animates while Claude is replying
- 👀 **Eye tracking** — eyes and head follow your mouse cursor when idle
- 😊 **Click or press Enter to interact** — triggers a smile, nod, and animation (if ON)
- 🎥 **OrbitControls** — drag to rotate, scroll to zoom, right-click to pan
- 🔄 **Change Avatar** — swap your VRM character anytime with the button at the top
- 💃 **VRMA Animations** — play `.vrma` motion clips when Claude finishes responding (toggle ON/OFF)
- 💬 **Custom speech messages** — edit the speech bubble messages via the Messages button (saved to settings)

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

## VRMA Animations

The **Animation** button lets your avatar play `.vrma` motion clips when Claude finishes responding.

Animation files are **not included** in the extension because they cannot be redistributed under their license terms. Download them yourself for free from the official VRoid Project:

👉 **[VRM Animation 7-Pack by VRoid Project (free)](https://booth.pm/en/items/5512385)**

The pack includes 7 animations: Show full body, Greeting, Peace sign, Shoot, Spin, Model pose, and Squat.

**How to set up:**
1. Download and unzip the pack
2. Click the **Animation** button in the sidebar — it opens a file picker on first click
3. Select the `.vrma` files you want to use
4. The button turns bright (ON) and a random clip plays each time Claude responds

When Animation is **ON** the button appears bright; when **OFF** it appears dim.

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
| `vroidCompanion.animationFolderPath` | Folder containing `.vrma` animation files | none |
| `vroidCompanion.speechMessages` | Messages shown in the speech bubble | `["You can do it!", "Nice work!", "Love that fix!"]` |
| `vroidCompanion.thinkingTimeoutMs` | Milliseconds before thinking state auto-reverts to idle | `30000` |

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

**v2 is now in progress!**
