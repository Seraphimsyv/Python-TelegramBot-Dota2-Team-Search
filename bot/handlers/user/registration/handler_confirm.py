from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot
from bot.keyboards.inline.registration import confirm_keyboard


async def handler_confirm(cb: types.CallbackQuery, state: FSMContext) -> None:

    await state.update_data(region=cb.data)
    
    data = await state.get_data()

    await RegistrationState.confirm.set()

    msg = "Так выглядит твоя анкета:"

    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")

    msg = "Test"

    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")

    msg = "Все верно?"

    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML", reply_markup=confirm_keyboard)