# -*- coding: utf-8 -*-
{
    'name': "g2modulojjg",

    'summary': """
        CRUD de una aplicacion de dietas""",

    'description': """
        Aplicacion para dietistas, clientes y un administrador.
        El dietista creara dietas, recetas, alimemtos; el cliente
        podra tener un dietista y seguir una dieta como tambien ver el
        seguimiento de su dieta. Por ultimo el administrador podra crear tanto
        clientes como dietista  y tambien podra crear dietas, recetas y alimentos.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/foods.xml',
        'views/recipes.xml',
        'views/userRecipes.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}