# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dap', '0002_calculation_dap_process_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculation',
            name='dap_process_temp',
        ),
        migrations.AddField(
            model_name='calculation',
            name='pix3',
            field=models.CharField(null=True, max_length=80, blank=True),
        ),
    ]
