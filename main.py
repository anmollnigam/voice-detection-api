from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ----- Request format -----
class Message(BaseModel):
    sender: str
    text: str
    timestamp: int

class RequestBody(BaseModel):
    sessionId: str
    message: Message


# ----- Root check -----
@app.get("/")
def root():
    return {"status": "API is running"}


# ----- Scam detection endpoint -----
@app.post("/detect-scam")
def detect_scam(data: RequestBody):

    text = data.message.text.lower()

    scam_keywords = [
        "blocked", "suspended", "verify",
        "urgent", "account", "bank",
        "click", "link", "otp"
    ]

    is_scam = any(word in text for word in scam_keywords)

    if is_scam:
        reply = "This message looks suspicious. Please do not share any personal information."
    else:
        reply = "This message does not appear to be a scam."

    return {
        "status": "success",
        "reply": reply
    }
