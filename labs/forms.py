from django.forms import ModelForm
from . models import Lab

class LabForm(ModelForm):
    """Form definition for Lab."""

    class Meta:
        """Meta definition for Labform."""

        model = Lab
        fields = ('standard','title','description','file')