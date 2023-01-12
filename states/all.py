from aiogram.dispatcher.filters.state import StatesGroup, State


class QuranState(StatesGroup):
    sura = State()
    oyat = State()
