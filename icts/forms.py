from django.forms import ModelForm
from . models import Ict

class IctForm(ModelForm):
    """Form definition for Ict."""

    class Meta:
        """Meta definition for Ictform."""

        model = Ict
        fields = ('title','link','image')