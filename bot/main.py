from aiogram import Dispatcher

from .settings import bot, dp
from .handlers import register_all_handlers


def register_handlers(dp: Dispatcher) -> None:
    register_all_handlers(dp)