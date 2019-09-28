import logging

log = logging.getLogger(__name__)


def parse_file(bucket, key):
    switcher = {"leumicard": lambda x: x}
    default = lambda x: x
    res = switcher.get(key.split("/")[0], default)(f"s3://{bucket}/{key}")
    print(res)


def handler(event, context):
    for r in event["Records"]:
        log.info(str(r))
        parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
