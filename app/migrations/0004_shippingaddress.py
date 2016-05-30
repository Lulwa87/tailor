# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_readytowear'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('block', models.IntegerField()),
                ('street', models.CharField(max_length=255)),
                ('avenue', models.CharField(max_length=255, blank=True)),
                ('house_number', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('extra_instructions', models.CharField(max_length=50, blank=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
