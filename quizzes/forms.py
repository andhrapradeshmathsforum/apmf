from django.forms import ModelForm
from . models import Quiz

class QuizForm(ModelForm):
    """Form definition for Quiz."""

    class Meta:
        """Meta definition for Quizform."""

        model = Quiz
        fields = ('standard','topic','sub_topic','link')