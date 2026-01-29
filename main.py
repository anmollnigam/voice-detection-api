from fastapi import FastAPI
from pydantic import BaseModel
import base64
import uuid

app = FastAPI()

class AudioRequest(BaseModel):
    audio_base64: str
    language: str = "en"

@app.post("/detect-voice")
def detect_voice(data: AudioRequest):
    try:
        # Decode base64 audio
        audio_bytes = base64.b64decode(data.audio_base64)

        # Save audio temporarily
        filename = f"audio_{uuid.uuid4()}.mp3"
        with open(filename, "wb") as f:
            f.write(audio_bytes)

        # Dummy classification logic (to be replaced with actual model inference)
        file_size_kb = len(audio_bytes) / 1024

        if file_size_kb < 100:
            classification = "AI-generated"
            confidence = 0.82
            explanation = "Audio has uniform structure and very low variation, commonly seen in synthetic voices."
        else:
            classification = "Human-generated"
            confidence = 0.76
            explanation = "Audio contains natural variations and background inconsistencies typical of human speech."

        return {
            "classification": classification,
            "confidence_score": confidence,
            "explanation": explanation
        }

    except Exception as e:
        return {
            "error": str(e)
        }