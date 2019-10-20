from lambda_decorators import cors_headers, json_http_resp, load_json_body

from auth.authorize import auth


def authorize(event, context):
    return auth(event, context)


@cors_headers
@load_json_body
def login(event, context):
    if event["body"]["username"] == "demo" and event["body"]["password"] == "1234":
        return {"statusCode": 200, "body": json.dumps({"token": "123454321"})}
    else:
        return {"statusCode": 403}
