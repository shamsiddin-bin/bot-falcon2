# keyboards.py
"""
Botda ishlatiladigan barcha Reply klaviaturalar shu yerda.
Faqat Reply Keyboard ishlatiladi (Web App tugmasi ham reply klaviatura ichida).
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

import config
from locales import t, LANGUAGE_BUTTONS


def language_keyboard() -> ReplyKeyboardMarkup:
    """Til tanlash klaviaturasi."""
    buttons = [[KeyboardButton(text=label)] for label in LANGUAGE_BUTTONS.keys()]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def main_menu_keyboard(lang: str, is_admin: bool = False) -> ReplyKeyboardMarkup:
    """
    Asosiy Reply menyu. Birinchi tugma - Web App.
    Admin bo'lsa, qo'shimcha 'Admin Panel' tugmasi qo'shiladi.
    """
    keyboard = [
        [KeyboardButton(text=t(lang, "btn_webapp"), web_app=WebAppInfo(url=config.WEBAPP_URL))],
        [KeyboardButton(text=t(lang, "btn_announcements")), KeyboardButton(text=t(lang, "btn_schedule"))],
        [KeyboardButton(text=t(lang, "btn_payment")), KeyboardButton(text=t(lang, "btn_language"))],
        [KeyboardButton(text=t(lang, "btn_contact"))],
    ]

    if is_admin:
        keyboard.append([KeyboardButton(text=t(lang, "btn_admin"))])

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def admin_menu_keyboard(lang: str) -> ReplyKeyboardMarkup:
    """Admin panel ichidagi Reply menyu."""
    keyboard = [
        [KeyboardButton(text=t(lang, "btn_admin_add_announcement"))],
        [KeyboardButton(text=t(lang, "btn_admin_update_schedule"))],
        [KeyboardButton(text=t(lang, "btn_admin_stats"))],
        [KeyboardButton(text=t(lang, "btn_back"))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def back_keyboard(lang: str) -> ReplyKeyboardMarkup:
    """Faqat 'Orqaga' tugmasi bo'lgan klaviatura (masalan admin kutish holatida)."""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(lang, "btn_back"))]],
        resize_keyboard=True,
    )
