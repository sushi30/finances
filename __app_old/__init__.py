import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

if os.getenv("ENV") == "LOCAL":
    from dotenv import load_dotenv

    load_dotenv()
