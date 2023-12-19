from aiogram.fsm.state import StatesGroup, State


class Place(StatesGroup):
    HOTEL_PRICE = State()
    KITCHEN = State()
    ACTIVE_RELAX = State()
    PASSIVE_RELAX = State()
    WEATHER = State()
