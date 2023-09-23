"""Lambda function."""
import json


# pylint: disable-next=unused-argument
def handler(event, context):
    """Lambda function."""
    print(f"request: {json.dumps(event)}")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": f"Hello, CDK! You have hit {event['path']}\n",
    }
