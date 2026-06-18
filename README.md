# SOLV Take-Home Task

## What this does

This small FastAPI application receives a customer message in JSON format and returns a reply based on the message content.

It handles:

* Pricing questions
* Opening hours questions
* Other messages using a fallback response

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to test the endpoint.

## Example Request

```json
{
  "from": "+255700000000",
  "name": "Asha",
  "message": "Hi, what are your prices?"
}
```

## Example Response

```json
{
  "recipient": "+255700000000",
  "reply": "Thank you for your interest. Our pricing starts from 75000tsh per month."
}
```

## My Approach

I used simple keyword matching to identify the type of customer request.

* Messages containing words like "price" or "pricing" return pricing information.
* Messages containing words like "hours" or "open" return business hours.
* If a message contains multiple keywords, the API returns combined responses in a single reply. 
* Any other message receives a fallback response offering human assistance.

For this task, keyword matching keeps the solution simple and easy to understand.

## Extending This for Real WhatsApp Webhooks

If this were part of a real WhatsApp automation platform like KIBO, I would:

* Verify webhook requests from WhatsApp.
* Store messages in a database.
* Process large numbers of messages asynchronously.
* Use NLP or AI-based intent detection instead of simple keyword matching.
* Add logging, monitoring, and error handling.
* Route complex conversations to a human support agent when needed.
