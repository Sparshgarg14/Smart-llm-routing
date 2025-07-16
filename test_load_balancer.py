import requests

url = "http://bedrock-alb-1638343709.eu-north-1.elb.amazonaws.com/invoke"
payload = {"text": "Explain quantum computing"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
