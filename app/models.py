import os
from uuid import uuid4
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class MyModel(Model):
    @classmethod
    def create(cls):
        return cls.create_table(
            read_capacity_units=1, write_capacity_units=1, wait=True
        )

    @classmethod
    def to_records(cls):
        return [i.attribute_values for i in list(cls.scan())]


class CashFlow(MyModel):
    class Meta:
        table_name = os.getenv("CASH_FLOW_TABLE")
        region = "us-west-2"

    id = UnicodeAttribute(hash_key=True)
    date = UTCDateTimeAttribute()
    name = UnicodeAttribute()
    value = NumberAttribute()
    details = UnicodeAttribute(null=True)
    source = UnicodeAttribute()


class CashFlowMapping(MyModel):
    class Meta:
        table_name = os.getenv("CASH_FLOW_MAPPING_TABLE")
        region = "us-west-2"

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=True)
    category = UnicodeAttribute()
    source = UnicodeAttribute()
    cash_flow_id = UnicodeAttribute(null=True)

    @classmethod
    def delete_single_cash_flow_mapping(cls, cash_flow_id):
        query = list(cls.scan(cls.cash_flow_id == cash_flow_id, limit=1))
        if len(query) > 0:
            query[0].delete()

    @classmethod
    def register_mapping_for_singl_cash_flow(cls, cf_id, category, source):
        query = list(cls.scan(cls.cash_flow_id == cf_id, limit=1))
        if len(query) > 0:
            item = cls.get(query[0].id)
            item.category = category
            item.save()
        else:
            new_id = str(uuid4())
            item = cls(id=new_id, cash_flow_id=cf_id, category=category, source=source)
            item.save()
        return item.id

    @classmethod
    def register_mapping_for_all_cash_flows(cls, name, category, source):
        query = list(cls.scan(cls.name == name, limit=1))
        if len(query) > 0:
            item = cls.get(query[0].id)
            item.category = category
            item.save()
        else:
            new_id = str(uuid4())
            item = cls(id=new_id, name=name, category=category, source=source)
            item.save()
        return item.id
