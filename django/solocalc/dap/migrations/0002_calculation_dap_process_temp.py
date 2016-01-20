# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='dap_process_temp',
            field=models.TextField(null=True, max_length=60, blank=True),
        ),
    ]
