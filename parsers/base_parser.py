import json
from abc import ABC


class Parser(ABC):
    transactions = []

    def transactions_as_dict(self):
        return [t.dumps() for t in self.transactions]

    def parser(self,):
        pass

    def from_string(self):
        pass

    def dumps(self, *args, **kwargs):
        return json.dumps(self.transactions_as_dict(), *args, **kwargs)
