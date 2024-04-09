from django.forms import ModelForm
from . models import Worksheet

class WorksheetForm(ModelForm):
    """Form definition for Worksheet."""

    class Meta:
        """Meta definition for Worksheetform."""

        model = Worksheet
        fields = ('standard','chapter','description','file')