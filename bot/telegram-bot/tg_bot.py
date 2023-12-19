from aiogram import types, Bot, Dispatcher, F
from aiogram.types import CallbackQuery

from config import bot_token, open_weather_token
import asyncio
import logging
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.states import Place
from keyboards.keyboards import restaurant_keyboard, active_relax_keyboard, passive_relax_keyboard, start_keyboard

from handlers.weather import lat, lon, weather


from handlers.restaurants import kitchen_catalog
from handlers.active_relax import active_relax
from handlers.passive_relax import passive_relax
from handlers.hotels import get_hotels, hotels_page, hotels_list

from keyboards.inline_keyboard import get_keyboard

bot = Bot(token=bot_token)
dp = Dispatcher()




async def logs():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)



@dp.message(Command('weather'))
async def get_weather(message: types.Message):

    await message.answer(f'{weather(lat, lon, open_weather_token)}')



@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Здравствуйте, расскажите, куда бы вы хотели попасть?\nЧтобы увидеть список команд, используйте /help', reply_markup=start_keyboard)



@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer('Конечно! Вот список команд:\n/restaurants - если вы хотите посетить ресторан;\n/hotels - если вы хотите посетить отель;\n'
                              '/active_relax - если вы хотите посетить место для активного отдыха;\n/passive_relax - если вы хотите посетить место для пассивного отдыха;\n'
                         '/weather - если вам интересна погода в Екатеринбурге на сегодня;\n/help - если вам снова понадобится помощь.' )



@dp.message(Command('restaurants'))
async def restaurants(message: types.Message, state: FSMContext):

    await state.set_state(Place.restaurant)



    await message.answer('Расскажите, какую кухню вы хотите попробовать?', reply_markup=restaurant_keyboard)



@dp.message(Place.restaurant)
async def find_restaurant(message: types.Message, state: FSMContext):

    await kitchen_catalog(message)
    await state.clear()



@dp.message (Command("hotels"))
async def filter_hotels(message: types.Message, state: FSMContext):
    await state.set_state(Place.hotel)
    await message.answer("Укажите желаемую стоимость за ночь (например 3500).")

# @dp.callback_query_handler(F.data.startswith('pages_'))
# async def hotels_page(callback_data: CallbackQuery):
#     page = int(callback_data.data.split('_')[1])
#
#     text = ''
#     for count in range((page - 1) * 10 + 1, page * 10 + 1):
#         try:
#             text += f'{count}. {hotels_list[count - 1][0]} | {hotels_list[count - 1][1]} | {hotels_list[count - 1][2]} | {hotels_list[count - 1][3]} | {hotels_list[count - 1][4]}\n\n'
#         except:
#             pass
#
#     await callback_data.message.edit_text(text=text, reply_markup=get_keyboard(hotels_list, page))
#     await callback_data.answer()


@dp.message(Place.hotel)
async def find_hotel(message: types.Message):

    await get_hotels(message)
    await hotels_page()

# @dp.callback_query(F.data.startswith('pages_'), Place.hotel)
# async def hotels_page(callback_data: CallbackQuery, state: FSMContext):
#     page = int(callback_data.data.split('')[1])
#
#     text = ''
#     for count in range((page - 1) * 10 + 1, page * 10 + 1):
#         try:
#             text += f'{count}. {hotels_list[count - 1][0]} | {hotels_list[count - 1][1]} | {hotels_list[count - 1][2]} | {hotels_list[count - 1][3]} | {hotels_list[count - 1][4]}\n\n'
#         except:
#             pass
#
#     await callback_data.message.edit_text(text=text, reply_markup=get_keyboard(hotels_list, page))
#     await callback_data.answer()
#     await state.clear()

@dp.message(Command('active_relax'))
async def which_active_relax(message: types.Message, state: FSMContext):

    await state.set_state(Place.active_relax)
    await message.answer('Расскажите подробнее, что бы вы хотели.', reply_markup=active_relax_keyboard, )


@dp.message(Place.active_relax)
async def find_active_chill(message: types.Message, state: FSMContext):


    await active_relax(message)

    await state.clear()




@dp.message(Command('passive_relax'))
async def which_passive_relax(message: types.Message, state: FSMContext):

    await state.set_state(Place.passive_relax)
    await message.answer('Расскажите подробнее, что бы вы хотели', reply_markup=passive_relax_keyboard)



@dp.message(Place.passive_relax)
async def find_passive_chill(message: types.Message, state: FSMContext):

    await passive_relax(message)

    await state.clear()





if __name__ == '__main__':
    asyncio.run(logs())