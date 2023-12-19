from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def get_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    active_relax = ['Клуб виртуальной реальности', 'Батутный центр', 'Веревочный парк', 'Страйкбол', 'Катание на коньках', 'Лыжная база', 'Горнолыжная база', 'Компьютерный клуб', 'Полет на воздушном шаре', 'Тир', 'Дайвинг', 'Развлекательный центр', 'Ипподром', 'Скейтпарк', 'Зоопарк', 'Картинг']

    for relax in active_relax:
        keyboard_builder.add(KeyboardButton(text=relax))

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
