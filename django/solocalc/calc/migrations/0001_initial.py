# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(blank=True, verbose_name='Address', max_length=120, null=True)),
                ('address_slug', models.SlugField(blank=True, max_length=120, null=True)),
                ('formatted_address', models.TextField(blank=True, max_length=120, null=True)),
                ('coordinates', models.CharField(blank=True, verbose_name='latitude, longitude', max_length=80, null=True)),
                ('elevation', models.FloatField(blank=True, default=0.0, null=True)),
                ('begin', models.CharField(blank=True, max_length=30, null=True)),
                ('begin_slug', models.SlugField(blank=True, max_length=120, null=True)),
                ('end', models.CharField(blank=True, max_length=30, null=True)),
                ('frequency', models.CharField(blank=True, default='10 min', max_length=20, null=True)),
                ('time_sequence', models.TextField(blank=True, max_length=600, null=True)),
                ('ephem_sequence', models.TextField(blank=True, max_length=6000, null=True)),
                ('statistics', models.TextField(blank=True, max_length=300, null=True)),
                ('irradiance_sequence', models.TextField(blank=True, max_length=6000, null=True)),
                ('panel_azimuth', models.FloatField(blank=True, verbose_name='Panel azimuth (degrees from north)', max_length=20, null=True, default=180)),
                ('panel_tilt', models.FloatField(blank=True, verbose_name='Panel tilt (degrees from vertical)', max_length=20, null=True, default=30)),
                ('doc', models.CharField(blank=True, max_length=80, null=True)),
                ('pix1', models.CharField(blank=True, max_length=80, null=True)),
                ('pix2', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
