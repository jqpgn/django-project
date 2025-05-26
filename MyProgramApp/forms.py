from django import forms
from .models import EducationProgram


class EducationProgramForm(forms.ModelForm):
    class Meta:
        model = EducationProgram
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
