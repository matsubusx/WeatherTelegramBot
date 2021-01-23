import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import variables
from modules import weather_module

logging.basicConfig(level=logging.INFO)
bot = Bot(token=variables['TG_TOKEN'])
dp = Dispatcher(bot)


def auth(func):

    async def wrapper(message):
        if message['from']['id'] != 487609708:
            return await message.reply("Access Denied", reply=False)
        return await func(message)

    return wrapper


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('IM HERE')


@dp.message_handler(commands=['weather'])
async def show_weather(message: types.Message):
    weather_info = weather_module.get_weather()
    user_message = f"""
Привет @{message['from']['username']}!
Сегодня: {weather_info['date'].day} {weather_module.months[weather_info['date'].month - 1]} {weather_info['date'].year} года

    """

    await message.reply(user_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
