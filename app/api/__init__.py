from flask import Blueprint
from flask_restplus import Api, Resource, fields
from .. import db
from ..models.cash_flow import CashFlow as CashFlowModel
from ..models.cash_flow_mapping import GeneralCashFlowMapping

blueprint = Blueprint("api", __name__)

api = Api(blueprint)


@blueprint.route("/")
def version():
    return "api!"


model = api.model(
    "Model",
    {
        "id": fields.String,
        "value": fields.Integer,
        "date": fields.DateTime,
        "name": fields.String,
        "category": fields.String,
        "source": fields.String,
    },
)


@api.route("/cash")
class CashFlow(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return db.engine.execute(
            "select * from cash_flow left join general_cash_flow_mapping using(name)"
        ).fetchall()


ns = api.namespace("todos", description="TODO operations")

todo = api.model(
    "Todo",
    {
        "name": fields.String(),
        "id": fields.String(),
        "category": fields.String(required=True),
        "source": fields.String(required=True),
    },
)


@api.route("/mapping")
class CashFlowMapping(Resource):
    @ns.expect(todo, validate=True)
    def put(self):
        params = api.payload
        if params.get("name"):
            db.session.add(GeneralCashFlowMapping(**api.payload))
            db.session.commit()
        elif params.get("id"):
            raise NotImplementedError()
        else:
            raise Exception("Specify id or name")
        return None, 201

    @ns.expect(todo, validate=True)
    def delete(self):
        body = api.payload
        if body.get("name"):
            mapping = GeneralCashFlowMapping.query.filter(
                GeneralCashFlowMapping.name == body["name"],
                GeneralCashFlowMapping.source == body["source"],
                GeneralCashFlowMapping.category == body["category"],
            ).first()
            db.session.delete(mapping)
            db.session.commit()
        elif body.get("id"):
            raise NotImplementedError()
        else:
            raise Exception("Specify id or name")
        return None, 202
