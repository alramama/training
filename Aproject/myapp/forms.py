# app/forms.py
from django.forms import ModelForm
from .models import BookLibrary


class BookLibForm(ModelForm):
	class Meta:
		model = BookLibrary
		fields = '__all__'



"""
class BookLibForm(forms.ModelForm):
    options = (
        ('sport', 'Sport'),
        ('history', 'History'),
        ('adventure', 'Adventure'),
        ('mystery', 'Mystery'),
        ('horror', 'Horror')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BookLibrary
        fields = ['name', 'about', 'category', 'author']"""
