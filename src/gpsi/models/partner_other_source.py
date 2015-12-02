# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PartnerOtherSource(models.Model):
    _name = 'gpsi.partner.other.source'
    _description = 'Other Source'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=False,
        groups=[])
