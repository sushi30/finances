def parse_file(bucket, key):
    switcher = {"leumicard": id}
    default = id
    switcher.get(key.split("/")[0], default)(f"s3://{bucket}/{key}")


def handler(event, context):
    for r in event["Records"]:
        parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
