# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'emis_account_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'account', unique=True, to=orm['auth.User'])),
            ('mobile_number', self.gf('django.db.models.fields.BigIntegerField')()),
            ('user_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emis_account.User_Category'])),
            ('associated_with', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'emis_account', ['Account'])

        # Adding model 'SignupCode'
        db.create_table(u'emis_account_signupcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('max_uses', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('expiry', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('inviter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('use_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'emis_account', ['SignupCode'])

        # Adding model 'SignupCodeResult'
        db.create_table(u'emis_account_signupcoderesult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('signup_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emis_account.SignupCode'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'emis_account', ['SignupCodeResult'])

        # Adding model 'EmailAddress'
        db.create_table(u'emis_account_emailaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'emis_account', ['EmailAddress'])

        # Adding model 'EmailConfirmation'
        db.create_table(u'emis_account_emailconfirmation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emis_account.EmailAddress'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 4, 0, 0))),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'emis_account', ['EmailConfirmation'])

        # Adding model 'AccountDeletion'
        db.create_table(u'emis_account_accountdeletion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('date_requested', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_expunged', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'emis_account', ['AccountDeletion'])

        # Adding model 'User_Category'
        db.create_table(u'emis_account_user_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_category', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'emis_account', ['User_Category'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'emis_account_account')

        # Deleting model 'SignupCode'
        db.delete_table(u'emis_account_signupcode')

        # Deleting model 'SignupCodeResult'
        db.delete_table(u'emis_account_signupcoderesult')

        # Deleting model 'EmailAddress'
        db.delete_table(u'emis_account_emailaddress')

        # Deleting model 'EmailConfirmation'
        db.delete_table(u'emis_account_emailconfirmation')

        # Deleting model 'AccountDeletion'
        db.delete_table(u'emis_account_accountdeletion')

        # Deleting model 'User_Category'
        db.delete_table(u'emis_account_user_category')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'emis_account.account': {
            'Meta': {'object_name': 'Account'},
            'associated_with': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.BigIntegerField', [], {}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'account'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'user_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emis_account.User_Category']"})
        },
        u'emis_account.accountdeletion': {
            'Meta': {'object_name': 'AccountDeletion'},
            'date_expunged': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'emis_account.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'emis_account.emailconfirmation': {
            'Meta': {'object_name': 'EmailConfirmation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 4, 0, 0)'}),
            'email_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emis_account.EmailAddress']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'emis_account.signupcode': {
            'Meta': {'object_name': 'SignupCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'expiry': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inviter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'max_uses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'use_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'emis_account.signupcoderesult': {
            'Meta': {'object_name': 'SignupCodeResult'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signup_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emis_account.SignupCode']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'emis_account.user_category': {
            'Meta': {'object_name': 'User_Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_category': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['emis_account']