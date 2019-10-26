from lambda_decorators import cors_headers, load_json_body, json_http_resp
from app.resources import cash_flow, cash_flow_mapping


def decorators(func):
    return cors_headers()(load_json_body((json_http_resp(func))))


class Resource:
    def __init__(self, event, context):
        self.event = event
        self.context = context

    @classmethod
    def handler(cls, event, context):
        method = event["httpMethod"].lower()
        return cls(event, context).__getattribute__(method)()


class CashFlow(Resource):
    def get(self):
        uuid = self.event["queryStringParameters"].get("id")
        return cash_flow.get(uuid)


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
