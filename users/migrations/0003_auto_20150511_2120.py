# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150511_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpass',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
