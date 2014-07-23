# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.runtime'
        db.alter_column(u'tomatoes_movie', 'runtime', self.gf('django.db.models.fields.CharField')(max_length=6, null=True))

    def backwards(self, orm):

        # Changing field 'Movie.runtime'
        db.alter_column(u'tomatoes_movie', 'runtime', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'critic_rating': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'runtime': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['tomatoes']