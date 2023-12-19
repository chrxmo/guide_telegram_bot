from aiogram.types import Message
from keyboards.catalog import keyboard_catalog


async def start(message: Message):
    await message.answer(text='Выберите категорию.', reply_markup=keyboard_catalog)
