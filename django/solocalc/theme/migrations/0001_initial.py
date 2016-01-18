# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(to='pages.Page', primary_key=True, serialize=False, auto_created=True, parent_link=True)),
                ('heading', models.CharField(max_length=100)),
                ('slide_in_one_icon', models.CharField(max_length=50, blank=True)),
                ('slide_in_one', models.CharField(max_length=200, blank=True)),
                ('slide_in_two_icon', models.CharField(max_length=50, blank=True)),
                ('slide_in_two', models.CharField(max_length=200, blank=True)),
                ('slide_in_three_icon', models.CharField(max_length=50, blank=True)),
                ('slide_in_three', models.CharField(max_length=200, blank=True)),
                ('header_background', mezzanine.core.fields.FileField(max_length=255, verbose_name='Header Background', blank=True)),
                ('header_image', mezzanine.core.fields.FileField(null=True, max_length=255, verbose_name='Header Image (optional)', blank=True)),
                ('welcome_heading', models.CharField(default='Welcome', max_length=100)),
                ('content', mezzanine.core.fields.RichTextField()),
                ('recent_blog_heading', models.CharField(default='Latest blog posts', max_length=100)),
                ('number_recent_posts', models.PositiveIntegerField(help_text='Number of recent blog posts to show', default=3)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', models.CharField(help_text='Enter the name of a font awesome icon, i.e. fa-eye. A list is available here http://fontawesome.io/', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('link_text', models.CharField(max_length=100)),
                ('link', models.CharField(help_text='Optional, if provided clicking the box will go here.', max_length=2000, blank=True)),
                ('homepage', models.ForeignKey(to='theme.HomePage', related_name='boxes')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('col1_heading', models.CharField(default='Contact us', max_length=200)),
                ('col1_content', mezzanine.core.fields.RichTextField()),
                ('col2_heading', models.CharField(default='Go social', max_length=200)),
                ('col2_content', mezzanine.core.fields.RichTextField(help_text='If present will override the social network icons.', blank=True)),
                ('col3_heading', models.CharField(default='Subscribe', max_length=200)),
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
                ('copyright', models.TextField(default='&copy {% now "Y" %} {{ settings.SITE_TITLE }}')),
                ('site', models.ForeignKey(to='sites.Site', editable=False)),
            ],
            options={
                'verbose_name': 'Site Configuration',
                'verbose_name_plural': 'Site Configuration',
            },
        ),
    ]
