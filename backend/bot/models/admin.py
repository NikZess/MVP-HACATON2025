from aiogram.fsm.state import State, StatesGroup

class AddAdmin(StatesGroup):
    password = State()
