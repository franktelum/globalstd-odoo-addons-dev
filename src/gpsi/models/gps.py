# -*- coding: utf-8 -*-

from openerp import models, fields, api

class GpsCertificacionTipo(models.Model):
    _name = 'gps.certificacion.tipo'
    _description = 'gps.certificacion.tipo'

    name = fields.Char(string='Name')

class GpsHabilidades(models.Model):
    _name = 'gps.habilidades'
    _description = 'gps.habilidades'

    name = fields.Char(related='nombre', string='Name')

    fields.Selection(
        selection=[
          ('key', 'value')
        ],
        string='TextField',
        help=None,
        readonly=False,
        required=False,
        groups=[])
        
    id_habilidad = fields.Integer(string='Id Habilidad')
    nombre = fields.Char(string='Nombre')
    tipo = fields.Integer(string='Tipo')
    description = fields.Char(string='Description')
    id_padre = fields.Many2one(comodel_name='gps.habilidades', string='Id Padre')
    no_horas = fields.Integer(string='No Horas')
    costo_persona = fields.Float(string='Costo Persona')
    tipo_moneda = fields.Integer(string='Tipo Moneda')
    es_seminario = fields.Boolean(string='¿Es Seminario?')
    abrevacion = fields.Char(string='Abreviación')
    tipo_curso = fields.Char(string='Tipo Curso')
    manual = fields.Char(string='Manual')

class GpsClientes(models.Model):
    _name = 'gps.clientes'
    _description = 'gps.clientes'

    name = fields.Char(related='clave_cliente', string='Name')

    clave_cliente = fields.Char(string='Clave')
    nombre_cliente = fields.Char(string='Nombre')
    domicilio = fields.Char(string='Domicilio')
    telefono = fields.Char(string='Teléfono')
    correos = fields.Char(string='Correos')
    rfc = fields.Char(string='RFC')
    domicilio_fiscal = fields.Char(string='Domicilio Fiscal')
    ciudad = fields.Char(string='Ciudad')
    cp = fields.Char(string='CP')
    estado = fields.Char(string='Estado')
    sitio_web = fields.Char(string='Sitio Web')
    no_empleados = fields.Char(string='No Empleados')
    id_referencia = fields.Char(string='Referencia')
    nombre_contacto = fields.Char(string='Nombre Contacto')
    correo_contacto = fields.Char(string='Correo Contacto')
    puesto_contacto = fields.Char(string='Puesto Contacto')
    baja = fields.Boolean(string='Baja')
    id_cliente = fields.Char(string='Id Cliente')
    id_cliente_padre = fields.Many2one(comodel_name='gps.clientes', string='Id Cliente Padre')
    perfil = fields.Char(string='Perfil')
    archivo_perfil = fields.Char(string='Archivo Perfil')
    nick_name = fields.Char(string='Nick Name')
    password = fields.Char(string='Password')
    id_oficina = fields.Char(string='Id Oficina')
    id_md5_qms = fields.Char(string='Id MQ5QMS')
    id_ref_prog = fields.Char(string='Coordinador Logistica')
    recommended = fields.Many2one(comodel_name='gps.recommended', string='Recommended')
    id_leader_sales = fields.Char(string='Leader Sales')
    id_fuente = fields.Many2one(comodel_name='gps.fuente', string='Fuente')

