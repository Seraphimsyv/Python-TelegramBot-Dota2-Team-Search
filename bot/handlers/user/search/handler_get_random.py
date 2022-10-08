from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.states import RandomSearchState
from bot.settings import bot
from bot.keyboards.inline.search import search_keyboard

from database.models import TargetsManager


async def handler_get_random(cb: types.CallbackQuery, state: FSMContext) -> None:
    await state.finish()

    random_teammate = TargetsManager.getRandomUser(cb.from_user.id)
    
    if "type" in random_teammate and random_teammate['type'] == 'error':

        msg = "Нет активных пользователей"

        await cb.answer(text=msg)
    
    else:

        await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)

        await state.update_data(id=random_teammate[0])
        await state.update_data(tg_id=random_teammate[1])

        with open(f'./config/assets/{random_teammate[9]}.jpg', 'rb') as ph:
            
            msg = f"Статус: {'Активен' if random_teammate[7] == True else 'Неактивен'}\n"\
                f"Имя: {random_teammate[6]}\n"\
                f"Рейтинг: {random_teammate[8]}\n"\
                f"Позиция: {random_teammate[9]}\n"\
                f"Предпочтения по серверам: {random_teammate[10]}\n"\
                f"\n{random_teammate[11]}\n"

            await RandomSearchState.next.set()
            await bot.send_photo(chat_id=cb.from_user.id,photo=ph,parse_mode="HTML",caption=msg,reply_markup=search_keyboard)