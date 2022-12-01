from aiogram.dispatcher.filters.state import StatesGroup, State


class NewClothes(StatesGroup):
    get_title = State()
    get_description = State()
    get_contacts = State()
    get_size = State()
    get_image = State()


class NewShoes(StatesGroup):
    get_title = State()
    get_description = State()
    get_contacts = State()
    get_size = State()
    get_image = State()
    

class DeleteAd(StatesGroup):
    get_title = State()
