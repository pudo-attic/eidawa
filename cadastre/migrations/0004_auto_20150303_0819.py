# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastre', '0003_auto_20150303_0818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='license',
            options={},
        ),
        migrations.AlterModelOptions(
            name='licenseholder',
            options={},
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='modified_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='source_url',
            field=models.URLField(max_length=4096, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companyplaceholder',
            name='created_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companyplaceholder',
            name='modified_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companyplaceholder',
            name='source_url',
            field=models.URLField(max_length=4096, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='created_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='modified_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='license',
            name='source_url',
            field=models.URLField(max_length=4096, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='licenseholder',
            name='created_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='licenseholder',
            name='modified_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='licenseholder',
            name='source_url',
            field=models.URLField(max_length=4096, null=True),
            preserve_default=True,
        ),
    ]
