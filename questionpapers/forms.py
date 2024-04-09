from django.forms import ModelForm
from . models import Questionpaper

class QuestionpaperForm(ModelForm):
    """Form definition for Questionpaper."""

    class Meta:
        """Meta definition for Questionpaperform."""

        model = Questionpaper
        fields = ('standard','exam','description','file')