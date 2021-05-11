from django.contrib import admin
from courier.models import Courier


@admin.register(Courier)
class CourierAdminModel(admin.ModelAdmin):
    list_display = ('surname', 'name', 'telephone')
