from fastapi import FastAPI, Request
import httpx  # instead of boto3

app = FastAPI()

EXTERNAL_LLM_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

@app.post("/invoke")
async def invoke(request: Request):
    user_input = await request.json()
    prompt = user_input.get("text", "")

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(EXTERNAL_LLM_URL, json=payload, headers=HEADERS)

    return response.json()
