import os

if os.getenv("ENV") == "LOCAL":
    from dotenv import load_dotenv

    load_dotenv()
