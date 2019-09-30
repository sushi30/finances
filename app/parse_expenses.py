import logging
from app.models import FlowModel
from helpers import get_leumicard
from uuid import uuid4

log = logging.getLogger(__name__)


def parse_file(bucket, key):
    switcher = {"leumicard": get_leumicard}
    return switcher[key.split("/")[0]](f"s3://{bucket}/{key}")


def handler(event, context):
    for r in event["Records"]:
        log.info(str(r))
        df = parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
        log.info(f"received {len(df)} rows of data")
        log.info(df.head(3))
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
                batch.save(item)
