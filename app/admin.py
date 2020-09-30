from django.contrib import admin
from .models import District, SeaTurtleCount


class DistrictAdmin(admin.ModelAdmin):
    list_display = [field.name for field in District._meta.fields]


admin.site.register(District, DistrictAdmin)


class SeaTurtleCountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SeaTurtleCount._meta.fields]


admin.site.register(SeaTurtleCount, SeaTurtleCountAdmin)
