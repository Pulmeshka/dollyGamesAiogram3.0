from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db import db

router = Router(name="start_help_router")


@router.message(CommandStart())
async def start_cmd(msg: Message):
    await msg.answer("команды бота /help")

    if not await db.get_balance(msg.from_user.id):
        await db.insert_user(msg.from_user.id)


# help - помощь
@router.message(Command("start"))
async def help_cmd(msg: Message):
    await msg.answer(
        "помощь по боту\n"
        "/game - все мини-игры бота\n"
        "/commands - все команды бота\n"
        "/rp - все рп команды по боту"
    )  # fmt: skip


@router.message(Command("rp"))
async def rp(msg: Message):
    await msg.answer(
        "рп команды нужно вводить ответом на сообщение игрока\n"
        "UPD 1.0\n"
        "обнять\n"
        "ударить\n"
        "кинуть\n"
        "выкинуть\n"
        "оскорбить\n"
        "--------------------------"
    )  # fmt: skip


@router.message(Command("commands"))
async def commands(msg: Message):
    await msg.answer("ми - просмотр профиля\n")
