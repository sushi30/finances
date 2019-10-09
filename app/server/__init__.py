import os
from flask import request
from flask_lambda import FlaskLambda as Flask
from flask_cors import CORS
from flask_restful import Api
from app.server.resources.cash_flow import CashFlow
from app.server.resources.cash_flow_mapping import CashFlowMapping


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        APP_NAME=os.environ.get("APP_NAME") or "Flask-Base",
        FLASK_ENV=os.getenv("FLASK_ENV"),
    )
    CORS(app)
    api = Api(app)
    api.add_resource(CashFlowMapping, "/mapping/<string:uuid>", "/mapping")
    api.add_resource(CashFlow, "/flow/<string:uuid>", "/flow")
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/test", methods=["GET", "POST"])
    def test():
        if request.method == "GET":
            return "Hi!"
        elif request.method == "POST":
            return request.json

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
