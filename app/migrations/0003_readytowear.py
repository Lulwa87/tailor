# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_productdesign_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadyToWear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('category', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.CharField(max_length=225, null=True, blank=True)),
                ('size', models.CharField(max_length=225, null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('brand', models.CharField(max_length=255, null=True, blank=True)),
                ('fabric_tag', models.ManyToManyField(to='app.FabricTag', null=True, blank=True)),
            ],
        ),
    ]
