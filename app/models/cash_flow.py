from .base import UUIDModel
from . import db


class CashFlow(UUIDModel, db.Model):
    __tablename__ = "cash_flow"

    date = db.Column(db.DATETIME(), nullable=False)
    name = db.Column(db.VARCHAR(256), nullable=False)
    value = db.Column(db.FLOAT(), nullable=False)
    details = db.Column(db.TEXT, nullable=True)
    source = db.Column(db.VARCHAR(256), nullable=False)
