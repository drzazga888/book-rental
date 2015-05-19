# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderedbook_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedbook',
            name='rated',
            field=models.BooleanField(default=0, verbose_name='rated'),
        ),
    ]
