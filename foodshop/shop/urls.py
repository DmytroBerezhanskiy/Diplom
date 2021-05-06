from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('restaurant/<slug:shop_slug>/', views.product_list, name='product_list_by_shop'),
    path('restaurant/<slug:shop_slug>/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('restaurant/product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    path('category/<slug:category_slug>/', views.product_list, name='product_category'),
]
