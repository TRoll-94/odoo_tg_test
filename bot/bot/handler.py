"""
Bot handler file
"""
import logging

from aiogram import types

import logic
import texts
import keyboards as kb
from helper import dp, bot
from states import UserStates


async def bot_handler():
    """ Check bot """
    me = await bot.get_me()
    logging.info(me)


@dp.message_handler(commands=['start'])
async def who_im_handler(message: types.Message):
    """ Check user in odoo """
    im = logic.who_im(message.from_user.id)
    if im is None:
        return await message.answer(texts.user_not_found)
    await message.answer(texts.user_info.format(tg_user=im), reply_markup=kb.get_base_menu_keyboard())


@dp.message_handler(lambda m: m.text == texts.btn_my_deals)
async def my_deals_handler(message: types.Message):
    """
    Show user deals
    :param message:
    :return:
    """
    im = logic.who_im(message.from_user.id)
    if im is None:
        return await message.answer(texts.user_not_found)
    leads = logic.leads_by_user(im.user_id.id)
    for lead in leads:
        msg = texts.deal_short_desc.format(lead['name'], lead['user_id'][1], lead['description'])
        await bot.send_message(message.chat.id, msg)


@dp.message_handler(lambda m: m.text == texts.btn_change_my_name)
async def change_my_name_start_handler(message: types.Message):
    """
    Show user deals
    :param message:
    :return:
    """
    im = logic.who_im(message.from_user.id)
    if im is None:
        return await message.answer(texts.user_not_found)

    state = dp.current_state(chat=message.chat.id)
    await state.set_state(UserStates.SET_CHANGE_NAME_STATE)
    await message.answer(f"{texts.write_name}:")


@dp.message_handler(state=UserStates.SET_CHANGE_NAME_STATE)
async def change_my_name_process_handler(message: types.Message):
    """
    Show user deals
    :param message:
    :return:
    """
    is_valid, desc = logic.validate_name(message.text)
    if not is_valid:
        return await message.answer(texts.err_name_msg.format(desc))

    im = logic.who_im(message.from_user.id)
    logic.update_user_name(im.user_id.id, message.text)
    await message.answer(f"{texts.change_name_success}!", reply_markup=kb.get_base_menu_keyboard())

    state = dp.current_state(chat=message.chat.id)
    await state.reset_state()
