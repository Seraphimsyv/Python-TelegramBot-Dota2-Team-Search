from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot

from database.models import TargetsManager


async def handler_target_finish(cb: types.CallbackQuery, state: FSMContext) -> None:
    await state.update_data(region=cb.data)
    data = await state.get_data()

    target_data = {"user_id": cb.from_user.id}
    target_data.update(data)

    TargetsManager.setUserTargetIfNotExist(target_data)

    msg = "<strong>Критерии поиска сохранены</strong>\n\n"\
        "Что бы изменить критерии используйте комманду\n"\
        "<code>/set_targets</code>"
    
    await state.finish()
    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML")