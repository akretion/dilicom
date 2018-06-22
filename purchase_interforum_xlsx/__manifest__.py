# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Interforum XLSX',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Generate XLSX file for Interforum",
    'description': """
Purchase Interforum XLSX
========================

This module adds a report *Interforum XLSX* on purchase orders. It
generates an XLSX file that can be uploaded on the Interforum website to
generate an order.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase', 'report_xlsx'],
    'data': ['report.xml'],
    'installable': True,
}
