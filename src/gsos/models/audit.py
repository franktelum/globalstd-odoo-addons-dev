# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Audit(models.Model):
    _name = 'gsos.audit'
    _description = 'gsos.audit'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Code',
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

    checklist_id = fields.Many2one(
        comodel_name='gsos.checklist',
        string='Checklist',
        help=None,
        readonly=False,
        required=False,
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
