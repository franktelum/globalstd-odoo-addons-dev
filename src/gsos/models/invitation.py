# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Invitation(models.Model):
    _name = "gsos.invitation"
    _description = 'Invitation'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Code',
        default='New',
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

    email = fields.Char(
        string='Email',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    notes = fields.Text(
        string='Notes',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    document_ids = fields.One2many(
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

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.invitation') or 'New'

        result = super(Invitation, self).create(vals)
        return result

    @api.multi
    def action_send_invitation(self):
        for record in self:
            record.state = 'sent'
        return

    @api.multi
    def action_accept_invitation(self):
        for record in self:
            record.state = 'accepted'
        return

    @api.multi
    def action_reject_invitation(self):
        for record in self:
            record.state = 'rejected'
        return
