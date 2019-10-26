from app.models import CashFlowMapping as CashFlowMappingModel
from shared.resource import Resource


class CashFlowMapping(Resource):
    def get(self):
        mappings = CashFlowMappingModel.scan()
        res = {}
        for mapping in mappings:
            res[mapping.name or mapping.cash_flow_id] = mapping.category
        return res

    def put(self):
        category, cash_flow_id, name, source = (
            self.event["body"].get(k)
            for k in ("category", "cashFlowId", "name", "source")
        )
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
