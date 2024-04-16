import asyncio
import logging
import aiogram

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Меня зовут Ваня!"
                         " Я исскуственный интелект, созданный для решения разных научных задач!"
                         " Если в боте что-то сломалось, введи команду /help")


@dp.message(Command('lc'))
async def local_crew(message: Message):
    await message.answer("https://t.me/zlochan")


@dp.message(Command('help'))
async def give_help(message: Message):
    await message.answer("Бот на стадии разработки. Все предъявы к моему лучшему разработчику @majorovvv")

@dp.message(F.text == 'Что ты умеешь делать?')
async def what_can_i_do(message: Message):
    await message.answer("Пока все на стадии разработки(")
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
