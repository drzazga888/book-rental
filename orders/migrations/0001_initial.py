# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('date_order', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date order')),
                ('street', models.CharField(max_length=40, verbose_name='street')),
                ('number', models.CharField(max_length=8, verbose_name='number of house')),
                ('zip', models.CharField(max_length=6, verbose_name='zip code')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2)),
                ('withdrawtype', models.CharField(max_length=50, verbose_name='withdraw type')),
                ('paid', models.BooleanField(default=0, verbose_name='paid')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70, verbose_name='title of book')),
                ('author', models.CharField(max_length=60, verbose_name='author')),
                ('publisher', models.CharField(max_length=60, verbose_name='publisher')),
                ('price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2)),
                ('returned', models.BooleanField(verbose_name='returned')),
                ('book', models.ForeignKey(verbose_name='book', to='books.Book')),
                ('order', models.ForeignKey(verbose_name='order', to='orders.Order')),
            ],
        ),
    ]
