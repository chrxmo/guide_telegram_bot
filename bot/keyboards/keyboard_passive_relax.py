from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard_passive_relax = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Кино'
        ),
        KeyboardButton(
            text='Парк'
        ),
        KeyboardButton(
            text='Библиотека'
        ),
        KeyboardButton(
            text='Театр'
        ),
        KeyboardButton(
            text='Музей'
        ),
        KeyboardButton(
            text='Цирк'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True)
