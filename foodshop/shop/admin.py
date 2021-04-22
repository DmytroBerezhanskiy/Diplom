from django.contrib import admin
from .models import Category, Product, Shop


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'image', 'created', 'updated',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    list_filter = ['available', 'created', 'updated']
    list_editable = ('price', 'available', 'image',)
