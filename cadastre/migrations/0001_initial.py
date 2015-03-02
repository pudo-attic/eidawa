# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('date_applied', models.DateTimeField(verbose_name=b'date applied')),
                ('date_granted', models.DateTimeField(verbose_name=b'date applied')),
                ('date_expires', models.DateTimeField(verbose_name=b'date applied')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
