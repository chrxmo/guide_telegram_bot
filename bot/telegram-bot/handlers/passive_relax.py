from aiogram.types import Message
import sqlite3


async def passive_relax(message: Message):
    connection = sqlite3.connect('passive_relax.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM passive_relax WHERE relax = ?', [message.text])
    passive_relax = cursor.fetchall()

    text = ''
    count = 0
    for relax in passive_relax:
        count += 1
        text += f'{count}. {relax[1]}| {relax[2]} | {relax[3]}\n'

    if text == '':
        await message.answer('К сожалению, ничего не найдено.')
    else:
        await message.answer(text=text)
