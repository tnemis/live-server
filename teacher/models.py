from django.db import models

from django.db import models
from django.db.models.fields import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

import caching.base
from baseapp.models import *
# Create your models here.




"""
Model for Teacher Personal details
"""


class Teacher_designation(models.Model):
    designation_code = models.CharField(max_length=100)
    designation_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.designation_name)


class Teacher_subject(models.Model):
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.subject_name)

class Teacher_family_relationship(models.Model):
    relationship_code = models.CharField(max_length=100)
    relationship_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.relationship_name)
class Teacher_qualification(models.Model):
    qualification_code = models.CharField(max_length=100)
    qualification_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.qualification_name)

class Teacher_leave_code(models.Model):
    leave_code = models.CharField(max_length=100)
    leave_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.leave_name)

class Teacher_rule_code(models.Model):
    rule_code = models.CharField(max_length=100)
    rule_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.rule_name)

class Teacher_loan_category(models.Model):
    loan_code = models.CharField(max_length=100)
    loan_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.loan_name)

class Teacher_post_category(models.Model):
    category_code = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.category_name)

class Teacher_pay_band(models.Model):
    pay_band = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.pay_band)

class Teacher_grade_pay(models.Model):
    grade_pay = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.grade_pay)

class Teacher_test_master(models.Model):
    test_code = models.CharField(max_length=100)
    test_name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.test_name)

class Teacher_fund_category(models.Model):
    fund_code = models.CharField(max_length=100)
    fund_name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.fund_name)
        
