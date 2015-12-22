# -*- coding: utf-8 -*-

from openerp import models, fields, api

class GpsCertificacionTipo(models.Model):
    _name = 'gps.certificacion.tipo'
    _description = 'gps.certificacion.tipo'

    name = fields.Char(string='Name')

class GpsHabilidades(models.Model):
    _name = 'gps.habilidades'
    _description = 'gps.habilidades'

    _rec_name = 'nombre'

    #id_habilidad = fields.Integer(string='Id Habilidad')
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

# class GpsClientes(models.Model):
#     _name = 'gps.clientes'
#     _description = 'gps.clientes'
#
#     _rec_name = 'nombre_cliente'
#
#     clave_cliente = fields.Char(string='Clave')
#     nombre_cliente = fields.Char(string='Nombre')
#     domicilio = fields.Char(string='Domicilio')
#     telefono = fields.Char(string='Teléfono')
#     correos = fields.Char(string='Correos')
#     rfc = fields.Char(string='RFC')
#     domicilio_fiscal = fields.Char(string='Domicilio Fiscal')
#     ciudad = fields.Char(string='Ciudad')
#     cp = fields.Char(string='CP')
#     estado = fields.Char(string='Estado')
#     sitio_web = fields.Char(string='Sitio Web')
#     no_empleados = fields.Char(string='No Empleados')
#     id_referencia = fields.Many2one(comodel_name='res.users', string='Id Referencia')
#     nombre_contacto = fields.Char(string='Nombre Contacto')
#     correo_contacto = fields.Char(string='Correo Contacto')
#     puesto_contacto = fields.Char(string='Puesto Contacto')
#     baja = fields.Boolean(string='Baja')
#     #id_cliente = fields.Char(string='Id Cliente')
#     id_cliente_padre = fields.Many2one(comodel_name='gps.clientes', string='Id Cliente Padre')
#     perfil = fields.Char(string='Perfil')
#     archivo_perfil = fields.Char(string='Archivo Perfil')
#     nick_name = fields.Char(string='Nick Name')
#     password = fields.Char(string='Password')
#     id_oficina = fields.Many2one(comodel_name='gps.oficinas', string='Id Oficinas')
#     id_md5_qms = fields.Char(string='Id MQ5QMS')
#     id_ref_prog = fields.Many2one(comodel_name='res.users', string='Coordinador Logistica')
#     recommended = fields.Many2one(comodel_name='gps.recommended', string='Recommended')
#     id_leader_sales = fields.Many2one(comodel_name='res.users', string='Leader Sales')
#     id_fuente = fields.Many2one(comodel_name='gps.fuente', string='Fuente')

