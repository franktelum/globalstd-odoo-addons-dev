# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Checklist(models.Model):
    _name = 'gsos.checklist'
    _description = 'Checklist'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    template_url = fields.Char(
        string='Template',
        help=None,
        readonly=False,
        required=True,
        groups=[])
