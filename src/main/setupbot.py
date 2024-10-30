
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import gachi.handler as gachi
from .config import BOT_TOKEN

async def setup_bot() -> None:

    dp = Dispatcher()
    dp.include_router(gachi.gachi_router)

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)