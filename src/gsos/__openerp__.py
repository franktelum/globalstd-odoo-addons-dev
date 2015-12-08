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
        'data/audit_sequence.xml',
        'data/checklist_sequence.xml',
        'data/complaint_sequence.xml',
        'data/invitation_sequence.xml',
        'views/user_menu.xml',
        'views/audit_view_tree.xml',
        'views/audit_view_form.xml',
        'views/audit_view_calendar.xml',
        'views/complaint_view_form.xml',
        'views/complaint_view_tree.xml',
        'views/checklist_view_form.xml',
        'views/checklist_view_tree.xml',
        'views/res_partner_view_form.xml',
        'views/complaint_view_graph.xml',
        'views/invitation_view_form.xml',
        'views/invitation_view_tree.xml'
    ]
}
