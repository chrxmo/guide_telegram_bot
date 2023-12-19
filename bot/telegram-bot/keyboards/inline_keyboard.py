from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_keyboard(hotels: list, page: int):
    keyboard_builder = InlineKeyboardBuilder()
    length = round(len(hotels) / 10)

    if page > 1:
        keyboard_builder.button(text='<--', callback_data=f'pages_{page - 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')
    keyboard_builder.button(text=f'{page}/{length}', callback_data='None')
    if page == length:
        keyboard_builder.button(text='⛔️', callback_data='None')
    else:
        keyboard_builder.button(text='-->', callback_data=f'pages_{page + 1}')

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()
