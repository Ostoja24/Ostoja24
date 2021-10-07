import os

from dotenv import load_dotenv


class Config:
    load_dotenv()
    URL = os.environ.get("URL")
