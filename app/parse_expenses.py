def parse_file(bucket, key):
    switcher = {"leumicard": id}
    default = id
    res = switcher.get(key.split("/")[0], default)(f"s3://{bucket}/{key}")
    print(res)



def handler(event, context):
    for r in event["Records"]:
        parse_file(r["s3"]["bucket"]["name"], r["s3"]["object"]["key"])
