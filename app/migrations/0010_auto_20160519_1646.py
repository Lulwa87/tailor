# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160503_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_id', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('description', models.CharField(max_length=225, null=True, blank=True)),
                ('size', models.CharField(max_length=225, null=True, blank=True)),
                ('fabric_tag', models.ManyToManyField(to='app.FabricTag', null=True, blank=True)),
                ('material_tag', models.ManyToManyField(to='app.MaterialTag', null=True, blank=True)),
                ('model_tag', models.ManyToManyField(to='app.ModelTag', null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='model',
            name='fabric_tag',
        ),
        migrations.RemoveField(
            model_name='model',
            name='material_tag',
        ),
        migrations.RemoveField(
            model_name='model',
            name='model_tag',
        ),
        migrations.RenameField(
            model_name='measurment',
            old_name='belly',
            new_name='length',
        ),
        migrations.RenameField(
            model_name='measurment',
            old_name='knee',
            new_name='neck',
        ),
        migrations.RenameField(
            model_name='measurment',
            old_name='upper_belly',
            new_name='sleeve',
        ),
        migrations.RemoveField(
            model_name='fabric',
            name='model',
        ),
        migrations.RemoveField(
            model_name='material',
            name='model',
        ),
        migrations.AddField(
            model_name='measurment',
            name='demo',
            field=models.FileField(null=True, upload_to=b'demos', blank=True),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='fabric_tag',
            field=models.ManyToManyField(to='app.FabricTag', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_tag',
            field=models.ManyToManyField(to='app.MaterialTag', null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='tailor',
            name='model',
        ),
        migrations.DeleteModel(
            name='Model',
        ),
        migrations.AddField(
            model_name='tailor',
            name='model',
            field=models.ForeignKey(blank=True, to='app.DesignModel', null=True),
        ),
    ]
