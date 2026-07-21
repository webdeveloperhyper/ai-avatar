"""
Kokoro TTS local server for AI Avatar VS Code / Chrome extension.

Install:
    pip install kokoro-onnx soundfile fastapi uvicorn

The "Kokoro Server" button in the extension starts/stops this server automatically.
Model files (~300 MB) are downloaded on first run.

If the button fails to start the server, run this script manually once:
    python scripts/kokoro_server.py
Wait for "Model loaded. Server ready" then try the button again.
"""

import io
import os
import sys
import urllib.request

try:
    import soundfile as sf
    from kokoro_onnx import Kokoro
    from fastapi import FastAPI, Request
    from fastapi.responses import Response, JSONResponse
    import uvicorn
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install kokoro-onnx soundfile fastapi uvicorn")
    sys.exit(1)

PORT = 8765

MODEL_DIR   = os.path.join(os.path.expanduser("~"), ".cache", "kokoro-onnx")
MODEL_PATH  = os.path.join(MODEL_DIR, "kokoro-v1.0.onnx")
VOICES_PATH = os.path.join(MODEL_DIR, "voices-v1.0.bin")

MODEL_URL  = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx"
VOICES_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"

def _download(url: str, dest: str) -> None:
    print(f"Downloading {os.path.basename(dest)}...")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    urllib.request.urlretrieve(url, dest)
    print(f"  -> saved to {dest}")

print("Kokoro TTS Server starting...")

try:
    if not os.path.exists(MODEL_PATH):
        _download(MODEL_URL, MODEL_PATH)
    if not os.path.exists(VOICES_PATH):
        _download(VOICES_URL, VOICES_PATH)
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)
    print("Model loaded. Server ready at http://127.0.0.1:8765")
except Exception as e:
    print(f"Failed to load model: {e}")
    sys.exit(1)

VOICE_MAP = {
    "female": "af_heart",
    "male":   "am_michael",
}

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tts")
async def tts(req: Request):
    body  = await req.json()
    text  = body.get("text", "").strip()
    voice = VOICE_MAP.get(body.get("voice", "female"), "af_heart")
    speed = float(body.get("speed", 1.0))
    if not text:
        return JSONResponse({"error": "empty text"}, status_code=400)
    try:
        samples, sample_rate = kokoro.create(text, voice=voice, speed=speed, lang="en-us")
        buf = io.BytesIO()
        sf.write(buf, samples, sample_rate, format="WAV")
        return Response(content=buf.getvalue(), media_type="audio/wav")
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT, log_level="warning")
