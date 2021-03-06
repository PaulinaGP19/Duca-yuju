import time

from .pyactiveresource import connection
from .base import ShopifyConnection


def patch_shopify_with_limits():
    func = ShopifyConnection._open

    def patched_open(self, *args, **kwargs):
        while True:
            try:
                return func(self, *args, **kwargs)

            except connection.ClientError as e:
                if e.response.code == 429:
                    retry_after = float(e.response.headers.get('Retry-After', 4))
                    print('Service exceeds Shopify API call limit, '
                          'will retry to send request in %s seconds' % retry_after)
                    time.sleep(retry_after)
                else:
                    raise e

    ShopifyConnection._open = patched_open


patch_shopify_with_limits()
