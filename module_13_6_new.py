import asyncio
import logging
from os import getenv
import sys
from dotenv import load_dotenv

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)

load_dotenv()

TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()

router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(CommandStart())
async def start(message) -> None:
    await message.answer(
        f"Привет! Я бот помогающий твоему здоровью.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Рассчитать"),
                    KeyboardButton(text="Информация"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(F.text.casefold() == "calculate")
async def main_menu(message: Message):
    await message.answer(
        "Выберите опцию:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Рассчитать норму калорий", callback_data="calories"
                    ),
                    InlineKeyboardButton(
                        text="Формулы расчёта", callback_data="formulas"
                    ),
                ]
            ],
        ),
    )


@router.callback_query(F.data == "formulas")
async def get_formulas(query: CallbackQuery):
    await query.message.answer(
        f"10 x вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) + 5 - для мужчин;\n10 x вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) - 161 - для женщин"
    )


@router.callback_query(F.data == "calories")
async def set_age(query: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.age)
    await query.message.answer("Введите свой возраст:")


@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer("Введите свой рост:")


@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer("Введите свой вес:")


@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    result = (
        10 * int(data["weight"])
        + 6.25 * int(data["growth"])
        - 5 * int(data["age"])
        - 161
    )

    await message.answer(f"Ваша норма калорий в сутки: {result}")

    await state.clear()


@router.message()
async def all_messages(message) -> None:
    await message.answer(f"Введите команду /start, чтобы начать общение.")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
