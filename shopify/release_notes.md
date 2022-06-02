1.0:

- Initial Release

1.1:

- Added error log while import product from Shopify and in Odoo product variant is in different product template.

1.2:

- Improve stock update process.
- Webhook bug fix.
- Fetch orders based on update date.
- Update fulfillment status and financial status if order found.

1.3:

- Fixed issue of invoice sometime not fully reconciled.

1.4:

- Fixed error while creating invoice/delivery contact
- Now import variants if some products is not found in Odoo.

1.5:

- Fixed issue of Order import from Webhook.

1.6:

- Added field to identify Order's Source(like Online store, POS or others).

1.7:

- Added configuration in instance for customer to create company customer or not.
- Added configuration in instance to import fraud analysis or not.
- Bug fix regarding Shopify Order Source import.

1.8:

- Bug fix while import order.
- Not create Customers if order's workflow is not found.

1.9

- Added Order warehouse that will set according to Shopify Location
- Added default POS Customer, will be used while customer is not found in POS order.
- Update Shopify SKD from 7.0(2019-10) to 8.4.1(2021-04)
- Skipped while Importing Stock from Shopify to Odoo only import products with Tracking field set to No Tracking in
  Odoo.
- Increase readability of Shopify Location in Sale order.
- Improved code for currency convert.
- Bug fix while search Shopify location in import stock operation.
- Bug fix of product's price set to zero while update single variant product with only update product operation.

1.9.1

- Update barcode in listing Item.

1.9.2

- Fixed issue while import order from import screen fetch order based on create date instead of write date. 

1.9.3

- Fixed issue while do refund. 
- Fixed issue for Kit type BOM product's fulfillment update.
- Fixed create/update customer Webhook issue.

1.9.4

- Skip product if in import Listing Single variant product is existing in Odoo and get variants from Shopify. 

2.0

- Improve update order status process.

2.0.1

- Fix issue of financial workflow.

2.0.2

- Fixed issue of access rights.
- Improved Log search.
- Payments will be registered according to payment methods(if an orders is paid using multiple payment method then it will register according to it).

2.0.3

- Fixed export location from Odoo to Shopify issue.
- Fixed issue of gateway.

2.0.4

- Fixed issue while using third party Fulfillment Service and import Listings.

2.1

- Updated Shopify Python SDK Version.

2.2

- Added Access token in Shopify instance configuration.

2.3

- Added Tip and Gift Card product configuration in Instance. 

2.4

- Sometime Charge tax on product is not working so fixed that issue.
- Fixed issue of not webhook.
- You can define Order prefix as well.
- Modified tax system of orders according to Tax System configured in instance.
- Fixed access rights issue while access Import operation with User access rights.

2.5

- Limit export listing process to 80.
- Schedule action for update product price.
- User can now select/change Weight Unit from Listing Item.

2.6

- While performing Update Order Status if tracking url is present than we also sent tracking url.

2.7

- Do not create taxes if set Default Tax System to Odoo's Default Tax Behaviour.

2.8

- Change flow of fulfillment. Before fulfillment update location of order. 
- Added Update Order Status in Marketplace in Pickings.

2.9

- Improved Shopify Authentication process.
- Improve shopify location flow.

3.0

- Added multi-currency in sale orders.

3.1

- Improve the Shopify API calls limit.
- Added shopify last stock update on(datetime) field and update that field while update stock to Odoo to Shopify.