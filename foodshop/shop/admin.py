from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Category, Product, Shop, Reviews, ReviewsAnswer


class ReviewsInline(admin.TabularInline):
    model = Reviews
    ordering = ('-created',)


@admin.register(Reviews)
class ReviewsAdminModel(admin.ModelAdmin):
    list_display = ('id', 'product', 'rating', 'created', 'show')
    ordering = ('created',)


@admin.register(ReviewsAnswer)
class ReviewsAnswerAdminModel(admin.ModelAdmin):
    list_display = ('review', 'author', 'body', 'created')
    ordering = ('review',)


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


@admin.register(LogEntry)
class LogAdminModel(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'change_message', 'is_addition', 'is_change', 'is_deletion')
    list_filter = ['action_time', 'user', 'content_type']
    ordering = ('-action_time',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

