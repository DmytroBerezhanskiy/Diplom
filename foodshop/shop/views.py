from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    context_object_name = 'product_list'
    queryset = Product.objects.available()
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
