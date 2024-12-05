# -*- coding: utf-8 -*-

{
    'name': "Lista de tareas",

    'summary': "Lista de tarea summary",

    'description': """No me sale nada""",

    'author': "Andrei",
    'website': "https://www.yourcompany.com",
    'aplication':True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    'assets':{
        'web.assets_backend':[
            'lista_tareas/views/custom.css',
        ],
    },

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}



