from sqlalchemy import create_engine
from app.models.cash_flow import CashFlow
from app.models.cash_flow_mapping import SpecificCashFlowMapping, GeneralCashFlowMapping


def main():
    engine = create_engine("mysql://root:1234@localhost/finance")
    # CashFlow.metadata.create_all(engine)
    SpecificCashFlowMapping.metadata.create_all(engine)
    GeneralCashFlowMapping.metadata.create_all(engine)


if __name__ == "__main__":
    main()
