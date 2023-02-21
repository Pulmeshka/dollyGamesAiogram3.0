from aiogram import types
from main import dp

@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    await message.answer('тест прошёл успешно')