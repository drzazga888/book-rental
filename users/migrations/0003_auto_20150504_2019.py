# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150504_1817'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adressess',
            new_name='Adress',
        ),
    ]
