import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from gandalf.handlers import start_router
from gandalf.utils.config import Config

config = Config()
dp = Dispatcher()

dp.include_router(start_router)


async def main():
    bot = Bot(
        token=config.TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True,
        ),
    )
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=config.LOGGING_LEVEL,
        format="%(asctime)s – %(levelname)s – %(name)s – %(message)s",
    )
    asyncio.run(main())
