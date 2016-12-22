
from django.db import models


from django.db.models.fields import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import caching.base  # cache data
#to validate min and max value
from django.core.validators import MaxValueValidator, MinValueValidator
from smart_selects.db_fields import ChainedForeignKey
from baseapp.models import *


# Create your models here.


class Crc(models.Model):
    code = IntegerField()
    crc = models.CharField(max_length=60)
    block = models.ForeignKey(Block)
    def __unicode__(self):
        return u'%d %s %s' % (self.code,self.crc,self.block.block_name)

class Brc(models.Model):
    code = IntegerField()
    brc = models.CharField(max_length=60)
    block = models.ForeignKey(Block)
    def __unicode__(self):
        return u'%d %s %s' % (self.code,self.brc,self.block.block_name)

class Area_classification(models.Model):
    area = models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s' % (self.area)

class School_category(models.Model):
    category_code = IntegerField()
    category = models.CharField(max_length=60)
    def __unicode__(self):
        return u'%d %s' % (self.category_code,self.category)

class School_type(models.Model):
    code = IntegerField()
    school_type = models.CharField(max_length=20)
    def __unicode__(self):
        return u'%d %s' % (self.code,self.school_type)

class School_managed(models.Model):
    management_code = IntegerField()
    management = models.CharField(max_length=100)
    def __unicode__(self):
        return u'%d %s' % (self.management_code,self.management)


"""
Model for School
"""

class School_info(models.Model):
    school = models.ForeignKey(School)
    medium1 = models.CharField(max_length=20)
    medium2 = models.CharField(max_length=20)
    medium3 = models.CharField(max_length=20)
    medium4 = models.CharField(max_length=20)
    area = models.ForeignKey(Area_classification)
    edu_block = models.ForeignKey(Educational_block)
    school_category = models.ForeignKey(Category)
    school_type = models.ForeignKey(School_type)
    school_managed = models.ForeignKey(Management)
    school_total_count = IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s' % (self.school,self.medium1,self.medium2,self.medium3,self.medium4,self.area.area,self.edu_block,self.school_category.category_name,self.school_type.school_type,self.school_managed.management_name)


class School_contact_detail(models.Model):
    school_key = models.ForeignKey(School_info)
    office_landline = models.CharField(max_length=15)
    office_mobile = models.CharField(max_length=15)
    office_email = models.EmailField()
    hm_landline = models.CharField(max_length=15)
    hm_mobile = models.CharField(max_length=20)
    hm_email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.office_landline,self.office_mobile,self.office_email,self.hm_landline,self.hm_mobile,self.hm_email)

"""
Model for School recognition
"""
class School_recognition(models.Model):
    school_key = models.ForeignKey(School_info)
    initial_primary = models.CharField(max_length=15)
    initial_up = models.CharField(max_length=15)
    initial_secondary = models.CharField(max_length=15)
    initial_hs = models.CharField(max_length=15)
    renewal_primary = models.CharField(max_length=15)
    renewal_up = models.CharField(max_length=15)
    renewal_secondary = models.CharField(max_length=15)
    renewal_hs = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.initial_primary,self.initial_up,self.initial_secondary,self.initial_hs,self.renewal_primary,self.renewal_up,self.renewal_secondary,self.renewal_hs)

class School_upgradation(models.Model):
    school_key = models.ForeignKey(School_info)
    Primary_to_up = models.CharField(max_length=15)
    elementary_to_secondary = models.CharField(max_length=15)
    secondary_to_hs = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.Primary_to_up,self.elementary_to_secondary,self.secondary_to_hs)

class School_residence(models.Model):
    school_key = models.ForeignKey(School_info)
    residential = IntegerField()
    primary = models.CharField(max_length=50)
    up = models.CharField(max_length=50)
    secondary = models.CharField(max_length=50)
    hs = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.residential,self.primary,self.up,self.secondary,self.hs)

class School_anganwadi(models.Model):
    school_key = models.ForeignKey(School_info)
    anganwadi = IntegerField()
    student_count = IntegerField()
    teacher_count = IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.anganwadi,self.student_count,self.teacher_count)

class School_crc(models.Model):
    school_key = models.ForeignKey(School_info)
    crc = models.ForeignKey(Crc)
    distance_crc = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.crc.crc,self.distance_crc)

class School_brc(models.Model):
    school_key = models.ForeignKey(School_info)
    brc = models.ForeignKey(Brc)
    distance_brc = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.brc.brc,self.distance_brc)

"""
Model for School details
"""
class School_detail(models.Model):
    school_key = models.ForeignKey(School_info)
    village_ward = models.CharField(max_length=50)
    pincode = BigIntegerField()
    panchayat_name = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    lowest_class = IntegerField()
    highest_class = IntegerField()
    road = IntegerField()
    year = IntegerField()
    spl_school = IntegerField()
    shift_school = IntegerField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    assembly = models.ForeignKey(Assembly)
    parliamentary = models.ForeignKey(Parliamentary)
    contact_detail = models.ForeignKey(School_contact_detail)
    recognition = models.ForeignKey(School_recognition)
    upgradation = models.ForeignKey(School_upgradation)
    residential = models.ForeignKey(School_residence)
    crc = models.ForeignKey(School_crc)
    brc = models.ForeignKey(School_brc)
    anganwadi = models.ForeignKey(School_anganwadi)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.school_key.school.school_code,self.school_key.school.school_name,self.pincode,self.anganwadi.anganwadi,self.anganwadi.student_count,self.anganwadi.teacher_count)

"""
School Flags
"""
class School_flag(models.Model):
    school_key = models.ForeignKey(School)
    area_flag = IntegerField(default=0)
    edu_block_flag = IntegerField(default=0)
    school_type_flag = IntegerField(default=0)
    school_managed_flag = IntegerField(default=0)
    school_category_flag = IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


