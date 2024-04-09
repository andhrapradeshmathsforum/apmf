from django.forms import ModelForm
from . models import Notes

class NotesForm(ModelForm):
    """Form definition for Notess."""

    class Meta:
        """Meta definition for Notesform."""

        model = Notes
        fields = ('standard','chapter','description','file')