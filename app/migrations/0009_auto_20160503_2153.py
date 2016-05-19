# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160503_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='material_tag',
            field=models.ManyToManyField(to='app.MaterialTag'),
        ),
        migrations.AddField(
            model_name='fabric',
            name='fabric_tag',
            field=models.ManyToManyField(to='app.FabricTag'),
        ),
        migrations.AddField(
            model_name='model',
            name='fabric_tag',
            field=models.ManyToManyField(to='app.FabricTag'),
        ),
    ]
