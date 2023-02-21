from aiogram import Router
from aiogram.filters import Text, Command
from aiogram.types import Message

from db import db

router = Router(name="me_router")


@router.message(Text("ми", ignore_case=True))
@router.message(Command("me"))
async def profile(msg: Message):
    balance = await db.get_balance(msg.from_user.id)
    minti = await db.get_minti(msg.from_user.id)

    if not balance:
        await db.insert_user(msg.from_user.id)

    else:
        await msg.answer(
            f"профиль {msg.from_user.first_name}\n"
            f"долли🧿 - {balance}\n"
            f"минтиⓂ - {minti}\n"
            f"брак💞 - скоро..."
        )  # fmt: skip
