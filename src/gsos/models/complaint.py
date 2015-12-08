# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Complaint(models.Model):
    _name = 'gsos.complaint'
    _description = 'Complaint'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Code',
        default='New',
        help=None,
        readonly=True,
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

    monitor = fields.Char(
        string='Monitor',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    supplier_id = fields.Many2one(
        comodel_name='res.partner',
        string='Supplier',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    reason = fields.Text(
        string='Reason',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        translate=False)

    severity = fields.Selection(
        selection=[
          ('low', 'Low'),
          ('medium', 'Medium'),
          ('high', 'High'),
        ],
        string='Severity',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.complaint') or 'New'

        result = super(Complaint, self).create(vals)
        return result
