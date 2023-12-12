from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    message_to_admin = State()

    add_new_category = State()
    add_new_item = State()

    enter_manually = State()