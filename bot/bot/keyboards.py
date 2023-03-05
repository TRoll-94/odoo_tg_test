"""
bot keyboards
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import texts


def get_base_menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Base meny keyboard
    :return:
    """
    kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.insert(KeyboardButton(texts.btn_my_deals))
    kb.insert(KeyboardButton(texts.btn_change_my_name))
    return kb
