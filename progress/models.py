from django.db import models
from django.db.models.fields import *
from baseapp.models import School,Block,District
from students.models import Child_detail,School_child_count
import caching.base




class Udise_count(models.Model):
    district_name=models.CharField(default='', max_length=1000,blank=True, null=True)
    district_code=models.BigIntegerField(default='', blank=True, null=True)
    district_id=models.BigIntegerField(default='', blank=True, null=True)
    block_name=models.CharField(default='', max_length=1000,blank=True, null=True)
    block_code=models.BigIntegerField(default='', blank=True, null=True)
    block_id=models.BigIntegerField(default='', blank=True, null=True)
    school_name=models.CharField(default='', max_length=1000,blank=True, null=True)
    school_code=models.BigIntegerField(default='', blank=True, null=True)
    school_id=models.BigIntegerField(default='', blank=True, null=True)
    department=models.CharField(default='', max_length=1000,blank=True, null=True)
    management_name=models.CharField(default='', max_length=1000,blank=True, null=True)
    category_name=models.CharField(default='', max_length=1000,blank=True, null=True)
    c1 = models.PositiveIntegerField()
    c2 = models.PositiveIntegerField()
    c3 = models.PositiveIntegerField()
    c4 = models.PositiveIntegerField()
    c5 = models.PositiveIntegerField()
    c6 = models.PositiveIntegerField()
    c7 = models.PositiveIntegerField()
    c8 = models.PositiveIntegerField()
    c9 = models.PositiveIntegerField()
    c10 = models.PositiveIntegerField()
    c11 = models.PositiveIntegerField()
    c12 = models.PositiveIntegerField()
    school_total = models.PositiveIntegerField()






class aadhaar_student_count(models.Model):
    school=models.ForeignKey(School,blank=True, null=True)                        
    c1 = models.PositiveIntegerField(blank=True, null=True)
    c2 = models.PositiveIntegerField(blank=True, null=True)
    c3 = models.PositiveIntegerField(blank=True, null=True)
    c4 = models.PositiveIntegerField(blank=True, null=True)
    c5 = models.PositiveIntegerField(blank=True, null=True)
    c6 = models.PositiveIntegerField(blank=True, null=True)
    c7 = models.PositiveIntegerField(blank=True, null=True)
    c8 = models.PositiveIntegerField(blank=True, null=True)
    c9 = models.PositiveIntegerField(blank=True, null=True)
    c10 = models.PositiveIntegerField(blank=True, null=True)
    c11 = models.PositiveIntegerField(blank=True, null=True)
    c12 = models.PositiveIntegerField(blank=True, null=True)
    school_total = models.PositiveIntegerField(blank=True, null=True)
    a_c1 = models.PositiveIntegerField(blank=True, null=True)
    a_c2 = models.PositiveIntegerField(blank=True, null=True)
    a_c3 = models.PositiveIntegerField(blank=True, null=True)
    a_c4 = models.PositiveIntegerField(blank=True, null=True)
    a_c5 = models.PositiveIntegerField(blank=True, null=True)
    a_c6 = models.PositiveIntegerField(blank=True, null=True)
    a_c7 = models.PositiveIntegerField(blank=True, null=True)
    a_c8 = models.PositiveIntegerField(blank=True, null=True)
    a_c9 = models.PositiveIntegerField(blank=True, null=True)
    a_c10 = models.PositiveIntegerField(blank=True, null=True)
    a_c11 = models.PositiveIntegerField(blank=True, null=True)
    a_c12 = models.PositiveIntegerField(blank=True, null=True)
    a_school_total = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.school)

  

    


