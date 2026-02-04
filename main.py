from fastapi import FastAPI, Header
from pydantic import BaseModel
import requests
import uuid

app = FastAPI()

class AudioRequest(BaseModel):
    audio_url: str
    language: str = "en"

@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/detect-voice")
def detect_voice(
    data: AudioRequest,
    
):
    
    try:
        # Download audio from URL
        response = requests.get(data.audio_url, timeout=15)
        audio_bytes = response.content

        filename = f"audio_{uuid.uuid4()}.mp3"
        with open(filename, "wb") as f:
            f.write(audio_bytes)

        file_size_kb = len(audio_bytes) / 1024

        if file_size_kb < 20:
            classification = "AI-generated"
            confidence = 0.82
        else:
            classification = "Human"
            confidence = 0.76

        return {
           "status":"success",
            "reply":"Voice processed successfully"
        }

    except Exception as e:
        return {"error": str(e)}

