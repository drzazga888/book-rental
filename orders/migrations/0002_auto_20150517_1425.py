# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='phone number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=32, verbose_name='title of money transfer'),
            preserve_default=False,
        ),
    ]
