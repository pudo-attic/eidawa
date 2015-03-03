from django.contrib import admin

from cadastre.models import License, LicenseHolder
from cadastre.models import Company, CompanyPlaceholder
from cadastre.merge import merge_model_objects
from cadastre.admin_filters import CountryFilter


class CadastreAdmin(admin.ModelAdmin):
    readonly_fields = ('modified', 'modified_by', 'created', 'created_by', )

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()

    class Media:
        css = {
            "all": ("css/hide_admin_original.css", )
        }


class LicenseHolderInlineAdmin(admin.TabularInline):
    model = LicenseHolder
    extra = 0
    fields = ('company_placeholder', 'interest', )


class LicenseAdmin(CadastreAdmin):
    list_display = ('title', 'country', 'area', 'date_expires')
    search_fields = ('title', )
    list_filter = (CountryFilter, 'commodities', )
    inlines = (LicenseHolderInlineAdmin, )

    fieldsets = ((
        'Base data', {
            'fields': ('title', 'country', 'date_applied', 'date_granted',
                       'date_expires')
        }), (
        'Geography and Minerals', {
            'fields': ('area', 'commodities', )
        }), (
        'Provenance', {
            'fields': ('source_url', 'modified', 'modified_by', 'created',
                       'created_by'),
            'classes': ('collapse',)
        })
    )

    def save_related(self, request, form, formsets, change):
        super(LicenseAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        for hd in License.objects.get(pk=obj.id).holders.all():
            if not hd.created_by:
                hd.created_by = request.user
            hd.modified_by = request.user
            hd.save()


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


class CompanyPlaceholderInlineAdmin(admin.TabularInline):
    model = CompanyPlaceholder
    extra = 0
    fields = ('label', 'jurisdiction', )


class CompanyAdmin(CadastreAdmin):
    list_display = ('label', 'jurisdiction')
    actions = ('merge', )
    search_fields = ('label', )
    inlines = (CompanyPlaceholderInlineAdmin, )

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

    def merge(self, request, queryset):
        main = queryset[0]
        tail = list(queryset[1:])
        merge_model_objects(main, tail)
        msg = "%s is merged, now you can give it a canonical name." % main
        self.message_user(request, msg)

    merge.short_description = "Merge company records"

    def save_related(self, request, form, formsets, change):
        super(CompanyAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        for ph in Company.objects.get(pk=obj.id).placeholders.all():
            if not ph.created_by:
                ph.created_by = request.user
            ph.modified_by = request.user
            ph.save()


admin.site.site_header = 'Extractive Industries Data Warehouse'
# admin.site.index_title = 'Drilling down until we hit money'
admin.site.register(License, LicenseAdmin)
# admin.site.register(LicenseHolder, LicenseHolderAdmin)
admin.site.register(Company, CompanyAdmin)
# admin.site.register(CompanyPlaceholder, CompanyPlaceholderAdmin)
