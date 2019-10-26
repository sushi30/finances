from app.models import CashFlow as CashFlowModel
from shared.resource import Resource
from marshmallow import Schema, fields, post_load


class GetCashFlowSchema(Schema):
    id = fields.String(missing=None)
    page = fields.Integer(missing=0)
    size = fields.Integer(missing=10)

    @post_load
    def return_args(self, data, **kwargs):
        return tuple(data[key] for key in ("id", "page", "size"))


class CashFlow(Resource):
    def get(self):
        uuid, page, key, page_size = GetCashFlowSchema().load(
            self.event["queryStringParameters"]
        )
        if uuid is None:
            records = CashFlowModel.to_records()
            return [{**o, "date": o["date"].isoformat()} for o in records][
                page * page_size : page * (page_size + 1)
            ]
        else:
            item = next(CashFlowModel.query(hash_key=uuid)).attribute_values
            return {**item, "date": item["date"].isoformat()}

    def put(*args, **kwargs):
        raise NotImplementedError()
