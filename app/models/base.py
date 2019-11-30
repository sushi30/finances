from datetime import datetime
from sqlalchemy import Column
from . import db


class UUID(db.VARCHAR):
    def __init__(self):
        super().__init__(36)


class UUIDModel:
    id = Column(UUID(), primary_key=True)
    created_at = Column(db.TIMESTAMP, default=datetime.now())
    updated_at = Column(db.TIMESTAMP, default=datetime.now())
