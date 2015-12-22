# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = ['res.partner']

    gpsi_rfc = fields.Char(string='RFC')
    gpsi_domicilio_fiscal = fields.Char(string='Domicilio Fiscal')
    gpsi_perfil = fields.Char(string='Perfil')
    gpsi_archivo_perfil = fields.Char(string='Archivo Perfil')
    gpsi_nick_name = fields.Char(string='Nick Name')
    gpsi_password = fields.Char(string='Password')
    gpsi_id_oficina = fields.Many2one(comodel_name='gps.oficinas', string='Id Oficina')
    gpsi_md5_qms = fields.Char(string='Md5QMS')
    gpsi_no_empleados = fields.Char(string='No Empleados')
    gpsi_recommended = fields.Many2one(comodel_name='gps.recommended', string='Id Recomendado')
    gpsi_id_leader_sales = fields.Integer(string='Id Leader Sales')
    gpsi_id_auditor = fields.Integer(string='Id Auditor Rec')
    gpsi_id_consultor = fields.Integer(string='Id Consultor Rec')
    gpsi_id_fuente = fields.Many2one(comodel_name='gps.fuente', string='Id Fuente')
    gpsi_id_referencia = fields.Integer(string='Id Referencia')
    gpsi_id_ref_prog = fields.Integer(string='Id Coordinador Logistica')
    gpsi_cve_cliente = fields.Char(string='Clave Cliente')

    gpsi_contract_ids = fields.One2many(
        comodel_name='gps.contratos',
        inverse_name='id_cliente',
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
        compute='_compute_quotation_count',
        string='Number quotations attached',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    @api.multi
    @api.depends('gpsi_contract_ids')
    def _compute_contract_count(self):
        for partner in self:
            partner.gpsi_contract_count = len(partner.gpsi_contract_ids)

    @api.multi
    @api.depends('gpsi_quotation_ids')
    def _compute_quotation_count(self):
        for partner in self:
            partner.gpsi_quotation_count = len(partner.gpsi_quotation_ids)
