import os
import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import set_inline_keyboard_restaurants
from keyboards.kitchens import get_keyboard
from utils.states import Place

restaurants_list = []


async def restaurants_catalog(message: Message, state: FSMContext):
    await message.answer('Выберите тип кухни', reply_markup=get_keyboard())
    await state.set_state(Place.KITCHEN)


def get_restaurants_list(kitchen):
    connection = sqlite3.connect(os.getenv('DATABASE_RESTAURANTS_NAME'))
    cursor_db = connection.cursor()

    cursor_db.execute('SELECT * FROM restaurants WHERE kitchen LIKE ?', ["%"+kitchen+"%"])
    restaurants = cursor_db.fetchall()

    return restaurants


async def get_restaurants(message: Message, state: FSMContext):
    global restaurants_list
    restaurants_list = get_restaurants_list(message.text)

    text = ''
    for count in range(1, 11):
        try:
            text += (
                f'{count}. {restaurants_list[count - 1][1]} | {restaurants_list[count - 1][2]} | {restaurants_list[count - 1][3]} | '
                f'{restaurants_list[count - 1][4]} | {restaurants_list[count - 1][5]}\n{restaurants_list[count - 1][6]}\n\n')
        except:
            break

    await message.answer(text=text, reply_markup=set_inline_keyboard_restaurants(restaurants_list, 1))
    await state.clear()


async def restaurants_page(callback_data: CallbackQuery):
    page = int(callback_data.data.split('_')[1])

    text = ''
    for count in range((page - 1) * 10 + 1, page * 10 + 1):
        try:
            text += (f'{count}. {restaurants_list[count - 1][1]} | {restaurants_list[count - 1][2]} | {restaurants_list[count - 1][3]}'
                     f'{restaurants_list[count - 1][4]} | {restaurants_list[count - 1][5]}\n{restaurants_list[count - 1][6]}\n\n')
        except:
            break

    await callback_data.message.edit_text(text=text, reply_markup=set_inline_keyboard_restaurants(restaurants_list, page))
    await callback_data.answer()
