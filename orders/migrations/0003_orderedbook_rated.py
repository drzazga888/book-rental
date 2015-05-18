# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150517_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedbook',
            name='rated',
            field=models.BooleanField(default=False, verbose_name='rated'),
            preserve_default=False,
        ),
    ]
