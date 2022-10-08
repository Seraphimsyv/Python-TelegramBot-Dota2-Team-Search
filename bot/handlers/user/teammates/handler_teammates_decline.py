from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot

from database.models import UsersManager


async def handler_teammates_decline(cb: types.CallbackQuery, state: FSMContext) -> None:

    await state.finish()
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)

    recipient = UsersManager.getUserById(cb.data.split('|')[2])
    
    msg = f"<strong>{recipient.name} отклонил запрос</strong>"
    
    await bot.send_message(chat_id=cb.data.split('|')[1], text=msg, parse_mode="HTML")