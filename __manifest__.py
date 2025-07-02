{
    'name': 'sid_actions_view_server_automation_scheduled',
    'version': '1.0',
    'category': 'Technical Settings',
    'summary': 'Acciones de todo el sistema',
    'description': 'Módulo con todas las acciones de todos los tipos de v15 personalizadas',
    'author': 'oscarsidsa81',
    'depends': ['base','crm','sale','purchase','stock'],
    'data': [
        'views/sid_view_actions.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
