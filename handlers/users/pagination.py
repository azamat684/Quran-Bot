from aiogram import types
from keyboards.inline.keyboards import make_pagination_markup
from loader import dp
from data.utils import get_quran_surahs, get_oyatlar
from states.all import QuranState
from keyboards.inline.keyboards import pagination
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(text_contains="next", state=QuranState.sura)
async def get_next_chapters(call: types.CallbackQuery):
    step = call.data.split("_")[-1]
    data = get_quran_surahs(int(step) + 1, 9)
    await call.message.edit_reply_markup(reply_markup=make_pagination_markup(data, int(step) + 1))


@dp.callback_query_handler(text_contains="previous", state=QuranState.sura)
async def get_previous_chapters(call: types.CallbackQuery):
    step = call.data.split("_")[-1]
    data = get_quran_surahs(int(step) - 1, 9)
    await call.message.edit_reply_markup(reply_markup=make_pagination_markup(data, int(step) - 1))


@dp.callback_query_handler(text_contains="next", state=QuranState.oyat)
async def get_next_oyat(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    chapter = data.get("chapter")
    await call.answer(cache_time=5)
    step = call.data.split("_")[-1]
    markup = types.InlineKeyboardMarkup(row_width=2)
    oyat = get_oyatlar(chapter=chapter, index=int(step) + 1)
    markup.add(*pagination(step=int(step) + 1))
    await call.message.edit_text(oyat["text"], reply_markup=markup)


@dp.callback_query_handler(text_contains="previous", state=QuranState.oyat)
async def get_previous_oyat(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    chapter = data.get("chapter")
    await call.answer(cache_time=5)
    step = call.data.split("_")[-1]
    markup = types.InlineKeyboardMarkup(row_width=2)
    oyat = get_oyatlar(chapter=chapter, index=int(step) - 1)
    markup.add(*pagination(step=int(step) - 1))
    await call.message.edit_text(oyat["text"], reply_markup=markup)


