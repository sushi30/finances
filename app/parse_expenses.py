import json
import logging
import os
import boto3
import pandas as pd
from app.models import CashFlow
from helpers import get_leumicard
from uuid import uuid4

log = logging.getLogger(__name__)


def parse_file(bucket, key):
    switcher = {"leumicard": get_leumicard}
    return switcher[key.split("/")[0]](f"s3://{bucket}/{key}")


def write_cash_flows_to_db(cash_flows: pd.DataFrame):
    with CashFlow.batch_write() as batch:
        for item in cash_flows.apply(
            lambda x: CashFlow(
                str(uuid4()),
                date=x.date.to_pydatetime(),
                name=x["name"],
                source=x.source,
                details=x.details,
                value=x.value,
            ),
            axis=1,
        ).tolist():
            batch.save(item)


def process_file(bucket, key):
    queue = boto3.resource("sqs").Queue(os.getenv("QUEUE_URL"))
    df = parse_file(bucket, key)
    log.info(f"received {len(df)} rows of data")
    log.info(df.head(3))
    ids = []
    with FlowModel.batch_write() as batch:
        for item in df.apply(
            lambda x: FlowModel(
                str(uuid4()),
                date=x.date.to_pydatetime(),
                name=x["name"],
                source=x.source,
                details=x.details,
                value=x.value,
            ),
            axis=1,
        ).tolist():
            ids.append(item.id)
            batch.save(item)
    queue.send_message(MessageBody=json.dumps(ids))
