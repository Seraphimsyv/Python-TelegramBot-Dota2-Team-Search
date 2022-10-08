from aiogram import types


register_user_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Профиль", callback_data="PROFILE"))\
    .add(types.InlineKeyboardButton("Поиск тимейта по критериям", callback_data="SEARCH_WITH_TARGETS"))\
    .add(types.InlineKeyboardButton("Поиск случайного тимейта", callback_data="SEARCH_RANDOM"))\
    .add(types.InlineKeyboardButton("Список тимейтов", callback_data="TEAMMATES_LIST"))

unregister_user_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Пройти регистрацию", callback_data="REGISTRATION"))