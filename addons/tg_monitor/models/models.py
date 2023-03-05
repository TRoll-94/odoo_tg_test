""" Models """

from odoo import models, fields


class TgUsersModel(models.Model):
    """
    Tg User model
    """
    _name = "tg.users"
    _description = "Tg user model description"

    tg_id = fields.Char('tg id', required=True)
    user_id = fields.Many2one('res.users', string="User")
