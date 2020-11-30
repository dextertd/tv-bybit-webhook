import json


def lambda_handler(event, context):
    """

    :param event: event data
    :param context: runtime info
    :return: always 200 (otherwise TV will keep trying to invoke webhook)
    """
    if "body" in event:
        # is request from TV
        body = event["body"]
    else:
        # is request from AWS receiver lambda
        body = event

    if type(body) != dict:
        body = json.loads(body)

    # do something; make orders, update existing orders, profit!

    return {
        "statusCode": 200,
        "body": json.dumps("OK")
    }
