from marshmallow import Schema, fields, pre_load, post_load

from app.models import CashFlowMapping as CashFlowMappingModel
from shared.resource import Resource


class PutCashFlowMapping(Schema):
    category = fields.String(required=True, allow_none=True)
    cashFlowId = fields.String(required=False, missing=None)
    name = fields.String(required=False, missing=None)
    source = fields.String(required=False, missing=None)

    @pre_load
    def pre(self, in_data, **kwargs):
        if not (
            in_data.get("cashFlowId") or (in_data.get("name") and in_data.get("source"))
        ):
            raise Exception("Need name or cashFlowId")

    @post_load
    def return_arguments(self, data, **kwargs):
        return tuple(data[key] for key in ("category, cashFlowId", "name"))


class CashFlowMapping(Resource):
    def get(self):
        mappings = CashFlowMappingModel.scan()
        res = {}
        for mapping in mappings:
            res[mapping.name or mapping.cash_flow_id] = mapping.category
        return res

    def put(self):
        category, cash_flow_id, name, source = PutCashFlowMapping().load(event["body"])
        if name:
            CashFlowMappingModel.delete_single_cash_flow_mapping(cash_flow_id)
            item_id = CashFlowMappingModel.register_mapping_for_all_cash_flows(
                name, category, source
            )
        else:
            item_id = CashFlowMappingModel.register_mapping_for_singl_cash_flow(
                cash_flow_id, category, source
            )

        return item_id
