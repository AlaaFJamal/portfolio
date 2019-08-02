from django import forms
from .models import Section

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = '__all__'
		

# new form class for confirming Delete option to user
# takes from Section model but with no fields to show 
class DeleteForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = []