import os
from flask import request
from flask_cors import CORS
from flask_lambda import FlaskLambda
from flask_restful import Api
from app.server.resources.cash_flow import CashFlow
from app.server.resources.cash_flow_mapping import CashFlowMapping

app = FlaskLambda(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY="dev")
CORS(app)
api = Api(app)
api.add_resource(CashFlowMapping, "/mapping/<string:uuid>", "/mapping")
api.add_resource(CashFlow, "/flow/<string:uuid>", "/flow")
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


if __name__ == "__main__":
    app.run()
