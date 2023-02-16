# Copyright 2021 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase - API chasse-aux-livres.fr',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Glue module between purchase and product_chasse_aux_livres",
    'description': """
Purchase - API chasse-aux-livres.fr
===================================

This is a glue module between the modules **purchase** and **product_chasse_aux_livres**.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase', 'product_chasse_aux_livres'],
    'data': [
        'wizard/api_chasse_aux_livres_menu.xml',
        'security/ir.model.access.csv',
        ],
    'installable': False,
    'auto_install': True,
}
