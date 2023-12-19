from aiogram.utils.keyboard import InlineKeyboardBuilder


def set_inline_keyboard_hotel(captions: list, page: int):
    keyboard_builder = InlineKeyboardBuilder()
    pages = round(len(captions) / 10)

    if page > 1:
        keyboard_builder.button(text='<--', callback_data=f'pageshotel_{page - 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.button(text=f'{page}/{pages}', callback_data='None')

    if page < pages:
        keyboard_builder.button(text='-->', callback_data=f'pageshotel_{page + 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def set_inline_keyboard_restaurants(captions: list, page: int):
    keyboard_builder = InlineKeyboardBuilder()
    pages = round(len(captions) / 10)

    if page > 1:
        keyboard_builder.button(text='<--', callback_data=f'pagesrestaurants_{page - 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.button(text=f'{page}/{pages}', callback_data='None')

    if page < pages:
        keyboard_builder.button(text='-->', callback_data=f'pagesrestaurants_{page + 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def set_inline_keyboard_passive_relax(captions: list, page: int):
    keyboard_builder = InlineKeyboardBuilder()
    pages = round(len(captions) / 10)

    if page > 1:
        keyboard_builder.button(text='<--', callback_data=f'pagespassive_{page - 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.button(text=f'{page}/{pages}', callback_data='None')

    if page < pages:
        keyboard_builder.button(text='-->', callback_data=f'pagespassive_{page + 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def set_inline_keyboard_active_relax(captions: list, page: int):
    keyboard_builder = InlineKeyboardBuilder()
    pages = round(len(captions) / 10)

    if page > 1:
        keyboard_builder.button(text='<--', callback_data=f'pagesactive_{page - 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.button(text=f'{page}/{pages}', callback_data='None')

    if page < pages:
        keyboard_builder.button(text='-->', callback_data=f'pagesactive_{page + 1}')
    else:
        keyboard_builder.button(text='⛔️', callback_data='None')

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()