class GpsContratos(models.Model):
    _name = 'gps.contratos'
    _description = 'gps.contratos'

    name = fields.Char(related='no_contrato', string='Name')

    no_contrato = fields.Char(string='No Contrato')
    id_habilidad = fields.Many2one(comodel_name='gps.habilidades', string='Habilidad')
    esquema = fields.Char(string='Esquema')
    ap_diseno = fields.Boolean(string='¿Diseño?')
    multisitio = fields.Boolean(string='¿Multisitio?')
    bilingue = fields.Boolean(string='¿Bilingue?')
    nivel_riesgo = fields.Char(string='Nivel Riesgo')
    duracion = fields.Integer(string='Duracion')
    fecha_contrato = fields.Date(string='Fecha Contrato')
    notas = fields.Char(string='Notas')
    cancelado = fields.Boolean(string='¿Cancelado?')
    transferencia = fields.Boolean(string='¿Transferencia?')
    archivo_contrato = fields.Char(string='Archivo Contrato')
    archivo_cuestionario = fields.Char(string='Archivo Cuestionario')
    archivo_carta = fields.Char(string='Archivo Carta')
    archivo_cotizacion = fields.Char(string='Archivo Cotización')
    archivo_transferencia = fields.Char(string='Archivo Transferencia')
    id_contrato = fields.Char(string='Id Contrato')
    id_cliente = fields.Char(string='Id Cliente')
    id_revisor = fields.Integer(string='Id Revisor')
    estado_revisor = fields.Char(string='Estado Revisor')
    nota_revisor = fields.Char(string='Nota Revisor')
    id_ventas = fields.Char(string='Id Ventas')
    fee01 = fields.Float(string='Fee01')
    fee02 = fields.Float(string='Fee02')
    fee03 = fields.Float(string='Fee03')
    ciclo_contrato = fields.Integer(string='Ciclo Contrato')
    moneda_tipo = fields.Integer(string='Moneda')
    moneda_tipo_cambio = fields.Float(string='Tipo de Cambio')
    recertificacion = fields.Boolean(string='¿Recertificación?')
    finalizado = fields.Boolean(string='¿Finalizado?')
    archivo_certificado = fields.Char(string='Archivo Certificado')
    informacion_avance = fields.Char(string='Información Avance')
    fechainicio = fields.Date(string='Fecha Inicio')
    fechafin = fields.Date(string='Fecha Fin')
    tipocertificacion = fields.Char(string='Tipo Certificación')
    mostrarnace = fields.Boolean(string='¿Mostrar NACE?')
    tipoesquema = fields.Char(string='Tipo Esquema')
    bloquearcontrato = fields.Boolean(string='¿Bloquear Contrato?')
    estatus_certificado = fields.Integer(string='Estatus Certificado')
    haccp = fields.Integer(string='HACCP')
    aplica_viaticos = fields.Char(string='Aplica Viaticos')
    id_md5_qms = fields.Float(string='Id Md5 Qms')
    observaciones_viaticos = fields.Char(string='Observaciones Viaticos')
    report_time = fields.Float(string='Report Time')
    archivo_rev_auditor = fields.Char(string='Archivo Rev. Auditor')

class GpsEventos(models.Model):
    _name = 'gps.eventos'
    _description = 'gps.eventos'

    name = fields.Char(related='numero_trabajo', string='Name')

    numero_trabajo = fields.Char(string='Número de Trabajo')
    id_habilidad = fields.Many2one(comodel_name='gps.habilidades', string='Id Habilidad')
    domicilio = fields.Char(string='Domicilio')
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_termino = fields.Date(string='Fecha Termino')
    estado_evento = fields.Integer(string='Estado Evento')
    tipo_evento = fields.Integer(string='Tipo Evento')
    introduccion = fields.Char(string='Introducción')
    pago = fields.Float(string='Pago')
    fecha_aviso = fields.Date(string='Fecha Aviso')
    comentarios = fields.Char(string='Comentarios')
    id_revisor = fields.Integer(string='Revisor')
    estado_revisor = fields.Integer(string='Estado Revisor')
    nota_revisor = fields.Char(string='Nota Revisor')
    id_comite = fields.Integer(string='Id Comite')
    estado_comite = fields.Integer(string='Estado Comite')
    nota_comite = fields.Char(string='Nota Comite')
    id_client_service = fields.Integer(string='Id Client Service')
    no_seguimiento_trans = fields.Integer(string='No Seguimiento Trans')
    id_contrato = fields.Char(string='Id Contrato')
    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
    estado_republica = fields.Integer(string='Estado Republica')
    discapacidad = fields.Boolean(string='¿Discapacidad?')
    es_conferencia = fields.Boolean(string='¿Es Conferencia?')
    archivo_plan_auditoria = fields.Char(string='Archivo Plan Auditoría')
    id_ubicacion = fields.Char(string='Id Ubicación')
    archivo_reporte_auditoria = fields.Char(string='Archivo Reporte Auditoría')
    id_oficina = fields.Char(string='Id Oficina')
    ciudad = fields.Char(string='Ciudad')
    nota_auditor = fields.Char(string='Nota Auditor')
    estatus = fields.Integer(string='Estaus')
    fecha_envio_fssc = fields.Date(string='Fecha Envio FSSC')

class GpsFuente(models.Model):
    _name = 'gps.fuente'
    _description = 'gps.fuente'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

class GpsRecommended(models.Model):
    _name = 'gps.recommended'
    _description = 'gps.recommended'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])
