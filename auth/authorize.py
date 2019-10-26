import os
import jwt
from auth import PRIVATE_KEY
from util import get_secret


def auth(token):
    if token == get_secret(os.environ["MASTER_SECRET"])["key"]:
        return "admin"
    return jwt_verify(token)


def jwt_verify(auth_token):
    payload = jwt.decode(auth_token, PRIVATE_KEY, algorithms=["HS256"])
    return payload["sub"]


def generate_policy(principal_id, effect, resource):
    return {
        "principalId": principal_id,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {"Action": "execute-api:Invoke", "Effect": effect, "Resource": resource}
            ],
        },
    }
