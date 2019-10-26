from app.models import CashFlow as CashFlowModel
from shared.resource import Resource


class CashFlow(Resource):
    def get(self):
        uuid = self.event["queryStringParameters"].get("id")
        page = self.event["queryStringParameters"].get("page", 0)
        if uuid is None:
            records = CashFlowModel.to_records()
            return [{**o, "date": o["date"].isoformat()} for o in records][
                20 * page : 20 * (page + 1)
            ]

    def put(*args, **kwargs):
        raise NotImplementedError()
