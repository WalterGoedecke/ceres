# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='number_recent_posts',
            field=models.PositiveIntegerField(default=3, help_text='Number of recent blog posts to show'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='recent_blog_heading',
            field=models.CharField(default='Latest blog posts', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='welcome_heading',
            field=models.CharField(default='Welcome', max_length=100),
        ),
        migrations.AlterField(
            model_name='iconbox',
            name='icon',
            field=models.CharField(max_length=50, help_text='Enter the name of a font awesome icon, i.e. fa-eye. A list is available here http://fontawesome.io/'),
        ),
        migrations.AlterField(
            model_name='iconbox',
            name='link',
            field=models.CharField(blank=True, max_length=2000, help_text='Optional, if provided clicking the box will go here.'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='col1_heading',
            field=models.CharField(default='Contact us', max_length=200),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='col2_content',
            field=mezzanine.core.fields.RichTextField(blank=True, help_text='If present will override the social network icons.'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='col2_heading',
            field=models.CharField(default='Go social', max_length=200),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='col3_heading',
            field=models.CharField(default='Subscribe', max_length=200),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='copyright',
            field=models.TextField(default='&copy {% now "Y" %} {{ settings.SITE_TITLE }}'),
        ),
    ]
