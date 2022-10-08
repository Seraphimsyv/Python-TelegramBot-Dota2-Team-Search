from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import TargetsSearchState
from bot.settings import bot


async def handler_target_set_rate(cb: types.CallbackQuery, state: FSMContext) -> None:

    msg = "По какому рейтингу искать?"

    await state.finish()
    await TargetsSearchState.rate.set()
    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")