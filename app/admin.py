from django.contrib import admin
from .models import District


class DistrictAdmin(admin.ModelAdmin):
    list_display = [field.name for field in District._meta.fields]


admin.site.register(District, DistrictAdmin)
