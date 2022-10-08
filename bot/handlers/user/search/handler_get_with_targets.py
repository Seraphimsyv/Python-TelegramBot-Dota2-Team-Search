from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import TargetsSearchState
from bot.settings import bot
from bot.keyboards.inline.search import search_keyboard

from bot.handlers.user.targets.handler_set_rate import handler_target_set_rate

from database.models import TargetsManager


async def handler_get_with_targets(cb: types.CallbackQuery, state: FSMContext) -> None:
    await state.finish()
    
    data = TargetsManager.getUserFromTarget(cb.from_user.id)

    if "type" in data and data['type'] == 'error':

        if data['msg'] == "Target parameters of user not exists":

            msg = "Не установлены параметры поиска\nТребуеться установка параметров поиска"

            await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")
            await handler_target_set_rate(cb, state)

        elif data['msg'] == "Not exists users for target":

            msg = "Нет активных пользователей подходящих под параметры поиска"
            await cb.answer(text=msg)
    
    else:

        await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)

        await state.update_data(id=data[0])
        await state.update_data(tg_id=data[1])

        with open(f'./config/assets/{data[9]}.jpg', 'rb') as ph:
            
            msg = f"Статус: {'Активен' if data[7] == True else 'Неактивен'}\n"\
                f"Имя: {data[6]}\n"\
                f"Рейтинг: {data[8]}\n"\
                f"Позиция: {data[9]}\n"\
                f"Предпочтения по серверам: {data[10]}\n"\
                f"\n{data[11]}\n"

            await TargetsSearchState.next.set()
            await bot.send_photo(chat_id=cb.from_user.id,photo=ph,parse_mode="HTML",caption=msg,reply_markup=search_keyboard)