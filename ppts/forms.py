from django.forms import ModelForm
from . models import Ppt

class PptForm(ModelForm):
    """Form definition for Ppt."""

    class Meta:
        """Meta definition for Pptform."""

        model = Ppt
        fields = ('standard','chapter','description','file')