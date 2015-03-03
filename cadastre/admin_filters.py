from django.contrib import admin
from django_countries import countries


class CountryFilter(admin.SimpleListFilter):
    title = 'country'
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        used = set([c.country for c in model_admin.model.objects.all()])
        existing = dict(countries)
        return [(c, existing[c]) for c in used]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(country__exact=self.value())
        else:
            return queryset
