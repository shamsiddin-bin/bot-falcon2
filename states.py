# states.py
"""Bot ichidagi FSM (holat) guruhlari."""

from aiogram.fsm.state import State, StatesGroup


class AdminStates(StatesGroup):
    waiting_announcement = State()
    waiting_schedule = State()


class PaymentStates(StatesGroup):
    waiting_amount = State()
