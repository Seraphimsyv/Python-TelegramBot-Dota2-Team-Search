from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot
from bot.handlers.user.profile.handler_profile import handler_profile

from database.models import UsersManager


async def handler_set_active_profile(cb: types.CallbackQuery, state: FSMContext) -> None:
    
    UsersManager.setUserActive(cb.from_user.id)

    msg = "Профиль активирован"

    await state.finish()
    await cb.answer(text=msg)
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    await handler_profile(cb, state)
