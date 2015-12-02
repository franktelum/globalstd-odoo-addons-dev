# -*- coding: utf-8 -*-

from openerp import models, fields, api

class GpsSource(models.Model):
    _name = 'gps.source'
    _description = 'Source'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

class GpsRecommended(models.Model):
    _name = 'gps.recommended'
    _description = 'Recommended'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])
