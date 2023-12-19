import os
import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import set_inline_keyboard_active_relax
from keyboards.keyboard_active_relax import get_keyboard
from utils.states import Place

active_relax_list = []


async def active_relax_catalog(message: Message, state: FSMContext):
    await message.answer('Выберите тип пассивного отдыха', reply_markup=get_keyboard())
    await state.set_state(Place.ACTIVE_RELAX)


def get_active_relax_list(active_relax):
    connection = sqlite3.connect(os.getenv('DATABASE_ACTIVE_RELAX_NAME'))
    cursor_db = connection.cursor()

    cursor_db.execute('SELECT * FROM active_relax WHERE relax = ?', [active_relax])
    active_relax_all = cursor_db.fetchall()
    print(active_relax_all)

    return active_relax_all


async def get_active_relax(message: Message, state: FSMContext):
    global active_relax_list
    active_relax_list = get_active_relax_list(message.text)
    print(active_relax_list)

    text = ''
    for count in range(1, 11):
        try:
            text += (
                f'{count}. {active_relax_list[count - 1][1]} | {active_relax_list[count - 1][2]} | '
                f'{active_relax_list[count - 1][3]}\n\n')
        except:
            break

    await message.answer(text=text, reply_markup=set_inline_keyboard_active_relax(active_relax_list, 1))
    await state.clear()


async def active_relax_page(callback_data: CallbackQuery):
    page = int(callback_data.data.split('_')[1])

    text = ''
    for count in range((page - 1) * 10 + 1, page * 10 + 1):
        try:
            text += (f'{count}. {active_relax_list[count - 1][1]} | {active_relax_list[count - 1][2]} | '
                     f'{active_relax_list[count - 1][3]}\n\n')
        except:
            break

    await callback_data.message.edit_text(text=text, reply_markup=set_inline_keyboard_active_relax(active_relax_list, page))
    await callback_data.answer()
