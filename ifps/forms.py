from django.forms import ModelForm
from . models import Ifp




class IfpForm(ModelForm):
    """Form definition for Ifps."""

    class Meta:
        """Meta definition for IfpForm."""

        model = Ifp
        fields = ('title','description','video')