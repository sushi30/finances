from .base import UUID
from . import db

class Category(db.UUIDModel):
    __tablename__ = "category"

    user = db.Column(UUID(), nullable=False)
    name = db.Column(db.VARCHAR(256), nullable=True)
    cash_flow_id = db.Column(UUID, nullable=True)
    category = db.Column(mysql.VARCHAR(256), nullable=False)
    source = db.Column(UUID, nullable=True)