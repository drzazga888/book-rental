# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70, verbose_name='title of book')),
                ('description', models.TextField(verbose_name='ddescription')),
                ('author', models.CharField(max_length=60, verbose_name='author')),
                ('publisher', models.CharField(max_length=60, verbose_name='publisher')),
                ('price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2)),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity of books')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
                ('sale', models.BooleanField(verbose_name='sale')),
                ('isbn', models.CharField(default=b'0000000000000', max_length=13, verbose_name='isbn')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='name of category')),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(verbose_name='rate')),
                ('comment', models.TextField(verbose_name='comment')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
                ('book', models.OneToOneField(verbose_name='book', to='books.Book')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='books.Categories'),
        ),
    ]
