from aiogram import types


profile_not_active_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Активировать", callback_data="SET_ACTIVE"))

profile_with_targets_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton('Изменить анкету поиска для игроков', callback_data="REGISTRATION"))\
    .add(types.InlineKeyboardButton("Вернуться", callback_data="BACK_TO_MENU"))

profile_without_targets_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton('Изменить анкету поиска для игроков', callback_data="REGISTRATION"))\
    .add(types.InlineKeyboardButton('Настроить параметры поиска игроков', callback_data="SET_TARGETS"))\
    .add(types.InlineKeyboardButton("Вернуться", callback_data="BACK_TO_MENU"))