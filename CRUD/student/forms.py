from django import forms
from student.models import Stud

class StudForm(forms.ModelForm):
    class Meta:
        model = Stud
        fields = '__all__'
