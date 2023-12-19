from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def get_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    kitchens = ['Восточная кухня', 'Общая кухня', 'Армянская кухня', 'Арабская кухня', 'Домашняя кухня', 'Сербская кухня', 'Американская кухня', 'Мексиканская кухня', 'Средиземноморская кухня', 'Кавказская кухня', 'Паназиатская кухня', 'Греческая кухня', 'Грузинская кухня', 'Авторская кухня', 'Испанская кухня', 'Украинская кухня', 'Адыгейская кухня', 'Чешская кухня', 'Европейская кухня', 'Узбекская кухня', 'Японская кухня', 'Итальянская кухня', 'Русская кухня']

    for kitchen in kitchens:
        keyboard_builder.add(KeyboardButton(text=kitchen))

    keyboard_builder.adjust(6)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)