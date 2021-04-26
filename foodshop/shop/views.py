from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Shop
from orderlist.forms import OrderListAddProductForm


# class ProductListView(ListView):
#     context_object_name = 'product_list'
#     queryset = Product.objects.available()
#     template_name = 'shop/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductListView, self).get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         return context

def product_list(request, shop_slug=None, category_slug=None):
    shop = None
    shops = Shop.objects.all()
    category = None
    categories = Category.objects.all()
    products = Product.objects.available()
    if shop_slug:
        # category = Category.objects.get(slug=category_slug)
        # products = products.filter(category=category)
        shop = Shop.objects.get(slug=shop_slug)
        products = products.filter(shop=shop)
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/index.html',
                  {'product_list': products,
                   'category': category,
                   'categories': categories,
                   'shop': shop,
                   'shops': shops})


def product_detail(request, id, slug):
    product = Product.objects.available().get(id=id, slug=slug)
    orderlist_form = OrderListAddProductForm()
    return render(request, 'shop/product_detail.html',
                  {'product': product,
                   'orderlist_form': orderlist_form})
