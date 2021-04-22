from django.urls import path, include

from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:shop_slug>/', views.product_list, name='product_list_by_shop'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
]