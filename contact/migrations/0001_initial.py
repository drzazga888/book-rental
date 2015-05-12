# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name='name')),
                ('value', models.CharField(max_length=70, verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=70, verbose_name='day')),
                ('open', models.TimeField(verbose_name='open hour')),
                ('close', models.TimeField(verbose_name='close hour')),
            ],
        ),
    ]
