import os
import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import set_inline_keyboard_hotel
from utils.states import Place

hotels_list = []


async def hotels_catalog(message: Message, state: FSMContext):
    await message.answer('Введите примерную цену за одну ночь')
    await state.set_state(Place.HOTEL_PRICE)


def get_hotel_list(user_price):
    connection = sqlite3.connect(os.getenv('DATABASE_HOTELS_NAME'))
    cursor_db = connection.cursor()

    price_spread = [user_price - 1000, user_price + 1000]

    cursor_db.execute('SELECT * FROM hotels WHERE price BETWEEN ? AND ? ORDER BY stars DESC', price_spread)
    hotels = cursor_db.fetchall()

    new_hotels = []
    for hotel in hotels:
        if hotel[3] == 0:
            stars = 'Без звёзд'
        else:
            stars = '⭐️' * hotel[3]

        new_hotel = (hotel[0], hotel[1], hotel[2], stars, hotel[4])
        new_hotels.append(new_hotel)

    return new_hotels


async def get_hotels(message: Message, state: FSMContext):
    global hotels_list
    hotels_list = get_hotel_list(int(message.text))

    text = ''
    for count in range(1, 11):
        try:
            text += f'{count}. {hotels_list[count - 1][0]} | {hotels_list[count - 1][1]} | {hotels_list[count - 1][2]} ₽ | {hotels_list[count - 1][3]} | {hotels_list[count - 1][4]}\n\n'
        except:
            break

    await message.answer(text=text, reply_markup=set_inline_keyboard_hotel(hotels_list, 1))
    await state.clear()


async def hotels_page(callback_data: CallbackQuery):
    page = int(callback_data.data.split('_')[1])

    text = ''
    for count in range((page - 1) * 10 + 1, page * 10 + 1):
        try:
            text += f'{count}. {hotels_list[count - 1][0]} | {hotels_list[count - 1][1]} | {hotels_list[count - 1][2]} ₽ | {hotels_list[count - 1][3]} | {hotels_list[count - 1][4]}\n\n'
        except:
            break

    await callback_data.message.edit_text(text=text, reply_markup=set_inline_keyboard_hotel(hotels_list, page))
    await callback_data.answer()
