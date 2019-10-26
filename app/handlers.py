import logging
from lambda_decorators import cors_headers, load_json_body, json_http_resp
from app import LOG_LEVEL
from app.parse_expenses import write_cash_flows_to_db, parse_file
from app.resources import cash_flow, cash_flow_mapping
from shared.resource import Resource

log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)


def decorators(func):
    return cors_headers()(load_json_body((json_http_resp(func))))


class CashFlow(Resource):
    def get(self):
        uuid = self.event["queryStringParameters"].get("id")
        return cash_flow.get(uuid)


cash_flow = CashFlow.handler


@decorators
def get_cash_flow_mapping(event, context):
    uuid = event["queryParameters"].get("id")
    return cash_flow_mapping.get(uuid)


@decorators
def put_cash_flow_mapping(event, context):
    category, cash_flow_id, name, source = (
        event["body"].get(k) for k in ("category", "cashFlowId", "name", "source")
    )
    return cash_flow_mapping.put(category, cash_flow_id, name, source)


def process_new_file(event, context):
    for r in event["Records"]:
        log.info(str(r))
        df = parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
        log.info(f"received {len(df)} rows of data")
        log.info(df.head(3))
        write_cash_flows_to_db(df)
