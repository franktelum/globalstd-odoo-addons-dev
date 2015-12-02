# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Checklist(models.Model):
    _name = "gsos.checklist"

    name = fields.Char(
        string='Name',
        required=True)

    checklist_template_url = fields.Char(
        string='Checklist Url',
        help=None,
        readonly=False,
        required=True,
        groups=[])
