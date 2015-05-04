# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewBooks',
            fields=[
                ('book', models.OneToOneField(primary_key=True, serialize=False, to='books.Book', verbose_name='book')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('book', models.OneToOneField(primary_key=True, serialize=False, to='books.Book', verbose_name='book')),
                ('sequence', models.IntegerField(unique=True, verbose_name='sequence')),
            ],
        ),
        migrations.CreateModel(
            name='TopLoaned',
            fields=[
                ('book', models.OneToOneField(primary_key=True, serialize=False, to='books.Book', verbose_name='book')),
            ],
        ),
        migrations.CreateModel(
            name='TopRates',
            fields=[
                ('book', models.OneToOneField(primary_key=True, serialize=False, to='books.Book', verbose_name='book')),
            ],
        ),
    ]
