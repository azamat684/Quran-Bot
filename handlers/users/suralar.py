from aiogram import types
from keyboards.inline.keyboards import make_pagination_markup
from loader import dp
from data.utils import get_quran_surahs
from states.all import QuranState


@dp.message_handler(text="📖 Suralar")
async def bot_echo(message: types.Message):
    data = get_quran_surahs(1, 9)
    await message.answer("Oʻzingizga kerakli surani tanlang", reply_markup=make_pagination_markup(data, 1))
    await QuranState.sura.set()