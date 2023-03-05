"""
Bot settings file
"""

from os import getenv

ODOO_URL = getenv('BASE_URL')
ODOO_DB = getenv('BASE_DB')
ODOO_PORT = int(getenv('BASE_PORT'))
ODOO_USERNAME = getenv('BASE_USER')
ODOO_PASSWORD = getenv('BASE_PASSWORD')

TG_TOKEN = getenv('TG_TOKEN')

REDIS_HOST = 'redis'
REDIS_PORT = '6379'

