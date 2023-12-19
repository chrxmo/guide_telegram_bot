from aiogram.types import Message

import sqlite3


async def kitchen_catalog(message: Message):
    connection = sqlite3.connect('restaurants.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM restaurants WHERE kitchen LIKE ?', ["%"+message.text+"%"])
    restaurants = cursor.fetchall()

    text = ''
    count = 0
    for restaurant in restaurants:
        count += 1
        text += f'{count}. {restaurant[1]}| {restaurant[2]} | {restaurant[3]} | {restaurant[4]} | {restaurant[5][:-2]} | {restaurant[6]}\n\n'



    if text == '':
        await message.answer('К сожелению, ничего не найдено')
    else:
        await message.answer(text=text)
