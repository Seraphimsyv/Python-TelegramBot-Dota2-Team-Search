from aiogram import types
from aiogram.dispatcher import FSMContext

from config.env import *
from bot.settings import bot

from database.models import UsersManager, TeammatesManager


async def handler_teammates_confirm(cb: types.CallbackQuery, state: FSMContext) -> None:
    
    await state.finish()
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)

    sender = UsersManager.getUserById(cb.data.split('|')[1])
    recipient = UsersManager.getUserById(cb.data.split('|')[2])
    
    TeammatesManager.createPairIfNotExists(user_id=cb.data.split('|')[1], teammate_id=cb.data.split('|')[2])

    msg = f'<strong><a href="tg://user?id={sender.tg_id}">{recipient.name}</a> принял запрос</strong>'

    await bot.send_message(chat_id=sender.tg_id, text=msg, parse_mode="HTML")

    msg = f'<strong>Вы приняли запрос <a href="tg://user?id={sender.tg_id}">пользователя</a></strong>'

    await bot.send_message(chat_id=recipient.tg_id, text=msg, parse_mode="HTML")