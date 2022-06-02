from odoo import fields, models, _


class StockInventory(models.Model):
    _inherit = "stock.inventory"

    is_shopify_adjustment = fields.Boolean("Is Shopify Adjustment")
    updated_in_shopify = fields.Boolean("Updated In Shopify", default=False)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def shopify_update_order_status_to_marketplace(self):
        self.mk_instance_id.connection_to_shopify()
        self.env['sale.order'].process_update_order_status_shopify(self.sale_id, self.mk_instance_id, manual_process=True)
        return True
