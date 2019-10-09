from flask_restful import Resource
from app.models import CashFlow as CashFlowModel


class CashFlow(Resource):
    def get(self, uuid=None):
        if uuid is None:
            return CashFlowModel.dumps()

    def put(self, todo_id):
        raise
