from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot


async def handler_set_description(cb: types.CallbackQuery, state: FSMContext) -> None:

    msg = "Опиши себя вкратце.\nЭто поможет лучше подобрать тебе тимейтов."

    await state.update_data(position=cb.data)
    await RegistrationState.desc.set()
    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")