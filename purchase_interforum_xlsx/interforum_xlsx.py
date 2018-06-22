# -*- coding: utf-8 -*-
# Copyright 2018 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx


class InterforumXlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, orders):
        sheet = workbook.add_worksheet(u'Interforum')
        regular = workbook.add_format({})
        sheet.set_column(0, 0, 20)
        i = 0
        for order in orders:
            for l in order.order_line:
                fallback = u'%s %s' % (l.product_id.display_name, 'NO BARCODE')
                sheet.write(
                    i, 0,
                    l.product_id.barcode or fallback, regular)
                sheet.write(i, 1, l.product_qty, regular)
                i += 1


InterforumXlsx('report.purchase.order.interforum.xlsx', 'purchase.order')
