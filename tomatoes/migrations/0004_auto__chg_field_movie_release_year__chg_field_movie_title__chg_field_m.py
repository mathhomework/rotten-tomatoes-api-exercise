# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.release_year'
        db.alter_column(u'tomatoes_movie', 'release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=20, null=True))

        # Changing field 'Movie.title'
        db.alter_column(u'tomatoes_movie', 'title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Movie.critic_rating'
        db.alter_column(u'tomatoes_movie', 'critic_rating', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'Movie.poster'
        db.alter_column(u'tomatoes_movie', 'poster', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Movie.release_year'
        raise RuntimeError("Cannot reverse this migration. 'Movie.release_year' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Movie.release_year'
        db.alter_column(u'tomatoes_movie', 'release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

        # User chose to not deal with backwards NULL issues for 'Movie.title'
        raise RuntimeError("Cannot reverse this migration. 'Movie.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Movie.title'
        db.alter_column(u'tomatoes_movie', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'Movie.critic_rating'
        raise RuntimeError("Cannot reverse this migration. 'Movie.critic_rating' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Movie.critic_rating'
        db.alter_column(u'tomatoes_movie', 'critic_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

        # User chose to not deal with backwards NULL issues for 'Movie.poster'
        raise RuntimeError("Cannot reverse this migration. 'Movie.poster' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Movie.poster'
        db.alter_column(u'tomatoes_movie', 'poster', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'critic_rating': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'runtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['tomatoes']