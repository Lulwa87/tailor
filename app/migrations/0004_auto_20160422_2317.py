# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160422_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurment',
            name='ankle',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='arm_hole',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='belly',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='bottom_length',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='bust',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='hips',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='knee',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='shoulder',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='thighs',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='upper_arm',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='upper_belly',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='waist',
            field=models.FloatField(default=None),
        ),
    ]
