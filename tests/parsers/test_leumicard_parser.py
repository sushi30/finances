from parsers.leumicard_parser import LeumiCardParser
from scripts.parse_credit_card import datetime_converter


def test_parse_leumicard():
    with open("tests/data/leumicard_test_data.xlsx", "rb") as excel_file:
        lcp = LeumiCardParser(excel_file).parse()
    assert len(lcp.transactions) == 20
    print(lcp.dumps(default=datetime_converter, indent=2))



