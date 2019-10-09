from flask import request
from flask_restful import Resource
from app.models import CashFlowMapping as CashFlowMappingModel


class CashFlowMapping(Resource):
    def get(self, uuid=None):
        mappings = CashFlowMappingModel.scan()
        res = {}
        for mapping in mappings:
            res[mapping.name or mapping.cash_flow_id] = mapping.category
        return res

    def put(self):
        body = request.json
        category = body["category"]
        cash_flow_id = body.get("id")
        name = body.get("name")
        if name:
            CashFlowMappingModel.delete_single_cash_flow_mapping(cash_flow_id)
            item_id = CashFlowMappingModel.register_mapping_for_all_cash_flows(
                name, category, body["source"]
            )
        else:
            item_id = CashFlowMappingModel.register_mapping_for_singl_cash_flow(
                cash_flow_id, category, body["source"]
            )

        return item_id
