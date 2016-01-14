# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SiteConfiguration.has_social_network_links'
        db.add_column(u'theme_siteconfiguration', 'has_social_network_links',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SiteConfiguration.has_social_network_links'
        db.delete_column(u'theme_siteconfiguration', 'has_social_network_links')


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
            'col2_content': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'col2_heading': ('django.db.models.fields.CharField', [], {'default': "'Go social'", 'max_length': '200'}),
            'col3_content': ('mezzanine.core.fields.RichTextField', [], {}),
            'col3_heading': ('django.db.models.fields.CharField', [], {'default': "'Subscribe'", 'max_length': '200'}),
            'copyright': ('django.db.models.fields.TextField', [], {'default': '\'{{ settings.SITE_TITLE }} &copy {% now "Y" %}\''}),
            'facebook_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'github_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'gplus_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'has_social_network_links': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'pinterest_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'twitter_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'vk_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']