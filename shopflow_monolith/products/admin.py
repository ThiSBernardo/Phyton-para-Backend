from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco')
    search_fields = ('titulo', 'preco')

admin.site.register(Product, ProductAdmin)
