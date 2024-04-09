from django.forms import ModelForm
from . models import Textbook

class TextbookForm(ModelForm):
    """Form definition for Textbook."""

    class Meta:
        """Meta definition for Textbookform."""

        model = Textbook
        fields = ('standard','semester','title','description','file')