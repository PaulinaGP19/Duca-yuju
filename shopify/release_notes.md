13.0.0.2:

- Visible Is Notify for fulfillment in instance view.
- Added note on Sale and Delivery Order for fulfillment.

13.0.0.3:

- Improve product barcode and sku search algorithm. Fix update product issue.

13.0.0.4:

- Improve all of the import api request.

13.0.0.5:

- Removed warnings shows in odoo.sh.

13.0.0.6:

- Removed use of Deprecated method.
- Removed update_at_min from get product list while page_info is present in api call.
- Fixed the issue of wrong Product Template set in Marketplace Listing.
- Fixed second page api calling issue.
- Increase default api limit from 200 to 250.
- Fetch only Active Location from Shopify
- Reduce 1 API call while Update Stock in Shopify through Schedule Action.
- Set delay if API limit is exceed.

13.0.0.7:

- Improve variants search algorithm. Improve to import/sync product with different no. of variants in Odoo and Shopify.

13.0.0.8:

- Added delay if API limit in export Stock.
- Fix bug of create sale order even if product not found.

13.0.0.9:

- Auto set Fulfillment Status field at the time of instance creation.
- Added functionality to manage Shopify's Custom Product Line
- Improvement in Logs

13.0.0.10:

- Improve import listing Process.
- Fixed issue of product variation price update.

13.0.0.11:

- Fixed bug of Webhook.

13.0.1.0:

- Refactor import inventory flow totally.
- Added Automated Job that will import Inventory.
- Improved Queue line process and Log management.
- Ability to import multiple Products and Orders by adding comma separated ids.
- Set weight in Odoo products if not set.

13.0.1.1:

- Improved fields visibility.
- Improved Import listing code.
- Changes Fulfillment Status Field's Type
- Change sql constraint to python constraint of financial workflow.
- Fixed issue of publish product from the Update Listing in Marketplace Popup.
- Fixed the issue of Import Product.
- Removed unnecessary fields and class.

13.0.1.2:

- Fixed bug of inventory Import.

13.0.1.3:

- Fixed bug of Order line Discount.

13.0.1.4:

- Fetch Orders based on Update order date instead of Create date.

13.0.1.5:

- Improved Export stock process for BOM type products.

1.6:

- Improve Product import process(You can't import products if its variants is linked with different Odoo Product
  template.)

1.7:

- Fixed issue of invoice sometime not fully reconciled.

1.8:

- Fixed error while creating invoice/delivery contact
- Now import variants if some products is not found in Odoo.
- Search for deactivated taxes and activate it if found.

1.9:

- Fixed issue of Order import from Webhook.

2.0:

- Added field to identify Order's Source(like Online store, POS or others).

2.1:

- Added configuration in instance for customer to create company customer or not.
- Added configuration in instance to import fraud analysis or not.
- Bug fix regarding Shopify Order Source import.
- Not create Customers if order's workflow is not found.

2.2

- Added Order warehouse that will set according to Shopify Location
- Added default POS Customer, will be used while customer is not found in POS order.
- Update Shopify SKD from 7.0(2019-10) to 8.4.1(2021-04)
- Skipped while Importing Stock from Shopify to Odoo only import products with Tracking field set to No Tracking in
  Odoo.
- Increase readability of Shopify Location in Sale order.
- Improved code for currency convert.
- Bug fix while search Shopify location in import stock operation.
- Bug fix of product's price set to zero while update single variant product with only update product operation.

2.2.1

- Update barcode in listing Item.

2.2.2

- Fixed issue while import order from import screen fetch order based on create date insted of write date. 

2.2.3

- Fixed issue while do refund.
- Fixed issue for Kit type BOM product's fulfillment update.
- Fixed create/update customer Webhook issue.

2.2.4

- Skip product if in import Listing Single variant product is existing in Odoo and get variants from Shopify. 

2.3

- Improve update order status process.

2.3.1

- Fix issue of financial workflow.

2.3.2

- Fixed issue of access rights.
- Improved Log search.
- Payments will be registered according to payment methods(if a orders is paid using multiple payment method then it
  will register according to it).

2.3.3

- Fixed export location from Odoo to Shopify issue.
- Fixed issue of gateway.

2.3.4

- Fixed issue while using third party Fulfillment Service and import Listings.

2.4

- Updated Shopify Python SDK Version.