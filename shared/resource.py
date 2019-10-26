import json
import logging
import traceback

from shared import LOG_LEVEL

log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)

HEADERS = {"Access-Control-Allow-Origin": "*"}


class Resource:
    def __init__(self, event, context):
        event["body"] = json.loads(event.get("body") or "{}")
        event["queryStringParameters"] = event["queryStringParameters"] or {}
        self.event = event
        self.context = context

    @classmethod
    def handler(cls, event, context):
        log.debug("received event: " + str(event))
        http_method = event["httpMethod"].lower()
        try:
            res = cls(event, context).__getattribute__(http_method)()
            response = {"statusCode": 200, "body": json.dumps(res), **HEADERS}
            log.debug("response: " + str(response))
            return response
        except Exception as exception:
            traceback.print_exc()
            return {"statusCode": 500, "body": str(exception), **HEADERS}
