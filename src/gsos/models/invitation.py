# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Invitation(models.Model):
    _name = "gsos.invitation"
    _description = 'gsos.invitation'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Code',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    email = fields.Char(
        string='Email',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    notes = fields.Text(
        string='Notes',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    documents = fields.One2many(
        comodel_name='ir.attachment',
        inverse_name='gsos_invitation_id',
        string=None,
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('sent', 'Sent'),
          ('accepted', 'Accepted'),
          ('rejected', 'Rejected')
        ],
        string='State',
        default='draft',
        help=None,
        readonly=False,
        required=False,
        groups=[])
