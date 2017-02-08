from django.db import models
# from simple_history.models import HistoricalRecords #to store history
from django.db.models.fields import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import caching.base  # cache data
#to validate min and max value
from django.core.validators import MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey


"""
Model for Bank District
"""

class Bank_districtnew(models.Model):
    district_code = models.PositiveIntegerField(
        unique=True, validators=[MinValueValidator(3300), MaxValueValidator(3399)])
    bank_dist = models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' % (self.bank_dist)

"""
Model for Bank Master
"""
class Banknew(caching.base.CachingMixin, models.Model):
    bank_dist=models.ForeignKey(Bank_districtnew)
    bankcode = models.CharField(max_length=4)
    bank = models.CharField(max_length=200)
    objects = caching.base.CachingManager()
    def __unicode__(self):
        return u'%s' % (self.bank)

"""
Model for Bank Branch Master
"""

class Branchnew(caching.base.CachingMixin, models.Model):
    bank = models.ForeignKey(Banknew)
    bank_name= models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    branch_add=models.CharField(max_length=300)
    contact_no=models.CharField(max_length=20,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    ifsc_code= models.CharField(max_length=30)
    micr_code=models.CharField(max_length=30)
    objects = caching.base.CachingManager()
    def __unicode__(self):
        return u'%s%s%s' % (self.branch,", IFSC:",self.ifsc_code)  



"""
Model for Assembly constituencies
"""


class Assembly(models.Model):
    assembly_name = models.CharField(max_length=100)
    district = models.ForeignKey('District')
    
    def __unicode__(self):
        return u'%s' % (self.assembly_name)

"""
Model for Parliamentary constituencies
"""


class Parliamentary(models.Model):
    parliamentary_name = models.CharField(max_length=100)
    

    def __unicode__(self):
        return u'%s' % (self.parliamentary_name)


"""
Model for State
"""

class State(caching.base.CachingMixin, models.Model):
    state_name = models.CharField(max_length=100)
    objects = caching.base.CachingManager()
    
    def __unicode__(self):
        return u'%s' % (self.state_name)

"""
Model for District
"""


class District(caching.base.CachingMixin, models.Model):
    district_code = models.PositiveIntegerField(
        unique=True, validators=[MinValueValidator(3300), MaxValueValidator(3399)])
    district_name = models.CharField(max_length=100)
    objects = caching.base.CachingManager()
    
    def __unicode__(self):
        return u'%s' % (self.district_name)

"""
Model for Block
"""


class Block(caching.base.CachingMixin, models.Model):
    block_code = models.PositiveIntegerField(
        unique=True, validators=[MinValueValidator(330000), MaxValueValidator(339999)])
    block_name = models.CharField(max_length=100)
    block_type = models.CharField(max_length=50)
    district = models.ForeignKey('District')
    objects = caching.base.CachingManager()
    
    def __unicode__(self):
        return u'%s %s %s' % (self.block_code, self.block_name, self.block_type)


"""
Model for Zone Type
"""


class Zone_type(models.Model):
    zone_type = models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s' % (self.zone_type)

"""
Model for zone
"""


class Zone (models.Model):
    zone_type = models.ForeignKey(Zone_type)
    code = models.PositiveIntegerField(unique=True, validators=[
                                       MinValueValidator(330000000), MaxValueValidator(339999999)])
    name = models.CharField(max_length=100)
    block = models.ForeignKey('Block')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.zone_type)


"""
Model for Habitation
"""


class Habitation(caching.base.CachingMixin, models.Model):
    code = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    #ward_number = models.CharField(max_length=100)
    block = models.ForeignKey('Block')
    zone = ChainedForeignKey(
        Zone, chained_field='block', chained_model_field='block', auto_choose=True)
    objects = caching.base.CachingManager()

    def __unicode__(self):
        return u'%s' % (self.name)


"""
Model for School
"""


class School(models.Model):
    school_code = BigIntegerField()
    school_name = models.CharField(max_length=100)
    district = models.ForeignKey('District')
    block = ChainedForeignKey(
        Block, chained_field='district', chained_model_field='district', auto_choose=True)
    #block = models.ForeignKey('Block')
    habitation = ChainedForeignKey(
        Habitation, chained_field='block', chained_model_field='block', auto_choose=True)
    management = models.ForeignKey('Management')
    category = models.ForeignKey('Category')
    student_id_count = models.PositiveIntegerField()
    
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.school_code, self.school_name, self.habitation.name, self.district.district_name, self.block.block_name, self.management.management_name, self.category.category_name, self.student_id_count)

