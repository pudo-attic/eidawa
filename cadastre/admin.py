from django.contrib import admin

from cadastre.models import License, LicenseHolder
from cadastre.models import Company, CompanyPlaceholder


class CadastreAdmin(admin.ModelAdmin):

    readonly_fields = ('modified', 'modified_by', 'created', 'created_by', )

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()


class LicenseAdmin(CadastreAdmin):
    list_display = ('title', 'country', 'date_granted', 'date_expires')
    list_filter = ('country', )

    fieldsets = ((
        'Base data', {
            'fields': ('title', 'country', 'date_applied', 'date_granted',
                       'date_expires')
        }), (
        'Provenance', {
            'fields': ('source_url', 'modified', 'modified_by', 'created',
                       'created_by'),
            'classes': ('collapse',)
        })
    )


class LicenseHolderAdmin(CadastreAdmin):
    list_display = ('company_placeholder', 'license')

    fieldsets = ((
        'Base data', {
            'fields': ('company_placeholder', 'license', 'interest', )
        }), (
        'Provenance', {
            'fields': ('source_url', 'modified', 'modified_by', 'created',
                       'created_by'),
            'classes': ('collapse',)
        })
    )


class CompanyAdmin(CadastreAdmin):
    list_display = ('label', 'jurisdiction')

    fieldsets = ((
        'Base data', {
            'fields': ('label', 'jurisdiction', 'opencorporates_uri', )
        }), (
        'Provenance', {
            'fields': ('source_url', 'modified', 'modified_by', 'created',
                       'created_by'),
            'classes': ('collapse',)
        })
    )


class CompanyPlaceholderAdmin(CadastreAdmin):
    list_display = ('label', 'jurisdiction')

    fieldsets = ((
        'Base data', {
            'fields': ('label', 'jurisdiction', 'company', )
        }), (
        'Provenance', {
            'fields': ('source_url', 'modified', 'modified_by', 'created',
                       'created_by'),
            'classes': ('collapse',)
        })
    )


admin.site.site_header = 'EI Data Warehouse'
# admin.site.index_title = 'Drilling down until we hit money'
admin.site.register(License, LicenseAdmin)
admin.site.register(LicenseHolder, LicenseHolderAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyPlaceholder, CompanyPlaceholderAdmin)
