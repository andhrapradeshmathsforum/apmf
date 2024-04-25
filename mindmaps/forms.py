from django.forms import ModelForm
from .models import Mindmap

class MindmapForm(ModelForm):
    
    class Meta:
        model = Mindmap
        fields = ('standard','chapter','title','description','file',)
        
