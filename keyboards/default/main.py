from aiogram.types import ReplyKeyboardMarkup

markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup.row("📖 Suralar")
markup.row("📝 Oyatlar")
markup.row("🔎 Umumiy izlash")