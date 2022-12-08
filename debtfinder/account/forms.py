from django import forms
from .models import *

class ParentForm(forms.ModelForm):
    
    class Meta:
        model = Parent
        fields = ("")
