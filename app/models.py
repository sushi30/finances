from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UUID(mysql.VARCHAR):
    def __init__(self, *args, **kwargs):
        super().__init__(36, *args, **kwargs)


class MyModel(Base):
    created_at = Column(mysql.TIMESTAMP, default=datetime.now())
    updated_at = Column(mysql.TIMESTAMP, default=datetime.now())


class UUIDModel(MyModel):
    id = Column(UUID(), primary_key=True)


class User(UUIDModel):
    __tablename__ = "user"

    name = Column(mysql.VARCHAR(256), nullable=False)
    email = Column(mysql.VARCHAR(256), nullable=False)


class CashFlow:
    __tablename__ = "cash_flow"

    date = Column(mysql.DATETIME(), nullable=False)
    name = Column(mysql.VARCHAR(256), nullable=False)
    value = Column(mysql.FLOAT(), nullable=False)
    details = Column(mysql.TEXT, nullable=True)
    source = Column(mysql.VARCHAR(256), nullable=False)


class CashFlowMapping(UUIDModel):
    __tablename__ = "cash_flow_mapping"

    name = Column(mysql.VARCHAR(256), nullable=True)
    cash_flow_id = Column(UUID, nullable=True)
    category = Column(mysql.VARCHAR(256), nullable=False)
    source = Column(UUID, nullable=True)
