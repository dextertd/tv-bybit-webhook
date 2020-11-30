import json
import boto3
import os

# AWS configuration for invoking other lambdas
client = boto3.client("lambda")
bot_arn = os.environ["arn"]


# is passed to main.py
accounts = [
    {
        "user": "Bob",
        "api_key": "sI1gpj3015dcvhfLyL",
        "api_secret": "tozSsvgTCHFFp6XOm32RE8joSop2fBAIoe2S",
        "net": "https://api-testnet.bybit.com"
        # and some other options, such as leverage, SL/TP/TS info, etc
    },
    {
        "user": "Alice",
        "api_key": "dyLsjvh51fp3I0L",
        "api_secret": "Fp68AeoXHvgTCoztom32FOfBSSsSp2oRjE",
        "net": "https://api-testnet.bybit.com"
    },
]


def lambda_handler(event, context):
    """

    :param event: event data
    :param context: runtime info
    :return: always 200 (otherwise TV will keep trying to invoke webhook)
    """
    body = event["body"]
    if type(body) != dict:
        body = json.loads(body)

    # invoke lambda function for each account which should act on TV signal
    for account in accounts:
        body["account"] = account
        r = client.invoke(
            FunctionName=bot_arn,
            InvocationType="Event",  # async
            Payload=json.dumps(body),
        )

    return {
        "statusCode": 200,
        "body": json.dumps("OK")
    }
