# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0005_auto_20150303_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='area',
            field=models.DecimalField(null=True, verbose_name=b'Area (ha)', max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
