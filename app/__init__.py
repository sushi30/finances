import os

from flask import Flask

if os.getenv("ENV") == "LOCAL":
    from dotenv import load_dotenv

    load_dotenv()
