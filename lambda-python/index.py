import json
import os

import boto3
from botocore.exceptions import ClientError


def handler(event, context):
    auth_token = os.getenv("AUTH_TOKEN")

    authorization_header = event["headers"].get("Authorization") or event[
        "headers"
    ].get("authorization")

    if not authorization_header or authorization_header != f"Bearer {auth_token}":
        print("Unauthorized request")
        return {
            "statusCode": 403,
            "body": json.dumps({"error": "Forbidden"}),
        }

    try:
        parsed_body = json.loads(event["body"])

        prompt = parsed_body.get("prompt")

        client = boto3.client("bedrock-agent-runtime")

        retrieve_and_generate_command = {
            "input": {"text": prompt},
            "retrieveAndGenerateConfiguration": {
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": os.getenv("KNOWLEDGE_BASE_ID"),
                    "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0",
                },
            },
        }

        response = client.retrieve_and_generate(**retrieve_and_generate_command)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"text": response.get("output", {}).get("text", "no response")}
            ),
        }
    except ClientError as error:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(error)}),
        }
