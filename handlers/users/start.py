import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import ADMINS, CHANNELS
from loader import dp, db, bot
# from keyboards.default.main import markup


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=1)
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        markup.insert(InlineKeyboardButton(text=chat.title, url=invite_link))
        channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"
    markup.insert(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Xush kelibsiz! {name}. Quyidagi kanallarga obuna bo'ling\n\n{channels_format}", reply_markup=markup, disable_web_page_preview=True)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name}. Quyidagi kanallarga obuna bo'ling\n\n{channels_format}", reply_markup=markup, disable_web_page_preview=True)
