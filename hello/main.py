from lambda_decorators import cors_headers, json_http_resp


@cors_headers
@json_http_resp
def handler(event, context):
    return "hello world!"
