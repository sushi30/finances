from datetime import timedelta, datetime
import jwt
from auth import PRIVATE_KEY


def login(username, password):
    if username == "demo" and password == "1234":
        issued_at = datetime.utcnow()
        expires_at = issued_at + timedelta(days=0.5)
        token = jwt.encode(
            {"sub": "demo", "iat": issued_at, "exp": expires_at},
            PRIVATE_KEY,
            algorithm="HS256",
        )
        return token
    else:
        raise Exception("forbidden")
