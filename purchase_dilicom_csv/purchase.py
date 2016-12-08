# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def dilicom_csv_single(self):
        settings = {'docs': self}
        csv_content = self.env.ref('purchase_dilicom_csv.single').render(
            settings)
        #f = open('/tmp/dilicom.csv', 'w')
        #f.write(csv_content)
        #f.close()
        filename = '%s-dilicom.csv' % self[0].name
        attachment = self.env['ir.attachment'].create({
            'res_model': 'purchase.order',
            'res_id': self[0].id,
            'name': filename,
            'datas': csv_content.encode('base64'),
            'datas_fname': filename,
            })
        action = {
            'name': _('Dilicom CSV file'),
            'view_mode': 'form',
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': attachment.id,
        }
        return action
