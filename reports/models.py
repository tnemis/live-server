from django.db import models
from django.db.models.fields import *
from baseapp.models import School,Block,District
from students.models import Child_detail,School_child_count
import caching.base

# Create your models here.
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

  

    

