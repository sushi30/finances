import os

if os.getenv("ENV") == "LOCAL":
    from dotenv import load_dotenv

    load_dotenv()

from .parse_expenses import handler as parse_expense_handlers
