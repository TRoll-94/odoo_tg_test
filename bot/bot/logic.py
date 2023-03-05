"""
Bot logic file
"""
from typing import Union

from odoo_rpc_client.orm import record

import texts
from helper import Odoo


def who_im(tg_id) -> Union[record.Record, None]:
    """
    Get user by tg_id form odoo
    :param tg_id:
    :return:
    """

    Users = Odoo['tg.users']
    users = Users.search_records([['tg_id', '=', tg_id]])
    if len(users) > 0:
        return users[0]
    return None


def leads_by_user(uid) -> record.RecordList:
    """
    Get list of leads by user id
    :param uid:
    :return:
    """
    Leads = Odoo['crm.lead']
    return Leads.search_read([['user_id', '=', uid]])


def update_user_name(uid, name) -> bool:
    """
    Change user name
    :param uid:
    :param name:
    :return:
    """
    Users = Odoo['res.users']
    return Users.write(uid, {'name': name})


def validate_name(name) -> tuple[bool, str]:
    """
    Name validate
    1. The name must be two words
    2. Each name must be at least two characters long
    :param name:
    :return:
    """
    name = name.split(' ')
    if len(name) != 2:
        return False, texts.err_name_not_complete
    name = all([len(x) > 2 for x in name])
    if not name:
        return False, texts.err_name_is_short
    return True, ''



