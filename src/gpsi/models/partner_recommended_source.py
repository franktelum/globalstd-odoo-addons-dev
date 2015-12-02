# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PartnerRecommendedSource(models.Model):
    _name = 'gpsi.partner.recommended.source'
    _description = 'Source'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=False,
        groups=[])
