# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0009_auto_20150304_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='source_label',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='source_label',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companyplaceholder',
            name='source_label',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='source_label',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='licenseholder',
            name='source_label',
            field=models.URLField(max_length=4096, null=True, verbose_name=b'Source', blank=True),
            preserve_default=True,
        ),
    ]
