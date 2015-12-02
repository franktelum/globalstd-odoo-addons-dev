# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BusinessSector(models.Model):
    _name = 'gsos.business.sector'
    _description = 'Business Sector'

    name = fields.Char(
        string='Name',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    parent_id = fields.Many2one(
        comodel_name='gsos.business.sector',
        string='Parent',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)
