# USE SQLALCHEMY INSTEAD OF RAW SQL !!!
import aiosqlite

from config import DB_PATH


async def init_tables():
    async with aiosqlite.connect(DB_PATH) as db:
        for table in TABLES:
            await db.execute(table)
            await db.commit()


USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id BIGINTEGER PRIMARY KEY,
    dolly INTEGER DEFAULT 100,
    minti INTEGER DEFAULT 0
);
"""

TABLES = [USERS_TABLE]
