from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RegistrationState
from bot.settings import bot

from database.models import UsersManager


async def handler_finish(cb: types.CallbackQuery, state: FSMContext) -> None:

    data = await state.get_data()

    new_data = {}
    new_data.update(cb.from_user.to_python())
    new_data.update(data)
    new_data['tg_id'] = new_data['id']
    del new_data['id']
    del new_data['is_bot']

    UsersManager.CreateOrUpdate(**new_data)

    msg = "Твоя анкета сохранена!"

    await RegistrationState.confirm.set()
    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")