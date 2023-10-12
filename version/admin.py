from django.contrib import admin

from version.models import Version


# Register your models here.
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['product', 'versions_number', 'versions_name', 'versions_activity']
    list_filter = ['id']
