# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabric',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='model',
            name='description',
            field=models.CharField(max_length=225, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='model',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='model',
            name='size',
            field=models.CharField(max_length=225, null=True, blank=True),
        ),
    ]
