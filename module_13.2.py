import asyncio
import logging
import sys
from aiogram import F
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = 'token'
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Хэй!, {html.bold(message.from_user.full_name)}!")
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def all_message(message):
    await message.answer(text="Введите команду /start, чтобы начать общение.")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Альтик работает!')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())