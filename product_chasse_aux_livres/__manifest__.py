# Copyright 2021 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product - API chasse-aux-livres.fr',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Create products from the API chasse-aux-livres.fr",
    'description': """
API chasse-aux-livres.fr
========================

This module allows to create products from the API of chasse-aux-livres.fr

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['product'],
    'data': [
        'wizard/api_chasse_aux_livres_view.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
}
