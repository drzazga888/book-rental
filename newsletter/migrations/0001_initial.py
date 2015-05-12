# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(error_messages={b'unique': 'Podany adres e-mail juz istnieje  w bazie.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@]+$', 'Wprowadz poprawny adres e-mail. Ta wartosc moze zawierac tylko litery, cyfry oraz znak @.', b'invalid')], help_text='Wymagane do 30 znakow, litery, cyfry oraz @/./+/-/_ only.', unique=True, verbose_name='e-mail')),
            ],
        ),
    ]
