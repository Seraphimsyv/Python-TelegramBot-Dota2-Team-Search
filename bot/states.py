from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


memory_storage = MemoryStorage()


class RegistrationState(StatesGroup):
    name = State()
    rate = State()
    pos = State()
    desc = State()
    region = State()
    confirm = State()


class RandomSearchState(StatesGroup):
    next = State()


class TargetsSearchState(StatesGroup):
    rate = State()
    pos = State()
    region = State()
    next = State()


class ReportState(StatesGroup): ...