from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot

from database.models import UsersManager, TeammatesManager


async def handler_list_teammates(cb: types.CallbackQuery, state: FSMContext) -> None:
    await state.finish()

    teammates = TeammatesManager.getAllTeammatesOfUser(user_id=cb.from_user.id)

    msg = "<strong>Список сокомандников</strong>\n"

    for teammate in teammates:
        user = UsersManager.getUserById(teammate[2])
        msg += f"\nИмя: {user.to_array()[6]}\n"\
            f"Рейтинг: {user.to_array()[8]}\n"\
            f"Позиция: {user.to_array()[9]}\n"\
            f"Предпочтения по серверам: {user.to_array()[10]}\n"\
            f'<a href="tg://user?id={user.to_array()[1]}">Ссылка</a>\n'

    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")