import json
import os
from datetime import datetime

import jwt

from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

# Set by serverless.yml
from auth import PRIVATE_KEY

AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_PUBLIC_KEY = os.getenv("AUTH0_CLIENT_PUBLIC_KEY")


def auth(token):
    return jwt_verify(token)


def jwt_verify(auth_token):
    payload = jwt.decode(auth_token, PRIVATE_KEY, algorithms=["HS256"])
    if payload["exp"] < datetime.utcnow().timestamp():
        raise Exception("expired token")
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


def convert_certificate_to_pem(public_key):
    cert_str = public_key.encode()
    cert_obj = load_pem_x509_certificate(cert_str, default_backend())
    pub_key = cert_obj.public_key()
    return pub_key
