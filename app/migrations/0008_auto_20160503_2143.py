# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160422_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='MaterialTag',
        ),
        migrations.RemoveField(
            model_name='model',
            name='tag',
        ),
        migrations.AddField(
            model_name='material',
            name='material_tag',
            field=models.ManyToManyField(to='app.MaterialTag'),
        ),
        migrations.AddField(
            model_name='model',
            name='model_tag',
            field=models.ManyToManyField(to='app.ModelTag'),
        ),
    ]
