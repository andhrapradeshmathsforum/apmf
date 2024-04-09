from django.forms import ModelForm
from . models import Solution

class SolutionForm(ModelForm):
    """Form definition for Solution."""

    class Meta:
        """Meta definition for Solutionform."""

        model = Solution
        fields = ('standard','chapter','description','file')