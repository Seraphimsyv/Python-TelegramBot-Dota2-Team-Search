from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot
from bot.keyboards.inline.registration import position_keyboard


async def handler_set_position(message: types.Message, state: FSMContext) -> None:

    msg = "На какой позиции играешь?"

    await state.update_data(rate=message.text)
    await RegistrationState.pos.set()
    await bot.send_message(chat_id=message.from_user.id, text=msg, parse_mode="HTML", reply_markup=position_keyboard)