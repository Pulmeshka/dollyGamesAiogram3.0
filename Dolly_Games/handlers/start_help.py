from main import dp
from aiogram import types
from .data import Database

db = Database()
#start - начало
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('команды бота /help')
    id = message.from_user.id
    if db.get_balance(id) is None:
        db.insert_user(id)

#help - помощь
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('помощь по боту\n/game - все мини-игры бота\n/commands - все команды бота\n/rp - все рп команды по боту')

@dp.message_handler(commands=['rp'])
async def rp(message: types.Message):
    await message.answer('рп команды нужно вводить ответом на сообщение игрока\nUPD 1.0\nобнять\nударить\nкинуть\nвыкинуть\nоскорбить\n--------------------------')

@dp.message_handler(commands=['commands'])
async def commands(message: types.Message):
    await message.answer('ми - просмотр профиля\n')

