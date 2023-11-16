from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    message_to_admin = State()