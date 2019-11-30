import xlrd
from parsers.trasaction import Transaction
from .base_parser import Parser


class LeumiCardParser(Parser):
    def __init__(self, file_):
        super().__init__()
        self.file = file_
        self.rows_as_dicts = []
        self.wb = None

    def parse(self):
        self.wb = xlrd.open_workbook(file_contents=self.file.read())
        for i in range(self.wb.nsheets):
            self.it = iter(self.wb.sheet_by_index(0).get_rows())
            while True:
                try:
                    row = next(self.it)
                except StopIteration:
                    break
                if "כל המשתמשים" in row[0].value:
                    continue
                if "כל הכרטיסים" in row[0].value:
                    continue
                if "תאריך עסקה" in row[0].value:
                    self.categories = [col.value for col in row]
                    self.parse_rows()
        self.parse_transactions()
        return self

    def parse_transactions(self):
        columns_dictionary = {
            'שער המרה ממטבע מקור/התחשבנות לש"ח': "conversion_rate_from_ils",
            "תאריך עסקה": "date",
            "שם בית העסק": "business",
            "קטגוריה": "category",
            "4 ספרות אחרונות של כרטיס האשראי": "credit_no",
            "סוג עסקה": "payment_type",
            "סכום חיוב": "value",
            "מטבע חיוב": "value_currency",
            "סכום עסקה מקורי": "original_value",
            "מטבע עסקה מקורי": "original_currency",
            "payment_date": "תאריך חיוב",
            "הערות": "comments",
            "אופן ביצוע ההעסקה": "payment_method",
        }
        for row in self.rows_as_dicts:
            kwargs = {columns_dictionary.get(k, k): v for k, v in row.items()}
            self.transactions.append(Transaction(**kwargs))

    def parse_rows(self):
        while True:
            try:
                row = next(self.it)
            except StopIteration:
                break
            self.rows_as_dicts.append(
                {col_name: col.value for (col_name, col) in zip(self.categories, row)}
            )
