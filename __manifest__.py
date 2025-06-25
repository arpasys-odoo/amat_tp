# -*- coding: utf-8 -*-
{
    'name': "Amat TP",

    'summary': "Ce module permet d\'étendre le devis, contact et permet de créer des bons d\'intervention",

    'description': """
Ce module permet d\'étendre le devis, contact et permet de créer des bons d\'intervention
    """,

    'author': "Arpasys",
    'website': "https://studio.arpasys.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale',
        'product',
        'contacts',
        'mail'
    ],

    # always loaded
    'data': [
        'security/bon_intervention_security.xml',
        'security/ir.model.access.csv',
        
        'report/ir_actions_report_templates.xml',
        'report/ir_actions_report.xml',

        'views/bon_intervention_views.xml',
    ],
    
    'assets': {
        'web.assets_backend': [
            # 'blank_module/static/src/css/blank_module.css',
        ],
        'web.assets_frontend': [
            # 'blank_module/static/src/css/blank_module.scss',
        ],
    },
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': "LGPL-3",
    'sequence': -100,
}