class Teacher_personal_detail(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        kb_limit = 50
        Kilobyte_limit = 1024 *50
        if filesize > Kilobyte_limit:
            raise ValidationError("Max file size is %sKB" % str(kb_limit))

    def get_path(instance, filename):
        import random
        import string
        random=''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        extension = filename.split('.')[-1]
        a = instance.block.block_name.replace(" ", ".")
        a.replace("(", '_')
        a.replace(")", '_')
        try:
            child = Child_detail.objects.get(unique_id_no=instance.unique_id_no)
            path=django_settings.MEDIA_ROOT+"/"+str(child.photograph)
            os.remove(path)
        except:
            pass
        dir = "images/teacher_pics/%s/%s" % (a, instance.school.school_code)
        name = str(instance.code)+"_"+random

        return "%s/%s.%s" % (dir, name, extension)
    code = models.CharField(max_length=50)
    gpf_no = models.CharField(max_length=50)
    school = models.ForeignKey(School,blank=True,null=True)
    name = models.CharField(max_length=50)
    photograph = ProcessedImageField(upload_to=get_path,
                                     processors=[ResizeToFill(200, 200)],
                                     format='JPEG',
                                     options={'quality': 60},
                                     blank=True,
                                     null=True,
                                     validators=[validate_image])
    aadhaar_uid_number = models.BigIntegerField(blank=True, null=True)
    designation = models.ForeignKey(Teacher_designation)
    subject = models.ForeignKey(Teacher_subject)
    pan = models.CharField(max_length=50)
    dob = models.DateField(blank=True,null=True)
    blood = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    community = models.ForeignKey(Community,blank=True,null=True)
    religion = models.ForeignKey(Religion)
    mother_tongue = models.ForeignKey(Language)
    # native_dist = models.CharField(max_length=50)
    # native_taluk = models.CharField(max_length=50)
    # native_village = models.CharField(max_length=50)
    languages = models.CharField(max_length=200)
    identification = models.CharField(max_length=1000)
    height = models.PositiveIntegerField(default=0,  blank=True, null=True)
    weight = models.PositiveIntegerField(default=0,  blank=True, null=True) 
    # railway = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=1000)
    permanent_pincode = models.CharField(max_length=50)
    permanent_phone = models.CharField(max_length=50)
    present_address = models.CharField(max_length=1000)
    present_pincode = models.CharField(max_length=50)
    present_phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    complete_flag = models.CharField(max_length=1,default="0",  blank=True, null=True)
    modification_flag = models.CharField(max_length=1,  blank=True, null=True)
    verification_flag = models.CharField(max_length=1,  blank=True, null=True)
    staff_id = models.CharField(max_length=100,  blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,  blank=True, null=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.code,self.gpf_no,self.name)

"""
Model for teacher family details
"""
class Teacher_family_detail(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    relation = models.ForeignKey(Teacher_family_relationship)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher immovalble property details
"""
class Teacher_immovalble_property(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    prop_description = models.CharField(max_length=50)
    doc_number = models.CharField(max_length=50)
    doc_date = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    acquired = models.CharField(max_length=50)
    purchase_value = models.CharField(max_length=50)
    present_value = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    order_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher movable property details
"""
class Teacher_movable_property(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    prop_description = models.CharField(max_length=50)
    purchase_value = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    order_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher education details
"""
class Teacher_education(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    qualification = models.ForeignKey(Teacher_qualification)
    subject = models.ForeignKey(Teacher_subject)
    year = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher passed tests details
"""
class Teacher_test(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    tests_passed = models.ForeignKey(Teacher_test_master)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=50)
    gaz_no = models.CharField(max_length=50)
    gaz_date = models.DateTimeField(blank=True,null=True)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for teacher's training details
"""
class Teacher_training(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    course = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    duration_from = models.CharField(max_length=50)
    duration_to = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    order_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher's Post related details
"""
class Teacher_post(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    designation = models.ForeignKey(Teacher_designation)
    school = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    category = models.ForeignKey(Teacher_post_category)
    post_from = models.CharField(max_length=50)
    post_to = models.CharField(max_length=50)
    pay_scale = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher professional details
"""
class Teacher_professional(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    doj_govt = models.CharField(max_length=50)
    doj_dept = models.CharField(max_length=50)
    desig_onjoining = models.ForeignKey(Teacher_designation)
    typewriting_english = models.CharField(max_length=50)
    typewriting_tamil = models.CharField(max_length=50)
    shorthand_english = models.CharField(max_length=50)
    shorthand_tamil = models.CharField(max_length=50)
    emply_status = models.CharField(max_length=50)
    # working_dist = models.CharField(max_length=50)
    # working_blk = models.CharField(max_length=50)
    # working_place = models.CharField(max_length=50)
    # controlling_officer = models.CharField(max_length=50)
    # pay_scale = models.CharField(max_length=50)
    pay_band = models.ForeignKey(Teacher_pay_band)
    grade_pay = models.ForeignKey(Teacher_grade_pay)
    incr_month = models.CharField(max_length=50)
    basic_pay = models.CharField(max_length=50)
    seniority_no = models.CharField(max_length=50)
    computer_training = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for teacher leave surrender details
"""
class Teacher_leave_surrender(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    # leave_from = models.CharField(max_length=50)
    # leave_to = models.CharField(max_length=50)
    surrender_date = models.DateTimeField(blank=True,null=True)
    days = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    order_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for teacher leave details
"""
class Teacher_leave(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    leave_type = models.ForeignKey(Teacher_leave_code)
    leave_from = models.CharField(max_length=50)
    leave_to = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    order_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for teacher previous LTC
"""
class Teacher_ltc(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    block_yr1 = models.CharField(max_length=50)
    block_yr2 = models.CharField(max_length=50)
    leave_type = models.ForeignKey(Teacher_leave_code)
    sanction_amt = models.CharField(max_length=50)
    sanction_number = models.CharField(max_length=50)
    sanction_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for teacher leave credits
"""
class Teacher_leave_credit(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    earned_effective = models.CharField(max_length=50)
    earned_credit = models.CharField(max_length=50)
    earned_prebalance = models.CharField(max_length=50)
    earned_curbalance = models.CharField(max_length=50)
    earned_orderno = models.CharField(max_length=50)
    earned_orderdate = models.CharField(max_length=50)
    half_effective = models.CharField(max_length=50)
    half_credit = models.CharField(max_length=50)
    half_prebalance = models.CharField(max_length=50)
    half_curbalance = models.CharField(max_length=50)
    half_orderno = models.CharField(max_length=50)
    half_orderdate = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Model for Teacher Previous Employment Details
"""
class Teacher_previous_employment(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    designation = models.ForeignKey(Teacher_designation)
    posting_place = models.CharField(max_length=50)
    posting_from = models.CharField(max_length=50)
    posting_to = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Models for Teacher loan details
"""
class Teacher_loan(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    loan_category = models.ForeignKey(Teacher_loan_category)
    loan_details = models.CharField(max_length=50)
    sanctioned_amt = models.CharField(max_length=50)
    monthly_installment = models.CharField(max_length=50)
    installments = models.CharField(max_length=50)
    first_insta_date = models.CharField(max_length=50)
    sanctioned_order = models.CharField(max_length=50)
    sanctioned_date = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Models for Teacher nomini details
"""
class Teacher_nomini(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    fund_name = models.ForeignKey(Teacher_fund_category)
    nominee_name = models.CharField(max_length=50)
    relationship = models.ForeignKey(Teacher_family_relationship)
    age = models.CharField(max_length=50)
    percentage = models.CharField(max_length=50)
    nom_sl_no = models.CharField(max_length=3)
    nom_dt  = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.teacher_key)

"""
Models for Teacher's Action
"""
class Teacher_action(models.Model):
    teacher_key = models.ForeignKey(Teacher_personal_detail)
    file_number = models.CharField(max_length=50)
    rule = models.ForeignKey(Teacher_rule_code)
    gist = models.CharField(max_length=50)
    present_stage = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    order_date = models.CharField(max_length=50)
    gist_final = models.CharField(max_length=50)
    complete_flag = models.CharField(max_length=1,default="0")
    modification_flag = models.CharField(max_length=1)
    verification_flag = models.CharField(max_length=1)
    staff_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
            return u'%s' % (self.teacher_key)


