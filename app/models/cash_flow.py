from sqlalchemy import DateTime, String, Float, JSON, Column
from sqlalchemy.ext.declarative import declarative_base
from .base import UUIDModel

Base = declarative_base()


class CashFlow(UUIDModel, Base):
    __tablename__ = "cash_flow"

    date = Column(DateTime(), nullable=False)
    name = Column(String(256), nullable=False)
    value = Column(Float(), nullable=False)
    details = Column(JSON, nullable=True)
    source = Column(String(256), nullable=False)
