from aiogram.types import Message
import sqlite3



async def active_relax(message: Message):
    connection = sqlite3.connect('active_relax.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM active_relax WHERE relax LIKE ? OR relax LIKE ?', ["%"+message.text+"%", "%"+message.text.lower()+"%"])
    active_relax = cursor.fetchall()

    text = ''
    count = 0
    for relax in active_relax:
        count += 1
        text += f'{count}. {relax[1]}| {relax[2]} | {relax[3]}\n'

    if text == '':
        await message.answer('К сожалению, ничего не найдено.')
    else:
        await message.answer(text=text)
