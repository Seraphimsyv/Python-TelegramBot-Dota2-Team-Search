from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import TargetsSearchState
from bot.settings import bot
from bot.keyboards.inline.targets import region_keyboard


async def handler_target_set_region(cb: types.CallbackQuery, state: FSMContext) -> None:

    msg = "По какому серверу искать?"

    await state.update_data(position=cb.data)
    await TargetsSearchState.region.set()
    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML", reply_markup=region_keyboard)