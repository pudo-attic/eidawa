from django.contrib import admin

from cadastre.models import License

admin.site.site_header = 'EI Data Warehouse'
admin.site.register(License)
