from django.forms import ModelForm
from . models import NmmsQuestionpaper

class NmmsQuestionpaperForm(ModelForm):
    """Form definition for nmms_matrials."""

    class Meta:
        """Meta definition for NmmsQuestionpaperForm."""

        model = NmmsQuestionpaper
        fields = ('title','description','file')