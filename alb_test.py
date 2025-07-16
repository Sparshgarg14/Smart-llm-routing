from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/test-alb")
def test_alb():
    url = "http://bedrock-alb-1638343709.eu-north-1.elb.amazonaws.com/invoke"
    payload = {"text": "What is AI?"}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        return {
            "status": response.status_code,
            "response": response.json()
        }
    except Exception as e:
        return {"error": str(e)}
