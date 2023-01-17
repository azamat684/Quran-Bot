from aiogram import types
from utils.misc.subscription import check
from data.config import ADMINS, CHANNELS
from loader import dp, db, bot
from keyboards.default.main import markup


@dp.callback_query_handler(text="check_subs")
async def check_channel_member(call: types.CallbackQuery):
    user_id = call.from_user.id
    final_status = True
    result = ""
    for channel in CHANNELS:
        status = await check(user_id=user_id, channel=channel)
        channel = await bot.get_chat(channel)

        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"

        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n"

    if final_status:
        await call.message.delete()
        await call.message.answer("Siz barcha kanallarga obuna bo'lgan ekansiz. Botdan foydalanishingiz mumkin", reply_markup=markup)
    else:
        inline_markup = types.InlineKeyboardMarkup(row_width=1)
        inline_markup.insert(types.InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
        await call.message.edit_text(result, disable_web_page_preview=True, reply_markup=inline_markup)
