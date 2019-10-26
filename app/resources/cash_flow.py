from app.models import CashFlow as CashFlowModel


def get(uuid=None):
    if uuid is None:
        return CashFlowModel.dumps()


def put(*args, **kwargs):
    raise NotImplementedError()
