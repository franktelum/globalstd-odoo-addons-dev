# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ResUsers(models.Model):
    _inherit = ['res.users']

    gsos_supplier_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='gsos_user_partner_rel',
        column1='user_id',
        column2='partner_id',
        string='Suppliers')
