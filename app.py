from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="SOLV Entry-Level Developer Take-Home",
    description="Simple message routing webhook",
    version="1.0.0"
)


class CustomerMessage(BaseModel):
    sender: str = Field(alias="from")
    name: str
    message: str

    class Config:
        populate_by_name = True


def route_message(message: str) -> str:
    """
    Route a response based on message keywords.
    Simple multi-intent handler.
    """

    message = message.lower()

    replies = []

    # Pricing intent
    if any(k in message for k in ["price", "prices", "cost", "pricing"]):
        replies.append(
            "Thank you for your interest. Our pricing starts from 75000 TSH per month."
        )

    # Opening hours intent
    if any(k in message for k in ["hours", "opening", "open"]):
        replies.append(
            "Our business hours are Monday to Friday, 8:00 AM to 5:00 PM."
        )

    # Default fallback
    if not replies:
        return (
            "Thank you for contacting us. "
            "I can connect you with a human agent for further assistance."
        )

    return " ".join(replies)


@app.post("/webhook")
def receive_message(payload: CustomerMessage):
    reply = route_message(payload.message)

    return {
        "recipient": payload.sender,
        "reply": reply
    }


@app.get("/")
def home():
    return {
        "message": "SOLV Take-Home API Running"
    }