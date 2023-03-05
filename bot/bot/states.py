"""
Bot states
"""
from aiogram.utils.helper import Helper, HelperMode, Item


class UserStates(Helper):
    """
    User states
    """
    mode = HelperMode.snake_case

    SET_CHANGE_NAME_STATE = Item()
