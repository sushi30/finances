import datetime
import json
import uuid
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.cash_flow import CashFlow
from parsers.leumicard_parser import LeumiCardParser

UUID_NAMESPACE = uuid.UUID("c9def9830ffd4a2293aeb804e0d121ec")


def datetime_converter(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


def transaction_to_to_cash_model(transaction, extra=""):
    kwargs = {
        "date": transaction.date.isoformat(),
        "name": transaction.business,
        "value": transaction.value,
        "source": "Leumicard",
        "id": uuid.uuid4(),
        "details": json.dumps(transaction.to_dict(), default=datetime_converter),
    }
    return CashFlow(**kwargs)


@click.command()
@click.argument("path")
@click.option("--out", default=None)
@click.option("--storage", default=None)
def main(path, out, storage):
    with open(path, "rb") as excel_file:
        res = LeumiCardParser(excel_file).parse()
    transactions = [t.to_dict() for t in res.transactions]
    if out is not None:
        with open(out, "wb") as excel_file:
            json.dump(transactions, excel_file, default=datetime_converter)
    elif storage is not None:
        engine = create_engine(storage)
        Session = sessionmaker(bind=engine)
        session = Session()
        cf_objects = []
        for cf in res.transactions:
            cf_objects.append(transaction_to_to_cash_model(cf))
        try:
            session.add(cf_objects[8])
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    else:
        print(json.dumps(transactions, default=datetime_converter, indent=2))



if __name__ == "__main__":
    main()
