from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from foodshop.settings import LOGIN_URL
from .forms import ReviewsForm
from .models import Product, Category, Shop, Reviews
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
    orderlist_form = OrderListAddProductForm()
    shop = None
    shops = Shop.objects.all()
    category = None
    categories = Category.objects.all()
    products = Product.objects.available()
    if shop_slug:
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
                   'shops': shops,
                   "form": orderlist_form})


def product_detail(request, id, slug):
    product = Product.objects.available().get(id=id, slug=slug)
    orderlist_form = OrderListAddProductForm()
    reviews = product.reviews.filter(show=True)
    new_review = None
    if request.method == "POST":
        reviews_form = ReviewsForm(request.POST)
        if reviews_form.is_valid() and request.user.is_authenticated:
            new_review = reviews_form.save(commit=False)
            new_review.product = product
            new_review.author = request.user
            new_review.save()
            reviews_form = ReviewsForm()
            messages.success(request, 'Your review has been successfully submitted for review')
            return HttpResponseRedirect(request.path)
        else:
            return redirect(LOGIN_URL)
    else:
        reviews_form = ReviewsForm()
    return render(request, 'shop/product_detail.html',
                  {'product': product,
                   'orderlist_form': orderlist_form,
                   'reviews': reviews,
                   'new_review': new_review,
                   'reviews_form': reviews_form})
