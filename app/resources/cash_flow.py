from app.models import CashFlow as CashFlowModel
from shared.resource import Resource


class CashFlow(Resource):
    def get(self):
        uuid = self.event["queryStringParameters"].get("id")
        if uuid is None:
            return CashFlowModel.to_records()

    def put(*args, **kwargs):
        raise NotImplementedError()
