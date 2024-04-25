from django.forms import ModelForm
from .models import Tlm


class TlmForm(ModelForm):
    
    class Meta:
        model = Tlm
        fields = ['title','description','image']
