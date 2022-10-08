from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot
from bot.keyboards.inline.profile import profile_not_active_keyboard
from bot.keyboards.inline.profile import profile_with_targets_keyboard
from bot.keyboards.inline.profile import profile_without_targets_keyboard

from database.models import UsersManager
from database.models import TargetsManager

from datetime import datetime


async def handler_profile(cb: types.CallbackQuery, state: FSMContext) -> None:
    await state.finish()

    try:
        await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    except: ...

    user = UsersManager.getUserById(cb.from_user.id)
    targets = TargetsManager.getUserTargets(cb.from_user.id)

    # f"\n<strong></strong> - {}"\
    msg = "<strong>Профиль пользователя</strong>"\
            f"\n<strong>ID</strong> - {user.tg_id}"\
              f"\n<strong>Статус</strong> - {'Активен' if user.status == True else 'Не активен'}"\
                f"\n<strong>Имя</strong> - {user.name if user.name != '' else 'undefiend'}"\
                  f"\n<strong>Username</strong> - {'@' + user.username if user.username != '' else 'undefiend'}"\
                    f"\n<strong>Дата регистрации</strong> - {datetime.strftime(datetime.fromtimestamp(user.registration_timestamp), '%m/%d/%Y %H:%M:%S')}"\
          "\n"\
          f"\n<strong>Настройки поиска в системе</strong>"\
            f"\n<strong>Рейтинг</strong> - {user.rate}"\
              f"\n<strong>Позиция</strong> - {user.position}"\
                f"\n<strong>Регион поиска игр</strong> - {user.region}"\
                  f"\n<strong>Описание</strong> - {user.description}"

    if targets != None:
      msg += "\n"\
          f"\n<strong>Настройки желаемого поиска в системе</strong>"\
            f"\n<strong>Рейтинг</strong> - {targets[2]}"\
              f"\n<strong>Позиция</strong> - {targets[3]}"\
                f"\n<strong>Регион поиска игр</strong> - {targets[4]}"

    if targets != None:
        keyboard = profile_with_targets_keyboard
    else:
        keyboard = profile_without_targets_keyboard

    if user.status == False:
        keyboard = profile_not_active_keyboard

    await bot.send_message(chat_id=cb.from_user.id, text=msg, parse_mode="HTML", reply_markup=keyboard)