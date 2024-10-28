import asyncio
import logging
import sys
import pymysql
from aiogram import F
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State

api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(F.text.lower().contains('calories'))
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    for_man = (10 * float(data['weight']) + 6.25 * float(data['growth']) -
               5* float(data['age']) + 5)
    for_woman = for_man - 166
    await message.answer(f'Норма калорий для мужчин: {for_man}, для женщин: {for_woman}')
    await state.clear()

@dp.message()
async def all_message(message: Message):
    await message.answer(text="Я не совсем понимаю, что вы имеете ввиду :(")

async def main() -> None:
        # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=api, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Альтик работает!')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


