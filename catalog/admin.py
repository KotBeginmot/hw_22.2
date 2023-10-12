from django.contrib import admin

from catalog.models import Product, Category, ContactData


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'purchase_price', 'category']
    list_filter = ['category']
    search_fields = ['name', 'overview']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'overview']
    list_filter = ['id']

@admin.register(ContactData)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'text']
    list_filter = ['id']
