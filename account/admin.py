from django.contrib import admin
from .models import Menu,Order

class MenuAdmin(admin.ModelAdmin):
    list_display=('name','price','available')
    search_fields=('name',)
    list_filter=('available',)

class OrderAdmin(admin.ModelAdmin):
    list_display=('customer_name','menu_item','quantity','status')
    search_fields=('customer_name',)
    list_filter=('status',)
