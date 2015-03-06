from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django_extensions.db.models import TimeStampedModel

percentage = [MaxValueValidator(100), MinValueValidator(0)]


class CadastreModel(TimeStampedModel):
    source_label = models.CharField(verbose_name='Source', max_length=4096,
                                    null=True, blank=True)
    source_url = models.URLField(verbose_name='Source URL', max_length=4096,
                                 null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, related_name='+')
    modified_by = models.ForeignKey(User, null=True, related_name='+')

    class Meta:
        abstract = True


class Commodity(CadastreModel):
    label = models.CharField(max_length=500)

    def __unicode__(self):
        return self.label


class License(CadastreModel):
    identifier = models.CharField(max_length=500)
    type = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    area = models.DecimalField(verbose_name='Area (ha)', decimal_places=1,
                               max_digits=30, null=True, blank=True)
    country = CountryField(null=True)
    date_applied = models.DateField('date applied', null=True, blank=True)
    date_granted = models.DateField('date granted', null=True, blank=True)
    date_expires = models.DateField('date expires', null=True, blank=True)
    date_pegged = models.DateField('date pegged', null=True, blank=True)
    date_renewal = models.DateField('date renewal', null=True, blank=True)
    commodities = models.ManyToManyField(Commodity, blank=True)

    def __unicode__(self):
        return self.identifier


class Company(CadastreModel):
    label = models.CharField(max_length=500)
    jurisdiction = CountryField(null=True)
    opencorporates_uri = models.URLField(verbose_name='OpenCorporates URI',
                                         max_length=4096, null=True,
                                         blank=True)
    date_created = models.DateField('date created', null=True)
    date_dissolved = models.DateField('date dissolved', null=True)

    def __unicode__(self):
        return self.label

    class Meta:
        unique_together = (('label', 'jurisdiction'),)
        verbose_name_plural = "companies"


class CompanyPlaceholder(CadastreModel):
    label = models.CharField(max_length=500, unique=True)
    jurisdiction = CountryField(null=True)
    company = models.ForeignKey(Company, null=True,
                                related_name='placeholders')

    def __unicode__(self):
        return self.label

    class Meta:
        unique_together = (('label', 'jurisdiction'), )


class LicenseHolder(CadastreModel):
    license = models.ForeignKey(License, related_name='holders')
    interest = models.IntegerField(verbose_name='Interest (%)',
                                   default=100, validators=percentage)
    company_placeholder = models.ForeignKey(CompanyPlaceholder)

    def __unicode__(self):
        try:
            return '%s -> %s (%s%%)' % (self.company_placeholder, self.license,
                                        self.interest)
        except:
            return '(bad data)'
