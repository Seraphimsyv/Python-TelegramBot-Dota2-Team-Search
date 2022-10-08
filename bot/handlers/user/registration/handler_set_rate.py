from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot


async def handler_set_rate(message: types.Message, state: FSMContext) -> None:

    msg = "Какой у тебя рейтинг?"

    await state.update_data(name=message.text)
    await RegistrationState.rate.set()
    await bot.send_message(chat_id=message.from_user.id, text=msg, parse_mode="HTML")