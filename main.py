from fastapi import FastAPI, Request
import boto3
import json

app = FastAPI()
client = boto3.client("bedrock-runtime", region_name="eu-north-1")


# Health check GET route
@app.get("/invoke")
async def health_check():
    return {"status": "healthy"}

@app.post("/invoke")
async def embed(request: Request):
    data = await request.json()
    text = data.get("text", "")

    response = client.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        body=json.dumps({"inputText": text}),
        contentType="application/json",
        accept="application/json"
    )

    result = response["body"].read().decode()
    return json.loads(result)
