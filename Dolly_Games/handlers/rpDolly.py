from main import dp
from aiogram import types
from aiogram.filters import Text


@dp.message_handler(Text(startswith="обнять "))  
async def hug_handler(message: Message):
    if not message.reply_to_message:
        await message.reply('вы не ответили на сообщение пользователя🎃')
    else:
        name = message.from_user.first_name
        reply_name = message.reply_to_message.from_user.first_name     
        await message.answer(f'{name} <b>обнял</b> {reply_name}', parse_mode='HTML')

@dp.message_handler(Text(startswith="ударить ")) 
async def hug2_handler(message: Message):
    if not message.reply_to_message:
        await message.reply('вы не ответили на сообщение пользователя🎃')
    else:
        name = message.from_user.first_name
        reply_name = message.reply_to_message.from_user.first_name     
        await message.answer(f'{name} <b>жёстко ударил</b> {reply_name}', parse_mode='HTML')