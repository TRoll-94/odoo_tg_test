"""
Bot helper file
"""

import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from odoo_rpc_client import Client

import settings


logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    logging.error("LOOP not founded. Trying to set new event loop.")
    loop = asyncio.new_event_loop()

bot = Bot(
    token=settings.TG_TOKEN,
)
storage = RedisStorage2(
    settings.REDIS_HOST,
    settings.REDIS_PORT,
    prefix='tg_bot'
)
dp = Dispatcher(bot, storage=storage, loop=loop)

Odoo = Client(
    settings.ODOO_URL,
    settings.ODOO_DB,
    settings.ODOO_USERNAME,
    settings.ODOO_PASSWORD,
    settings.ODOO_PORT
)