"""
Model for Taluk
"""


class Taluk(caching.base.CachingMixin, models.Model):
    taluk_name = models.CharField(max_length=100)
    district = models.ForeignKey('District')

    objects = caching.base.CachingManager()

    def __unicode__(self):
        return u'%s' % (self.taluk_name)

"""
Model for Educational District :
"""


class Educational_district(models.Model):
    educational_district = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.educational_district)


"""
Model for Educational Block/ Mandal/ Taluk Name
"""


class Educational_block(models.Model):
    educational_block = models.CharField(max_length=100)
    district = models.ForeignKey('District')

    def __unicode__(self):
        return u'%s' % (self.educational_block)

"""
Model for Revenue Block/ Mandal / Taluk name :
"""


class Revenue_block(models.Model):
    revenue_block = models.CharField(max_length=100)
    district = models.ForeignKey('District')

    def __unicode__(self):
        return u'%s' % (self.revenue_block)


"""
Model for Community
"""


class Community(models.Model):
    community_code = models.CharField(max_length=100)
    community_name = models.CharField(max_length=100)
    religion = models.ForeignKey('Religion')
    def __unicode__(self):
        return u'%s' % (self.community_name)

"""
Model for Sub Castes
"""


class Sub_Castes(models.Model):
    caste_code = models.CharField(max_length=10)
    caste_name = models.CharField(max_length=1000)
    community = models.ForeignKey('Community')

    def __unicode__(self):
        return u'%s %s %s' % (self.caste_name,self.caste_code, self.community.community_name)


"""
Model for Religion
"""


class Religion(models.Model):
    religion_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.religion_name)

"""
Model for Language
"""


class Language(models.Model):
    language_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.language_name)

"""
Model for Differently Abled
"""


class Differently_abled(models.Model):
    da_code = models.CharField(max_length=100)
    da_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.da_code, self.da_name)

"""
Model for Disadvantaged Group
"""


class Disadvantaged_group(models.Model):
    dis_group_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.dis_group_name)


"""
Model for Government Schemes
"""


class Schemes(models.Model):
    scheme_code = models.CharField(max_length=100)
    scheme_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.scheme_code, self.scheme_name)

"""
Model for School Management
"""


class Management(models.Model):
    management_code = models.CharField(max_length=100)
    management_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.management_code, self.management_name)

"""
Model for School Category
"""


class Category(models.Model):
    category_code = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.category_code, self.category_name)

"""
Model for Nationality
"""


class Nationality(models.Model):
    nationality = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.nationality)

"""
Model for class studying
"""


class Class_Studying(models.Model):
    class_studying = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s' % (self.class_studying)

"""
Model for group code for hsc
"""


class Group_code(models.Model):
    group_code = models.PositiveIntegerField()
    group_name = models.CharField(max_length=100)
    group_description = models.TextField(max_length=500)

    def __unicode__(self):
        return u'%s %s %s' % (self.group_code, self.group_name, self.group_description)


class Group_code_cbse(models.Model):
    group_code = models.PositiveIntegerField()
    group_name = models.CharField(max_length=100)
    

    def __unicode__(self):
        return u'%s %s' % (self.group_code, self.group_name)


"""
Model for Education Medium
"""


class Education_medium(models.Model):
    education_medium = models.CharField(max_length=15)

    def __unicode__(self):
        return u'%s' % (self.education_medium)

"""
Model for bank
"""


class Bank(models.Model):
    bank = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % (self.bank)

"""
Model for academic unique_for_year
"""


class Academic_Year(models.Model):
    academic_year = models.CharField(max_length=9)

    def __unicode__(self):
        return u'%s' % (self.academic_year)


""" Model for pool database """
class Child_detail_pool_database(models.Model):
    district = models.ForeignKey('District')
    block = ChainedForeignKey(
        Block, chained_field='district', chained_model_field='district', auto_choose=True)
    school = ChainedForeignKey(
        School, chained_field='block', chained_model_field='block', auto_choose=True)
    class_last_studied = models.CharField(max_length=20,blank=True,null=True)
    unique_id_no = models.BigIntegerField(blank=True, null=True)
    class_studying = models.ForeignKey(Class_Studying) 
    migrated_school = models.CharField(max_length=100,blank=True,null=True)

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.district.district_name, self.block.block_name, self.school.school_name, self.class_last_studied, self.unique_id_no, self.class_studying, self.migrated_school)

