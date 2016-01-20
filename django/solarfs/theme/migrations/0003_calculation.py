# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20151204_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('address', models.TextField(max_length=120, verbose_name='Address', null=True, blank=True)),
                ('address_slug', models.SlugField(max_length=120, null=True, blank=True)),
                ('formatted_address', models.TextField(max_length=120, null=True, blank=True)),
                ('coordinates', models.CharField(max_length=80, verbose_name='latitude, longitude', null=True, blank=True)),
                ('elevation', models.FloatField(default=0.0, null=True, blank=True)),
                ('begin', models.CharField(max_length=30, null=True, blank=True)),
                ('begin_slug', models.SlugField(max_length=120, null=True, blank=True)),
                ('end', models.CharField(max_length=30, null=True, blank=True)),
                ('frequency', models.CharField(default='10 min', max_length=20, null=True, blank=True)),
                ('time_sequence', models.TextField(max_length=600, null=True, blank=True)),
                ('ephem_sequence', models.TextField(max_length=6000, null=True, blank=True)),
                ('statistics', models.TextField(max_length=300, null=True, blank=True)),
                ('irradiance_sequence', models.TextField(max_length=6000, null=True, blank=True)),
                ('panel_azimuth', models.FloatField(default=180, max_length=20, verbose_name='Panel azimuth (degrees from north)', null=True, blank=True)),
                ('panel_tilt', models.FloatField(default=30, max_length=20, verbose_name='Panel tilt (degrees from vertical)', null=True, blank=True)),
                ('doc', models.CharField(max_length=80, null=True, blank=True)),
                ('pix1', models.CharField(max_length=80, null=True, blank=True)),
                ('pix2', models.CharField(max_length=80, null=True, blank=True)),
            ],
        ),
    ]
