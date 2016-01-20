# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteConfiguration'
        db.create_table(u'theme_siteconfiguration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('col1_heading', self.gf('django.db.models.fields.CharField')(default='Contact us', max_length=200)),
            ('col1_content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('col2_heading', self.gf('django.db.models.fields.CharField')(default='Go social', max_length=200)),
            ('col2_content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('col3_heading', self.gf('django.db.models.fields.CharField')(default='Subscribe', max_length=200)),
            ('col3_content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('twitter_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('facebook_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('pinterest_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('youtube_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('github_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('linkedin_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('vk_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('gplus_link', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('copyright', self.gf('django.db.models.fields.TextField')(default='{{ settings.SITE_TITLE }} &copy {% now "Y" %}')),
        ))
        db.send_create_signal(u'theme', ['SiteConfiguration'])


    def backwards(self, orm):
        # Deleting model 'SiteConfiguration'
        db.delete_table(u'theme_siteconfiguration')


    models = {
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.siteconfiguration': {
            'Meta': {'object_name': 'SiteConfiguration'},
            'col1_content': ('mezzanine.core.fields.RichTextField', [], {}),
            'col1_heading': ('django.db.models.fields.CharField', [], {'default': "'Contact us'", 'max_length': '200'}),
            'col2_content': ('mezzanine.core.fields.RichTextField', [], {}),
            'col2_heading': ('django.db.models.fields.CharField', [], {'default': "'Go social'", 'max_length': '200'}),
            'col3_content': ('mezzanine.core.fields.RichTextField', [], {}),
            'col3_heading': ('django.db.models.fields.CharField', [], {'default': "'Subscribe'", 'max_length': '200'}),
            'copyright': ('django.db.models.fields.TextField', [], {'default': '\'{{ settings.SITE_TITLE }} &copy {% now "Y" %}\''}),
            'facebook_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'github_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'gplus_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'pinterest_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'twitter_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'vk_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'youtube_link': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['theme']