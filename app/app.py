import os
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)
app.config.from_mapping(
    SECRET_KEY="dev", APP_NAME=os.environ.get("APP_NAME") or "Flask-Base"
)


@app.route("/test")
def test():
    return "hi"
