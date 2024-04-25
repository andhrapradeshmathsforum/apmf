from django.forms import ModelForm
from .models import Rp


class RpForm(ModelForm):
    
    class Meta:
        model = Rp
        fields = '__all__'

