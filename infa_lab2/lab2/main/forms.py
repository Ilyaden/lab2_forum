from django import forms
from .models import *
class add_notes(forms.ModelForm):
	class Meta:
		model = notes  
		fields = ['title','image']
		widgets = {
			
			'title' :forms.TextInput(attrs={'placeholder':'Введите название', 'class':'form-control'}),
		}
		
class add_comment(forms.Form):
			
	single_comment = forms.CharField(
		widget=forms.TextInput(attrs={'placeholder':'Введите комментарий', 'class':'form-control'}))
		