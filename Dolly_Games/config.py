from pathlib import Path

from aiogram import Bot, Dispatcher

DB_PATH = Path(__file__).parent / "db.sqlite3"

bot = Bot(token="")
dp = Dispatcher()
