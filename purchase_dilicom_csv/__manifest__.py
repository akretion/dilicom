# -*- coding: utf-8 -*-
# © 2014-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Dilicom CSV',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Generate CSV files to order on the Dilicom website",
    'description': """
Dilicom is a French book distributor (https://dilicom-prod.centprod.com/)

This module adds a *Dilicom CSV report* on the purchase order. It
generate a CSV file that can be uploaded on the Dilicom website to
generate an order.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase'],
    'data': [
        #'report.xml',
        'purchase_view.xml',
        'report/dilicom_purchase_order_csv.xml',
        ],
    'installable': True,
}
