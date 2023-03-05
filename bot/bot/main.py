""" Bot """
import logging

from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from handler import bot_handler
from helper import bot, dp, loop


def bot_init():
    """
    Bot main function
    :return:
    """
    loop.run_until_complete(bot_handler())

    # setup middleware
    dp.middleware.setup(LoggingMiddleware())

    # start polling
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)


async def shutdown(dispatcher: Dispatcher):
    """ Shutdown handler """
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    bot_init()
