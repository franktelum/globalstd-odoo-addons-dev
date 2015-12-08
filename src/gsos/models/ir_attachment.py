# -*- coding: utf-8 -*-

from openerp import models, fields, api

class IrAttachment(models.Model):
    _inherit = ['ir.attachment']

    gsos_invitation_id = fields.Many2one(
        comodel_name='gsos.invitation',
        string='Invitation',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)
