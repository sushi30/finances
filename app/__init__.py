import os

from flask import Flask

if os.getenv("ENV") == "LOCAL":
    from dotenv import load_dotenv

    load_dotenv()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev", APP_NAME=os.environ.get("APP_NAME") or "Flask-Base"
    )

    @app.route("/test")
    def test():
        return "hi"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
