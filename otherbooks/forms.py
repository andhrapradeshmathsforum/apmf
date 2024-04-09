from django.forms import ModelForm
from . models import Otherbook

class OtherbookForm(ModelForm):
    """Form definition for Otherbook."""

    class Meta:
        """Meta definition for Otherbookform."""

        model = Otherbook
        fields = ('title','description','file')