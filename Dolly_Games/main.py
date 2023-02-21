from aiogram import Bot, Dispatcher

bot = Bot(token='')
dp = Dispatcher(bot)

async def main():
    await dp.start_polling(
        bot,
    )


if __name__ == "__main__":
    from handlers import dp
    asyncio.run(main())