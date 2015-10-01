# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Othername', models.CharField(max_length=200)),
                ('DOB', models.DateTimeField(verbose_name='date born')),
                ('Gender', models.CharField(max_length=8)),
                ('IdType', models.CharField(max_length=200)),
                ('IdNumber', models.CharField(max_length=200)),
                ('FarmArea', models.CharField(max_length=200)),
                ('FarmAreaDimensions', models.CharField(max_length=200)),
                ('ZoneId', models.CharField(max_length=200)),
                ('BlockId', models.CharField(max_length=200)),
                ('CampId', models.CharField(max_length=200)),
                ('DistrictId', models.CharField(max_length=200)),
                ('FarmAreaId', models.CharField(max_length=200)),
            ],
        ),
    ]
