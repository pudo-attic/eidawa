# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0007_license_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='title',
            new_name='identifier',
        ),
        migrations.AlterField(
            model_name='license',
            name='commodities',
            field=models.ManyToManyField(to='cadastre.Commodity', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='licenseholder',
            name='interest',
            field=models.IntegerField(default=100, verbose_name=b'Interest (%)', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
