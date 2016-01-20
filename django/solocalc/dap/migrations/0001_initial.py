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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('address', models.TextField(null=True, max_length=120, blank=True, verbose_name='Address')),
                ('address_slug', models.SlugField(null=True, max_length=120, blank=True)),
                ('formatted_address', models.TextField(null=True, max_length=120, blank=True)),
                ('coordinates', models.CharField(null=True, max_length=80, blank=True, verbose_name='latitude, longitude')),
                ('elevation', models.FloatField(null=True, default=0.0, blank=True)),
                ('begin', models.CharField(null=True, max_length=30, blank=True)),
                ('begin_slug', models.SlugField(null=True, max_length=120, blank=True)),
                ('end', models.CharField(null=True, max_length=30, blank=True)),
                ('frequency', models.CharField(null=True, default='10 min', max_length=20, blank=True)),
                ('time_sequence', models.TextField(null=True, max_length=600, blank=True)),
                ('ephem_sequence', models.TextField(null=True, max_length=6000, blank=True)),
                ('statistics', models.TextField(null=True, max_length=300, blank=True)),
                ('irradiance_sequence', models.TextField(null=True, max_length=6000, blank=True)),
                ('panel_azimuth', models.FloatField(null=True, default=180, max_length=20, blank=True, verbose_name='Panel azimuth (degrees from north)')),
                ('panel_tilt', models.FloatField(null=True, default=30, max_length=20, blank=True, verbose_name='Panel tilt (degrees from vertical)')),
                ('doc', models.CharField(null=True, max_length=80, blank=True)),
                ('pix1', models.CharField(null=True, max_length=80, blank=True)),
                ('pix2', models.CharField(null=True, max_length=80, blank=True)),
            ],
        ),
    ]
