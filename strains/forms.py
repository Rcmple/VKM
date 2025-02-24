from django import forms
from .models import Strains

class AddStrainForm(forms.ModelForm):
    class Meta:
        model = Strains
        fields = '__all__'