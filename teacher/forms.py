from django import forms

from teacher.models import Teacher_personal_detail


class Teacher_personal_detailform(forms.ModelForm):
    """Upload files with this form"""
    dob = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))

    class Meta:
        model = Teacher_personal_detail
       


class Teacher_personal_detail_Poolform(forms.ModelForm):
    class Meta:
        model = Teacher_personal_detail
        fields = ['name','gpf_no','dob']