from django import forms
from student.models import Stud

class BIDForm(forms.ModelForm):
    class Meta:
        model = BID
        fields = '__all__'
