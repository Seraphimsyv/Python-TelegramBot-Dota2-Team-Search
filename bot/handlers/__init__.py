from aiogram import Dispatcher

from .user import register_user_handlers
from .admin import register_admin_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_admin_handlers(dp)