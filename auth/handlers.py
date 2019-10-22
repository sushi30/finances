from lambda_decorators import cors_headers, load_json_body, dump_json_body
from auth.authorize import auth, generate_policy
from auth.login import login as login_inner


def authorize(event, context):
    token = event.get("authorizationToken")
    if not token:
        raise Exception("Unauthorized")
    user = auth(token)
    return generate_policy(user, "Allow", event["methodArn"])


@cors_headers
@load_json_body
@dump_json_body
def login(event, context):
    username = event["body"]["username"]
    password = event["body"]["password"]
    try:
        return {"statusCode": 200, "body": {"token": login_inner(username, password)}}
    except:
        return {"statusCode": 403}
