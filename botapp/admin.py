from django.contrib import admin

from botapp.models import Client, Box


@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


@admin.register(Box)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'client', 'start_storage', 'end_storage')
