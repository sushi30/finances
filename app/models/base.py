from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from . import db

Base = declarative_base()


class UUID(db.VARCHAR):
    def __init__(self, *args, **kwargs):
        super().__init__(36, *args, **kwargs)


class MyModel(db.Model):
    created_at = Column(db.TIMESTAMP, default=datetime.now())
    updated_at = Column(db.TIMESTAMP, default=datetime.now())


class UUIDModel(MyModel):
    id = Column(UUID(), primary_key=True)
