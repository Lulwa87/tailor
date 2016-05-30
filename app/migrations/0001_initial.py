# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('username', models.CharField(unique=True, max_length=255, verbose_name=b'username')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name=b'last name', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=False, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabric_id', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('pattern', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FabricTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material_id', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Measurment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demo', models.FileField(null=True, upload_to=b'demos', blank=True)),
                ('neck', models.FloatField(default=0.0, null=True, blank=True)),
                ('shoulder', models.FloatField(default=0.0, null=True, blank=True)),
                ('arm_hole', models.FloatField(default=0.0, null=True, blank=True)),
                ('upper_arm', models.FloatField(default=0.0, null=True, blank=True)),
                ('bust', models.FloatField(default=0.0, null=True, blank=True)),
                ('length', models.FloatField(default=0.0, null=True, blank=True)),
                ('sleeve', models.FloatField(default=0.0, null=True, blank=True)),
                ('waist', models.FloatField(default=0.0, null=True, blank=True)),
                ('hips', models.FloatField(default=0.0, null=True, blank=True)),
                ('thighs', models.FloatField(default=0.0, null=True, blank=True)),
                ('bottom_length', models.FloatField(default=0.0, null=True, blank=True)),
                ('ankle', models.FloatField(default=0.0, null=True, blank=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModelTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDesign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('description', models.CharField(max_length=225, null=True, blank=True)),
                ('size', models.CharField(max_length=225, null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('fabric_tag', models.ManyToManyField(to='app.FabricTag', null=True, blank=True)),
                ('material_tag', models.ManyToManyField(to='app.MaterialTag', null=True, blank=True)),
                ('model_tag', models.ManyToManyField(to='app.ModelTag', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tailor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('experience', models.CharField(max_length=200, null=True, blank=True)),
                ('specialest', models.CharField(max_length=200, null=True, blank=True)),
                ('model', models.ForeignKey(blank=True, to='app.ProductDesign', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='material_tag',
            field=models.ManyToManyField(to='app.MaterialTag', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fabric',
            name='fabric_tag',
            field=models.ManyToManyField(to='app.FabricTag', null=True, blank=True),
        ),
    ]
