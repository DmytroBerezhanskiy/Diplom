from django.urls import path, include

from django.urls import path
from .views import ProductListView, ProductDetailView
from . import views


urlpatterns = [
    # path("", ProductListView.as_view()),

    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:category_slug>/', ProductListView.product_list_by_category, name='product_list_by_category'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]