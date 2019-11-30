






class CashFlowMapping(UUIDModel):
    __tablename__ = "cash_flow_mapping"

    name = Column(mysql.VARCHAR(256), nullable=True)
    cash_flow_id = Column(UUID, nullable=True)
    category = Column(mysql.VARCHAR(256), nullable=False)
    source = Column(UUID, nullable=True)
