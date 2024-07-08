from django.contrib import admin
from .models import UrlData


class UrlDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'status_code', 'created_at', 'checked_at')


admin.site.register(UrlData, UrlDataAdmin)
