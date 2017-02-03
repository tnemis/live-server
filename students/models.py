from django.db import models

from django.db.models.fields import *
from baseapp.models import *
import caching.base
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db.models.signals import post_save, post_delete
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill
from django.conf import settings as django_settings
import os
from django.core.exceptions import ValidationError


fl_choice =(
    ('TAM','TAMIL'),
    ('KAN','KANNADA'),
    ('TEL','TELUGU'),
    ('MAL','MALAYALAM'),
    ('URD','URDU'),
    ('FRE','FRENCH'),  
    ('SAN','SANSKRIT'),
    ('GER','GERMAN'),
    ('ARA','ARABIC'),
    ('HIN','HINDI'),
)
gcl_choice =(
    ('TAM','TAMIL'),
    ('KAN','KANNADA'),
    ('TEL','TELUGU'),
    ('MAL','MALAYALAM'),
    ('URD','URDU'),
    ('HIN','HINDI'),
    ('ENG','ENGLISH'),
)
ol_choice =(
    ('KAN','KANNADA'),
    ('TEL','TELUGU'),
    ('MAL','MALAYALAM'),
    ('URD','URDU'),
    ('FRE','FRENCH'),
    ('HIN','HINDI'),
    ('SAN','SANSKRIT'),
    ('ARA','ARABIC'),
    ('GUJ','GUJARATHI'),
)

sp_choice =(
    ('Y','YES'),
    ('N','NO')
)

