{
    'name': 'Gsos',
    'category': 'GlobalSTD',
    'version': '1.0',
    'summary': 'Gestiona procesos de auditoría para segundas partes',
    'description': 'Gestiona procesos de auditoría para segundas partes',
    'application': True,
    'depends': ['mail'],
    'data': [
        'security/gsos_security.xml',
        'security/ir.model.access.csv',
        'views/user_menu.xml'
    ]
}
