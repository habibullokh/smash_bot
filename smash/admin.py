from django.contrib import admin

from .models import Products, ProductsCategory, Product, Type


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'products_name']
    list_filter = ['products_name']
    search_fields = ['products_name']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(ProductsCategory, ProductsCategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Type, TypeAdmin)


