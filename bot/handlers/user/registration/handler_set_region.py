from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot
from bot.keyboards.inline.registration import region_keyboard


async def handler_set_region(message: types.Message, state: FSMContext) -> None:

    msg = "На серверах какого региона играешь?"

    await state.update_data(description=message.text)
    await RegistrationState.region.set()
    await bot.send_message(chat_id=message.from_user.id, text=msg, parse_mode="HTML", reply_markup=region_keyboard)