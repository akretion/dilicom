# -*- encoding: utf-8 -*-
##############################################################################
#
#    Purchase Dilicom CSV module for Odoo
#    Copyright (C) 2014 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Purchase Dilicom CSV',
    'version': '0.1',
    'license': 'AGPL-3',
    'summary': "Generate CSV files to order on the Dilicom website",
    'description': """
Dilicom is a French book distributor (https://dilicom-prod.centprod.com/)

This module adds a *Dilicom CSV report* on the purchase order. It
generate a CSV file that can be uploaded on the Dilicom website to
generate an order (it also works on Hachette Diffusion (https://www.hachette-diffusion.fr/). It also adds an XLS order file that can be uploaded on Interforum (https://www.interforum.fr/), which is another book distributor.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['purchase', 'report_aeroo'],
    'data': ['report.xml'],
    'installable': True,
}
