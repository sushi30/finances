from app.models import CashFlow as CashFlowModel
from shared.resource import Resource


class CashFlow(Resource):
    def get(self):
        uuid = self.event["queryStringParameters"].get("id")
        page = self.event["queryStringParameters"].get("page", 0)
        page_size = self.event["queryStringParameters"].get("size", 1)
        if uuid is None:
            records = CashFlowModel.to_records()
            return [{**o, "date": o["date"].isoformat()} for o in records][
                page * page_size : page * (page_size + 1)
            ]
        else:
            item = next(CashFlowModel.query(hash_key=uuid)).attribute_values
            return {**o, "date": o["date"].isoformat(), **item}

    def put(*args, **kwargs):
        raise NotImplementedError()
