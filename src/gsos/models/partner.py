# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = ['res.partner']

    gsos_user_ids = fields.One2many(
        comodel_name='res.users',
        inverse_name='partner_id',
        string='Users',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    gsos_client_ids = fields.Many2many(
        comodel_name='res.users',
        string='Clients')

    gsos_business_sector_id = fields.Many2one(
        comodel_name='gsos.business.sector',
        string='Business Sector',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)
