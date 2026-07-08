# main.py
"""
Maktab Telegram Boti - asosiy ishga tushirish fayli.

Ishga tushirish:
    1. .env.example -> .env qilib nusxalang va API_TOKEN, ADMIN_ID ni kiriting
    2. pip install -r requirements.txt
    3. python main.py
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
import database as db
from handlers import router


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger(__name__)

    await db.init_db()
    logger.info("✅ Ma'lumotlar bazasi tayyor.")

    bot = Bot(
        token=config.API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)

    logger.info("🚀 Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Bot to'xtatildi.")
