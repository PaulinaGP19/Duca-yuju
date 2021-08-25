# -*- coding: utf-8 -*-
# File:           res_partner.py
# Author:         Israel Calderón
# Copyright:      (C) 2019 All rights reserved by Madkting
# Created:        2019-07-19

from odoo import models, api, fields
from odoo import exceptions

from ..log.logger import logger

from collections import defaultdict
import math

class ProductProduct(models.Model):
    _inherit = "product.product"

    
    @api.model
    def update_product(self, product_data, product_type, id_shop=None):
        """
        :param product_data:
        :type product_data: dict
        :param product_type: type of the product being updated: 'product' or 'variation'
        :type product_type: str
        :return:
        :rtype: dict
        """
        logger.info("### MULTI IMAGENES MODULE ###")
        multi_images = []
        if "multi_images" in product_data:
            multi_images = product_data.pop("multi_images")
            logger.info(len(multi_images))
        
        product_id = product_data.get('id', None)
        
        res = super(ProductProduct, self).update_product(product_data, product_type, id_shop)

        logger.info("#### PRODUCT ID #### {}".format(product_id))
        # logger.info(multi_images)
        if product_id and multi_images:


            product = self.browse(int(product_id))
            product_tmpl_id = product.product_tmpl_id.id
            product_tmpl = self.env["product.template"].browse(product_tmpl_id)
            product_tmpl.product_template_image_ids.unlink()
            # product_images = self.env["product.image"]
            multi_images_data = []
            for image in multi_images:
                # new_id = product_images.create({
                #     "name" : "",
                #     "image_1920" : image
                # })
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
   