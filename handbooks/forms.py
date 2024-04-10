from django.forms import ModelForm
from . models import Handbook

class HandbookForm(ModelForm):
    """Form definition for Handbook."""

    class Meta:
        """Meta definition for Handbookform."""

        model = Handbook
        fields = ('standard','title','description','file')