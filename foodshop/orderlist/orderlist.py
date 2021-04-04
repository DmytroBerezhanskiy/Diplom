from django.conf import settings
from decimal import Decimal
from foodshop.shop.models import Product


class OrderList(object):
    def __init__(self, request):
        self.session = request.session
        orderlist = self.session.get(settings.ORDERLIST_SESSION_ID)
        if not orderlist:
            orderlist = self.session[settings.ORDERLIST_SESSION_ID] = {}
        self.orderlist = orderlist

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.orderlist:
            self.orderlist[product_id] = {'count': 0,
                                          'price': str(product.price)}
        if update_count:
            self.orderlist[product_id]['count'] = count
        else:
            self.orderlist[product_id]['count'] += count
        self.save()

    def save(self):
        self.session[settings.ORDERLIST_SESSION_ID] = self.orderlist
        self.session.modified = True
