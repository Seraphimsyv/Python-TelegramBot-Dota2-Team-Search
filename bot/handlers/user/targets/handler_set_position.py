from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import TargetsSearchState
from bot.settings import bot
from bot.keyboards.inline.targets import position_keyboard


async def handler_target_set_position(message: types.Message, state: FSMContext) -> None:

    msg = "По какой позиции искать?"

    await state.update_data(rate=message.text)
    await TargetsSearchState.pos.set()
    await bot.send_message(chat_id=message.from_user.id, text=msg, parse_mode="HTML", reply_markup=position_keyboard)