# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adressess',
            new_name='Adress',
        ),
        migrations.RenameField(
            model_name='newuser',
            old_name='key',
            new_name='userkey',
        ),
        migrations.AddField(
            model_name='resetpass',
            name='password',
            field=models.CharField(default=b'', max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='number',
            field=models.CharField(max_length=8, verbose_name='number of house'),
        ),
    ]
