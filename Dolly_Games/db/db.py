from typing import Union

import aiosqlite

from config import DB_PATH


async def insert_user(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO users (id) VALUES (?)", (user_id,))
        await db.commit()


async def get_balance(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT dolly FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None


async def update_balance(user_id: int, dolly: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET dolly = ? WHERE id = ?", (dolly, user_id))
        await db.commit()


async def get_minti(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT minti FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
