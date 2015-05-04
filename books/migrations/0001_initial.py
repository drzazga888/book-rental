# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rate', models.IntegerField(verbose_name='rate')),
                ('comment', models.TextField(verbose_name='comment')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='books.Categories'),
        ),
    ]
