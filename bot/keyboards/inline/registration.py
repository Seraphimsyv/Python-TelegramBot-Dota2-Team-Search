from aiogram import types


position_keyboard = types.InlineKeyboardMarkup()\
    .add(
        types.InlineKeyboardButton("1", callback_data="1"),
        types.InlineKeyboardButton("2", callback_data="2")
      )\
    .add(
        types.InlineKeyboardButton("3", callback_data="3"),
        types.InlineKeyboardButton("4", callback_data="4")
    )\
    .add(types.InlineKeyboardButton("5", callback_data="5"))


region_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Все равно", callback_data="Все равно"))


confirm_keyboard = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Верно", callback_data="CONFIRM"))\
    .add(types.InlineKeyboardButton("Изменить", callback_data="REGISTRATION"))