import os
from dotenv import load_dotenv

load_dotenv()

YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DB_NAME = os.getenv("DB_NAME", "alertbase.db")
