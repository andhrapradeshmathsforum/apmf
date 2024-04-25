from .models import Key
from django import forms


class KeyForm(forms.ModelForm):
    
    class Meta:
        model = Key
        fields = ['standard','year','exam','title','description', 'file']
