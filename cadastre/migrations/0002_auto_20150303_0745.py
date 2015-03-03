# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import django_extensions.db.fields
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('label', models.CharField(max_length=500)),
                ('jurisdiction', django_countries.fields.CountryField(max_length=2, null=True)),
                ('date_created', models.DateField(null=True, verbose_name=b'date created')),
                ('date_dissolved', models.DateField(null=True, verbose_name=b'date dissolved')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyPlaceholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('label', models.CharField(unique=True, max_length=500)),
                ('jurisdiction', django_countries.fields.CountryField(max_length=2, null=True)),
                ('company', models.ForeignKey(to='cadastre.Company', null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LicenseHolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('interest', models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('company_placeholder', models.ForeignKey(to='cadastre.CompanyPlaceholder')),
                ('license', models.ForeignKey(to='cadastre.License')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='license',
            options={'ordering': ('-modified', '-created'), 'get_latest_by': 'modified'},
        ),
        migrations.AddField(
            model_name='license',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_applied',
            field=models.DateField(null=True, verbose_name=b'date applied'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_expires',
            field=models.DateField(null=True, verbose_name=b'date applied'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_granted',
            field=models.DateField(null=True, verbose_name=b'date applied'),
            preserve_default=True,
        ),
    ]
