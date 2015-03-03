# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastre', '0004_auto_20150303_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('source_url', models.URLField(max_length=4096, null=True, verbose_name=b'Source URL', blank=True)),
                ('label', models.CharField(max_length=500)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='license',
            name='area',
            field=models.FloatField(null=True, verbose_name=b'Area (ha)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='commodities',
            field=models.ManyToManyField(to='cadastre.Commodity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='status',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='opencorporates_uri',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'OpenCorporates URI', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='source_url',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companyplaceholder',
            name='company',
            field=models.ForeignKey(related_name='placeholders', to='cadastre.Company', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companyplaceholder',
            name='source_url',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_applied',
            field=models.DateField(null=True, verbose_name=b'date applied', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_expires',
            field=models.DateField(null=True, verbose_name=b'date expires', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_granted',
            field=models.DateField(null=True, verbose_name=b'date granted', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='source_url',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='licenseholder',
            name='license',
            field=models.ForeignKey(related_name='holders', to='cadastre.License'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='licenseholder',
            name='source_url',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source URL', blank=True),
            preserve_default=True,
        ),
    ]
