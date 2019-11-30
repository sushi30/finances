from datetime import datetime


def date_json_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()
