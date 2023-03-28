# Copyright 2023 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    chasse_aux_livres_default_product_categ_id = fields.Many2one(
        'product.category',
        string='Chasse aux Livres Product Category',
        config_parameter='product_chasse_aux_livres.default_product_categ_id',
        )
