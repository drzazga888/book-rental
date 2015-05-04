# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adressess',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('street', models.CharField(max_length=40, verbose_name='street')),
                ('number', models.CharField(max_length=6, verbose_name='number of house')),
                ('zip', models.CharField(max_length=6, verbose_name='zip code')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(error_messages={b'unique': 'Uzytkownik z ta nazwa juz istnieje.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Wprowadz poprawna  nazwe uzytkownika. Ta wartosc moze zawierac tylko litery, cyfry oraz znaki @/./+/-/_', b'invalid')], help_text='Wymagane do 30 znakow, litery, cyfry oraz @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('street', models.CharField(max_length=40, verbose_name='street')),
                ('number', models.CharField(max_length=6, verbose_name='number of house')),
                ('zip', models.CharField(max_length=6, verbose_name='zip code')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('key', models.CharField(unique=True, max_length=32, verbose_name='key')),
            ],
        ),
        migrations.CreateModel(
            name='ResetPass',
            fields=[
                ('key', models.CharField(unique=True, max_length=32, verbose_name='key')),
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
        ),
    ]
