from lambda_decorators import json_http_resp, cors_headers

@cors_headers
@json_http_resp
def put(event, context):
    return "success"


@cors_headers
@json_http_resp
def get(event, context):
    return "hello11"
