from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def pagination(step):
    previous = InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"previous_{step}")
    next = InlineKeyboardButton(text="➡️ Keyingi", callback_data=f"next_{step}")
    return [previous, next]

def make_pagination_markup(data, step):
    markup = InlineKeyboardMarkup(row_width=3)
    for key, value in data.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=value))
    markup.add(*pagination(step))
    return markup