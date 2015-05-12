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
            name='OrderedBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70, verbose_name='title of book')),
                ('author', models.CharField(max_length=60, verbose_name='author')),
                ('publisher', models.CharField(max_length=60, verbose_name='publisher')),
                ('price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2)),
                ('date_order', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date order')),
                ('paid', models.BooleanField(default=0, verbose_name='paid')),
                ('returned', models.BooleanField(verbose_name='returned')),
                ('book', models.ForeignKey(verbose_name='book', to='books.Book')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