le_choice =(
    ('PART1','LANGUAGE PART-I'),
    ('PART2','LANGUAGE PART-II'),
)
class Thumbnail(ImageSpec):
    processors = [ResizeToFill(150, 150)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('students:thumbnail', Thumbnail)
 


class Child_detail(caching.base.CachingMixin, models.Model):

    def save(self):

        if not self.unique_id_no:
            self.unique_id_no = (
                self.school.school_code * 100000) + (
                self.school.student_id_count + 1)
        super(Child_detail, self).save()

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
        dir = "images/child_pics/%s/%s" % (a, instance.school.school_code)
        name = str(instance.unique_id_no)+"_"+random

        return "%s/%s.%s" % (dir, name, extension)

    name = models.CharField(default='', max_length=200)
    name_tamil = models.CharField(default='', max_length=200,blank=True, null=True)
    aadhaar_id = models.CharField(max_length=3)
    aadhaar_eid_number = models.CharField(max_length=50,blank=True, null=True)
    aadhaar_uid_number = models.BigIntegerField(blank=True, null=True)
    photograph = ProcessedImageField(upload_to=get_path,
                                     processors=[ResizeToFill(200, 200)],
                                     format='JPEG',
                                     options={'quality': 60},
                                     blank=True,
                                     null=True,
                                     validators=[validate_image])
    photo = ProcessedImageField(upload_to=get_path,
                                     processors=[ResizeToFill(125, 125)],
                                     format='JPEG',
                                     options={'quality': 60},
                                     blank=True,
                                     null=True,
                                     )
    gender = models.CharField(max_length=15)
    dob = models.DateField(default='1990-01-01')
    religion=models.ForeignKey(Religion,blank=True,null=True)
    community =ChainedForeignKey(
        Community, chained_field='religion', chained_model_field='religion', auto_choose=True,blank=True,null=True)
    community_certificate = models.CharField(max_length=3,blank=True,null=True)
    community_certificate_no = models.CharField(max_length=200,blank=True,null=True)
    community_certificate_date = models.DateField(blank=True,null=True,default='1990-01-01')
    nativity_certificate = models.CharField(max_length=3,blank=True,null=True)
    
    mothertounge = models.ForeignKey(Language)
    phone_number = BigIntegerField(default=0,  blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    child_differently_abled = models.CharField(max_length=3)
    differently_abled = models.CharField(max_length=30,blank=True,null=True)
    da_id_no = models.CharField(max_length=20,blank=True,null=True)
    sci_practical = models.CharField(choices=sp_choice,max_length=30,blank=True,null=True)
    lang_exemption = models.CharField(choices=le_choice,max_length=30,blank=True,null=True)
    lang_exemption1 = models.CharField(choices=le_choice,max_length=30,blank=True,null=True)
    child_admitted_under_reservation = models.CharField(max_length=3,blank=True,null=True)
    weaker_section = models.CharField(max_length=3,blank=True,null=True)
    weaker_section_income_certificate_no = models.CharField(max_length=200,blank=True,null=True)
    child_disadvantaged_group = models.CharField(max_length=3,blank=True,null=True)
    disadvantaged_group = models.CharField(max_length=1000,blank=True,null=True)
    subcaste = ChainedForeignKey(Sub_Castes, chained_field='community',
                                 chained_model_field='community',
                                 auto_choose=True,
                                 blank=True,
                                 null=True)
    nationality = models.ForeignKey(Nationality)
    child_status = models.CharField(max_length=200,blank=True, null=True)
    house_address = models.CharField(default='', max_length=1000,blank=True, null=True)
    street_name = models.CharField(default='', max_length=1000,blank=True, null=True)
    area_village = models.CharField(default='', max_length=1000,blank=True, null=True)
    city_district = models.CharField(default='', max_length=1000,blank=True, null=True)
    native_district = models.CharField(max_length=50)
    pin_code = models.PositiveIntegerField(blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    height = models.PositiveIntegerField(max_length=3, default=0,  blank=True, null=True)
    weight = models.PositiveIntegerField(default=0,  blank=True, null=True)
    mother_name = models.CharField(default='', max_length=100, blank=True, null=True)
    mother_occupation = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(default='', max_length=100, blank=True, null=True)
    father_occupation = models.CharField(max_length=50, blank=True, null=True)
    parent_income = models.PositiveIntegerField(default=0, blank=True, null=True)
    guardian_name = models.CharField(default='', max_length=100, blank=True, null=True)
    class_studying = models.ForeignKey(Class_Studying)
    class_section = models.CharField(max_length=30)
    group_code = models.ForeignKey(Group_code, blank=True, null=True)
    grpcode_language1 = models.CharField(choices=gcl_choice,max_length=3,blank=True,null=True)
    grpcode_language2 = models.CharField(choices=gcl_choice,max_length=3,blank=True,null=True)
    grpcode_language3 = models.CharField(choices=gcl_choice,max_length=3,blank=True,null=True)
    grpcode_language4 = models.CharField(choices=gcl_choice,max_length=3,blank=True,null=True)
    cbse_subject1 = models.ForeignKey(Group_code_cbse, related_name='subject1',blank=True,null=True)
    cbse_subject2 = models.ForeignKey(Group_code_cbse, related_name='subject2',blank=True,null=True)
    cbse_subject3 = models.ForeignKey(Group_code_cbse, related_name='subject3',blank=True,null=True)
    cbse_subject4 = models.ForeignKey(Group_code_cbse, related_name='subject4',blank=True,null=True)
    cbse_opt_subject = models.ForeignKey(Group_code_cbse, related_name='opt_subject',blank=True,null=True)
    first_language = models.CharField(choices=fl_choice,max_length=30,default='',blank=True,null=True)
    optional_language = models.CharField(choices=ol_choice,max_length=30,default='',blank=True,null=True)
    attendance_status = models.CharField(max_length=30, blank=True, null=True)
    sport_participation = models.CharField(max_length=20, blank=True, null=True)
    laptop_issued = models.CharField(max_length=3,blank=True,null=True)
    laptop_slno = models.CharField(max_length=200,blank=True,null=True)
    education_medium = models.ForeignKey(Education_medium,blank=True,null=True)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    block = models.ForeignKey(Block)
    unique_id_no = models.BigIntegerField(blank=True, null=True)
    school = models.ForeignKey(School)
    staff_id = models.CharField(max_length=30)
    student_admitted_section = models.CharField(max_length=100,blank=True, null=True)
    school_admission_no = models.CharField(max_length=100)

    bank_dist = models.ForeignKey(Bank_districtnew, blank=True, null=True)
    banknew = ChainedForeignKey(Banknew, chained_field='bank_dist',
                                 chained_model_field='bank_dist',
                                 auto_choose=True,
                                 blank=True,
                                 null=True)
    branchnew = ChainedForeignKey(Branchnew, chained_field='banknew',
                                 chained_model_field='bank',
                                 auto_choose=True,
                                 blank=True,
                                 null=True)
    bank_ifsc_codenew = models.CharField(max_length=50, default='', blank=True, null=True)




#     bank = models.ForeignKey(Bank, blank=True, null=True)
#     bank_branch = models.CharField(default='', max_length=200, blank=True, null=True)
    bank_account_no = models.CharField(default='', max_length=30, blank=True, null=True)
#     bank_ifsc_code = models.CharField(max_length=50, default='', blank=True, null=True)
    sports_player = models.CharField(max_length=3)
    sports_name = models.CharField(max_length=1000,blank=True,null=True)
    # govt_schemes_status = models.CharField(max_length=5)
    schemes = models.CharField(max_length=1000,blank=True,null=True)
    academic_year = models.ForeignKey(Academic_Year)
    scholarship_from_other_source = models.CharField(max_length=3)
    scholarship_details = models.CharField(max_length=1000,blank=True,null=True)
    scholarship_other_details = models.CharField(max_length=1000,blank=True,null=True)
    bus_pass = models.CharField(max_length=3)
    bus_from_route = models.CharField(max_length=50,blank=True,null=True)
    bus_to_route = models.CharField(max_length=50,blank=True,null=True)
    bus_route_no = models.CharField(max_length=5,blank=True,null=True)
    transfer_flag = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    transfer_date = models.DateField(blank=True, null=True)
    nutritious_meal_flag = models.CharField(default='', max_length=5, blank=True, null=True)
    modification_flag = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    verification_flag = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    # thamarai added two fields
    schl_cat_10 = models.IntegerField(blank=True, null=True)
    schl_cat_12 = models.IntegerField(blank=True, null=True)


    objects = caching.base.CachingManager()
    # history = HistoricalRecords()

    def __unicode__(self):
        return u'%s %s %s %s' % (self.unique_id_no, self.name, self.staff_id,
                                 self.verification_flag)


class Child_family_detail(caching.base.CachingMixin, models.Model):
    child_key = models.ForeignKey(Child_detail)
    si_no = models.PositiveIntegerField()
    block = models.ForeignKey(Block)
    sibling_name = models.CharField(max_length=50)
    sibling_relationship = models.CharField(max_length=20)
    sibling_age = models.IntegerField(max_length=3)
    sibling_status = models.CharField(max_length=50, blank=True, null=True)
    sibling_studying = models.CharField(max_length=50, blank=True, null=True)
    sibling_studying_same_school = models.CharField(max_length=3)
    staff_id = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    # history = HistoricalRecords()
    objects = caching.base.CachingManager()

    def __unicode__(self):
        return u'%s %s' % (self.child_key, self.sibling_name)

"""
Model for Old school
"""


class Child_Transfer_History(models.Model):
    child_key = models.ForeignKey(Child_detail)
    old_school = models.ForeignKey(School)
    tc_issue_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    # history = HistoricalRecords()
    # objects = caching.base.CachingManager()

    def __unicode__(self):
        return u'%s %s' % (self.child_key, self.old_school)


def ensure_stud_count_increase(sender, instance, **kwargs):
        if kwargs.get('created', True):
            school = School.objects.get(
                school_code=instance.school.school_code)
            school.student_id_count += 1
            school.save()

post_save.connect(ensure_stud_count_increase, sender=Child_detail)


"""
Model for school child count
"""
class School_child_count(models.Model):
    school = models.ForeignKey(School)
    one = models.PositiveIntegerField()
    two = models.PositiveIntegerField()
    three = models.PositiveIntegerField()
    four = models.PositiveIntegerField()
    five = models.PositiveIntegerField()
    six = models.PositiveIntegerField()
    seven = models.PositiveIntegerField()
    eight = models.PositiveIntegerField()
    nine = models.PositiveIntegerField()
    ten = models.PositiveIntegerField()
    eleven = models.PositiveIntegerField()
    twelve = models.PositiveIntegerField()
    total_count = models.PositiveIntegerField()


def school_child_count_increase(sender, instance, **kwargs):
    # import ipdb;ipdb.set_trace()
    if kwargs.get('created', True):
        try:
            child = School_child_count.objects.get(school=instance.school)
        except School_child_count.DoesNotExist:
            child=School_child_count.objects.create(school=instance.school,one=0,two=0,three=0,four=0,five=0,six=0,seven=0,eight=0,nine=0,ten=0,eleven=0,twelve=0,total_count=0)
        class_studying= instance.class_studying
        if str(class_studying)=='I':
            child.one += 1
        elif str(class_studying)=='II':
            child.two += 1
        elif str(class_studying)=='III':
            child.three += 1
        elif str(class_studying)=='IV':
            child.four += 1
        elif str(class_studying)=='V':
            child.five += 1
        elif str(class_studying)=='VI':
            child.six += 1
        elif str(class_studying)=='VII':
            child.seven += 1
        elif str(class_studying)=='VIII':
            child.eight += 1
        elif str(class_studying)=='IX':
            child.nine+= 1
        elif str(class_studying)=='X':
            child.ten += 1
        elif str(class_studying)=='XI':
            child.eleven += 1
        elif str(class_studying)=='XII':
            child.twelve += 1
        child.total_count += 1
        child.save()
post_save.connect(school_child_count_increase, sender=Child_detail)

def school_child_count_decrease(sender, instance, **kwargs):
    
    child = School_child_count.objects.get(school=instance.school)
    class_studying= instance.class_studying
    if str(class_studying)=='I':
        child.one -=1
    elif str(class_studying)=='II':
        child.two -=1
    elif str(class_studying)=='III':
        child.three -=1
    elif str(class_studying)=='IV':
        child.four -=1
    elif str(class_studying)=='V':
        child.five -=1
    elif str(class_studying)=='VI':
        child.six -=1
    elif str(class_studying)=='VII':
        child.seven -=1
    elif str(class_studying)=='VIII':
        child.eight -=1
    elif str(class_studying)=='IX':
        child.nine-=1
    elif str(class_studying)=='X':
        child.ten -=1
    elif str(class_studying)=='XI':
        child.eleven -=1
    elif str(class_studying)=='XII':
        child.twelve -=1
    child.total_count -= 1
    child.save()
post_delete.connect(school_child_count_decrease, sender=Child_detail)


"""
Model for Parent's Annual Income
"""


class Parent_annual_income(models.Model):
    income = models.CharField(max_length=50)

class Pool_child_count(models.Model):
    school = models.ForeignKey(School)
    one = models.PositiveIntegerField()
    two = models.PositiveIntegerField()
    three = models.PositiveIntegerField()
    four = models.PositiveIntegerField()
    five = models.PositiveIntegerField()
    six = models.PositiveIntegerField()
    seven = models.PositiveIntegerField()
    eight = models.PositiveIntegerField()
    nine = models.PositiveIntegerField()
    ten = models.PositiveIntegerField()
    eleven = models.PositiveIntegerField()
    twelve = models.PositiveIntegerField()
    total_count = models.PositiveIntegerField()
