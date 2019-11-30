from flask import Blueprint
from flask_restplus import Api, Resource, fields
from ..models.cash_flow import CashFlow as CashFlowModel
from ..models.cash_flow_mapping import CashFlowMapping as CashFlowMappingModel

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
    },
)


@api.route("/cash")
class CashFlow(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        t0 = CashFlowMappingModel.__table__.alias("t0")
        t1 = CashFlowMappingModel.__table__.alias("t1")
        return (
            CashFlowModel.query.outerjoin(
                t0, CashFlowModel.id == t0.columns.cash_flow_id
            )
            .outerjoin(t1, CashFlowModel.name == t1.columns.name)
            .all()
        )


ns = api.namespace("todos", description="TODO operations")

todo = api.model(
    "Todo",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "task": fields.String(required=True, description="The task details"),
    },
)


@api.route("/mapping")
class CashFlowMapping(Resource):
    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        print(id)
