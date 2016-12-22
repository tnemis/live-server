# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Assembly'
        db.create_table(u'baseapp_assembly', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assembly_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'baseapp', ['Assembly'])

        # Adding model 'Parliamentary'
        db.create_table(u'baseapp_parliamentary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parliamentary_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'baseapp', ['Parliamentary'])

        # Adding model 'District'
        db.create_table(u'baseapp_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district_code', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('district_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'baseapp', ['District'])

        # Adding model 'Block'
        db.create_table(u'baseapp_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('block_code', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('block_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'baseapp', ['Block'])

        # Adding model 'Zone_type'
        db.create_table(u'baseapp_zone_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zone_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'baseapp', ['Zone_type'])

        # Adding model 'Zone'
        db.create_table(u'baseapp_zone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zone_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Zone_type'])),
            ('code', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Block'])),
        ))
        db.send_create_signal(u'baseapp', ['Zone'])

        # Adding model 'Habitation'
        db.create_table(u'baseapp_habitation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Block'])),
            ('zone', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['baseapp.Zone'])),
        ))
        db.send_create_signal(u'baseapp', ['Habitation'])

        # Adding model 'School'
        db.create_table(u'baseapp_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school_code', self.gf('django.db.models.fields.BigIntegerField')()),
            ('school_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
            ('block', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['baseapp.Block'])),
            ('habitation', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['baseapp.Habitation'])),
            ('management', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Management'])),
            ('student_id_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'baseapp', ['School'])

        # Adding model 'Taluk'
        db.create_table(u'baseapp_taluk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taluk_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
        ))
        db.send_create_signal(u'baseapp', ['Taluk'])

        # Adding model 'Educational_district'
        db.create_table(u'baseapp_educational_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('educational_district', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Educational_district'])

        # Adding model 'Educational_block'
        db.create_table(u'baseapp_educational_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('educational_block', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
        ))
        db.send_create_signal(u'baseapp', ['Educational_block'])

        # Adding model 'Revenue_block'
        db.create_table(u'baseapp_revenue_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('revenue_block', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
        ))
        db.send_create_signal(u'baseapp', ['Revenue_block'])

        # Adding model 'Community'
        db.create_table(u'baseapp_community', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('community_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('community_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Community'])

        # Adding model 'Sub_Castes'
        db.create_table(u'baseapp_sub_castes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caste_code', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('caste_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('community', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Community'])),
        ))
        db.send_create_signal(u'baseapp', ['Sub_Castes'])

        # Adding model 'Religion'
        db.create_table(u'baseapp_religion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('religion_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Religion'])

        # Adding model 'Language'
        db.create_table(u'baseapp_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Language'])

        # Adding model 'Differently_abled'
        db.create_table(u'baseapp_differently_abled', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('da_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('da_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Differently_abled'])

        # Adding model 'Disadvantaged_group'
        db.create_table(u'baseapp_disadvantaged_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dis_group_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Disadvantaged_group'])

        # Adding model 'Schemes'
        db.create_table(u'baseapp_schemes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('scheme_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Schemes'])

        # Adding model 'Management'
        db.create_table(u'baseapp_management', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('management', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'baseapp', ['Management'])

        # Adding model 'Nationality'
        db.create_table(u'baseapp_nationality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'baseapp', ['Nationality'])

        # Adding model 'Class_Studying'
        db.create_table(u'baseapp_class_studying', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_studying', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'baseapp', ['Class_Studying'])

        # Adding model 'Group_code'
        db.create_table(u'baseapp_group_code', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_code', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('group_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('group_description', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'baseapp', ['Group_code'])

        # Adding model 'Education_medium'
        db.create_table(u'baseapp_education_medium', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('education_medium', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'baseapp', ['Education_medium'])

        # Adding model 'Bank'
        db.create_table(u'baseapp_bank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'baseapp', ['Bank'])

        # Adding model 'Academic_Year'
        db.create_table(u'baseapp_academic_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('academic_year', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal(u'baseapp', ['Academic_Year'])


    def backwards(self, orm):
        # Deleting model 'Assembly'
        db.delete_table(u'baseapp_assembly')

        # Deleting model 'Parliamentary'
        db.delete_table(u'baseapp_parliamentary')

        # Deleting model 'District'
        db.delete_table(u'baseapp_district')

        # Deleting model 'Block'
        db.delete_table(u'baseapp_block')

        # Deleting model 'Zone_type'
        db.delete_table(u'baseapp_zone_type')

        # Deleting model 'Zone'
        db.delete_table(u'baseapp_zone')

        # Deleting model 'Habitation'
        db.delete_table(u'baseapp_habitation')

        # Deleting model 'School'
        db.delete_table(u'baseapp_school')

        # Deleting model 'Taluk'
        db.delete_table(u'baseapp_taluk')

        # Deleting model 'Educational_district'
        db.delete_table(u'baseapp_educational_district')

        # Deleting model 'Educational_block'
        db.delete_table(u'baseapp_educational_block')

        # Deleting model 'Revenue_block'
        db.delete_table(u'baseapp_revenue_block')

        # Deleting model 'Community'
        db.delete_table(u'baseapp_community')

        # Deleting model 'Sub_Castes'
        db.delete_table(u'baseapp_sub_castes')

        # Deleting model 'Religion'
        db.delete_table(u'baseapp_religion')

        # Deleting model 'Language'
        db.delete_table(u'baseapp_language')

        # Deleting model 'Differently_abled'
        db.delete_table(u'baseapp_differently_abled')

        # Deleting model 'Disadvantaged_group'
        db.delete_table(u'baseapp_disadvantaged_group')

        # Deleting model 'Schemes'
        db.delete_table(u'baseapp_schemes')

        # Deleting model 'Management'
        db.delete_table(u'baseapp_management')

        # Deleting model 'Nationality'
        db.delete_table(u'baseapp_nationality')

        # Deleting model 'Class_Studying'
        db.delete_table(u'baseapp_class_studying')

        # Deleting model 'Group_code'
        db.delete_table(u'baseapp_group_code')

        # Deleting model 'Education_medium'
        db.delete_table(u'baseapp_education_medium')

        # Deleting model 'Bank'
        db.delete_table(u'baseapp_bank')

        # Deleting model 'Academic_Year'
        db.delete_table(u'baseapp_academic_year')


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