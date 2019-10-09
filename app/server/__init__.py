import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.server.resources.cash_flow import CashFlow
from app.server.resources.cash_flow_mapping import CashFlowMapping


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
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

    @app.route("/test")
    def test():
        return "Hi!"

    return app


app = create_app()
