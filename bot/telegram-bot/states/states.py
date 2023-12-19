from aiogram.fsm.state import StatesGroup, State



class Place(StatesGroup):
    restaurant = State()
    hotel = State()
    active_relax = State()
    passive_relax = State()
    more = State()