from django import forms

from students.models import Child_detail


class Child_detailform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Child_detailform, self).__init__(*args, **kwargs)
        dob= forms.DateField(input_formats='%d/%m/%Y')

        

    class Meta:
         model = Child_detail
