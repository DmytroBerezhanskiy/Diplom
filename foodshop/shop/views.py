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

    def product_list_by_category(request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.available()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/index.html',
                      {'product_list': products,
                       'category': category,
                       'categories': categories})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
