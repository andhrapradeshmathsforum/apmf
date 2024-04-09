from django.forms import ModelForm
from . models import NmmsMaterial

class NmmsMaterialForm(ModelForm):
    """Form definition for nmms_matrials."""

    class Meta:
        """Meta definition for NmmsMaterialForm."""

        model = NmmsMaterial
        fields = ('title','description','file')