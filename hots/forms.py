from django.forms import ModelForm
from .models import Hot

class HotForm(ModelForm):
    
    class Meta:
        model = Hot
        fields = ('standard','chapter','title','description','file',)
        
