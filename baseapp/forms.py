from django import forms

from baseapp.models import Child_detail_pool_database

class Pool_databaseform(forms.ModelForm):
    class Meta:
        model = Child_detail_pool_database