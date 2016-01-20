# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('heading', models.CharField(max_length=100)),
                ('slide_in_one_icon', models.CharField(max_length=50, blank=True)),
                ('slide_in_one', models.CharField(max_length=200, blank=True)),
                ('slide_in_two_icon', models.CharField(max_length=50, blank=True)),
                ('slide_in_two', models.CharField(max_length=200, blank=True)),
                ('slide_in_three_icon', models.CharField(max_length=50, blank=True)),
                ('slide_in_three', models.CharField(max_length=200, blank=True)),
                ('header_background', mezzanine.core.fields.FileField(max_length=255, verbose_name='Header Background', blank=True)),
                ('header_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Header Image (optional)', blank=True)),
                ('welcome_heading', models.CharField(default=b'Welcome', max_length=100)),
                ('content', mezzanine.core.fields.RichTextField()),
                ('recent_blog_heading', models.CharField(default=b'Latest blog posts', max_length=100)),
                ('number_recent_posts', models.PositiveIntegerField(default=3, help_text=b'Number of recent blog posts to show')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='IconBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', models.CharField(help_text=b'Enter the name of a font awesome icon, i.e. fa-eye. A list is available here http://fontawesome.io/', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('link_text', models.CharField(max_length=100)),
                ('link', models.CharField(help_text=b'Optional, if provided clicking the box will go here.', max_length=2000, blank=True)),
                ('homepage', models.ForeignKey(related_name='boxes', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('col1_heading', models.CharField(default=b'Contact us', max_length=200)),
                ('col1_content', mezzanine.core.fields.RichTextField()),
                ('col2_heading', models.CharField(default=b'Go social', max_length=200)),
                ('col2_content', mezzanine.core.fields.RichTextField(help_text=b'If present will override the social network icons.', blank=True)),
                ('col3_heading', models.CharField(default=b'Subscribe', max_length=200)),
                ('col3_content', mezzanine.core.fields.RichTextField()),
                ('twitter_link', models.CharField(max_length=2000, blank=True)),
                ('facebook_link', models.CharField(max_length=2000, blank=True)),
                ('pinterest_link', models.CharField(max_length=2000, blank=True)),
                ('youtube_link', models.CharField(max_length=2000, blank=True)),
                ('github_link', models.CharField(max_length=2000, blank=True)),
                ('linkedin_link', models.CharField(max_length=2000, blank=True)),
                ('vk_link', models.CharField(max_length=2000, blank=True)),
                ('gplus_link', models.CharField(max_length=2000, blank=True)),
                ('has_social_network_links', models.BooleanField(default=False)),
                ('copyright', models.TextField(default=b'&copy {% now "Y" %} {{ settings.SITE_TITLE }}')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Site Configuration',
                'verbose_name_plural': 'Site Configuration',
            },
        ),
    ]