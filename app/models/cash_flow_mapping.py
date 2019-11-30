from .base import UUIDModel, UUID
from . import db


class CashFlowMapping(UUIDModel):
    __tablename__ = "cash_flow_mapping"

    name = db.Column(db.VARCHAR(256), nullable=True)
    cash_flow_id = db.Column(UUID, nullable=True)
    category = db.Column(db.VARCHAR(256), nullable=False)
    source = db.Column(UUID, nullable=True)
