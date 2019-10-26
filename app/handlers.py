import json
import logging

from lambda_decorators import cors_headers, load_json_body, json_http_resp

from app import LOG_LEVEL
from app.resources import cash_flow, cash_flow_mapping

log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)


def decorators(func):
    return cors_headers()(load_json_body((json_http_resp(func))))


class Resource:
    def __init__(self, event, context):
        event["body"] = json.loads(event.get("body", "{}"))
        self.event = event
        self.context = context

    @classmethod
    def handler(cls, event, context):
        log.debug("received event: " + json.dumps(event))
        http_method = event["httpMethod"].lower()
        try:
            res = cls(event, context).__getattribute__(http_method)()
            response = {"statusCode": 200, "body": json.dumps(res)}
        except Exception as exception:
            response = {"statusCode": 500, "body": str(exception)}
        response["headers"] = {"Access-Control-Allow-Origin": "*"}
        log.debug("response: " + str(response))
        return response


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


def process_expenses_files(event, context):
    for r in event["Records"]:
        process_file()
        log.info(str(r))
        df = parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
        log.info(f"received {len(df)} rows of data")
        log.info(df.head(3))
        write_cash_flows_to_db(df)
