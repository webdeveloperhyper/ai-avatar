# Privacy Policy — AI Avatar VS Code Extension

Last updated: 2026-09-29

## Data Collection

AI Avatar does not collect, store, transmit, or share personal data or user
information with the extension developer.

## What the Extension Does

- Detects Claude Code, Codex, and GitHub Copilot activity to trigger local avatar
  animations. Claude/Codex monitoring reads local session files and can include
  other local projects, not just the open workspace.
- Stores avatar preferences, custom prompts, and model selections in VS Code and
  webview storage. Custom model and animation files remain in local storage or
  locations you select. Sync or backups may copy stored data.
- The Pose Capture tool optionally accesses your camera to capture body poses
  and export animation files. Camera frames are processed locally, not uploaded
  or recorded as video. Close the capture page to end camera use.

## Third-Party Services

Certain optional features may make network connections depending on your configuration:

- **Hugging Face CDN** — Local Text-to-Speech downloads Kokoro voice models on
  first use and caches them locally. Speech synthesis runs locally after setup;
  resources may be downloaded again if needed.
- **VOICEVOX** — Japanese Local TTS connects to a VOICEVOX server running on
  localhost:50021 for speech synthesis. This connection is local. When the service
  and model run on your device without cloud forwarding, the text stays on your device.
- **Kokoro Server** — connects to a Kokoro server on localhost for faster local
  speech synthesis. This connection is local. When the service and model run on
  your device without cloud forwarding, the text stays on your device.
- **Piper** — downloads a native speech engine from GitHub and voice models from
  Hugging Face when needed, then synthesizes speech locally. Speech text is
  processed on your device and is not sent to the download hosts.
- **Google Gemini API** — if you enter a Gemini API key and use AI Chat, AI Speech
  Bubble, or Speech: AI, relevant messages, recent chat history, prompts, and
  speech text are sent to Google. Speech-bubble prompts may include a short
  excerpt of a Claude request. The key is stored in VS Code SecretStorage and
  sent to Google for authentication, never to the extension developer.
  Note: if you use the free tier of the Gemini API, Google may use your input and output
  data to improve their models. Please check Google's latest "Generative AI Use Policy" on
  their official website for details.
- **Ollama** — sends chat or speech-bubble prompts to your local Ollama service.
  This connection is local. When the service and model run on your device without
  cloud forwarding, the text stays on your device.
- **Jev (TypeSafe)** — Off by default. When enabled, sends new user messages from
  local Claude/Codex projects, sentiment instructions, and configured word examples
  to TypeSafe for avatar reactions. The separate, optional Dev Log recording control
  sends new user messages with category instructions to TypeSafe to classify requests.
  Dev Log saves timestamps, tool names and categories locally, not message text.
  Both features start Off after restart; when both are enabled, they share one request.
  AI replies are not sent. The key is stored in VS Code SecretStorage and sent
  to TypeSafe for authentication. See the privacy terms applicable to your
  TypeSafe account on their official website.

Pose Capture may download resources from jsDelivr. Browser/OS speech voices may
use an external service. External services may receive standard connection
information and handle it under their own privacy policies. Separately configured
services or remote environments may handle data differently.

## Contact

If you have questions, please open an issue at
[GitHub](https://github.com/webdeveloperhyper/ai-avatar/issues).
Issues are public—do not post API keys or private conversations.
