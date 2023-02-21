from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="test_router")


@router.message(Command("test"))
async def test(msg: Message):
    await msg.answer("тест прошёл успешно")
