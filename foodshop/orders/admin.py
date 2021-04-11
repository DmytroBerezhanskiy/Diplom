from django.contrib import admin

from orders.models import Order, OrderItem


class OrderInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderInline]
