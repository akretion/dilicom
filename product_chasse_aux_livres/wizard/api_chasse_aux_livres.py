# Copyright 2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, tools, _
from odoo.exceptions import UserError
import requests
from stdnum.ean import is_valid
import base64
import logging
TIMEOUT = 20

logger = logging.getLogger(__name__)


class ApiChasseAuxLivres(models.TransientModel):
    _name = 'api.chasse.aux.livres'
    _description = 'API chasse-aux-livres.fr'

    ean = fields.Char(
        string="Code Barre du Livre", required=True)

    def run(self):
        self.ensure_one()
        ean = self.ean.strip()
        if len(ean) != 13:
            raise UserError(_("The barcode must have 13 digits (it has %d digits).") % len(ean))
        if not is_valid(ean):
            raise UserError(_("The barcode %s is not a valid EAN-13 barcode.") % ean)
        ppo = self.env['product.product']
        action = self.env["ir.actions.actions"]._for_xml_id('product.product_template_action_all')
        action['view_mode'] = 'form,tree,kanban'
        action['views'] = [
            (False, 'form'),
            (False, 'tree'),
            (False, 'kanban'),
            ]
        existing_product = ppo.with_context(active_test=False).search([('barcode', '=', ean)], limit=1)
        if existing_product:
            action['res_id'] = existing_product.product_tmpl_id.id
            action_notif = {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "type": "success",
                    "title": _("Product Already Exists"),
                    "message": _("Display existing product '%s'.") % existing_product.display_name,
                    "next": action,
                },
            }
            return action_notif
        apikey = tools.config.get('chasseauxlivres_apikey', False)
        if not apikey:
            raise UserError(_("API Key of chasse-aux-livres.fr missing in the Odoo server config file."))
        url = "https://www.chasse-aux-livres.fr/api/v1/item?key=%s&ids=%s" % (apikey, ean)
        try:

            res = requests.get(url, timeout=TIMEOUT)
            if res.status_code not in (200, 201):
                raise UserError(_("The webservice of chasse-aux-livres.fr returned an HTTP error code %s.") % res.status_code)
            res_dict = res.json()
        except Exception as e:
            raise UserError(_("Error in the webservice call to chasse-aux-livres.fr. Technical error details: %s.") % e)
        logger.info('The webservice of chasse-aux-livres.fr returned %s', res_dict)
        if not res_dict.get("results"):
            raise UserError(_("The answer of the chasse-aux-livres.fr webservice is invalid (missing 'results' key)."))
        if not res_dict['results'].get(ean):
            raise UserError(_("TODO"))
        if not isinstance(res_dict['results'][ean], list):
            raise
        if len(res_dict['results'][ean]) <= 0:
            raise
        res_book = res_dict['results'][ean][0]
        image_url = res_book.get('image')
        logger.info('Image URL = %s', image_url)
        image_1920 = False
        if image_url:
            try:
                image_res = requests.get(image_url, timeout=TIMEOUT)
                if image_res.status_code in (200, 201):
                    image_1920 = base64.encodebytes(image_res.content)
            except Exception as e:
                logger.warning('Failed to download image. Error: %s', e)
        action['context'] = self._prepare_context(res_book, image_1920)
        return action

    def _prepare_context(self, res_book, image_1920):
        name = res_book.get('title')
        list_price = 0
        if res_book.get('listPrice'):
            try:
                list_price = round(res_book.get('listPrice') / 100, 2)
            except Exception:
                raise UserError(_("Error when converting price (%s).") % res_book.get('listPrice'))
        author = res_book.get('authors')
        if isinstance(author, list):
            author = ', '.join(author)
        if author and author.lower() == 'nc':
            author = False
        manufacturer_id = False
        if res_book.get('editor') and len(res_book['editor']) > 2:
            editor = res_book['editor'].strip()
            partner_editor = self.env['res.partner'].search([('name', 'ilike', editor), ('is_company', '=', True)], limit=1)
            if partner_editor:
                manufacturer_id = partner_editor.id
        weight = 0
        if res_book.get('weight'):
            try:
                weight = round(res_book['weight']/1000, self.env['decimal.precision'].precision_get('Stock Weight'))
            except Exception:
                logger.warning('Could not convert weight %s', res_book['weight'])
        categ_id = int(self.env['ir.config_parameter'].sudo().get_param(
            'product_chasse_aux_livres.default_product_categ_id'))
        if not categ_id:
            raise UserError(_("Default product category for Chasse aux Livres is not set on the General Settings configuration page."))

        context = {
            'default_name': name,
            'default_detailed_type': 'product',
            'default_categ_id': categ_id,
            'default_author': author,
            'default_barcode': self.ean,
            'default_list_price': list_price,
            'default_image_1920': image_1920,
            'default_manufacturer_id': manufacturer_id,
            'default_weight': weight,
            # 'default_collection': res_book.get('collection'),
            }
        return context
