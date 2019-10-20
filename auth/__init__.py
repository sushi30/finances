import json
from lambda_decorators import json_http_resp, load_json_body, cors_headers


@cors_headers
@load_json_body
@json_http_resp
def sign_in(event, context):
    body = event["body"]
    if body["user"] == "demo" and body["password"] == "1234":
        return {
            "statusCode": 200,
            "body": json.dumps({"token": "wX2gJc86hqrFYtGM4r8p"}),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
        }
    else:
        return {"statusCode": 403}


def authorize(event, context):
    event["headers"]["acces_token"] = "wX2gJc86hqrFYtGM4r8p"
