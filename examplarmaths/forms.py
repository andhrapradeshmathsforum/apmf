from django.forms import ModelForm
from . models import Examplarmath

class ExamplarmathForm(ModelForm):
    """Form definition for examplarmath."""

    class Meta:
        """Meta definition for ExamplarmathForm."""

        model = Examplarmath
        fields = ('standard','title','description','file')