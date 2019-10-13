import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
    APP_NAME=os.environ.get("APP_NAME") or "Flask-Base",
    FLASK_ENV=os.getenv("FLASK_ENV"),
    DEBUG=os.getenv("DEBUG"),
)
CORS(app)


@app.route("/test")
def test():
    return "hi"
