# -*- coding: utf-8 -*-

{
    'name': 'Odoo Medica',
    
    'summary':"""medica app to manage date""",
    
    'description': """
        Medica Module to manage :
        -Medicos
        -Pacientes
        -Citas
    """,
    
    'author': 'Ivan',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends':['base'],
    
    'data':[
        'views/medica_menuitems.xml',
        'views/medico_views.xml',
    ],
    
    
    
     'license': 'LGPL-3',
    
}