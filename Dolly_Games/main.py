import asyncio

from aiogram import Dispatcher

from config import dp, bot
from db.tables import init_tables
from handlers import router as handlers_router


@dp.startup()
async def startup(dispatcher: Dispatcher):
    await init_tables()

    dp.include_router(handlers_router)


@dp.shutdown()
async def shutdown(dispatcher: Dispatcher):
    pass


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
