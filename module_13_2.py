import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "token"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Хэй!, {html.bold(message.from_user.full_name)}!", reply_markup=kb)

@dp.message(Command('Help'.lower()))
async def Help_command(message: Message):
    await message.reply("Команды бота:\n/start - Начать работу\n/AddKlass - Добавить в систему новый класс")


@dp.message(Command('AddKlass'.lower()))
async def AddKlass_command(message: Message):
    await message.reply("Добавляем новый класс в систему")

@dp.message(F.text.lower().contains("hi"))
async def hi_handler(message: Message) -> None:
    await message.answer(text="И тебе привет от бота!")

@dp.message(F.text.lower().contains("setup"))
async def setup_handler(message: Message) -> None:
    global dbid
    for dbid in range(1000, 1007):
        connect_id(dbid,0,0,0,0,0,0,0)
    await message.answer(text="Я выполнил первичные настройки MySQL")

@dp.message(F.text.lower().contains("addklass"))
async def addklass_handler(message: Message) -> None:

    await message.answer(text="Я выполнил первичные настройки MySQL")


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Хорошая попытка!")
@dp.message()
async def all_message(message):
    await message.answer(text="Я не совсем понимаю, что вы имеете ввиду :(")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Альтик работает!')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
