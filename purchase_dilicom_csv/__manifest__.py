# Copyright 2014-2023 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Dilicom CSV',
    'version': '16.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Generate CSV files to order on the Dilicom website",
    'description': """
Purchase Dilicom CSV
====================

Dilicom is a French book distributor (https://dilicom-prod.centprod.com/)

This module adds a report *Dilicom CSV Order* on purchase orders. It
generates a CSV file that can be uploaded on the Dilicom website to
generate an order.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase'],
    'data': [
        'report/dilicom_purchase_order_csv.xml',
        'report.xml',
        ],
    'installable': True,
}
