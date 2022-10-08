from aiogram import Bot, Dispatcher

from config.env import *
from .states import memory_storage


bot = Bot(token=TelegramEnv.TOKEN)
dp = Dispatcher(bot, storage=memory_storage)