import logging
from app import LOG_LEVEL
from app.parse_expenses import parse_file, write_cash_flows_to_db
from app.resources import CashFlow, CashFlowMapping

log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)


cash_flow_handler = CashFlow.handler
cash_flow_mapping_handler = CashFlowMapping.handler


def process_new_file(event, context):
    for r in event["Records"]:
        log.info(str(r))
        df = parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
        log.info(f"received {len(df)} rows of data")
        log.info(df.head(3))
        write_cash_flows_to_db(df)
