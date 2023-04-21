# Copyright 2018-2023 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class InterforumXlsx(models.AbstractModel):
    _name = "report.purchase.order.interforum.xlsx"
    _inherit = "report.report_xlsx.abstract"
    _description = "Interforum XLSX"

    def generate_xlsx_report(self, workbook, data, orders):
        sheet = workbook.add_worksheet('-'.join([o.name for o in orders]))
        regular = workbook.add_format({})
        sheet.set_column(0, 0, 20)
        i = 0
        for order in orders:
            for line in order.order_line.filtered(lambda x: not x.display_type):
                fallback = '%s %s' % (line.product_id.display_name, 'NO BARCODE')
                sheet.write(
                    i, 0,
                    line.product_id.barcode or fallback, regular)
                sheet.write(i, 1, line.product_qty, regular)
                i += 1
