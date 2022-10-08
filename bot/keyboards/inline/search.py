from aiogram import types


search_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Связатся", callback_data="ADD_TO_TEAM"))\
    .add(types.InlineKeyboardButton("Дальше", callback_data="SEARCH_NEXT"))\
    .add(types.InlineKeyboardButton("Вернуться", callback_data="BACK_TO_MENU"))