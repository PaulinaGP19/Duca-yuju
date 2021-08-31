# -*- coding: utf-8 -*-
# File:           product_template.py
# Author:         Israel Calderón
# Copyright:      (C) 2019 All rights reserved by Madkting
# Created:        2019-04-17

from odoo import models, api
from odoo import exceptions
from collections import defaultdict
from ..log.logger import logger
import psycopg2

# import logging
# _log = logging.getLogger(__name__)

class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.model
    def mdk_create(self, product_data, id_shop=None):
        """
        OVERRIDES mdk_create method in madkting module 
        :param product_data:
        {
            'name': str,
            'default_code': str, # sku
            'type': str, # 'product', 'service', 'consu'
            'description': str,
            'description_purchase': str,
            'description_sale': str,
            'list_price': float,
            'company_id': int,
            'description_picking': str,
            'description_pickingout': str,
            'description_pickingin': str,
            'image': str, # base64 string
            'category_id': int,
            'taxes': list, # list of int
            'cost': float,
            'weight': float, # only if is parente product
            'weight_unit': str,
            'barcode': str, # only if is parent product
            'initial_stock': int, # TODO: implement initial stock functionality
            'variation_attributes': {
                'color':['blue', 'black'], # example variation
                'size': ['S', 'L'] # example variation
            }, # dict with variation as key and values in a list
            'variations': [
                {
                    'default_code': str,
                    'company_id': int,
                    'barcode': str,
                    'weight': float,
                    'cost': float,
                    'initial_stock': int, # TODO: implement initial stock functionality
                    'color': 'blue',
                    'size': 'S'
                }
            ]
        }
        :type product_data: dict
        :return:
        :rtype: dict
        """
        logger.info("### MULTI IMAGENES MODULE ###")
        multi_images = []
        if "multi_images" in product_data:
            multi_images = product_data.pop("multi_images")
            logger.info(len(multi_images))

        res = super(ProductTemplate, self).mdk_create(product_data, id_shop)
        logger.info("## RESPONSE ##")
        logger.info(res)
        
        if res and res["success"]:

            if multi_images:
                
                product_tmpl_id = res.get("data", {}).get('template_id')
                product_tmpl = self.browse(product_tmpl_id)
                product_tmpl.product_template_image_ids.unlink()

                multi_images_data = []
                for image in multi_images:
                    multi_images_data.append([0, 0, {
                        "name" : product_tmpl.name,
                        "image_1920" : image
                    }])

                try:                
                    product_tmpl.write({"product_template_image_ids" : multi_images_data})
                except Exception as e:
                    logger.info(e)
                    pass

        return res
