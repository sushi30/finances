import json
import os
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
    APP_NAME=os.environ.get("APP_NAME") or "Flask-Base",
    FLASK_ENV=os.getenv("FLASK_ENV"),
)


@app.route("/test")
def test():
    return json.dumps("hello"), 200, {"Content-Type": "application/json"}
