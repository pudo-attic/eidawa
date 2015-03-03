# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0006_auto_20150303_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='type',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
