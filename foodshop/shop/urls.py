from django.urls import path, include

from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:category_slug>/', ProductListView.product_list_by_category, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', ProductDetailView.product_detail, name='product_detail')
]