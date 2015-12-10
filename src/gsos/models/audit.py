# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Audit(models.Model):
    _name = 'gsos.audit'
    _description = 'Audit'
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

    supplier_id = fields.Many2one(
        comodel_name='res.partner',
        string='Supplier',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    checklist_id = fields.Many2one(
        comodel_name='gsos.checklist',
        string='Checklist',
        help=None,
        readonly=False,
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    date_proposed = fields.Date(
        string='Proposed Date',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    report_results_url = fields.Char(
        string='Report Results Url',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('sent', 'Sent'),
          ('scheduled', 'Scheduled'),
          ('cancelled', 'Cancelled'),
          ('done', 'Done')
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
            vals['name'] = self.env['ir.sequence'].next_by_code('gsos.audit') or 'New'

        result = super(Audit, self).create(vals)
        return result
