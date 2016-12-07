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


												
