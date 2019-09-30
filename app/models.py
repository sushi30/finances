from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
import os


class FlowModel(Model):
    class Meta:
        table_name = os.getenv("EXPENSES_TABLE_NAME")
        region = "us-west-2"

    id = UnicodeAttribute(hash_key=True)
    date = UTCDateTimeAttribute()
    name = UnicodeAttribute()
    value = NumberAttribute()
    details = UnicodeAttribute(null=True)
    source = UnicodeAttribute()
