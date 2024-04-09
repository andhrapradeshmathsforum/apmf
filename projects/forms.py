from django.forms import ModelForm
from . models import Project

class ProjectForm(ModelForm):
    """Form definition for Projects."""

    class Meta:
        """Meta definition for Projects."""

        model = Project
        fields = ('standard','exam','chapter','description','file')