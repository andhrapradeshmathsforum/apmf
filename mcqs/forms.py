from django.forms import ModelForm
from . models import Mcq

class McqForm(ModelForm):
    """Form definition for Mcq."""

    class Meta:
        """Meta definition for Mcqform."""

        model = Mcq
        fields = ('standard','chapter','description','file')