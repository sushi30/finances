from datetime import datetime
from sqlalchemy import Column
from . import db


class UUID(db.VARCHAR):
    def __init__(self):
        super().__init__(36)


class TimestampModel:
    created_at = Column(db.TIMESTAMP, default=datetime.now())
    updated_at = Column(db.TIMESTAMP, default=datetime.now())


class UUIDModel(TimestampModel):
    id = Column(UUID(), primary_key=True)
