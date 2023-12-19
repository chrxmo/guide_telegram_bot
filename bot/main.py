import asyncio
import logging
from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from utils.commands import set_commands
from utils.states import Place

from handlers.basic import start, commands_list
from handlers.hotels import hotels_catalog, get_hotels, hotels_page
from handlers.restaurants import restaurants_catalog, get_restaurants, restaurants_page
from handlers.passive_relax import passive_relax_catalog, get_passive_relax, passive_relax_page
from handlers.active_relax import active_relax_catalog, get_active_relax, active_relax_page
from handlers.weather import weather_info

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')


async def start_bot(bot: Bot):
    await set_commands(bot)



async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token)
    dp = Dispatcher()

    dp.startup.register(start_bot)

    dp.message.register(start, Command(commands='start'))
    dp.message.register(commands_list, Command(commands='help'))

    dp.message.register(hotels_catalog, Command(commands='hotels'))
    dp.message.register(get_hotels, Place.HOTEL_PRICE)
    dp.callback_query.register(hotels_page, F.data.startswith('pageshotel_'))

    dp.message.register(restaurants_catalog, Command(commands='restaurants'))
    dp.message.register(get_restaurants, Place.KITCHEN)
    dp.callback_query.register(restaurants_page, F.data.startswith('pagesrestaurants_'))

    dp.message.register(passive_relax_catalog, Command(commands='passive_relax'))
    dp.message.register(get_passive_relax, Place.PASSIVE_RELAX)
    dp.callback_query.register(passive_relax_page, F.data.startswith('pagespassive_'))

    dp.message.register(active_relax_catalog, Command(commands='active_relax'))
    dp.message.register(get_active_relax, Place.ACTIVE_RELAX)
    dp.callback_query.register(active_relax_page, F.data.startswith('pagesactive_'))

    dp.message.register(weather_info, Command(commands='weather'))



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
