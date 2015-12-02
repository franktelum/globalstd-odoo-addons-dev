# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = ['res.partner']

    gpsi_contract_ids = fields.One2many(
        comodel_name='gpsi.contract',
        inverse_name='client_id',
        string='Contracts',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    gpsi_contract_count = fields.Integer(
        compute='_compute_contract_count',
        string='Number contracts attached',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    gpsi_quotation_ids = fields.One2many(
        comodel_name='gpsi.quotation',
        inverse_name='client_id',
        string='Quotations',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    gpsi_quotation_count = fields.Integer(
        compute='_compute_quitation_count',
        string='Number quotations attached',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    gpsi_employees_count = fields.Integer(
        string='No. Employees',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    gpsi_logistics_coordinator_id = fields.Many2one(
        comodel_name='res.partner',
        string='Logistics Coordinator',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    gpsi_source_id = fields.Many2one(
        comodel_name='gps.recommended',
        string='Source',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    @api.multi
    @api.depends('gpsi_contract_ids')
    def _compute_contract_count(self):
        for partner in self:
            partner.gpsi_contract_count = len(partner.gpsi_contract_ids)

    @api.multi
    @api.depends('gpsi_quotation_ids')
    def _compute_quitation_count(self):
        for partner in self:
            partner.gpsi_quotation_count = len(partner.gpsi_quotation_ids)
