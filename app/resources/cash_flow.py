from app.models import CashFlow as CashFlowModel


def get(self, uuid=None):
    if uuid is None:
        return CashFlowModel.dumps()


def put(data):
    raise
