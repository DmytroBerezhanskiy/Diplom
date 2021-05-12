from django.contrib import admin
from .models import Category, Product, Shop, Reviews


class ReviewsInline(admin.TabularInline):
    model = Reviews
    ordering = ('-created',)


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    list_display = ('name', 'slug', "owner")
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ('name', 'shop', 'category', 'slug', 'price', 'available', 'image', 'created', 'updated',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    list_filter = ['available', 'created', 'updated']
    list_editable = ('price', 'available', 'image',)
    inlines = [ReviewsInline]



