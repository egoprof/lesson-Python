import asyncio
import logging
import sys
import datetime
from gc import callbacks
from pyexpat.errors import messages
import aiogram.types
import pymysql
from aiogram import F, types
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import StatesGroup, State


api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def get_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Рассчитать", callback_data="calories")
    builder.button(text="Информация", callback_data="formulas")
    builder.adjust(2)
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Выбери опцию:", reply_markup=get_inline_keyboard())

@dp.callback_query(F.data == "formulas")
async def handle_formulas(callback: types.CallbackQuery):
    await callback.answer('Формулы расчёта')
    await callback.message.edit_text("10 x вес (кг) + 6,25 х рост (см) - 5 х возраст (г) - 161")

@dp.callback_query(F.data == 'calories')
async def calories(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("рассчитать")
    await callback.message.edit_text("Введите свой возраст:")
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    for_man = (10 * float(data['weight']) + 6.25 * float(data['growth']) -
               5 * float(data['age']) + 5)
    for_woman = for_man - 166
    await message.answer(f'Норма калорий для мужчин: {for_man}, для женщин: {for_woman}')
    await state.clear()

@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        'Кoманда /start поможет тебе начать работу с ботом\nрассчитать - поможет рассчитать каллории под ваш типаж\nКоманда /help вернет к списку команд')

@dp.message()
async def all_message(message: Message):
    await message.answer(text="Я не совсем понимаю, что вы имеете ввиду :(")


async def main():
    bot = Bot(token=api, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Альтик работает!')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
