import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='eu-north-1')  # Use your region

response = bedrock.invoke_model(
    modelId='amazon.titan-embed-text-v2:0',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        "inputText": "What is semantic search?"
    })
)

# Read response body
result = response['body'].read().decode()
print(json.loads(result))
