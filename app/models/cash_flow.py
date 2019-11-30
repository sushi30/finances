from .base import UUIDModel
from . import db

class CashFlow(UUIDModel):
    __tablename__ = "cash_flow"

    date = db.Column(mysql.DATETIME(), nullable=False)
    name = Column(mysql.VARCHAR(256), nullable=False)
    value = Column(mysql.FLOAT(), nullable=False)
    details = Column(mysql.TEXT, nullable=True)
    source = Column(mysql.VARCHAR(256), nullable=False)
