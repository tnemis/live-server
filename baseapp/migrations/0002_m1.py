# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'baseapp.academic_year': {
            'Meta': {'object_name': 'Academic_Year'},
            'academic_year': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.assembly': {
            'Meta': {'object_name': 'Assembly'},
            'assembly_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'baseapp.bank': {
            'Meta': {'object_name': 'Bank'},
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.block': {
            'Meta': {'object_name': 'Block'},
            'block_code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'block_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'baseapp.class_studying': {
            'Meta': {'object_name': 'Class_Studying'},
            'class_studying': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.community': {
            'Meta': {'object_name': 'Community'},
            'community_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'community_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.differently_abled': {
            'Meta': {'object_name': 'Differently_abled'},
            'da_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'da_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.disadvantaged_group': {
            'Meta': {'object_name': 'Disadvantaged_group'},
            'dis_group_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.district': {
            'Meta': {'object_name': 'District'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district_code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'district_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'baseapp.education_medium': {
            'Meta': {'object_name': 'Education_medium'},
            'education_medium': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.educational_block': {
            'Meta': {'object_name': 'Educational_block'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            'educational_block': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.educational_district': {
            'Meta': {'object_name': 'Educational_district'},
            'educational_district': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.group_code': {
            'Meta': {'object_name': 'Group_code'},
            'group_code': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'group_description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.habitation': {
            'Meta': {'object_name': 'Habitation'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Block']"}),
            'code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zone': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['baseapp.Zone']"})
        },
        u'baseapp.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'language_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.management': {
            'Meta': {'object_name': 'Management'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'management': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.nationality': {
            'Meta': {'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'baseapp.parliamentary': {
            'Meta': {'object_name': 'Parliamentary'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parliamentary_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.religion': {
            'Meta': {'object_name': 'Religion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'religion_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.revenue_block': {
            'Meta': {'object_name': 'Revenue_block'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue_block': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.schemes': {
            'Meta': {'object_name': 'Schemes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheme_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'scheme_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.school': {
            'Meta': {'object_name': 'School'},
            'block': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['baseapp.Block']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            'habitation': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['baseapp.Habitation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'management': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Management']"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'school_code': ('django.db.models.fields.BigIntegerField', [], {}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student_id_count': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'baseapp.sub_castes': {
            'Meta': {'object_name': 'Sub_Castes'},
            'caste_code': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'caste_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Community']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'baseapp.taluk': {
            'Meta': {'object_name': 'Taluk'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taluk_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'baseapp.zone': {
            'Meta': {'object_name': 'Zone'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Block']"}),
            'code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zone_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Zone_type']"})
        },
        u'baseapp.zone_type': {
            'Meta': {'object_name': 'Zone_type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zone_type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['baseapp']
    symmetrical = True
