from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot


async def handler_set_name(cb: types.CallbackQuery, state: FSMContext) -> None:
    await state.finish()

    msg = "Как мне тебя называть?"
    
    await RegistrationState.name.set()
    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")