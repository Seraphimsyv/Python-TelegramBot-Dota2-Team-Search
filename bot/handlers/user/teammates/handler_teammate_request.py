from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot
from bot.keyboards.inline.teammates import add_or_decline_menu

from database.models import UsersManager


async def handler_teammate_request(cb: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()

    user = UsersManager.getUserById(cb.from_user.id)
    
    msg = "<strong>Запрос на совместную игру</strong>\n"\
        f"Рейтинг: {user.to_array()[8]}\n"\
        f"Позиция: {user.to_array()[9]}\n"\
        f"Предпочтения по серверам: {user.to_array()[10]}\n"\
        f"\n{user.to_array()[11]}\n"\
        f"\n👍{user.to_array()[12]} 👎{user.to_array()[13]}"

    keyboard = add_or_decline_menu.to_python()
    keyboard['inline_keyboard'][0][0]['callback_data'] += f"|{cb.from_user.id}|{data['tg_id']}"
    keyboard['inline_keyboard'][1][0]['callback_data'] += f"|{cb.from_user.id}|{data['tg_id']}"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=keyboard["inline_keyboard"])

    await cb.answer(text="Запрос отправлен")
    await bot.send_message(chat_id=data['tg_id'], text=msg, parse_mode="HTML", reply_markup=keyboard)