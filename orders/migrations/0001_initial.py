# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_order', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date order')),
                ('total_price', models.DecimalField(verbose_name='total price', max_digits=5, decimal_places=2)),
                ('paid', models.BooleanField(verbose_name='paid')),
                ('realized', models.BooleanField(verbose_name='realized')),
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
