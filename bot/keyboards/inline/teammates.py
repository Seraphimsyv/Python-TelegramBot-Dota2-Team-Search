from aiogram import types


add_or_decline_menu = types.InlineKeyboardMarkup()\
    .add(types.InlineKeyboardButton("Принять", callback_data="CONFIRM"))\
    .add(types.InlineKeyboardButton("Отклонить", callback_data="DECLINE"))