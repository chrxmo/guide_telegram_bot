import requests

from aiogram.types import Message

lat = 56.843416
lon = 60.647221
open_weather_token = 'fe0f5dfe29f430049a2e54eadd9d4f83'


def weather(lat, lon, open_weather_token):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric')
        data = r.json()

        tempr = data['main']['temp']
        max_tempr = data['main']['temp_max']
        min_tempr = data['main']['temp_min']
        wind = data['wind']['speed']

        return f'В Екатеринубрге сегодня {tempr} градуса(-ов), максимальная температура: {max_tempr}, минимальная: {min_tempr}, скорость ветра {wind} м/c'
    except Exception as ex:
        print(ex)
        return 'Данных не найдено'

async def weather_info(message: Message):
    await message.answer(text=weather(lat, lon, open_weather_token))