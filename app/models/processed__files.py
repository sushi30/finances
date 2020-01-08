from .base import UUID, TimestampModel
from . import db


class CashFlowMapping(TimestampModel):
    category = db.Column(db.VARCHAR(256), nullable=False, primary_key=True)
    source = db.Column(UUID, nullable=True)


class GeneralCashFlowMapping(CashFlowMapping, db.Model):
    __tablename__ = "general_cash_flow_mapping"

    name = db.Column(db.VARCHAR(256), nullable=True, primary_key=True)


class SpecificCashFlowMapping(CashFlowMapping, db.Model):
    __tablename__ = "specific_cash_flow_mapping"

    cash_flow_id = db.Column(UUID, nullable=True, primary_key=False)
