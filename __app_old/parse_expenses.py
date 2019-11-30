import logging
from uuid import uuid4
import pandas as pd
from app.models import CashFlow
from helpers import get_leumicard

log = logging.getLogger(__name__)


def parse_file(bucket, key):
    switcher = {"leumicard": get_leumicard}
    return switcher[key.split("/")[0]](bucket, key)


def write_cash_flows_to_db(cash_flows: pd.DataFrame):
    latest = CashFlow.max(
        CashFlow.date, CashFlow.source == cash_flows.iloc[0].source
    ).replace(tzinfo=None)
    cash_flows = cash_flows[cash_flows.date > latest]
    with CashFlow.batch_write() as batch:
        for item in cash_flows.apply(
            lambda x: CashFlow(
                str(uuid4()),
                date=x.date.to_pydatetime(),
                name=x["name"],
                source=x.source,
                details=x.details,
                value=x.value,
            ),
            axis=1,
        ).tolist():
            batch.save(item)
