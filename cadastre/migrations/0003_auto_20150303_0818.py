# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0002_auto_20150303_0745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='companyplaceholder',
            options={},
        ),
        migrations.AddField(
            model_name='company',
            name='opencorporates_uri',
            field=models.URLField(max_length=4096, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_expires',
            field=models.DateField(null=True, verbose_name=b'date expires'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='license',
            name='date_granted',
            field=models.DateField(null=True, verbose_name=b'date granted'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together=set([('label', 'jurisdiction')]),
        ),
        migrations.AlterUniqueTogether(
            name='companyplaceholder',
            unique_together=set([('label', 'jurisdiction')]),
        ),
    ]
