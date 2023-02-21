from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

router = Router(name='rpDolly_router')


# @router.message(F.text.regex(r'обнять\s+\w+$'))
@router.message(Text("обнять", ignore_case=True))
async def hug_handler(message: Message):
    if not message.reply_to_message:
        await message.reply('вы не ответили на сообщение пользователя🎃')

    else:
        name = message.from_user.first_name
        reply_name = message.reply_to_message.from_user.first_name
        await message.answer(f'{name} <b>обнял</b> {reply_name}', parse_mode='HTML')


@router.message(Text("ударить", ignore_case=True))
async def hit_handler(message: Message):
    if not message.reply_to_message:
        await message.reply('вы не ответили на сообщение пользователя🎃')

    else:
        name = message.from_user.first_name
        reply_name = message.reply_to_message.from_user.first_name
        await message.answer(f'{name} <b>жёстко ударил</b> {reply_name}', parse_mode='HTML')
