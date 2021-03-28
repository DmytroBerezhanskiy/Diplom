from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    queryset = Product.objects.available()
    template_name = 'shop/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
