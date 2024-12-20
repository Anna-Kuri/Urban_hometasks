import asyncio
import logging
import sys
from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart


load_dotenv()

TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message) -> None:
    print(f"Привет! Я бот помогающий твоему здоровью.")


@dp.message()
async def all_messages(message) -> None:
    print(f"Введите команду /start, чтобы начать общение.")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
