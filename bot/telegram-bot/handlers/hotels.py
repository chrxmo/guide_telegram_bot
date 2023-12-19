from aiogram import Bot
from aiogram.types import Message, CallbackQuery
import sqlite3
from keyboards.inline_keyboard import get_keyboard

hotels_list = []


async def hotels_catalog(message: Message, bot: Bot):
    await message.answer('Введите примерную цену')


def get_hotel_list(user_price):
    connection = sqlite3.connect('hotels.db')
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


async def get_hotels(message: Message):
    try:
        global hotels_list
        hotels_list = get_hotel_list(int(message.text))
    except:
        await message.answer('Вы неверно ввели цену!')
        hotels_list = None

    text = ''
    if not hotels_list or hotels_list == '':
        await message.answer('К сожалению ничего не найдено(')
    else:
        for count in range(1, 11):
            text += f'{count}. {hotels_list[count - 1][0]} | {hotels_list[count - 1][1]} | {hotels_list[count - 1][2]} | {hotels_list[count - 1][3]} | {hotels_list[count - 1][4]}\n\n'

        await message.answer(text=text, reply_markup=get_keyboard(hotels_list, 1))


async def hotels_page(callback_data: CallbackQuery):
    page = int(callback_data.data.split('_')[1])

    text = ''
    for count in range((page - 1) * 10 + 1, page * 10 + 1):
        try:
            text += f'{count}. {hotels_list[count - 1][0]} | {hotels_list[count - 1][1]} | {hotels_list[count - 1][2]} | {hotels_list[count - 1][3]} | {hotels_list[count - 1][4]}\n\n'
        except:
            pass

    await callback_data.message.edit_text(text=text, reply_markup=get_keyboard(hotels_list, page))
    await callback_data.answer()
