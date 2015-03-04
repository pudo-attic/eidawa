# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0008_auto_20150304_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='date_pegged',
            field=models.DateField(null=True, verbose_name=b'date pegged', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='date_renewal',
            field=models.DateField(null=True, verbose_name=b'date renewal', blank=True),
            preserve_default=True,
        ),
    ]
