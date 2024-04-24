import asyncio
import logging
from abc import ABC

import aiogram

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.filters import Filter

import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config
import re

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


class RegexFilter(Filter, ABC):
    def __init__(self, pattern):
        self.pattern = pattern

    async def check(self, message: Message) -> bool:
        return bool(re.match(self.pattern, message.text))


class WeatherFilter(RegexFilter):
    def __init__(self):
        super().__init__(r'Какая погода в (.+)')

    def __call__(self, message: Message):
        return self.check(message)


class CalculateFilter(RegexFilter):
    def __init__(self):
        super().__init__(r'Сколько будет (.+)')

    def __call__(self, message: Message):
        return self.check(message)


class RemindFilter(RegexFilter):
    def __init__(self):
        super().__init__(r'Напомни мне о (.+) через (.+) минут?')

    def __call__(self, message: Message):
        return self.check(message)


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
    await message.answer(
        "Я похож на яндекс станцию Алису! Я могу подсказать погоду, выполнять сложные арифметические действия, и напоминать о важных вещах ")


@dp.message(WeatherFilter())
async def weather(message: Message):
    match = re.search(WeatherFilter().pattern, message.text)
    city = match.group(1)
    owm = OWM('7c1f7b5fc6232356b89797f0cd53af19')

    try:
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        await message.answer(f"В городе {city} сейчас {w.detailed_status}. "
                             f"Температура воздуха: {w.temperature('celsius')['temp']}°C")

    except Exception as e:
        await message.answer(f"Не удалось получить погоду в городе {city}. "
                             f"Попробуйте указать другой город или проверьте правильность написания.")


@dp.message(CalculateFilter())
async def calculate(message: Message):
    expression = re.match(CalculateFilter().pattern, message.text).group(1)
    try:
        result = eval(expression)
        await message.answer(f"Результат: {result}")
    except Exception as e:
        await message.answer(f"Не удалось выполнить вычисление. Проверьте правильность ввода.")


@dp.message(RemindFilter())
async def remind(message: Message):
    try:
        match = re.search(RemindFilter().pattern, message.text)
        subject = match.group(1)
        minutes = match.group(2)
        minutes = int(minutes)
        await asyncio.sleep(minutes * 60)  # ожидание указанного количества часов
        await message.answer(f"Время {subject}!")
    except Exception as e:
        await message.answer(f"Не удалось создать напоминание. Проверьте правильность ввода.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
