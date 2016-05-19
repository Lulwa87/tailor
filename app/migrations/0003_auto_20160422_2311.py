# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160422_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurment',
            name='ankle',
            field=models.FloatField(default=datetime.datetime(2016, 4, 22, 23, 10, 24, 197039, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurment',
            name='arm_hole',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='belly',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='bottom_length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='bust',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='hips',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='knee',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='shoulder',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='thighs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='upper_arm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='upper_belly',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurment',
            name='waist',
            field=models.FloatField(),
        ),
    ]
