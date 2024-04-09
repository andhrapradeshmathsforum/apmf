from django.forms import ModelForm
from . models import Lessonplan

class LessonplanForm(ModelForm):
    """Form definition for Lessonplans."""

    class Meta:
        """Meta definition for Lessonplanform."""

        model = Lessonplan
        fields = ('standard','chapter','description','file')