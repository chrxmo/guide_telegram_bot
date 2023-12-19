import os
import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import set_inline_keyboard_passive_relax
from keyboards.keyboard_passive_relax import keyboard_passive_relax
from utils.states import Place

passive_relax_list = []


async def passive_relax_catalog(message: Message, state: FSMContext):
    await message.answer('Выберите тип пассивного отдыха', reply_markup=keyboard_passive_relax)
    await state.set_state(Place.PASSIVE_RELAX)


def get_passive_relax_list(passive_relax):
    connection = sqlite3.connect(os.getenv('DATABASE_PASSIVE_RELAX_NAME'))
    cursor_db = connection.cursor()

    cursor_db.execute('SELECT * FROM passive_relax WHERE relax = ?', [passive_relax])
    passive_relax_all = cursor_db.fetchall()
    print(passive_relax_all)

    return passive_relax_all


async def get_passive_relax(message: Message, state: FSMContext):
    global passive_relax_list
    passive_relax_list = get_passive_relax_list(message.text)

    text = ''
    for count in range(1, 11):
        try:
            text += (
                f'{count}. {passive_relax_list[count - 1][1]} | {passive_relax_list[count - 1][2]} | '
                f'{passive_relax_list[count - 1][3]}\n\n')
        except:
            break

    await message.answer(text=text, reply_markup=set_inline_keyboard_passive_relax(passive_relax_list, 1))
    await state.clear()


async def passive_relax_page(callback_data: CallbackQuery):
    page = int(callback_data.data.split('_')[1])

    text = ''
    for count in range((page - 1) * 10 + 1, page * 10 + 1):
        try:
            text += (f'{count}. {passive_relax_list[count - 1][1]} | {passive_relax_list[count - 1][2]} | '
                     f'{passive_relax_list[count - 1][3]}\n\n')
        except:
            break

    await callback_data.message.edit_text(text=text, reply_markup=set_inline_keyboard_passive_relax(passive_relax_list, page))
    await callback_data.answer()
