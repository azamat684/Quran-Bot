from aiogram import types
from loader import dp
from states.all import QuranState
from data.utils import get_oyatlar
from keyboards.inline.keyboards import pagination
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(state=QuranState.sura)
async def get_chapter_data(call: types.CallbackQuery, state: FSMContext):
    chapter = call.data
    await state.update_data({"chapter": chapter})
    markup = types.InlineKeyboardMarkup(row_width=2)
    oyat = get_oyatlar(chapter=chapter, index=1)
    markup.add(*pagination(step=chapter))
    await call.message.edit_text(oyat["text"], reply_markup=markup)
    await QuranState.next()

