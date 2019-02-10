# -*- coding: utf-8 -*-
{
    'name': "Library Books",

    'summary': """
        Manage your books""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ievgen Synchyshyn",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'license': "AGPL-3",
    'category': 'Uncategorized',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}