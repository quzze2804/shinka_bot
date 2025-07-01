import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    from bot.handlers import start  # Імпортуємо стартові хендлери
    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
