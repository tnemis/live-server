# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Child_detail'
        db.create_table(u'students_child_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aadhaar_eid_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('aadhaar_uid_number', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('photograph', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('community', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Community'])),
            ('religion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Religion'])),
            ('mothertounge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Language'])),
            ('phone_number', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('child_differently_abled', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('differently_abled', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Differently_abled'], null=True, blank=True)),
            ('child_disadvantaged_group', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('disadvantaged_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Disadvantaged_group'], null=True, blank=True)),
            ('subcaste', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['baseapp.Sub_Castes'], null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Nationality'])),
            ('house_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('native_district', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pin_code', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('blood_group', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('class_studying', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Class_Studying'])),
            ('group_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Group_code'], null=True, blank=True)),
            ('attendance_status', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sport_participation', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('education_medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Education_medium'])),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.District'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Block'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Zone'])),
            ('habitation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Habitation'])),
            ('unique_id_no', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.School'])),
            ('staff_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Bank'], null=True, blank=True)),
            ('bank_account_no', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('govt_schemes_status', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('academic_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Academic_Year'])),
            ('transfer_flag', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('transfer_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('modification_flag', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('verification_flag', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'students', ['Child_detail'])

        # Adding M2M table for field schemes on 'Child_detail'
        m2m_table_name = db.shorten_name(u'students_child_detail_schemes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('child_detail', models.ForeignKey(orm[u'students.child_detail'], null=False)),
            ('schemes', models.ForeignKey(orm[u'baseapp.schemes'], null=False))
        ))
        db.create_unique(m2m_table_name, ['child_detail_id', 'schemes_id'])

        # Adding model 'Child_family_detail'
        db.create_table(u'students_child_family_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('child_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Child_detail'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.Block'])),
            ('member_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('member_relationship', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('member_age', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('member_qualification', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('member_employed', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('member_income', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('staff_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'students', ['Child_family_detail'])

        # Adding model 'Child_Transfer_History'
        db.create_table(u'students_child_transfer_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('child_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Child_detail'])),
            ('old_school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['baseapp.School'])),
            ('tc_issue_date', self.gf('django.db.models.fields.DateField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'students', ['Child_Transfer_History'])


    def backwards(self, orm):
        # Deleting model 'Child_detail'
        db.delete_table(u'students_child_detail')

        # Removing M2M table for field schemes on 'Child_detail'
        db.delete_table(db.shorten_name(u'students_child_detail_schemes'))

        # Deleting model 'Child_family_detail'
        db.delete_table(u'students_child_family_detail')

        # Deleting model 'Child_Transfer_History'
        db.delete_table(u'students_child_transfer_history')


    models = {
        u'baseapp.academic_year': {
            'Meta': {'object_name': 'Academic_Year'},
            'academic_year': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        u'baseapp.religion': {
            'Meta': {'object_name': 'Religion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'religion_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        },
        u'students.child_detail': {
            'Meta': {'object_name': 'Child_detail'},
            'aadhaar_eid_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'aadhaar_uid_number': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'academic_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Academic_Year']"}),
            'attendance_status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Bank']", 'null': 'True', 'blank': 'True'}),
            'bank_account_no': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Block']"}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'child_differently_abled': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'child_disadvantaged_group': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'class_studying': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Class_Studying']"}),
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Community']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'differently_abled': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Differently_abled']", 'null': 'True', 'blank': 'True'}),
            'disadvantaged_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Disadvantaged_group']", 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.District']"}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'education_medium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Education_medium']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'govt_schemes_status': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'group_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Group_code']", 'null': 'True', 'blank': 'True'}),
            'habitation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Habitation']"}),
            'house_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_flag': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mothertounge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Nationality']"}),
            'native_district': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'photograph': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pin_code': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Religion']"}),
            'schemes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['baseapp.Schemes']", 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.School']"}),
            'sport_participation': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'staff_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subcaste': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['baseapp.Sub_Castes']", 'null': 'True', 'blank': 'True'}),
            'transfer_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transfer_flag': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'unique_id_no': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'verification_flag': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Zone']"})
        },
        u'students.child_family_detail': {
            'Meta': {'object_name': 'Child_family_detail'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.Block']"}),
            'child_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['students.Child_detail']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'member_employed': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'member_income': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'member_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'member_qualification': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'member_relationship': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'staff_id': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'students.child_transfer_history': {
            'Meta': {'object_name': 'Child_Transfer_History'},
            'child_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['students.Child_detail']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'old_school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baseapp.School']"}),
            'tc_issue_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['students']