class GpsContratos(models.Model):
    _name = 'gps.contratos'
    _description = 'gps.contratos'
    _inherit = ['mail.thread']

    _rec_name = 'no_contrato'

    no_contrato = fields.Char(string='No Contrato', default='New')
    esquema = fields.Selection(
        selection=[
          (0, 'Semestral'),(1,'Anual')
        ],
        string='Esquema',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    id_habilidad = fields.Many2one(comodel_name='gps.habilidades', string='Habilidad')
    ap_diseno = fields.Boolean(string='¿Aplica Diseño?')
    multisitio = fields.Boolean(string='¿Es Multisitio?')
    bilingue = fields.Boolean(string='¿Necesita Auditor Bilingüe?')
    nivel_riesgo = fields.Char(string='Nivel Riesgo')
    duracion = fields.Integer(string='Duracion')
    fecha_contrato = fields.Date(string='Fecha Contrato')
    notas = fields.Text(string='Notas')
    cancelado = fields.Boolean(string='¿Cancelado?')
    transferencia = fields.Boolean(string='¿Transferencia?')
    archivo_contrato = fields.Char(string='Archivo Contrato')
    archivo_cuestionario = fields.Char(string='Archivo Cuestionario')
    archivo_carta = fields.Char(string='Archivo Carta')
    archivo_cotizacion = fields.Char(string='Archivo Cotizacion')
    archivo_transferencia = fields.Char(string='Archivo Transferencia')
    #Mapeado a external id
    #id_contrato = fields.Char(string='Id Contrato')
    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
    id_revisor = fields.Integer(string='Id Revisor')
    estado_revisor = fields.Selection(
        selection=[
          (0, 'Ninguno')
          ,(1,'Aprobado')
          ,(2,'Hold')
          ,(3,'Revision')
        ],
        string='Estado Revisor',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    nota_revisor = fields.Char(string='Nota Revisor')
    id_ventas = fields.Many2one(comodel_name='res.users', string='Id Ventas')
    fee01 = fields.Float(string='Fee01')
    fee02 = fields.Float(string='Fee02')
    fee03 = fields.Float(string='Fee03')
    ciclo_contrato = fields.Integer(string='Ciclo Contrato')
    moneda_tipo = fields.Integer(string='Moneda')
    moneda_tipo_cambio = fields.Float(string='Tipo de Cambio')
    recertificacion = fields.Boolean(string='¿Recertificacion?')
    finalizado = fields.Boolean(string='¿Finalizado?')
    archivo_certificado = fields.Char(string='Archivo Certificado')
    informacion_avance = fields.Text(string='Informacion Avance')
    fechainicio = fields.Date(string='Fecha Inicio')
    fechafin = fields.Date(string='Fecha Fin')
    tipocertificacion = fields.Selection(
        selection=[
          (1, 'Initial')
          ,(2,'Recertification')
          ,(3,'Takeover')
        ],
        string='Tipo Certificacion',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    mostrarnace = fields.Boolean(string='¿Mostrar NACE?')
    tipoesquema = fields.Char(string='Tipo Esquema')
    bloquearcontrato = fields.Boolean(string='¿Bloquear Contrato?')
    estatus_certificado = fields.Selection(
        selection=[
          (0, 'Active')
          ,(1,'Expired')
          ,(2,'Suspended')
          ,(3,'Canceled')
        ],
        string='Estatus Certificado',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    haccp = fields.Integer(string='HACCP')
    aplica_viaticos = fields.Char(string='Aplica Viaticos')
    id_md5_qms = fields.Char(string='MD5QMS')
    observaciones_viaticos = fields.Char(string='Observaciones Viaticos')
    report_time = fields.Float(string='Report Time')
    archivo_rev_auditor = fields.Char(string='Archivo Rev Auditor')

class GpsEventos(models.Model):
    _name = 'gps.eventos'
    _description = 'gps.eventos'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Char(string='Número de Trabajo')
    id_habilidad = fields.Many2one(comodel_name='gps.habilidades', string='Id Habilidad')
    domicilio = fields.Char(string='Domicilio')
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_termino = fields.Date(string='Fecha Termino')
    estado_evento = fields.Selection(
        selection=[
          (1, 'Agendado')
          ,(2,'Confirmado')
          ,(3,'Ejecutado')
          ,(4,'Revision')
          ,(5,'Comite')
          ,(6,'Cerrado')
        ],
        string='Estado Evento',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    tipo_evento = fields.Selection(
        selection=[
          (0, 'Todos')
          ,(1,'Ninguno')
          ,(2,'PreAuditoria')
          ,(3,'EtapaI')
          ,(4,'EtapaII')
          ,(5,'Seguimiento1')
          ,(6,'CARS')
          ,(7,'Recertificacion')
          ,(8,'Seguimiento2')
          ,(9,'Seguimiento3')
          ,(10,'Seguimiento4')
          ,(11,'Seguimiento5')
          ,(12,'Transferencia')
          ,(13,'Recertificacion')
          ,(14,'Takeover')
          ,(16,'AuditoriaEspecial')
          ,(17,'RRPriortoExpiration')
        ],
        string='Tipo Evento',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    introduccion = fields.Char(string='Introducción')
    pago = fields.Float(string='Pago')
    fecha_aviso = fields.Date(string='Fecha Aviso')
    comentarios = fields.Text(string='Comentarios')
    id_revisor = fields.Char(string='Id Revisor')
    estado_revisor = fields.Selection(
        selection=[
          (0, 'Ninguno')
          ,(1,'Aprovado')
          ,(2,'Hold')
          ,(3,'Revision')
        ],
        string='Estado Revisor',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    nota_revisor = fields.Text(string='Nota Revisor')
    id_comite = fields.Char(string='Id Comite')
    estado_comite = fields.Selection(
        selection=[
          (0, 'Ninguno')
          ,(1,'Aprovado')
          ,(2,'Hold')
          ,(3,'Revision')
        ],
        string='Estado Comite',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    nota_comite = fields.Char(string='Nota Comite')
    id_client_service = fields.Char(string='Id Cliente Service')
    no_seguimiento_trans = fields.Integer(string='No Seguimiento Trans')
    id_contrato = fields.Many2one(comodel_name='gps.contratos', string='Id Contrato')
    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
    estado_republica = fields.Many2one(comodel_name='res.country.state', string='Estado Republica')
    discapacidad = fields.Boolean(string='¿Discapacidad?')
    es_conferencia = fields.Boolean(string='¿Es Conferencia?')
    archivo_plan_auditoria = fields.Char(string='Archivo Plan Auditoría')
    id_ubicacion = fields.Char(string='Id Ubicación')
    archivo_reporte_auditoria = fields.Char(string='Archivo Reporte Auditoría')
    id_oficina = fields.Many2one(comodel_name='gps.oficinas', string='Id Oficina')
    ciudad = fields.Char(string='Ciudad')
    nota_auditor = fields.Char(string='Nota Auditor')
    estatus = fields.Selection(
        selection=[
          (0, 'Created')
          ,(1,'Rejected')
          ,(2,'Approved')
        ],
        string='Estatus',
        help=None,
        readonly=False,
        required=False,
        groups=[])
    fecha_envio_fssc = fields.Date(string='Fecha Envio FSSC')

class GpsFuente(models.Model):
    _name = 'gps.fuente'
    _description = 'gps.fuente'

    _rec_name = 'name'

    name = fields.Char(string='Name')

class GpsRecommended(models.Model):
    _name = 'gps.recommended'
    _description = 'gps.recommended'

    _rec_name = 'name'

    name = fields.Char(string='Name')

class GpsNaceCode(models.Model):
    _name = 'gps.nacecode'
    _description = 'gps.nacecode'

    _rec_name = 'nombre'

    #id_nace_code = fields.Integer(string='Id NaceCode')
    nombre = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    id_habilidad = fields.Many2one(comodel_name='gps.habilidades',string='Id Habilidad')
    baja = fields.Integer(string='Baja')
    acreditado_por_anaf = fields.Boolean(string='Acreditado por ANAB')
    clase_riesgo = fields.Char(string='Clase Riesgo')
    iaf = fields.Integer(string='IAF')

class GpsNoConformidades(models.Model):
    _name = 'gps.noconformidades'
    _description = 'gps.noconformidades'

    _rec_name = 'numero_trabajo'

    #id_no_conformidad = fields.Char(string='Id NoConformidad')
    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    sentencia = fields.Char(string='Sentencia')
    sentencia_archivo = fields.Char(string='Sentencia Archivo')
    tipo = fields.Integer(string='Tipo')
    contencion = fields.Char(string='Contencion')
    contencion_archivo = fields.Char(string='Contencion Archivo')
    causa_raiz = fields.Char(string='Causa Raiz')
    causa_raiz_archivo = fields.Char(string='Causa Raiz Archivo')
    implementacion = fields.Char(string='Implementacion')
    implementacion_archivo = fields.Char(string='Implementacion Archivo')
    status = fields.Integer(string='Status')
    notas = fields.Char(string='Notas')
    fecha_apertura = fields.Date(string='Fecha Apertura')
    fecha_cierre = fields.Date(string='Fecha Cierre')
    cierre_Count = fields.Integer(string='Cierre Count')
    fecha_cambio = fields.Date(string='Fecha Cambio')
    is_site = fields.Integer(string='In Site')

class GpsEventosFacturacion(models.Model):
    _name = 'gps.eventos.facturacion'
    _description = 'gps.eventos.facturacion'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    estatus = fields.Char(string='Estatus')
    pagado = fields.Char(string='Pagado')
    fecha_pagado = fields.Char(string='Fecha Pagado')
    fecha_actualizacion = fields.Char(string='Fecha Actualizacion')
    fecha_facturado = fields.Char(string='Fecha Facturado')
    id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
    comentarios = fields.Char(string='Comentarios')

class GpsEventosConfirmacion(models.Model):
    _name = 'gps.eventos.confirmacion'
    _description = 'gps.eventos.confirmacion'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    confirmado = fields.Char(string='Confirmado')
    fecha = fields.Char(string='fecha')
    consultoria_previa = fields.Char(string='Consultoria Previa')
    comentarios = fields.Char(string='Comentarios')
    confirma_programacion = fields.Char(string='Confirma Programación')
    conflicto_intereses = fields.Char(string='Conflicto Intereses')

class GpsEventosContrato(models.Model):
    _name = 'gps.eventos.contrato'
    _description = 'gps.eventos.contrato'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    confirmado = fields.Char(string='Confirmado')
    fecha = fields.Char(string='fecha')
    consultoria_previa = fields.Char(string='Consultoria Previa')
    comentarios = fields.Char(string='Comentarios')
    confirma_programacion = fields.Char(string='Confirma Programación')
    conflicto_intereses = fields.Char(string='Conflicto Intereses')

class GpsArchivos(models.Model):
    _name = 'gps.archivos'
    _description = 'gps.archivos'

    _rec_name = 'nombre'

    #id_archivo = fields.Char(string='Id Archivo')
    id_propietario = fields.Many2one(comodel_name='res.partner', string='Id Propietario')
    nombre = fields.Char(string='Nombre')
    fecha_registrro = fields.Date(string='Fecha Registro')
    description = fields.Char(string='Description')

class GpsArchivosTracking(models.Model):
    _name = 'gps.archivos.tracking'
    _description = 'gps.archivos.tracking'

    _rec_name = 'nombre'

    id_archivo = fields.Many2one(comodel_name='gps.archivos', string='Id Archivo')
    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    nombre = fields.Char(string='Nombre')
    fecha_registro = fields.Date(string='Fecha Registro')
    tipo_archivo = fields.Char(string='Tipo Archivo')
    numero_archivo = fields.Integer(string='Número Archivo')

class GpsArchivosEvento(models.Model):
    _name = 'gps.archivos.evento'
    _description = 'gps.archivos.evento'

    _rec_name = 'nombre_archivo'

    id_archivo = fields.Many2one(comodel_name='gps.archivos', string='Id Archivo')
    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    nombre_archivo = fields.Char(string='Nombre Archivo')

class GpsArchivosUsuarios(models.Model):
    _name = 'gps.archivos.usuarios'
    _description = 'gps.archivos.usuarios'

    _rec_name = 'nombre_archivo'

    id_archivo = fields.Many2one(comodel_name='gps.archivos', string='Id Archivo')
    id_nacecode_soporte = fields.Char(string='Id NaceCode Soporte')
    id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
    id_nacecode = fields.Many2one(comodel_name='gps.nacecodes', string='Id NaceCode')
    tipo_archivo = fields.Char(string='Id Tipo Archivo')
    nombre_archivo = fields.Char(string='Nombre Archivo')

class GpsAuditorExpertoTecnico(models.Model):
    _name = 'gps.usuarios.auditorexpertotecnixo'
    _description = 'gps.archivos.auditorexpertotecnixo'

    _rec_name = 'id_auditor'

    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
    id_auditor = fields.Many2one(comodel_name='res.users', string='Id Auditor')
    fecha = fields.Date(string='Fecha')

class GpsComentarioCliente(models.Model):
    _name = 'gps.clientes.comentario'
    _description = 'gps.clientes.comentario'

    _rec_name = 'id_cliente'

    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
    id_oficina = fields.Many2one(comodel_name='gps.oficinas', string='Id Oficina')
    id_proceso = fields.Many2one(comodel_name='gps.procesos.global', string='Id Proceso')
    comentario = fields.Char(string='Comentario')
    fecha = fields.Date(string='Fecha')
    id_user_connected = fields.Many2one(comodel_name='res.users', string='Id User Connected')

class GpsComentariosTracking(models.Model):
    _name = 'gps.clientes.comentario.tracking'
    _description = 'gps.clientes.comentario.tracking'

    _rec_name = 'numero_trabajo'

    #comentarios_tracking_key = fields.Char(string='Comentarios Tracking Key')
    comentarios = fields.Char(string='Comentarios')
    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')

class GpsEncuestas(models.Model):
    _name = 'gps.encuestas'
    _description = 'gps.encuestas'

    _rec_name = 'fecha_creado'

    revision = fields.Char(string='Revision')
    tipo_evento = fields.Integer(string='Tipo Evento')
    activo = fields.Boolean(string='Activo')
    fecha_creado = fields.Date(string='Fecha Creado')

class GpsEncuestasClientes(models.Model):
    _name = 'gps.encuestas.clientes'
    _description = 'gps.encuestas.clientes'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    fecha_enviado = fields.Date(string='Fecha Enviado')
    fecha_resuelto = fields.Date(string='Fecha Resuelto')
    md5 = fields.Many2one(comodel_name='gps.md5qms', string='MD5')
    encuesta_id = fields.Many2one(comodel_name='gps.encuestas', string='Encuesta Id')
    acciones = fields.Char(string='Accionestring=s')
    quejas = fields.Char(string='Quejas')

class GpsEncuestasClientesRespuestas(models.Model):
    _name = 'gps.encuestas.clientes.respuestas'
    _description = 'gps.encuestas.clientes.respuestas'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    encuesta_respuesta_id = fields.Many2one(comodel_name='gps.encuestas.respuestas', string='Encuestas Respuestas Id')

class GpsEncuestasClientesRespuestasComentarios(models.Model):
    _name = 'gps.encuestas.clientes.respuestas.comentarios'
    _description = 'gps.encuestas.clientes.respuestas.comentarios'

    _rec_name = 'numero_trabajo'

    encuesta_respuesta_id = fields.Many2one(comodel_name='gps.encuestas.respuestas', string='Encuestas Respuestas Id')
    comentario = fields.Char(string='Comentario')
    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')

class GpsEncuestasPreguntas(models.Model):
    _name = 'gps.encuestas.preguntas'
    _description = 'gps.encuestas.preguntas'

    _rec_name = 'pregunta'

    encuesta_id = fields.Many2one(comodel_name='gps.encuestas', string='Encuesta Id')
    idioma = fields.Char(string='Idioma')
    pregunta = fields.Char(string='Pregunta')
    orden = fields.Integer(string='Orden')

class GpsEncuestasRespuestas(models.Model):
    _name = 'gps.encuestas.preguntas'
    _description = 'gps.encuestas.preguntas'

    _rec_name = 'encuesta_pregunta_id'

    encuesta_pregunta_id = fields.Many2one(comodel_name='gps.encuestas.preguntas', string='Encuesta Pregunta Id')
    respuesta = fields.Char(string='Respuesta')
    valor = fields.Integer(string='Valor')
    orden = fields.Char(string='Orden')

class GpsLastNC(models.Model):
    _name = 'gps.lastnc'
    _description = 'gps.lastnc'

    _rec_name = 'numero_trabajo'

    id_no_conformidades = fields.Many2one(comodel_name='gps.noconformidades', string='Id No Conformidades')
    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    fecha_apertura = fields.Date(string='Fecha Apertura')

class GpsMD5QMS(models.Model):
    _name = 'gps.md5qms'
    _description = 'gps.md5qms'

    _rec_name = 'num_empleados'

    num_empleados = fields.Char(string='Num Empleados')
    dias_auditor = fields.Char(string='Dias Auditor')

class GpsNaceCodesCliente(models.Model):
    _name = 'gps.nacecodes.cliente'
    _description = 'gps.nacecodes.cliente'

    _rec_name = 'id_nacecode'

    id_nacecode = fields.Many2one(comodel_name='gps.nacecode', string='Id NaceCode')
    id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')

class GpsNaceCodesUsuario(models.Model):
    _name = 'gps.nacecodes.usuario'
    _description = 'gps.nacecodes.usuario'

    _rec_name = 'id_usuario'

    id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
    id_nacecode = fields.Many2one(comodel_name='gps.nacecodes', string='Id NaceCode')
    calificacion = fields.Integer(string='Calificacion')

class GpsNaceCodesUsuariosSoporte(models.Model):
    _name = 'gps.nacecodes.usuario.soporte'
    _description = 'gps.nacecodes.usuario.soporte'

    _rec_name = 'nombre_archivo'

    id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
    id_nacecode = fields.Many2one(comodel_name='gps.nacecodes', string='ID NaceCode')
    tipo_archivo = fields.Char(string='Tipo Archivo')
    nombre_archivo = fields.Char(string='Nombre Archivo')
    extension = fields.Char(string='Extension')
    aprobado = fields.Boolean(string='Aprobado')
    calificacion = fields.Integer(string='Calificacion')
    comentarios_auditor = fields.Char(string='Comentarios Auditor')
    comentarios_admin = fields.Char(string='Comentarios Admin')
    fecha_creado = fields.Date(string='Fecha Creado')
    fecha_actualizado = fields.Date(string='Fecha Actualizado')
    fecha_aprobado = fields.Date(string='Fecha Aprobado')
    descripcion = fields.Char(string='Descripcion')

class GpsNaceCodesUsuariosSoporteArchivo(models.Model):
    _name = 'gps.nacecodes.usuario.soporte.archivo'
    _description = 'gps.nacecodes.usuario.soporte.archivo'

    _rec_name = 'id_nacecode_soporte'

    id_nacecode_soporte = fields.Many2one(comodel_name='gps.nacecodes.usuario.soporte', string='Id NaceCode Soporte')

class GpsNoConformidadesAcciones(models.Model):
    _name = 'gps.noconformidades.acciones'
    _description = 'gps.noconformidades.acciones'

    _rec_name = 'numero_trabajo'

    numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    seccion = fields.Integer(string='Seccion')
    nombre_archivo = fields.Char(string='Nombre Archivo')
    ocurrio_error = fields.Boolean(string='Ocurrio Error')
    descripcion_error = fields.Char(string='Descripcion Error')
    instante_accion = fields.Date(string='Instante Accion')

class GpsOficinas(models.Model):
    _name = 'gps.oficinas'
    _description = 'gps.oficinas'

    _rec_name = 'nombre'

    id_ubicacion = fields.Many2one(comodel_name='gps.ubicaciones', string='Id Ubicacion')
    codigo = fields.Integer(string='Codigo')
    nombre = fields.Char(string='Nombre')
    es_principal = fields.Boolean(string='Es Principal')

class GpsPersonas(models.Model):
    _name = 'gps.personas'
    _description = 'gps.personas'

    _rec_name = 'nombres'

    id_oficina = fields.Many2one(comodel_name='gps.oficinas', string='Id Oficina')
    nombres = fields.Char(string='Nombres')
    apellido_paterno = fields.Char(string='Apellido Paterno')
    apellido_materno = fields.Char(string='Apellido Materno')
    correo = fields.Char(string='Correo')
    telefono = fields.Char(string='Telegono')
    baja = fields.Boolean(string='baja')
    fecha_baja = fields.Date(string='Fecha Baja')
    comentarios_persona = fields.Char(string='Comentarios Persona')

class GpsPersonasEvento(models.Model):
    _name = 'gps.personas.evento'
    _description = 'gps.personas.evento'

    _rec_name = 'id_persona'

    id_evento = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
    id_persona = fields.Many2one(comodel_name='gps.personas', string='Id Persona')
    costo = fields.Float(string='Costo')
    tipo_moneda = fields.Char(string='Tipo Moneda')

class GpsProcesoGlobal(models.Model):
        _name = 'gps.proceso.global'
        _description = 'gps.proceso.global'

        _rec_name = 'nombre'

        id_oficina = fields.Many2one(comodel_name='gps.oficinas', string='Id Oficina')
        nombre = fields.Char(string='Nombre')
        fecha = fields.Date(string='Fecha')

class GpsRangoEstandaresCalidad(models.Model):
        _name = 'gps.rango.estandarescalidad'
        _description = 'gps.rango.estandarescalidad'

        _rec_name = 'cve_estandar'

        rango_inicial = fields.Integer(string='Rango Inicial')
        rango_final = fields.Integer(string='Rango Final')
        cve_estandar = fields.Many2one(comodel_name='gps.habilidades', string='Cve Estandar')
        descripcion = fields.Char(string='Descripcion')
        fecha_alta = fields.Date(string='Fecha Alta')
        fecha_baja = fields.Date(string='Fecha Baja')
        estatus = fields.Integer(string='Estatus')

class GpsRegistro(models.Model):
        _name = 'gps.registro'
        _description = 'gps.registro'

        _rec_name = 'fecha_reg'

        id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
        id_concepto = fields.Many2one(comodel_name='gps.concepto', string='Id Concepto')
        fecha_reg = fields.Date(string='Fecha Reg')
        horas = fields.Float(string='Horas')
        cliente = fields.Many2one(comodel_name='res.partner', string='Cliente')
        certificacion = fields.Char(string='Certificacion')
        curso = fields.Char(string='Curso')
        observacion = fields.Char(string='Observacion')
        id_permiso = fields.Char(string='Id Permiso')

class GpsConcepto(models.Model):
        _name = 'gps.concepto'
        _description = 'gps.concepto'

        _rec_name = 'concepto'

        concepto = fields.Char(string='Concepto')

class GpsTipoArchivo(models.Model):
        _name = 'gps.tipoarchivo'
        _description = 'gps.tipoarchivo'

        _rec_name = 'tipo_archivo'

        tipo_archivo = fields.Char(string='Tipo Archivo')
        modulo = fields.Integer(string='Modulo')
        abrev = fields.Char(string='Abrev')

class GpsUbicaciones(models.Model):
        _name = 'gps.ubcaciones'
        _description = 'gps.ubicaciones'

        _rec_name = 'id_ciudad'

        id_ciudad = fields.Many2one(comodel_name='gps.city', string='Id Ciudad')
        direccion = fields.Char(string='Direccion')

class GpsUbicacionesCliente(models.Model):
        _name = 'gps.ubcaciones.cliente'
        _description = 'gps.ubicaciones.cliente'

        _rec_name = 'direccion'

        id_cliente = fields.Many2one(comodel_name='res.partner', string='Id Cliente')
        id_ubicacion = fields.Many2one(comodel_name='gps.ubicaciones', string='Id Ubicacion')
        direccion = fields.Char(string='Direccion')
        location = fields.Integer(string='Location')

class GpsUbicacionesContrato(models.Model):
        _name = 'gps.ubcaciones.contrato'
        _description = 'gps.ubicaciones.contrato'

        _rec_name = 'id_ubicacion'

        id_contrato = fields.Many2one(comodel_name='gps.contratos', string='Id Contrato')
        id_ubicacion = fields.Many2one(comodel_name='gps.ubicaciones', string='Id Ubicacion')
        location = fields.Char(string='Location')


class GpsUsuariosPassword(models.Model):
        _name = 'gps.usuarios.password'
        _description = 'gps.usuarios.password'

        _rec_name = 'id_usuario'

        id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
        password_actualizado = fields.Char(string='Password Actualizado')

class GpsUsuariosEvento(models.Model):
        _name = 'gps.usuarios.evento'
        _description = 'gps.usuarios.evento'

        _rec_name = 'numero_trabajo'

        numero_trabajo = fields.Many2one(comodel_name='gps.eventos', string='Numero Trabajo')
        id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
        lider = fields.Integer(string='Lider')
        traductor = fields.Integer(string='Traductor')

class GpsUsuariosFoto(models.Model):
        _name = 'gps.usuarios.foto'
        _description = 'gps.usuarios.foto'

        _rec_name = 'nombre_archivo'

        id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
        nombre_archivo = fields.Char(string='Nombre Archivo')

class GpsCiudades(models.Model):
        _name = 'gps.city'
        _description = 'gps.city'

        _rec_name = 'nombre'

        nombre = fields.Char(string='Nombre')

class GpsConsultores(models.Model):
        _name = 'gps.consultores'
        _description = 'gps.consultores'

        _rec_name = 'nombre'

        nombre = fields.Char(string='Nombre')
        consultoria = fields.Char(string='Consultoria')
        telefono = fields.Char(string='Telefono')
        correo = fields.Char(string='Correo')
        id_usuario = fields.Many2one(comodel_name='res.users', string='Id Usuario')
