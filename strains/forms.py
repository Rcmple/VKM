from django import forms
from .models import Strains

class StrainForm(forms.ModelForm):
    class Meta:
        model = Strains
        fields = ['Genus', 'Species', 'CollectedDate']