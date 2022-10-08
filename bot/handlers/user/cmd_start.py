from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot
from bot.keyboards.inline.start import register_user_keyboard, unregister_user_keyboard
from database.models.Users import UsersManager


async def cmd_start(message: types.Message, state: FSMContext) -> None:
    await state.finish()

    if "message" in message:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message.message_id)
    else:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

    user = UsersManager.getUserById(id=message.from_user.id)

    if user != False:
        
        msg = "Registered"

        keyboard = register_user_keyboard

    else:

        msg = "Unregistered"

        keyboard = unregister_user_keyboard

    await bot.send_message(chat_id=message.from_user.id, text=msg, parse_mode="HTML", reply_markup=keyboard)